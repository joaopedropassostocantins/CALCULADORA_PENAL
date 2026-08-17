import fs from 'node:fs';
const catalog = JSON.parse(fs.readFileSync('src/data/tiposPenais.json', 'utf8'));
const pending = catalog.registros.filter((r) => !r.inventarioValidado);
const groups = new Map();
for (const record of pending) {
  const key = record.vigencia.observacoes || 'sem observação';
  groups.set(key, (groups.get(key) || 0) + 1);
}
const modules = new Map();
for (const record of pending) modules.set(record.modulo, (modules.get(record.modulo) || 0) + 1);
const report = [
  '# Fila de validação do catálogo',
  '',
  `- Total de registros: ${catalog.registros.length}`,
  `- Inventário conferido: ${catalog.registros.filter((r) => r.inventarioValidado).length}`,
  `- Pendentes: ${pending.length}`,
  '',
  '## Pendências por módulo',
  '',
  '| Módulo | Pendentes |',
  '| --- | ---: |',
  ...[...modules.entries()].sort((a, b) => b[1] - a[1]).map(([module, count]) => `| ${module} | ${count} |`),
  '',
  '## Pendências por motivo declarado',
  '',
  '| Motivo | Registros |',
  '| --- | ---: |',
  ...[...groups.entries()].sort((a, b) => b[1] - a[1]).map(([reason, count]) => `| ${reason.replaceAll('|', '\\|')} | ${count} |`),
  '',
  '## Registros pendentes',
  '',
  '| ID | Módulo | Dispositivo | Fonte |',
  '| --- | --- | --- | --- |',
  ...pending.map((r) => `| ${r.id} | ${r.modulo} | ${r.dispositivo} | ${r.fonteOficial} |`),
  '',
].join('\n');
fs.writeFileSync('docs/catalogo/FILA_VALIDACAO.md', report);
console.log(report);
