"use client";

import { FormEvent, useMemo, useState } from "react";
import publicCatalog from "../data/tiposPenais.public.json";

type Plan = {
  name: string;
  quantity: number;
  price: number;
  description: string;
  featured?: boolean;
};

type CrimeEntry = {
  id: string;
  name: string;
  article: string;
  law: string;
  category: string;
  minimum: number;
  maximum: number;
  penalty: string;
  keywords: string[];
  sourceUrl: string;
  validationState: string;
  canCalculate: boolean;
};

type NarrativeAnalysis = {
  candidates: CrimeEntry[];
  signals: { label: string; detail: string }[];
  caveats: string[];
};

const crimeCatalog = publicCatalog.registros as CrimeEntry[];

function normalizeText(value: string) {
  return value.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
}

function analyzeNarrativeText(narrative: string): NarrativeAnalysis {
  const text = normalizeText(narrative);
  const scores = new Map<string, number>();
  const add = (id: string, points: number) => scores.set(id, (scores.get(id) ?? 0) + points);

  crimeCatalog.forEach((entry) => {
    entry.keywords.forEach((keyword) => {
      if (text.includes(normalizeText(keyword))) add(entry.id, 3);
    });
  });

  const violence = /(violencia|grave ameaca|arma|faca|revolver|pistola|agred)/.test(text);
  if (/(subtraiu|levou o celular|levando (o|seu|a|sua)|tomou o bem|pegou o bem|assalto)/.test(text)) add(violence ? "cp-157" : "cp-155", 7);
  if (/(enganou|golpe|fraude|vantagem ilicita|pix falso)/.test(text)) add("cp-171", 5);
  if (/(matou|morte|faleceu|disparo fatal)/.test(text)) add("cp-121", 5);
  if (/(menor de 14|crianca de \d+ anos)/.test(text) && /(sexual|libidinoso|relacao)/.test(text)) add("cp-217a", 7);
  if (/(drogas|cocaina|maconha|entorpecente)/.test(text) && /(vendeu|comercializ|tráfico|trafico|transportava)/.test(text)) add("drogas-33", 6);
  if (/(servidor|funcionario publico|agente publico)/.test(text) && /(exigiu|cobrou)/.test(text)) add("cp-316", 6);
  if (/(servidor|funcionario publico|agente publico)/.test(text) && /(solicitou|recebeu)/.test(text)) add("cp-317", 6);
  if (/(ofereceu|prometeu)/.test(text) && /(propina|vantagem.*servidor)/.test(text)) add("cp-333", 6);
  if (scores.has("cp-157") || scores.has("cp-158")) scores.delete("cp-147");

  const signals: NarrativeAnalysis["signals"] = [];
  if (/(tentou|nao conseguiu|nao consumou|vitima sobreviveu)/.test(text)) signals.push({ label: "Possível tentativa", detail: "Avaliar início de execução, não consumação e circunstâncias alheias à vontade do agente." });
  if (violence) signals.push({ label: "Violência ou grave ameaça", detail: "O meio de execução pode alterar o enquadramento ou configurar causa de aumento." });
  if (/(arma de fogo|revolver|pistola)/.test(text)) signals.push({ label: "Arma de fogo", detail: "Verificar natureza da arma, perícia, potencialidade e eventual majorante ou crime autônomo." });
  if (/(duas pessoas|dois agentes|tres pessoas|comparsa|em conjunto|juntos)/.test(text)) signals.push({ label: "Concurso de agentes", detail: "Confirmar vínculo subjetivo, contribuição individual e previsão específica de aumento ou qualificadora." });
  if (/(menor de 14|crianca|idoso|maior de 60|deficiencia|vulneravel)/.test(text)) signals.push({ label: "Vulnerabilidade da vítima", detail: "Idade ou condição da vítima pode mudar o tipo penal ou a fração aplicável." });
  if (/(confessou|confissao)/.test(text)) signals.push({ label: "Confissão narrada", detail: "Pode haver atenuante, sujeita à forma, utilidade e orientação jurisprudencial." });
  if (/(reparou o dano|devolveu|restituiu)/.test(text)) signals.push({ label: "Reparação ou restituição", detail: "Avaliar arrependimento posterior ou outro efeito jurídico conforme o momento e os requisitos." });

  const candidates = [...scores.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, 3)
    .map(([id]) => crimeCatalog.find((entry) => entry.id === id))
    .filter((entry): entry is CrimeEntry => Boolean(entry));

  return {
    candidates,
    signals,
    caveats: [
      "A narrativa pode admitir enquadramentos alternativos, concurso de crimes ou absorção.",
      "Qualificadoras, majorantes, minorantes e jurisprudência devem ser confirmadas antes do cálculo.",
      "O protótipo não substitui a leitura dos autos nem a revisão por profissional habilitado.",
    ],
  };
}

