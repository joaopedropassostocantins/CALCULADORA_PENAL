const packs = {
  avulsa: { name: "Consulta avulsa", price: 3.99, consultations: 1 },
  cinco: { name: "Pacote 5 consultas", price: 17.95, consultations: 5 },
  dez: { name: "Pacote 10 consultas", price: 31.90, consultations: 10 },
};

const brl = value => new Intl.NumberFormat("pt-BR", { style: "currency", currency: "BRL" }).format(value);
const number = id => Number(document.getElementById(id).value) || 0;
const duration = months => {
  const total = Math.max(0, Math.round(months));
  const years = Math.floor(total / 12);
  const rest = total % 12;
  if (!years) return `${rest} ${rest === 1 ? "mês" : "meses"}`;
  if (!rest) return `${years} ${years === 1 ? "ano" : "anos"}`;
  return `${years} ${years === 1 ? "ano" : "anos"} e ${rest} ${rest === 1 ? "mês" : "meses"}`;
};

function updateEstimate() {
  const minimum = Math.max(0, number("minimum"));
  const maximum = Math.max(minimum, number("maximum"));
  const baseInput = number("base");
  const base = Math.min(maximum, Math.max(minimum, baseInput));
  const second = Math.max(0, base * (1 + (number("aggravating") - number("mitigating")) / 100));
  const final = Math.max(0, second * (1 + (number("increase") - number("decrease")) / 100));

  document.getElementById("first-phase").textContent = `${base.toLocaleString("pt-BR", { maximumFractionDigits: 2 })} meses`;
  document.getElementById("second-phase").textContent = `${second.toLocaleString("pt-BR", { maximumFractionDigits: 2 })} meses`;
  document.getElementById("third-phase").textContent = `${final.toLocaleString("pt-BR", { maximumFractionDigits: 2 })} meses`;
  document.getElementById("final-months").textContent = final.toLocaleString("pt-BR", { maximumFractionDigits: 2 });
  document.getElementById("duration").textContent = duration(final);

  const warning = document.getElementById("warning");
  if (final > maximum) {
    warning.textContent = "O resultado excede a pena máxima informada. Revise os parâmetros e a aplicação das regras jurídicas.";
    warning.classList.remove("hidden");
  } else if (baseInput !== base) {
    warning.textContent = "A pena-base foi limitada ao intervalo mínimo/máximo informado.";
    warning.classList.remove("hidden");
  } else {
    warning.classList.add("hidden");
  }
}

document.querySelectorAll("#calculator-form input").forEach(input => input.addEventListener("input", updateEstimate));

function showCheckoutMessage(message, isError = false) {
  const element = document.getElementById("checkout-message");
  element.textContent = message;
  element.classList.remove("hidden", "error");
  if (isError) element.classList.add("error");
}

document.querySelectorAll("[data-pack]").forEach(button => button.addEventListener("click", async () => {
  const packId = button.dataset.pack;
  const pack = packs[packId];
  if (!pack) return;
  button.disabled = true;
  button.dataset.originalText = button.innerHTML;
  button.innerHTML = "Criando checkout...";
  showCheckoutMessage(`Solicitando a preferência para ${pack.name} (${brl(pack.price)}). O navegador não recebe o Access Token.`);
  try {
    const response = await fetch("/api/checkout", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ packId }) });
    const body = await response.json();
    if (!response.ok || !body.checkoutUrl) throw new Error(body.message || "O servidor não retornou um checkout válido.");
    showCheckoutMessage("Preferência criada. Você será redirecionado para o Checkout Pro do Mercado Pago.");
    window.location.assign(body.checkoutUrl);
  } catch (error) {
    showCheckoutMessage(error.message || "Não foi possível iniciar o checkout.", true);
    button.disabled = false;
    button.innerHTML = button.dataset.originalText;
  }
}));

document.getElementById("health-button").addEventListener("click", async event => {
  const button = event.currentTarget;
  const result = document.getElementById("health-result");
  button.disabled = true;
  result.textContent = "Consultando /api/health...";
  try {
    const response = await fetch("/api/health");
    const body = await response.json();
    result.textContent = body.ok ? "✓ Servidor local online. O proxy está disponível para o teste." : "Servidor respondeu com estado inesperado.";
  } catch {
    result.textContent = "✕ Não foi possível acessar o servidor local.";
  } finally {
    button.disabled = false;
  }
});

updateEstimate();
