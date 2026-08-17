import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

const root = process.cwd();
const canonicalPath = path.join(root, "src/data/tiposPenais.json");
const schemaPath = path.join(root, "src/data/tiposPenais.schema.json");
const normsPath = path.join(root, "src/data/catalogoNormas.json");
const canonical = JSON.parse(fs.readFileSync(canonicalPath, "utf8"));
const schema = JSON.parse(fs.readFileSync(schemaPath, "utf8"));
const norms = JSON.parse(fs.readFileSync(normsPath, "utf8"));
const consultationDate = canonical.dataCorte;
const auditedUrls = new Set([
  "https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm",
  "https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11343.htm",
  "https://www.planalto.gov.br/ccivil_03/leis/2003/l10.826compilado.htm",
  "https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12850.htm",
]);

function ensureDir(filePath) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
}

function stableJson(value) {
  return `${JSON.stringify(value, null, 2)}\n`;
}

function csvValue(value) {
  const text = Array.isArray(value) ? value.join(" | ") : value == null ? "" : String(value);
  return `"${text.replaceAll('"', '""')}"`;
}

function flatten(record) {
  return {
    id: record.id,
    nomeJuridico: record.nomeJuridico,
    aliases: record.aliases,
    classe: record.classe,
    jurisdicao: record.jurisdicao,
    modulo: record.modulo,
    norma: record.norma,
    dispositivo: record.dispositivo,
    naturezaFigura: record.naturezaFigura,
    tipoPaiId: record.tipoPaiId,
    descricaoObjetiva: record.descricaoObjetiva,
    penaMinimaMeses: record.pena.minimoMeses,
    penaMaximaMeses: record.pena.maximoMeses,
    penaUnidade: record.pena.unidadePrincipal,
    penaDescricao: record.pena.descricao,
    multa: record.pena.multa,
    vigencia: record.vigencia.estado,
    inicioVigenciaRedacao: record.vigencia.inicioVigenciaRedacao,
    dataConsulta: record.vigencia.dataConsulta,
    estadoConferencia: record.vigencia.estadoConferencia,
    fonteOficial: record.fonteOficial,
    leiCriadoraOuModificadora: record.leiCriadoraOuModificadora,
    inventarioValidado: record.inventarioValidado,
    enriquecimentoValidado: record.enriquecimentoValidado,
    usavelNaCalculadora: record.usavelNaCalculadora,
    palavrasChave: record.palavrasChave,
  };
}

const records = [...canonical.registros].sort((a, b) => a.nomeJuridico.localeCompare(b.nomeJuridico, "pt-BR") || a.id.localeCompare(b.id));
const publicRecords = records.map((record) => ({
  id: record.id,
  name: record.nomeJuridico,
  article: record.dispositivo,
  law: record.norma,
  category: record.modulo,
  minimum: record.pena.minimoMeses == null ? 0 : record.pena.minimoMeses / 12,
  maximum: record.pena.maximoMeses == null ? 0 : record.pena.maximoMeses / 12,
  penalty: record.pena.descricao,
  keywords: record.palavrasChave,
  sourceUrl: record.fonteOficial,
  validationState: record.vigencia.estadoConferencia,
  canCalculate: record.usavelNaCalculadora,
}));

const headers = Object.keys(flatten(records[0]));
const csv = [headers.map(csvValue).join(","), ...records.map((record) => headers.map((header) => csvValue(flatten(record)[header])).join(","))].join("\n") + "\n";

const sourceMap = new Map();
for (const norm of norms.norms) {
  if (!norm.officialUrl || !norm.officialUrl.startsWith("https://")) continue;
  sourceMap.set(norm.officialUrl, {
    id: `fonte-${crypto.createHash("sha256").update(norm.officialUrl).digest("hex").slice(0, 12)}`,
    norma: norm.norm,
    assunto: norm.subject,
    bloco: norm.block,
    urlOficial: norm.officialUrl,
    dataConsulta: consultationDate,
    estadoConferencia: auditedUrls.has(norm.officialUrl) ? "auditada" : "pendente",
    observacao: auditedUrls.has(norm.officialUrl)
      ? "Fonte oficial aberta e utilizada na carga inicial; alterações posteriores devem ser conferidas antes de publicação completa."
      : "Diploma identificado no inventário de normas, mas ainda não auditado dispositivo a dispositivo.",
  });
}
for (const record of records) {
  if (!sourceMap.has(record.fonteOficial)) {
    sourceMap.set(record.fonteOficial, {
      id: `fonte-${crypto.createHash("sha256").update(record.fonteOficial).digest("hex").slice(0, 12)}`,
      norma: record.norma,
      assunto: record.modulo,
      bloco: "Fonte de registro penal",
      urlOficial: record.fonteOficial,
      dataConsulta: consultationDate,
      estadoConferencia: auditedUrls.has(record.fonteOficial) ? "auditada" : "pendente",
      observacao: auditedUrls.has(record.fonteOficial) ? "Fonte utilizada na carga inicial." : "Fonte associada a registro pendente de conferência.",
    });
  }
}
const sources = [...sourceMap.values()].sort((a, b) => a.norma.localeCompare(b.norma, "pt-BR") || a.urlOficial.localeCompare(b.urlOficial));
const sourceCounts = sources.reduce((acc, source) => {
  acc[source.estadoConferencia] = (acc[source.estadoConferencia] ?? 0) + 1;
  return acc;
}, {});

