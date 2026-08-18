import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const source = JSON.parse(fs.readFileSync(path.join(root, "src/data/catalogoNormas.json"), "utf8"));
const norms = source.norms ?? source.normas ?? source;
const blocks = {};
for (const item of norms) {
  const block = item.block ?? item.bloco ?? "sem bloco";
  (blocks[block] ??= []).push({
    norm: item.norm ?? item.norma ?? item.name,
    subject: item.subject ?? item.assunto,
    officialUrl: item.officialUrl ?? item.fonteOficial,
    nature: item.nature,
  });
}
const summary = {
  total: norms.length,
  materialPenal: norms.filter((item) => /M/.test(item.nature ?? "")).length,
  blocks: Object.fromEntries(Object.entries(blocks).map(([name, items]) => [name, { count: items.length, norms: items }]).sort(([a], [b]) => a.localeCompare(b, "pt-BR"))),
};
const output = path.join(root, "docs/catalogo/INVENTARIO_DIPLOMAS_2026-08-17.md");
const lines = ["# Inventário de diplomas e fontes para cobertura nacional", "", `Total de diplomas catalogados: **${summary.total}**. Registros de natureza material ou mista: **${summary.materialPenal}**.`, "", "| Bloco | Quantidade |", "| --- | ---: |"];
for (const [block, data] of Object.entries(summary.blocks)) lines.push(`| ${block} | ${data.count} |`);
for (const [block, data] of Object.entries(summary.blocks)) {
  lines.push("", `## ${block}`, "", "| Diploma | Natureza | Assunto | Fonte oficial |", "| --- | --- | --- | --- |");
  for (const item of data.norms) lines.push(`| ${item.norm} | ${item.nature ?? ""} | ${item.subject ?? ""} | ${item.officialUrl ? `<${item.officialUrl}>` : ""} |`);
}
fs.writeFileSync(output, `${lines.join("\n")}\n`);
console.log(`Wrote ${output} with ${norms.length} diplomas.`);