const plans: Plan[] = [
  {
    name: "Consulta avulsa",
    quantity: 1,
    price: 3.99,
    description: "Para testar ou resolver uma necessidade pontual.",
  },
  {
    name: "Pacote essencial",
    quantity: 10,
    price: 29.9,
    description: "Para estudantes e profissionais com uso recorrente.",
    featured: true,
  },
  {
    name: "Pacote profissional",
    quantity: 30,
    price: 69.9,
    description: "Mais economia para a rotina jurídica.",
  },
  {
    name: "Pacote escritório",
    quantity: 100,
    price: 149.9,
    description: "Volume maior para equipes e escritórios.",
  },
];

const thirdPhaseOptions = [
  { label: "Sem causa de aumento ou diminuição", value: 1 },
  { label: "Aumento de 1/3", value: 4 / 3 },
  { label: "Aumento de 1/2", value: 1.5 },
  { label: "Aumento de 2/3", value: 5 / 3 },
  { label: "Pena em dobro", value: 2 },
  { label: "Diminuição de 1/6", value: 5 / 6 },
  { label: "Diminuição de 1/3", value: 2 / 3 },
  { label: "Diminuição de 1/2", value: 0.5 },
  { label: "Diminuição de 2/3", value: 1 / 3 },
];

const currency = new Intl.NumberFormat("pt-BR", {
  style: "currency",
  currency: "BRL",
});

function formatPenalty(decimalYears: number) {
  const totalDays = Math.max(0, Math.round(decimalYears * 365));
  const years = Math.floor(totalDays / 365);
  const remainingAfterYears = totalDays % 365;
  const months = Math.floor(remainingAfterYears / 30);
  const days = remainingAfterYears % 30;
  const parts = [];

  if (years) parts.push(`${years} ${years === 1 ? "ano" : "anos"}`);
  if (months) parts.push(`${months} ${months === 1 ? "mês" : "meses"}`);
  if (days || parts.length === 0) parts.push(`${days} ${days === 1 ? "dia" : "dias"}`);

  return parts.join(", ");
}