const activeCounts = records.reduce((acc, record) => {
  acc[record.modulo] = (acc[record.modulo] ?? 0) + 1;
  return acc;
}, {});
const activeClassCounts = records.reduce((acc, record) => {
  acc[record.classe] = (acc[record.classe] ?? 0) + 1;
  return acc;
}, {});
const validatedCount = records.filter((record) => record.inventarioValidado).length;
const enrichedCount = records.filter((record) => record.enriquecimentoValidado).length;
const pendingRecords = records.filter((record) => !record.inventarioValidado);
const pendingModules = [...new Set(norms.norms.filter((norm) => /M|MP/.test(norm.nature) && !auditedUrls.has(norm.officialUrl)).map((norm) => norm.block.replace(/^\\d+\\s+/, "")))].sort();
const versionHash = crypto.createHash("sha256").update(stableJson(records)).digest("hex").slice(0, 16);

canonical.quantidadeTotalAtiva = records.length;
canonical.quantidadePorModulo = activeCounts;
canonical.fontesPrevistas = norms.norms.length;
canonical.fontesAuditadas = sources.filter((source) => source.estadoConferencia === "auditada").length;
canonical.registrosInventariados = validatedCount;
canonical.registrosEnriquecidos = enrichedCount;
canonical.registrosPendentes = pendingRecords.length;
canonical.identificadorVersao = `cntp-br-${consultationDate}-${versionHash}`;
canonical.modulosPendentes = pendingModules;
canonical.estadoGeral = "incompleto";

ensureDir(canonicalPath);
fs.writeFileSync(canonicalPath, stableJson(canonical));
fs.writeFileSync(path.join(root, "src/data/tiposPenais.csv"), csv);
fs.writeFileSync(path.join(root, "src/data/fontesPenais.json"), stableJson({
  versaoEsquema: "1.0.0",
  dataCorte: consultationDate,
  fontesPrevistas: sources.length,
  fontesAuditadas: sourceCounts.auditada ?? 0,
  fontesPendentes: sourceCounts.pendente ?? 0,
  fontes: sources,
}));
const publicDataPath = path.join(root, "sites/calculadora-penal/data/tiposPenais.public.json");
ensureDir(publicDataPath);
fs.writeFileSync(publicDataPath, stableJson({
  versaoCatalogo: canonical.identificadorVersao,
  dataCorte: consultationDate,
  estadoGeral: canonical.estadoGeral,
  registros: publicRecords,
}));

const report = `# Relatório de cobertura do catálogo penal\n\nData de corte: **${consultationDate}**. Identificador: **${canonical.identificadorVersao}**.\n\n> O estado global permanece **incompleto**. A carga abaixo é um checkpoint auditável; ela não declara conter todos os tipos penais vigentes.\n\n## Contagem atual\n\n| Indicador | Quantidade |\n| --- | ---: |\n| Registros ativos na fonte canônica | ${records.length} |\n| Crimes | ${activeClassCounts.crime ?? 0} |\n| Contravenções | ${activeClassCounts.contravencao ?? 0} |\n| Inventário validado | ${validatedCount} |\n| Enriquecimento jurídico validado | ${enrichedCount} |\n| Registros pendentes | ${pendingRecords.length} |\n| Diplomas no inventário de normas | ${norms.norms.length} |\n| Fontes auditadas | ${sourceCounts.auditada ?? 0} |\n| Fontes pendentes | ${sourceCounts.pendente ?? 0} |\n\n## Registros por módulo\n\n| Módulo | Registros |\n| --- | ---: |\n${Object.entries(activeCounts).sort(([a], [b]) => a.localeCompare(b, "pt-BR")).map(([module, count]) => `| ${module} | ${count} |`).join("\n")}\n\n## Critério de publicação\n\nTodos os registros do checkpoint são exportados para a busca pública com estado de conferência visível. O uso na calculadora exige inventarioValidado=true e usavelNaCalculadora=true; nenhum registro com inventário pendente é enviado para o cálculo. O enriquecimento permanece separado e ainda não foi validado neste checkpoint.\n\n## Módulos ainda não concluídos\n\n${pendingModules.map((module) => `- ${module}`).join("\n")}\n\nA pendência inclui, entre outros, contravenções, crimes eleitorais, crimes militares, tipos de legislação penal especial e estatutos setoriais. O inventário de normas atual é uma lista de diplomas e não foi contado como inventário de tipos.\n\n## Fontes\n\nAs fontes oficiais utilizadas ou previstas estão em [src/data/fontesPenais.json](../../src/data/fontesPenais.json). A auditoria registrada neste checkpoint cobre apenas as páginas oficiais acessadas e usadas na carga inicial; URLs bloqueadas ou não acessadas permanecem pendentes.\n`;
fs.writeFileSync(path.join(root, "docs/catalogo/RELATORIO_COBERTURA.md"), report);

