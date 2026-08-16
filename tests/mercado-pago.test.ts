import { describe, expect, it } from "vitest";
import { isApprovedPayment } from "../server/mercado-pago";

describe("validação de pagamento Mercado Pago", () => {
  it("só considera aprovado quando o status é approved e há referência externa", () => {
    expect(isApprovedPayment({ id: "1", status: "approved", external_reference: "consulta-avulsa-1" })).toBe(true);
    expect(isApprovedPayment({ id: "2", status: "pending", external_reference: "consulta-avulsa-2" })).toBe(false);
    expect(isApprovedPayment({ id: "3", status: "approved" })).toBe(false);
  });
});