export default function Home() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [crime, setCrime] = useState("Homicídio simples");
  const [minimum, setMinimum] = useState(6);
  const [maximum, setMaximum] = useState(20);
  const [unfavorable, setUnfavorable] = useState(0);
  const [aggravating, setAggravating] = useState(0);
  const [mitigating, setMitigating] = useState(0);
  const [thirdPhase, setThirdPhase] = useState(1);
  const [hasResult, setHasResult] = useState(false);
  const [selectedPlan, setSelectedPlan] = useState<Plan | null>(null);
  const [paymentMethod, setPaymentMethod] = useState<"pix" | "card">("pix");
  const [checkoutNotice, setCheckoutNotice] = useState(false);
  const [catalogSearch, setCatalogSearch] = useState("");
  const [catalogCategory, setCatalogCategory] = useState("Todos");
  const [narrative, setNarrative] = useState("");
  const [narrativeAnalysis, setNarrativeAnalysis] = useState<NarrativeAnalysis | null>(null);

  const catalogCategories = useMemo(
    () => ["Todos", ...Array.from(new Set(crimeCatalog.map((entry) => entry.category)))],
    [],
  );

  const filteredCrimes = useMemo(() => {
    const query = normalizeText(catalogSearch.trim());
    return crimeCatalog.filter((entry) => {
      const matchesCategory = catalogCategory === "Todos" || entry.category === catalogCategory;
      const haystack = normalizeText(`${entry.name} ${entry.article} ${entry.law} ${entry.category} ${entry.keywords.join(" ")}`);
      return matchesCategory && (!query || haystack.includes(query));
    });
  }, [catalogCategory, catalogSearch]);

  const calculation = useMemo(() => {
    const safeMinimum = Math.max(0, Number(minimum) || 0);
    const safeMaximum = Math.max(safeMinimum, Number(maximum) || safeMinimum);
    const base = safeMinimum + ((safeMaximum - safeMinimum) / 8) * unfavorable;
    const secondPhaseVariation = (aggravating - mitigating) / 6;
    const intermediate = Math.max(safeMinimum, base * (1 + secondPhaseVariation));
    const final = Math.max(0, intermediate * thirdPhase);

    return { base, intermediate, final };
  }, [minimum, maximum, unfavorable, aggravating, mitigating, thirdPhase]);

  function calculate(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setHasResult(true);
  }

  function choosePlan(plan: Plan) {
    setSelectedPlan(plan);
    setPaymentMethod("pix");
    setCheckoutNotice(false);
  }

  function useCrime(entry: CrimeEntry) {
    if (!entry.canCalculate) return;
    setCrime(entry.name);
    setMinimum(entry.minimum);
    setMaximum(entry.maximum);
    setHasResult(false);
    document.getElementById("calculadora")?.scrollIntoView({ behavior: "smooth" });
  }

  function analyzeNarrative(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setNarrativeAnalysis(analyzeNarrativeText(narrative));
  }

  return (
    <main>
      <header className="site-header">
        <div className="shell header-inner">
          <a className="brand" href="#inicio" aria-label="Calculadora Penal — início">
            <span className="brand-mark" aria-hidden="true">§</span>
            <span>
              <strong>Calculadora</strong>
              <small>Penal</small>
            </span>
          </a>

          <button
            className="menu-button"
            type="button"
            aria-expanded={menuOpen}
            aria-controls="main-navigation"
            onClick={() => setMenuOpen((open) => !open)}
          >
            <span />
            <span />
            <span />
            <span className="sr-only">Abrir menu</span>
          </button>

          <nav id="main-navigation" className={menuOpen ? "nav open" : "nav"} aria-label="Navegação principal">
            <a href="#como-funciona" onClick={() => setMenuOpen(false)}>Como funciona</a>
            <a href="#catalogo" onClick={() => setMenuOpen(false)}>Crimes</a>
            <a href="#narrativa" onClick={() => setMenuOpen(false)}>Analisar fato</a>
            <a href="#calculadora" onClick={() => setMenuOpen(false)}>Calculadora</a>
            <a href="#planos" onClick={() => setMenuOpen(false)}>Planos</a>
            <a href="#duvidas" onClick={() => setMenuOpen(false)}>Dúvidas</a>
          </nav>

          <a className="button button-small header-cta" href="#calculadora">
            Fazer simulação
          </a>
        </div>
      </header>

      <section className="hero" id="inicio">
        <div className="hero-grid shell">
          <div className="hero-copy">
            <p className="eyebrow"><span /> Dosimetria penal, fase por fase</p>
            <h1>Transforme cálculos complexos em uma análise <em>clara.</em></h1>
            <p className="hero-lead">
              Organize as três fases da dosimetria, visualize os critérios utilizados e gere uma estimativa didática em poucos minutos.
            </p>
            <div className="hero-actions">
              <a className="button" href="#calculadora">Simular agora</a>
              <a className="text-link" href="#como-funciona">Entender o método <span aria-hidden="true">→</span></a>
            </div>
            <div className="trust-row" aria-label="Características do serviço">
              <span>✓ Em português</span>
              <span>✓ Sem assinatura</span>
              <span>✓ Resultado explicável</span>
            </div>
          </div>

          <div className="hero-visual" aria-label="Prévia das três fases da dosimetria">
            <div className="orb orb-one" />
            <div className="orb orb-two" />
            <article className="result-card">
              <div className="result-topline">
                <span>Simulação de pena</span>
                <span className="status-dot">Demonstrativo</span>
              </div>
              <p className="result-label">Pena estimada</p>
              <strong className="result-number">08 <small>anos</small> 04 <small>meses</small></strong>
              <div className="phase-list">
                <div>
                  <span className="phase-number">1</span>
                  <p><strong>Pena-base</strong><small>Circunstâncias judiciais</small></p>
                  <b>7a 2m</b>
                </div>
                <div>
                  <span className="phase-number">2</span>
                  <p><strong>Pena intermediária</strong><small>Agravantes e atenuantes</small></p>
                  <b>6a 3m</b>
                </div>
                <div>
                  <span className="phase-number">3</span>
                  <p><strong>Pena definitiva</strong><small>Causas de aumento/diminuição</small></p>
                  <b>8a 4m</b>
                </div>
              </div>
              <div className="document-lines"><i /><i /><i /></div>
            </article>
            <span className="floating-note note-one">Art. 59</span>
            <span className="floating-note note-two">Art. 68</span>
          </div>
        </div>
      </section>

      <section className="legal-strip" aria-label="Aviso importante">
        <div className="shell legal-strip-inner">
          <span className="legal-icon" aria-hidden="true">!</span>
          <p>
            <strong>Aviso importante:</strong> todos os valores e resultados fornecidos são sugestões hipotéticas e demonstrativas. Não representam decisão judicial nem substituem a análise individualizada de profissional habilitado.
          </p>
        </div>
      </section>

      <section className="section shell" id="como-funciona">
        <div className="section-heading split-heading">
          <div>
            <p className="eyebrow"><span /> Método organizado</p>
            <h2>Do tipo penal ao resultado, sem perder o raciocínio.</h2>
          </div>
          <p>A ferramenta transforma os dados informados em uma memória de cálculo simples de revisar, explicar e conferir.</p>
        </div>

        <div className="steps-grid">
          <article className="step-card">
            <span className="step-index">01</span>
            <div className="step-icon" aria-hidden="true">⌨</div>
            <h3>Informe os parâmetros</h3>
            <p>Insira as penas mínima e máxima, as circunstâncias judiciais e os fatores das fases seguintes.</p>
          </article>
          <article className="step-card featured-step">
            <span className="step-index">02</span>
            <div className="step-icon" aria-hidden="true">⚖</div>
            <h3>Revise cada fase</h3>
            <p>Acompanhe pena-base, pena intermediária e pena definitiva com os critérios separados.</p>
          </article>
          <article className="step-card">
            <span className="step-index">03</span>
            <div className="step-icon" aria-hidden="true">✓</div>
            <h3>Use como referência</h3>
            <p>Obtenha uma estimativa didática para estudo e conferência, sempre sujeita à validação jurídica.</p>
          </article>
        </div>
      </section>

      <section className="catalog-section" id="catalogo">
        <div className="shell">
          <div className="section-heading split-heading catalog-heading">
            <div>
              <p className="eyebrow"><span /> Base penal estruturada</p>
              <h2>Escolha o crime sem digitar penas ou artigos.</h2>
            </div>
            <p>O catálogo conecta cada tipo penal à faixa abstrata de pena e envia os parâmetros diretamente à calculadora.</p>
          </div>

          <div className="catalog-toolbar">
            <label>
              <span className="sr-only">Pesquisar crime, artigo ou lei</span>
              <input
                type="search"
                placeholder="Pesquisar crime, artigo ou lei..."
                value={catalogSearch}
                onChange={(event) => setCatalogSearch(event.target.value)}
              />
            </label>
            <label>
              <span className="sr-only">Filtrar por categoria</span>
              <select value={catalogCategory} onChange={(event) => setCatalogCategory(event.target.value)}>
                {catalogCategories.map((category) => <option key={category}>{category}</option>)}
              </select>
            </label>
            <span className="catalog-count">{filteredCrimes.length} tipos exibidos</span>
          </div>

          <div className="crime-catalog" aria-live="polite">
            {filteredCrimes.map((entry) => (
              <article className="crime-card" key={entry.id}>
                <div className="crime-card-top">
                  <div className="crime-card-badges">
                    <span>{entry.category}</span>
                    <span className={entry.validationState === "confirmada" ? "catalog-status is-valid" : "catalog-status is-pending"}>
                      {entry.validationState === "confirmada" ? "Conferido" : "Pendente"}
                    </span>
                  </div>
                  <b>{entry.article}</b>
                </div>
                <h3>{entry.name}</h3>
                <p>{entry.penalty}</p>
                <div className="crime-source">
                  <span>{entry.law}</span>
                  <div>
                    <a href={entry.sourceUrl} target="_blank" rel="noreferrer">Fonte oficial ↗</a>
                    <button type="button" onClick={() => useCrime(entry)} disabled={!entry.canCalculate}>Usar no cálculo →</button>
                  </div>
                </div>
              </article>
            ))}
            {filteredCrimes.length === 0 && (
              <div className="catalog-empty"><strong>Nenhum resultado</strong><p>Tente pesquisar pelo nome, artigo ou diploma legal.</p></div>
            )}
          </div>

          <div className="catalog-disclaimer">
            <strong>Catálogo público com validação de inventário</strong>
            <p>Esta interface exibe registros exportados da fonte canônica com o estado de conferência visível; pendências não podem alimentar a calculadora. O catálogo nacional permanece em expansão e não deve ser tratado como lista integral enquanto houver módulos pendentes.</p>
          </div>
        </div>
      </section>

      <section className="narrative-section" id="narrativa">
        <div className="shell">
          <div className="section-heading centered narrative-heading">
            <p className="eyebrow light"><span /> Triagem explicável da narrativa</p>
            <h2>Conte o fato. O sistema organiza as hipóteses.</h2>
            <p>O modelo identifica possíveis enquadramentos e circunstâncias, mas exige sua confirmação antes de preencher a dosimetria.</p>
          </div>

          <div className="narrative-grid">
            <form className="narrative-form" onSubmit={analyzeNarrative}>
              <div className="narrative-form-title"><span>✦</span><div><strong>Narrativa do fato</strong><small>Não informe nomes, CPF ou outros dados pessoais.</small></div></div>
              <label>
                <span className="sr-only">Descreva objetivamente o que aconteceu</span>
                <textarea
                  value={narrative}
                  onChange={(event) => setNarrative(event.target.value)}
                  placeholder="Ex.: Dois agentes abordaram a vítima com uma arma de fogo e levaram seu celular. O bem foi recuperado depois..."
                  minLength={20}
                  required
                />
              </label>
              <div className="narrative-actions">
                <button className="example-button" type="button" onClick={() => setNarrative("Dois agentes abordaram a vítima com uma arma de fogo e grave ameaça, levando seu celular. O objeto foi recuperado e um dos agentes confessou os fatos.")}>Usar exemplo</button>
                <button className="button" type="submit">Analisar narrativa</button>
              </div>
              <p className="privacy-hint">A demonstração é processada no navegador e não envia o texto a um serviço externo.</p>
            </form>

            <aside className="narrative-result" aria-live="polite">
              {!narrativeAnalysis ? (
                <div className="analysis-empty">
                  <span>§</span>
                  <h3>A análise aparecerá aqui</h3>
                  <p>Você verá crimes candidatos, sinais jurídicos detectados e pontos que exigem confirmação.</p>
                </div>
              ) : (
                <div className="analysis-content">
                  <div className="analysis-header"><div><small>Resultado da triagem</small><strong>{narrativeAnalysis.candidates.length ? `${narrativeAnalysis.candidates.length} hipóteses encontradas` : "Narrativa insuficiente"}</strong></div><span>Revisão obrigatória</span></div>

                  <div className="candidate-list">
                    <h3>Enquadramentos candidatos</h3>
                    {narrativeAnalysis.candidates.length ? narrativeAnalysis.candidates.map((entry, index) => (
                      <article key={entry.id}>
                        <span>{index + 1}</span>
                        <div><strong>{entry.name}</strong><small>{entry.article} · {entry.penalty}</small></div>
                        <button type="button" onClick={() => useCrime(entry)} disabled={!entry.canCalculate}>{entry.canCalculate ? "Selecionar" : "Pendente"}</button>
                      </article>
                    )) : <p className="no-candidate">Não foi possível sugerir um tipo com segurança. Acrescente conduta, meio, resultado e contexto.</p>}
                  </div>

                  <div className="signal-list">
                    <h3>Sinais identificados</h3>
                    {narrativeAnalysis.signals.length ? narrativeAnalysis.signals.map((signal) => (
                      <div key={signal.label}><span>✓</span><p><strong>{signal.label}</strong><small>{signal.detail}</small></p></div>
                    )) : <p className="no-candidate">Nenhuma circunstância adicional foi identificada automaticamente.</p>}
                  </div>

                  <details className="analysis-caveats">
                    <summary>Premissas e limites da análise</summary>
                    <ul>{narrativeAnalysis.caveats.map((caveat) => <li key={caveat}>{caveat}</li>)}</ul>
                  </details>
                </div>
              )}
            </aside>
          </div>
        </div>
      </section>

      <section className="calculator-section" id="calculadora">
        <div className="shell">
          <div className="section-heading centered">
            <p className="eyebrow"><span /> Prévia gratuita</p>
            <h2>Experimente a lógica da calculadora</h2>
            <p>Preencha os parâmetros abaixo. O método demonstrativo usa 1/8 do intervalo na primeira fase e 1/6 por ocorrência na segunda.</p>
          </div>

          <div className="calculator-layout">
            <form className="calculator-form" onSubmit={calculate}>
              <div className="form-section-title">
                <span>1</span>
                <div><strong>Pena-base</strong><small>Art. 59 do Código Penal</small></div>
              </div>

              <label className="field field-wide">
                <span>Infração penal</span>
                <input value={crime} onChange={(event) => setCrime(event.target.value)} placeholder="Ex.: Homicídio simples" />
              </label>

              <div className="field-row">
                <label className="field">
                  <span>Pena mínima (anos)</span>
                  <input type="number" min="0" step="0.1" value={minimum} onChange={(event) => setMinimum(Number(event.target.value))} />
                </label>
                <label className="field">
                  <span>Pena máxima (anos)</span>
                  <input type="number" min="0" step="0.1" value={maximum} onChange={(event) => setMaximum(Number(event.target.value))} />
                </label>
              </div>

              <label className="field field-wide">
                <span>Circunstâncias judiciais desfavoráveis <b>{unfavorable} de 8</b></span>
                <input className="range" type="range" min="0" max="8" value={unfavorable} onChange={(event) => setUnfavorable(Number(event.target.value))} />
                <div className="range-labels"><small>Nenhuma</small><small>Todas</small></div>
              </label>

              <div className="form-divider" />
              <div className="form-section-title compact-title">
                <span>2</span>
                <div><strong>Agravantes e atenuantes</strong><small>Segunda fase</small></div>
              </div>

              <div className="field-row">
                <label className="field">
                  <span>Nº de agravantes</span>
                  <input type="number" min="0" max="6" value={aggravating} onChange={(event) => setAggravating(Number(event.target.value))} />
                </label>
                <label className="field">
                  <span>Nº de atenuantes</span>
                  <input type="number" min="0" max="6" value={mitigating} onChange={(event) => setMitigating(Number(event.target.value))} />
                </label>
              </div>

              <div className="form-divider" />
              <div className="form-section-title compact-title">
                <span>3</span>
                <div><strong>Aumento ou diminuição</strong><small>Terceira fase</small></div>
              </div>

              <label className="field field-wide">
                <span>Fração aplicável</span>
                <select value={thirdPhase} onChange={(event) => setThirdPhase(Number(event.target.value))}>
                  {thirdPhaseOptions.map((option) => (
                    <option key={option.label} value={option.value}>{option.label}</option>
                  ))}
                </select>
              </label>

              <button className="button calculate-button" type="submit">Calcular estimativa</button>
            </form>

            <aside className={hasResult ? "calculation-result revealed" : "calculation-result"} aria-live="polite">
              <div className="result-placeholder">
                <span aria-hidden="true">§</span>
                <h3>{hasResult ? crime || "Simulação penal" : "Seu resultado aparecerá aqui"}</h3>
                <p>{hasResult ? "Memória demonstrativa das três fases" : "Preencha os campos e clique em “Calcular estimativa”."}</p>
              </div>

              {hasResult && (
                <div className="live-result">
                  <div className="live-result-main">
                    <small>Pena definitiva estimada</small>
                    <strong>{formatPenalty(calculation.final)}</strong>
                    <span>Sugestão hipotética</span>
                  </div>
                  <ol className="live-phases">
                    <li><span>1ª fase</span><strong>{formatPenalty(calculation.base)}</strong></li>
                    <li><span>2ª fase</span><strong>{formatPenalty(calculation.intermediate)}</strong></li>
                    <li><span>3ª fase</span><strong>{formatPenalty(calculation.final)}</strong></li>
                  </ol>
                  <div className="result-warning">
                    <strong>Como interpretar</strong>
                    <p>O resultado é uma aproximação matemática. O julgador deve fundamentar a fração e pode adotar metodologia diversa conforme o caso e a jurisprudência aplicável.</p>
                  </div>
                  <button className="button report-button" type="button" onClick={() => choosePlan(plans[0])}>
                    Gerar relatório completo · R$ 3,99
                  </button>
                </div>
              )}
            </aside>
          </div>
        </div>
      </section>

      <section className="benefits-section">
        <div className="shell benefits-grid">
          <div>
            <p className="eyebrow light"><span /> Pensada para o Brasil</p>
            <h2>Mais transparência para estudar, conferir e argumentar.</h2>
            <p className="benefits-lead">Uma experiência simples para quem precisa visualizar o caminho do cálculo sem tratar a matemática como resposta jurídica definitiva.</p>
          </div>
          <div className="benefits-list">
            <article><span>01</span><div><strong>Memória de cálculo</strong><p>Entenda de onde saiu cada resultado e identifique rapidamente os pontos que merecem revisão.</p></div></article>
            <article><span>02</span><div><strong>Critérios editáveis</strong><p>Ajuste circunstâncias e frações para comparar cenários possíveis sem refazer tudo do zero.</p></div></article>
            <article><span>03</span><div><strong>Limites bem definidos</strong><p>Avisos claros evitam que a estimativa seja confundida com sentença, parecer ou garantia de resultado.</p></div></article>
          </div>
        </div>
      </section>

      <section className="section pricing-section shell" id="planos">
        <div className="section-heading centered">
          <p className="eyebrow"><span /> Pagamento único</p>
          <h2>Escolha apenas quantas consultas precisa.</h2>
          <p>Sem mensalidade e sem alternância mensal/anual. Compre créditos conforme o seu uso.</p>
        </div>

        <div className="single-call-banner">
          <div>
            <span className="single-call-icon" aria-hidden="true">1</span>
            <p><strong>Consulta avulsa por R$ 3,99</strong><small>Pagamento por Pix ou cartão no checkout do Mercado Pago.</small></p>
          </div>
          <button className="button" type="button" onClick={() => choosePlan(plans[0])}>Comprar 1 consulta</button>
        </div>

        <div className="plans-grid">
          {plans.slice(1).map((plan) => (
            <article className={plan.featured ? "plan-card featured-plan" : "plan-card"} key={plan.name}>
              {plan.featured && <span className="popular-label">Mais escolhido</span>}
              <p className="plan-name">{plan.name}</p>
              <div className="plan-quantity"><strong>{plan.quantity}</strong><span>consultas</span></div>
              <p className="plan-price">{currency.format(plan.price)} <small>pagamento único</small></p>
              <p className="plan-description">{plan.description}</p>
              <ul>
                <li>✓ Memória das três fases</li>
                <li>✓ Comparação de cenários</li>
                <li>✓ Resultado em português</li>
              </ul>
              <button className={plan.featured ? "button" : "button button-outline"} type="button" onClick={() => choosePlan(plan)}>
                Escolher {plan.quantity} consultas
              </button>
              <small className="unit-price">{currency.format(plan.price / plan.quantity)} por consulta</small>
            </article>
          ))}
        </div>
        <p className="pricing-note">Os preços dos pacotes são uma proposta comercial inicial e podem ser ajustados antes do lançamento.</p>
      </section>

      <section className="faq-section" id="duvidas">
        <div className="shell faq-grid">
          <div className="faq-intro">
            <p className="eyebrow"><span /> Dúvidas frequentes</p>
            <h2>Antes de fazer sua consulta.</h2>
            <p>Transparência jurídica e comercial desde o primeiro acesso.</p>
          </div>
          <div className="faq-list">
            <details open>
              <summary>O resultado da calculadora é uma sentença?</summary>
              <p>Não. É uma estimativa hipotética baseada nos parâmetros informados. A dosimetria real depende da fundamentação judicial, das provas e da jurisprudência aplicável.</p>
            </details>
            <details>
              <summary>Existe assinatura mensal?</summary>
              <p>Não. A proposta usa somente pacotes por quantidade de consultas, com pagamento único e consumo conforme a necessidade.</p>
            </details>
            <details>
              <summary>Como funciona o pagamento?</summary>
              <p>A consulta avulsa custa R$ 3,99. O checkout será processado pelo Mercado Pago, com opção de Pix ou cartão, após a integração da conta comercial.</p>
            </details>
            <details>
              <summary>Posso informar dados pessoais do processo?</summary>
              <p>Evite inserir nomes, documentos ou outros dados pessoais desnecessários. Use descrições genéricas até que a política de privacidade e a estrutura definitiva de tratamento de dados estejam publicadas.</p>
            </details>
          </div>
        </div>
      </section>

      <section className="final-cta">
        <div className="shell final-cta-inner">
          <div>
            <p className="eyebrow light"><span /> Comece com uma consulta</p>
            <h2>Uma forma mais clara de visualizar a dosimetria.</h2>
          </div>
          <button className="button button-light" type="button" onClick={() => choosePlan(plans[0])}>
            Consultar por R$ 3,99
          </button>
        </div>
      </section>

      <footer>
        <div className="shell footer-grid">
          <a className="brand footer-brand" href="#inicio">
            <span className="brand-mark" aria-hidden="true">§</span>
            <span><strong>Calculadora</strong><small>Penal</small></span>
          </a>
          <p>Ferramenta educacional de apoio à organização do cálculo penal.</p>
          <div className="footer-links">
            <a href="#calculadora">Calculadora</a>
            <a href="#planos">Planos</a>
            <a href="#duvidas">Avisos</a>
            <a href="https://github.com/joaopedropassostocantins/CALCULADORA_PENAL" target="_blank" rel="noreferrer">Projeto no GitHub</a>
          </div>
        </div>
        <div className="shell footer-bottom">
          <span>© 2026 Calculadora Penal</span>
          <span>Resultados hipotéticos · Não substitui análise jurídica</span>
        </div>
      </footer>

      {selectedPlan && (
        <div className="modal-backdrop" role="presentation" onMouseDown={() => setSelectedPlan(null)}>
          <section className="checkout-modal" role="dialog" aria-modal="true" aria-labelledby="checkout-title" onMouseDown={(event) => event.stopPropagation()}>
            <button className="modal-close" type="button" onClick={() => setSelectedPlan(null)} aria-label="Fechar">×</button>
            <p className="eyebrow"><span /> Checkout seguro</p>
            <h2 id="checkout-title">{selectedPlan.name}</h2>
            <div className="checkout-summary">
              <span>{selectedPlan.quantity} {selectedPlan.quantity === 1 ? "consulta" : "consultas"}</span>
              <strong>{currency.format(selectedPlan.price)}</strong>
            </div>
            <fieldset>
              <legend>Como deseja pagar?</legend>
              <div className="payment-options">
                <label className={paymentMethod === "pix" ? "selected" : ""}>
                  <input type="radio" name="payment" value="pix" checked={paymentMethod === "pix"} onChange={() => setPaymentMethod("pix")} />
                  <span className="payment-symbol">◆</span>
                  <span><strong>Pix</strong><small>Aprovação imediata</small></span>
                </label>
                <label className={paymentMethod === "card" ? "selected" : ""}>
                  <input type="radio" name="payment" value="card" checked={paymentMethod === "card"} onChange={() => setPaymentMethod("card")} />
                  <span className="payment-symbol">▰</span>
                  <span><strong>Cartão</strong><small>Crédito ou débito</small></span>
                </label>
              </div>
            </fieldset>
            <button className="button checkout-button" type="button" onClick={() => setCheckoutNotice(true)}>
              Continuar no Mercado Pago
            </button>
            {checkoutNotice && (
              <div className="integration-notice" role="status">
                <strong>Integração pendente</strong>
                <p>O checkout está preparado visualmente. Para receber pagamentos reais, falta vincular o link ou as credenciais da conta Mercado Pago do projeto.</p>
              </div>
            )}
            <p className="checkout-footnote">Ambiente demonstrativo: nenhuma cobrança será realizada nesta versão.</p>
          </section>
        </div>
      )}
    </main>
  );
}
