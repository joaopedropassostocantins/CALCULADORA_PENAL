import { useMemo, useState } from "react";
import { createRoot } from "react-dom/client";
import catalog from "./data/catalogoNormas.json";
import { estimatePenalty, type PenaltyInputs } from "./lib/calculator";
import { consultationPacks, formatBRL, type ConsultationPack } from "./data/pricing";
import type { LegalCatalog } from "./types";
import "./styles.css";

const legalCatalog = catalog as LegalCatalog;

const initialInputs: PenaltyInputs = {
  minimumMonths: 12,
  maximumMonths: 60,
  baseMonths: 24,
  aggravatingPercentage: 0,
  mitigatingPercentage: 0,
  increasePercentage: 0,
  decreasePercentage: 0,
};

type CheckoutState = "idle" | "loading" | "error";

function NumericField({ label, value, onChange, hint, suffix = "meses" }: { label: string; value: number; onChange: (value: number) => void; hint?: string; suffix?: string }) {
  return <label className="field"><span>{label}</span><span className="input-wrap"><input type="number" min="0" step="0.01" value={value} onChange={event => onChange(Number(event.target.value))} /><b>{suffix}</b></span>{hint && <small>{hint}</small>}</label>;
}

function App() {
  const [inputs, setInputs] = useState<PenaltyInputs>(initialInputs);
  const [search, setSearch] = useState("");
  const [selectedPack, setSelectedPack] = useState<ConsultationPack>(consultationPacks[0]);
  const [checkoutState, setCheckoutState] = useState<CheckoutState>("idle");
  const [checkoutMessage, setCheckoutMessage] = useState("");
  const estimate = useMemo(() => estimatePenalty(inputs), [inputs]);
  const paymentStatus = new URLSearchParams(window.location.search).get("pagamento");
  const filteredNorms = useMemo(() => {
    const query = search.trim().toLocaleLowerCase("pt-BR");
    if (!query) return legalCatalog.norms.slice(0, 6);
    return legalCatalog.norms.filter(norm => [norm.norm, norm.subject, norm.block].join(" ").toLocaleLowerCase("pt-BR").includes(query)).slice(0, 8);
  }, [search]);

  function updateInput(key: keyof PenaltyInputs, value: number) {
    setInputs(previous => ({ ...previous, [key]: Number.isFinite(value) ? value : 0 }));
  }

  async function startCheckout(pack: ConsultationPack) {
    setSelectedPack(pack);
    setCheckoutState("loading");
    setCheckoutMessage("");
    try {
      const response = await fetch("/api/checkout", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ packId: pack.id }) });
      const body = await response.json() as { checkoutUrl?: string; message?: string };
      if (!response.ok || !body.checkoutUrl) throw new Error(body.message ?? "Não foi possível iniciar o pagamento.");
      window.location.assign(body.checkoutUrl);
    } catch (error) {
      setCheckoutState("error");
      setCheckoutMessage(error instanceof Error ? error.message : "Não foi possível iniciar o pagamento.");
    }
  }

  return <div className="app-shell">
    <a className="skip-link" href="#calculadora">Ir para a calculadora</a>
    <header className="topbar"><div className="container nav"><a href="#inicio" className="brand"><span className="brand-mark">§</span><span>Calculadora<span>Penal</span></span></a><nav aria-label="Navegação principal"><a href="#calculadora">Simulador</a><a href="#normas">Normas</a><a href="#valores">Consultas</a></nav><a href="#valores" className="nav-cta">Fazer consulta</a></div></header>
    <main>
      <section id="inicio" className="hero"><div className="hero-grid container"><div><p className="eyebrow">DOSIMETRIA · REFERÊNCIA ESTRUTURADA</p><h1>Organize cenários de pena com <em>clareza técnica.</em></h1><p className="hero-copy">Uma ferramenta de apoio para estruturar os parâmetros informados, consultar normas e revisar a aritmética de uma simulação penal.</p><div className="hero-actions"><a href="#calculadora" className="button primary">Iniciar simulação <span>→</span></a><a href="#normas" className="button ghost">Explorar catálogo</a></div><p className="hero-meta">Base normativa importada <b>·</b> cálculo por parâmetros <b>·</b> consulta avulsa</p></div><aside className="legal-alert"><div className="alert-icon">!</div><div><strong>Uso informativo e profissional</strong><p>Esta calculadora não substitui a análise jurídica do caso concreto, a legislação vigente nem a revisão por advogado(a) habilitado(a).</p></div></aside></div></section>

      {paymentStatus && <section className={`payment-status ${paymentStatus}`}><div className="container"><strong>{paymentStatus === "sucesso" ? "Pagamento informado como aprovado." : paymentStatus === "pendente" ? "Pagamento pendente de confirmação." : "O pagamento não foi concluído."}</strong><span> A liberação de créditos deve ser confirmada pelo webhook do Mercado Pago antes do uso do relatório.</span></div></section>}

      <section id="calculadora" className="calculator-section"><div className="container"><div className="section-intro"><p className="eyebrow">SIMULAÇÃO PARAMÉTRICA</p><h2>Construa a linha de cálculo</h2><p>Informe os valores que serão avaliados no seu cenário. A ferramenta apenas processa a aritmética preenchida; não seleciona regras, percentuais ou teses jurídicas automaticamente.</p></div><div className="calculator-layout"><form className="calculator-form" onSubmit={event => event.preventDefault()}><div className="form-heading"><span className="step">01</span><div><h3>Faixa e pena-base</h3><p>Use meses para manter o cálculo consistente.</p></div></div><div className="field-grid"><NumericField label="Pena mínima" value={inputs.minimumMonths} onChange={value => updateInput("minimumMonths", value)} /><NumericField label="Pena máxima" value={inputs.maximumMonths} onChange={value => updateInput("maximumMonths", value)} /><NumericField label="Pena-base escolhida" value={inputs.baseMonths} onChange={value => updateInput("baseMonths", value)} hint="O sistema limita este valor à faixa indicada." /></div><div className="divider" /><div className="form-heading"><span className="step">02</span><div><h3>Segunda fase</h3><p>Informe percentuais conforme a sua metodologia.</p></div></div><div className="field-grid"><NumericField label="Agravantes" suffix="%" value={inputs.aggravatingPercentage} onChange={value => updateInput("aggravatingPercentage", value)} /><NumericField label="Atenuantes" suffix="%" value={inputs.mitigatingPercentage} onChange={value => updateInput("mitigatingPercentage", value)} /></div><div className="divider" /><div className="form-heading"><span className="step">03</span><div><h3>Terceira fase</h3><p>Inclua as frações convertidas em percentual.</p></div></div><div className="field-grid"><NumericField label="Causas de aumento" suffix="%" value={inputs.increasePercentage} onChange={value => updateInput("increasePercentage", value)} /><NumericField label="Causas de diminuição" suffix="%" value={inputs.decreasePercentage} onChange={value => updateInput("decreasePercentage", value)} /></div><p className="form-note">Atenção: concurso de crimes, continuidade delitiva, regimes, substituições e limites normativos demandam análise jurídica específica e não são inferidos automaticamente.</p></form>
        <aside className="result-panel" aria-live="polite"><div className="result-header"><div><p className="eyebrow">RESULTADO ESTIMADO</p><h3>Memória de cálculo</h3></div><span className="result-badge">Rascunho</span></div><div className="result-main"><span>Resultado em meses</span><strong>{estimate.finalMonths.toLocaleString("pt-BR", { maximumFractionDigits: 2 })}</strong><p>{estimate.formattedDuration}</p></div><div className="result-steps"><div><span>1ª fase</span><b>{estimate.firstPhase.toLocaleString("pt-BR", { maximumFractionDigits: 2 })} meses</b></div><div><span>2ª fase</span><b>{estimate.secondPhase.toLocaleString("pt-BR", { maximumFractionDigits: 2 })} meses</b></div><div><span>3ª fase</span><b>{estimate.finalMonths.toLocaleString("pt-BR", { maximumFractionDigits: 2 })} meses</b></div></div>{estimate.warnings.length > 0 && <div className="warnings">{estimate.warnings.map(warning => <p key={warning}>• {warning}</p>)}</div>}<a href="#valores" className="button result-cta">Desbloquear relatório detalhado <span>→</span></a><p className="result-note">A visualização é uma estimativa paramétrica. Valide o resultado com a fonte oficial e revisão técnica.</p></aside></div></div></section>

      <section id="normas" className="norms-section"><div className="container"><div className="section-row"><div><p className="eyebrow">CATÁLOGO NORMATIVO</p><h2>Referências para a sua conferência</h2><p>Catálogo estruturado a partir da planilha enviada, com links de acesso às fontes oficiais.</p></div><div className="catalog-counter"><strong>{legalCatalog.norms.length}</strong><span>normas catalogadas</span></div></div><label className="search-box"><span aria-hidden="true">⌕</span><input value={search} onChange={event => setSearch(event.target.value)} placeholder="Busque por lei, tema ou objeto normativo" aria-label="Buscar no catálogo normativo" /></label><div className="norm-grid">{filteredNorms.map(norm => <article key={`${norm.norm}-${norm.subject}`} className="norm-card"><p>{norm.block}</p><h3>{norm.norm}</h3><span className="nature-tag">Natureza {norm.nature}</span><p className="norm-subject">{norm.subject}</p><a href={norm.officialUrl} target="_blank" rel="noreferrer">Abrir fonte oficial <span>↗</span></a></article>)}</div><p className="catalog-note">A exibição deste catálogo não confirma vigência, redação atual ou aplicabilidade ao caso concreto. Consulte a fonte oficial antes de utilizar qualquer referência.</p></div></section>

      <section className="reference-strip"><div className="container"><div><span>15</span><p>súmulas vinculantes<br />catalogadas</p></div><div><span>{legalCatalog.courtStatements.length}</span><p>súmulas STF e STJ<br />para consulta</p></div><div><span>{legalCatalog.precedents.length}</span><p>precedentes vinculantes<br />estruturados</p></div><a href="#normas">Acessar referências <span>→</span></a></div></section>

      <section id="valores" className="pricing-section"><div className="container"><div className="pricing-intro"><p className="eyebrow">ACESSO POR CONSULTA</p><h2>Escolha a quantidade de consultas</h2><p>Sem assinatura recorrente. Cada opção libera somente a quantidade de usos informada.</p><aside><strong>Valores hipotéticos.</strong> As condições comerciais abaixo são sugestões para prototipagem e devem ser confirmadas antes da operação.</aside></div><div className="pricing-grid">{consultationPacks.map(pack => <article key={pack.id} className={`price-card ${pack.featured ? "featured" : ""}`}><div>{pack.featured && <span className="popular">Mais escolhido</span>}<h3>{pack.name}</h3><p>{pack.description}</p></div><div className="price"><strong>{formatBRL(pack.price)}</strong><span>{pack.consultations} {pack.consultations === 1 ? "consulta" : "consultas"}</span></div><p className="unit-value">{formatBRL(pack.price / pack.consultations)} por consulta</p><button onClick={() => startCheckout(pack)} disabled={checkoutState === "loading"} className="button price-button">{checkoutState === "loading" && selectedPack.id === pack.id ? "Iniciando checkout..." : pack.id === "avulsa" ? "Pagar consulta avulsa" : `Comprar ${pack.consultations} consultas`} <span>→</span></button></article>)}</div>{checkoutState === "error" && <p className="checkout-error" role="alert">{checkoutMessage}</p>}<div className="payment-note"><span className="lock">⌁</span><p><strong>Checkout Mercado Pago.</strong> O fluxo está preparado para redirecionar ao Checkout Pro, onde o comprador pode selecionar os meios liberados à sua conta, incluindo PIX e cartão quando disponíveis.</p></div></div></section>
    </main>
    <footer><div className="container footer-grid"><div><a href="#inicio" className="brand footer-brand"><span className="brand-mark">§</span><span>Calculadora<span>Penal</span></span></a><p>Ferramenta de organização e conferência para profissionais do Direito.</p></div><div><strong>Importante</strong><p>Não substitui parecer jurídico, consulta profissional, legislação atualizada ou análise do processo.</p></div><div><strong>Fonte do catálogo</strong><p>Planilha normativa fornecida pelo usuário, com endereços oficiais de referência.</p></div></div><div className="container footer-bottom">© 2026 Calculadora Penal · Ambiente informativo e de prototipagem.</div></footer>
  </div>;
}

createRoot(document.getElementById("root")!).render(<App />);
