import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const catalogPath = path.join(root, "src/data/tiposPenais.json");
const schemaPath = path.join(root, "src/data/tiposPenais.schema.json");
const catalog = JSON.parse(fs.readFileSync(catalogPath, "utf8"));
const schema = JSON.parse(fs.readFileSync(schemaPath, "utf8"));
const errors = [];
const warnings = [];
const records = catalog.registros ?? [];
const isoDate = /^\d{4}-\d{2}-\d{2}$/;
const officialUrl = /^https:\/\//;

function error(message) { errors.push(message); }
function warn(message) { warnings.push(message); }
function requireString(value, label) {
  if (typeof value !== "string" || value.trim() === "") error(`${label} deve ser texto não vazio.`);
}

if (!catalog || typeof catalog !== "object") error("Catálogo deve ser um objeto JSON.");
if (catalog.estadoGeral === "completo") error("estadoGeral= completo é proibido neste validador incremental sem auditoria integral.");
if (!schema.$schema) error("Schema sem identificador JSON Schema.");
if (!isoDate.test(catalog.dataCorte ?? "")) error("dataCorte inválida.");
if (catalog.quantidadeTotalAtiva !== records.length) error(`quantidadeTotalAtiva=${catalog.quantidadeTotalAtiva} não corresponde a ${records.length} registros.`);

const ids = new Set();
const devices = new Set();
const recordIds = new Set(records.map((record) => record.id));
const modules = {};
const classes = {};

for (const [index, record] of records.entries()) {
  const prefix = `registros[${index}]`;
  requireString(record.id, `${prefix}.id`);
  requireString(record.nomeJuridico, `${prefix}.nomeJuridico`);
  requireString(record.norma, `${prefix}.norma`);
  requireString(record.dispositivo, `${prefix}.dispositivo`);
  requireString(record.modulo, `${prefix}.modulo`);
  requireString(record.fonteOficial, `${prefix}.fonteOficial`);
  if (ids.has(record.id)) error(`ID duplicado: ${record.id}`);
  ids.add(record.id);
  const deviceKey = `${record.norma}::${record.dispositivo}`;
  if (devices.has(deviceKey)) error(`Dispositivo duplicado sem justificativa: ${deviceKey}`);
  devices.add(deviceKey);
  if (record.tipoPaiId && !recordIds.has(record.tipoPaiId)) error(`${record.id} referencia tipo-pai inexistente: ${record.tipoPaiId}`);
  if (!officialUrl.test(record.fonteOficial)) error(`${record.id} não possui URL oficial HTTPS.`);
  if (!isoDate.test(record.vigencia?.dataConsulta ?? "")) error(`${record.id} possui dataConsulta inválida.`);
  if (record.vigencia?.inicioVigenciaRedacao !== null && !isoDate.test(record.vigencia?.inicioVigenciaRedacao ?? "")) error(`${record.id} possui início de vigência inválido.`);
  const min = record.pena?.minimoMeses;
  const max = record.pena?.maximoMeses;
  if (min !== null && typeof min !== "number") error(`${record.id} pena mínima deve ser numérica ou null.`);
  if (max !== null && typeof max !== "number") error(`${record.id} pena máxima deve ser numérica ou null.`);
  if (typeof min === "number" && typeof max === "number" && min > max) error(`${record.id} possui pena mínima maior que a máxima.`);
  if (record.vigencia?.estado === "vigente" && !record.fonteOficial) error(`${record.id} vigente sem fonte.`);
  if (record.usavelNaCalculadora && (!record.inventarioValidado || min === null || max === null)) error(`${record.id} está marcado para cálculo sem inventário e pena validados.`);
  if (record.inventarioValidado && record.vigencia?.estadoConferencia !== "confirmada") error(`${record.id} inventariado mas estado de conferência não é confirmada.`);
  if (record.enriquecimentoValidado && !record.inventarioValidado) error(`${record.id} enriquecido sem inventário validado.`);
  if (!record.inventarioValidado && record.usavelNaCalculadora) error(`${record.id} pendente enviado ao cálculo.`);
  modules[record.modulo] = (modules[record.modulo] ?? 0) + 1;
  classes[record.classe] = (classes[record.classe] ?? 0) + 1;
}

for (const [module, count] of Object.entries(modules)) {
  if (catalog.quantidadePorModulo?.[module] !== count) error(`Contagem do módulo ${module} divergente.`);
}
for (const [className, count] of Object.entries(classes)) {
  const expected = className === "crime" ? catalog.registrosCrimes : catalog.registrosContravencoes;
  if (expected !== undefined && expected !== count) error(`Contagem de classe ${className} divergente.`);
}
if ((catalog.registrosPendentes ?? 0) !== records.filter((record) => !record.inventarioValidado).length) error("registrosPendentes divergente.");
if ((catalog.registrosInventariados ?? 0) !== records.filter((record) => record.inventarioValidado).length) error("registrosInventariados divergente.");
if ((catalog.registrosEnriquecidos ?? 0) !== records.filter((record) => record.enriquecimentoValidado).length) error("registrosEnriquecidos divergente.");
if (catalog.registrosPendentes > 0) warn(`${catalog.registrosPendentes} registros permanecem pendentes; o catálogo não pode ser marcado completo.`);
if ((catalog.modulosPendentes ?? []).length === 0) warn("Nenhum módulo pendente declarado; confirme a cobertura integral antes de publicar.");

if (errors.length) {
  console.error(errors.map((message) => `ERROR ${message}`).join("\n"));
  process.exitCode = 1;
} else {
  console.log(`OK: ${records.length} registros, ${ids.size} IDs, ${devices.size} dispositivos e ${catalog.registrosPendentes} pendências estruturais.`);
}
if (warnings.length) console.warn(warnings.map((message) => `WARN ${message}`).join("\n"));
