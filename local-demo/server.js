import http from "node:http";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import crypto from "node:crypto";

const root = path.dirname(fileURLToPath(import.meta.url));
const port = Number(process.env.PORT || 3002);
const accessToken = process.env.MERCADO_PAGO_ACCESS_TOKEN;
const appUrl = process.env.APP_URL || `http://localhost:${port}`;
const publicReturnUrl = /^https:\/\//.test(appUrl) && !appUrl.includes("localhost");
const packs = {
  avulsa: { name: "Consulta avulsa", price: 3.99 },
  cinco: { name: "Pacote 5 consultas", price: 17.95 },
  dez: { name: "Pacote 10 consultas", price: 31.90 },
};

const mime = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8" };
const send = (response, status, body, headers = {}) => { response.writeHead(status, { "Content-Type": "application/json; charset=utf-8", ...headers }); response.end(JSON.stringify(body)); };

async function bodyOf(request) {
  let data = "";
  for await (const chunk of request) data += chunk;
  return data ? JSON.parse(data) : {};
}

async function createPreference(packId) {
  if (!accessToken) throw new Error("MERCADO_PAGO_ACCESS_TOKEN não está configurado no processo local.");
  const pack = packs[packId];
  if (!pack) throw new Error("Pacote inválido.");
  const externalReference = `consulta-${packId}-${crypto.randomUUID()}`;
  const payload = {
    items: [{ id: packId, title: `${pack.name} — Calculadora Penal`, quantity: 1, currency_id: "BRL", unit_price: pack.price }],
    external_reference: externalReference,
    statement_descriptor: "CALCULADORA PENAL",
    ...(publicReturnUrl ? {
      back_urls: {
        success: `${appUrl}/?pagamento=sucesso`,
        failure: `${appUrl}/?pagamento=falhou`,
        pending: `${appUrl}/?pagamento=pendente`,
      },
      auto_return: "approved",
    } : {}),
  };
  const mercadoPago = await fetch("https://api.mercadopago.com/checkout/preferences", {
    method: "POST",
    headers: { Authorization: `Bearer ${accessToken}`, "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const result = await mercadoPago.json();
  if (!mercadoPago.ok || !result.init_point) throw new Error(result.message || "Mercado Pago recusou a preferência.");
  return { checkoutUrl: result.init_point, externalReference };
}

const server = http.createServer(async (request, response) => {
  try {
    const url = new URL(request.url || "/", `http://${request.headers.host || "localhost"}`);
    if (request.method === "GET" && url.pathname === "/api/health") return send(response, 200, { ok: true, hasAccessToken: Boolean(accessToken) });
    if (request.method === "POST" && url.pathname === "/api/checkout") {
      const body = await bodyOf(request);
      const result = await createPreference(body.packId);
      return send(response, 201, result);
    }
    if (request.method !== "GET") return send(response, 405, { message: "Método não permitido." });
    const requested = url.pathname === "/" ? "index.html" : url.pathname.replace(/^\//, "");
    const file = path.resolve(root, requested);
    if (!file.startsWith(root)) return send(response, 403, { message: "Arquivo bloqueado." });
    const content = await fs.readFile(file);
    response.writeHead(200, { "Content-Type": mime[path.extname(file)] || "application/octet-stream" });
    return response.end(content);
  } catch (error) {
    return send(response, 502, { message: error instanceof Error ? error.message : "Erro inesperado no servidor local." });
  }
});

server.listen(port, () => console.log(`Demo local disponível em http://localhost:${port}`));
