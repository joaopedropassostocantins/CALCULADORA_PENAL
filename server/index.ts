import "dotenv/config";
import path from "node:path";
import { fileURLToPath } from "node:url";
import express from "express";
import { z } from "zod";
import { consultationPacks, getPack } from "../src/data/pricing";
import { createExternalReference, getPaymentFromMercadoPago, isApprovedPayment } from "./mercado-pago";

const app = express();
const port = Number(process.env.PORT ?? 3000);
const appUrl = process.env.APP_URL ?? `http://localhost:${port}`;
const hasPublicAppUrl = /^https:\/\//.test(appUrl) && !appUrl.includes("localhost");
const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

app.use(express.json());

app.get("/api/health", (_request, response) => response.json({ ok: true }));
app.get("/api/consultation-packs", (_request, response) => response.json({ packs: consultationPacks }));

const checkoutSchema = z.object({ packId: z.string() });

app.post("/api/webhooks/mercadopago", async (request, response) => {
  const accessToken = process.env.MERCADO_PAGO_ACCESS_TOKEN;
  const paymentId = typeof request.body?.data?.id === "string" ? request.body.data.id : "";
  if (!accessToken || !paymentId) return response.status(200).json({ received: true, verified: false });
  try {
    const payment = await getPaymentFromMercadoPago(paymentId, accessToken);
    if (!isApprovedPayment(payment)) return response.status(200).json({ received: true, verified: false, status: payment.status ?? "unknown" });
    console.log("[Mercado Pago] Pagamento aprovado aguardando persistência de créditos", { paymentId: payment.id, externalReference: payment.external_reference });
    return response.status(200).json({ received: true, verified: true, status: payment.status });
  } catch (error) {
    console.error("[Mercado Pago] Falha ao validar webhook", error);
    return response.status(200).json({ received: true, verified: false });
  }
});

app.post("/api/checkout", async (request, response) => {
  const parsed = checkoutSchema.safeParse(request.body);
  if (!parsed.success) return response.status(400).json({ message: "Selecione um pacote válido." });
  const pack = getPack(parsed.data.packId);
  if (!pack) return response.status(400).json({ message: "Pacote de consultas não encontrado." });

  const accessToken = process.env.MERCADO_PAGO_ACCESS_TOKEN;
  if (!accessToken) {
    return response.status(503).json({
      message: "O checkout ainda não foi configurado. Adicione MERCADO_PAGO_ACCESS_TOKEN nas variáveis de ambiente para habilitá-lo.",
    });
  }

  const externalReference = createExternalReference(pack.id);
  try {
    const mercadoPagoResponse = await fetch("https://api.mercadopago.com/checkout/preferences", {
      method: "POST",
      headers: { Authorization: `Bearer ${accessToken}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        items: [{ id: pack.id, title: `${pack.name} — Calculadora Penal`, quantity: 1, currency_id: "BRL", unit_price: pack.price }],
        external_reference: externalReference,
        ...(hasPublicAppUrl
          ? {
              back_urls: {
                success: `${appUrl}/?pagamento=sucesso`,
                failure: `${appUrl}/?pagamento=falhou`,
                pending: `${appUrl}/?pagamento=pendente`,
              },
              auto_return: "approved",
            }
          : {}),
        statement_descriptor: "CALCULADORA PENAL",
      }),
    });
    const preference = await mercadoPagoResponse.json() as { init_point?: string; sandbox_init_point?: string; message?: string };
    if (!mercadoPagoResponse.ok || !preference.init_point) {
      console.error("[Mercado Pago] Falha ao criar preferência", preference);
      return response.status(502).json({ message: "Não foi possível iniciar o checkout. Revise as configurações do Mercado Pago." });
    }
    return response.status(201).json({ checkoutUrl: preference.init_point, externalReference });
  } catch (error) {
    console.error("[Mercado Pago] Erro de comunicação", error);
    return response.status(502).json({ message: "O serviço de pagamento não respondeu. Tente novamente em instantes." });
  }
});

async function start() {
  if (process.env.NODE_ENV !== "production") {
    const { createServer } = await import("vite");
    const vite = await createServer({ root: rootDir, server: { middlewareMode: true }, appType: "spa" });
    app.use(vite.middlewares);
  } else {
    app.use(express.static(path.join(rootDir, "dist")));
    app.get("*", (_request, response) => response.sendFile(path.join(rootDir, "dist", "index.html")));
  }
  app.listen(port, () => console.log(`[Calculadora Penal] Servidor iniciado na porta ${port}`));
}

void start();
