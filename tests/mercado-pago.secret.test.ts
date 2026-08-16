import { describe, expect, it } from "vitest";

describe("credencial do Mercado Pago", () => {
  it("autentica em um endpoint leve sem criar cobrança ou preferência", async () => {
    const token = process.env.MERCADO_PAGO_ACCESS_TOKEN;
    expect(token, "MERCADO_PAGO_ACCESS_TOKEN precisa estar configurado no ambiente do teste").toBeTruthy();
    const response = await fetch("https://api.mercadopago.com/users/me", {
      headers: { Authorization: `Bearer ${token}` },
    });
    expect(response.status).toBe(200);
    const body = await response.json() as { id?: number; email?: string };
    expect(body.id).toBeTypeOf("number");
  });
});