const decisions = `# Decisões metodológicas\n\n## Unidade de cadastro\n\nA unidade é a **figura incriminadora autônoma**. Formas culposas, preterdolosas, qualificadas ou equiparadas só aparecem como registros separados quando o dispositivo apresenta elementos e pena próprios. Majorantes, minorantes, agravantes, atenuantes, regras de concurso e efeitos da condenação permanecem vinculados ao tipo-pai no campo de enriquecimento e não são contados autonomamente.\n\n## Fonte canônica e derivados\n\n\`src/data/tiposPenais.json\` é a fonte canônica. O CSV e o JSON público do site são derivados por \`scripts/generate_tipos_penais.mjs\`; não devem ser editados manualmente. \`src/data/fontesPenais.json\` preserva o inventário de URLs oficiais, inclusive fontes ainda pendentes.\n\n## Estados de validação\n\n\`inventarioValidado\` representa a confirmação da existência, dispositivo, conduta e pena na fonte primária. \`enriquecimentoValidado\` representa a conferência posterior de ação penal, rito, competência, tentativa, jurisprudência e demais campos jurídicos. O catálogo pode ser buscado com o primeiro estado, mas a calculadora aceita somente registros explicitamente marcados para cálculo.\n\n## Vigência e tempo\n\nO catálogo usa a data de corte **${consultationDate}**. Alterações legislativas recentes, sobretudo aquelas cuja página foi bloqueada na consulta, ficam pendentes; não se presume vigência ou data inicial a partir de snippets de busca. Tipos revogados não entram na coleção ativa.\n\n## Escopo do checkpoint\n\nA carga inicial cobre uma seleção auditada do Código Penal e páginas oficiais acessadas de drogas, armas e organização criminosa. Ela não é um inventário nacional integral. O relatório de cobertura deve permanecer incompleto até que todos os módulos e dispositivos previstos estejam mapeados, auditados e justificados.\n`;
fs.writeFileSync(path.join(root, "docs/catalogo/DECISOES_METODOLOGICAS.md"), decisions);

const pending = `# Pendências jurídicas\n\nEste documento é atualizado junto com os derivados do catálogo e lista bloqueios ou lacunas que impedem a marcação global como completa.\n\n| Pendência | Impacto | Próximo passo seguro |\n| --- | --- | --- |\n| Lei das Contravenções Penais | A URL oficial respondeu com acesso negado na consulta; jogo do bicho, porte de arma branca e dispositivos revogados ainda não foram auditados. | Reconsultar a página oficial ou obter cópia oficial consolidada e registrar a data da conferência. |\n| Código Penal Militar e tipos militares esparsos | Não extraídos neste checkpoint. | Auditar o CPM artigo a artigo e aplicar a regra de crime comum militar por extensão sem duplicar o tipo-base. |\n| Crimes eleitorais | Código Eleitoral, Lei das Eleições e leis esparsas não foram extraídos. | Consultar Planalto e TSE; separar art. 359-P do CP, art. 326-B do Código Eleitoral, boca de urna e ilícitos administrativos. |\n| Legislação penal especial e estatutos setoriais | O catálogo de 88 diplomas ainda não equivale a catálogo de tipos; vários diplomas estão apenas previstos. | Extrair dispositivos incriminadores de drogas, armas, tortura, abuso de autoridade, ambientais, trânsito, ECA, pessoa idosa, racismo, sistema financeiro, tributário, falimentar, propriedade intelectual e demais módulos. |\n| Alterações legislativas de 2025 e 2026 | Páginas de leis recentes foram bloqueadas em algumas consultas; a redação atual do CP mostra alterações que precisam de validação temporal independente. | Conferir a lei criadora/modificadora e o início de vigência diretamente em fonte oficial acessível, sem usar apenas snippet. |\n| Enriquecimento jurídico | Nenhum registro está marcado como enriquecimento validado neste checkpoint. | Completar bem jurídico, sujeitos, elemento subjetivo, consumação, tentativa, ação penal, competência, rito, hediondez, jurisprudência e controvérsias. |\n| Cobertura integral | O estado global é incompleto e há ${pendingRecords.length} registros pendentes na fonte canônica. | Trabalhar módulo por módulo, atualizar as contagens e não declarar integralidade enquanto houver lacunas. |\n\n## Fontes bloqueadas na consulta de 2026-08-17\n\n- <https://www.planalto.gov.br/ccivil_03/decreto-lei/del3688.htm> — código de bloqueio registrado em \`docs/catalogo/fonte_consulta_2026-08-17.md\`.\n- <https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15358.htm> — código de bloqueio registrado no mesmo arquivo.\n- <https://www.planalto.gov.br/ccivil_03/leis/l9613compilado.htm> — código de bloqueio registrado no mesmo arquivo.\n- <https://www.planalto.gov.br/ccivil_03/leis/l9455.htm> — código de bloqueio registrado no mesmo arquivo.\n`;
fs.writeFileSync(path.join(root, "docs/catalogo/PENDENCIAS_JURIDICAS.md"), pending);

console.log(`Generated ${records.length} canonical records, ${publicRecords.length} public records and ${sources.length} source entries.`);
