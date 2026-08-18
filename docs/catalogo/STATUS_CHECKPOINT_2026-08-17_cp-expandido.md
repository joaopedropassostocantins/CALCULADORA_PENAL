# Status do checkpoint — catálogo penal nacional

## Status real

O checkpoint foi publicado na branch `agent/catalogo-integral-tipos-penais` do repositório `joaopedropassostocantins/CALCULADORA_PENAL`, no commit `f3a83e4`. O catálogo canônico agora contém **673 registros**, dos quais **226 pertencem ao módulo Código Penal**. O estado global permanece **incompleto**, como exigido, porque ainda existem **461 pendências estruturais** de inventário, conferência temporal, normalização de penas históricas/remissivas ou enriquecimento jurídico.

Nenhum registro pendente foi liberado para cálculo. A interface pública e os derivados foram regenerados a partir de `src/data/tiposPenais.json`, preservando o bloqueio de cálculo e a exposição do estado de conferência.

## Cobertura adicionada neste ciclo

Foram adicionados oito crimes sexuais vigentes dos arts. 215 a 218-C do Código Penal; 31 crimes de perigo comum, transporte e serviços públicos dos arts. 250 a 266; e os derivados e testes correspondentes. O lote foi construído com parentagem para modalidades culposas e resultados com pena própria. Dispositivos revogados — como os arts. 216, 217, 219, 220 e 350 — não foram inseridos na coleção ativa.

A cobertura anterior deste ciclo também está preservada nos commits publicados anteriormente, incluindo crimes patrimoniais, direitos autorais, Administração Pública, Administração da Justiça e fé pública.

## URLs oficiais consultadas

| Fonte | Finalidade |
|---|---|
| <https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm> | Texto oficial compilado do Código Penal, arts. 134–154-A, 159–180-A, 184, 215–218-C, 250–266, 289–311, 312–326, 338–349-A. |
| <https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11340.htm> | Conferência paralela do art. 24-A da Lei Maria da Penha, mantido distinto do art. 338-A do Código Penal. |
| <https://github.com/joaopedropassostocantins/CALCULADORA_PENAL/pull/2> | Pull request draft do catálogo para acompanhamento da integração. |

## Testes executados

| Verificação | Resultado | Observação |
|---|---|---|
| `pnpm exec vitest run tests/tipos_penais.test.ts` | PASSOU | 4 testes e 4 testes internos aprovados. |
| `pnpm exec tsc --noEmit` | PASSOU | Nenhum erro de TypeScript. |
| `node scripts/validate_tipos_penais.mjs` | PASSOU com aviso controlado | 673 IDs, 673 dispositivos e 461 pendências; o aviso não é falha e impede corretamente o estado `completo`. |
| `git diff --check` | PASSOU | Nenhum erro de whitespace no checkpoint. |
| `git push origin agent/catalogo-integral-tipos-penais` | PASSOU | Commit `f3a83e4` publicado no remoto. |

## Pendências e próximo ciclo

O catálogo ainda precisa de cobertura integral do Código Penal em intervalos não cadastrados, auditoria integral do Código Penal Militar, reconciliação dos crimes eleitorais e contravenções, além da conferência individual das 461 pendências estruturais. Multas históricas, penas remissivas — por exemplo, o art. 304 e o art. 264, parágrafo único, na hipótese de morte — e dispositivos dependentes de normalização permanecem sem faixa numérica e bloqueados para cálculo.

> Critério de completude: o estado global não deve ser alterado para `completo` enquanto houver fonte pendente de auditoria, registro vigente sem conferência ou pendência estrutural.

## Referências

[1]: <https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848.htm> "Decreto-Lei nº 2.848/1940 — Código Penal, texto oficial compilado"
[2]: <https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11340.htm> "Lei nº 11.340/2006 — Lei Maria da Penha, texto oficial"
[3]: <https://github.com/joaopedropassostocantins/CALCULADORA_PENAL/pull/2> "Pull request draft do catálogo penal nacional"
