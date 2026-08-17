import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const normsSource = JSON.parse(fs.readFileSync(path.join(root, "src/data/catalogoNormas.json"), "utf8"));
const norms = normsSource.norms ?? normsSource.normas ?? normsSource;
const catalog = JSON.parse(fs.readFileSync(path.join(root, "src/data/tiposPenais.json"), "utf8"));
const typesByNorm = new Map();
for (const record of catalog.registros) typesByNorm.set(record.norma, (typesByNorm.get(record.norma) ?? 0) + 1);
const material = norms
  .filter((item) => /M/.test(item.nature ?? ""))
  .map((item) => ({
    block: item.block ?? item.bloco ?? "sem bloco",
    norm: item.norm ?? item.norma ?? item.name,
    subject: item.subject ?? item.assunto ?? "",
    officialUrl: item.officialUrl ?? item.fonteOficial ?? "",
    currentTypes: typesByNorm.get(item.norm ?? item.norma ?? item.name) ?? 0,
  }))
  .sort((a, b) => a.block.localeCompare(b.block, "pt-BR") || a.norm.localeCompare(b.norm, "pt-BR"));
const missing = material.filter((item) => item.currentTypes === 0);
const lines = [
  "# Mapa de cobertura material restante",
  "",
  `Diplomas materiais ou mistos no inventário: **${material.length}**. Diplomas sem nenhum tipo associado no catálogo atual: **${missing.length}**.`,
  "",
  "| Bloco | Diploma | Tipos atuais | Assunto | Fonte oficial |",
  "| --- | --- | ---: | --- | --- |",
];
for (const item of material) lines.push(`| ${item.block} | ${item.norm} | ${item.currentTypes} | ${item.subject} | ${item.officialUrl ? `<${item.officialUrl}>` : ""} |`);
fs.writeFileSync(path.join(root, "docs/catalogo/MAPA_COBERTURA_RESTANTE.md"), `${lines.join("\n")}\n`);
console.log(`Wrote remaining coverage map: ${material.length} material diplomas, ${missing.length} without catalog records.`);
