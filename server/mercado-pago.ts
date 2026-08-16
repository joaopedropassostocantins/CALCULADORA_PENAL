import crypto from "node:crypto";

export type MercadoPagoPayment = {
  id: string;
  status?: string;
  external_reference?: string;
  transaction_amount?: number;
};

export function createExternalReference(packId: string) {
  return `consulta-${packId}-${crypto.randomUUID()}`;
}

export async function getPaymentFromMercadoPago(paymentId: string, accessToken: string) {
  const response = await fetch(`https://api.mercadopago.com/v1/payments/${encodeURIComponent(paymentId)}`, {
    headers: { Authorization: `Bearer ${accessToken}` },
  });
  if (!response.ok) throw new Error(`Mercado Pago retornou HTTP ${response.status}`);
  return await response.json() as MercadoPagoPayment;
}

export function isApprovedPayment(payment: MercadoPagoPayment) {
  return payment.status === "approved" && Boolean(payment.external_reference);
}
