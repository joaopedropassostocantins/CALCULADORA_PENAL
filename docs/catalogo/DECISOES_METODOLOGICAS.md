# Decisões metodológicas

## Unidade de cadastro

A unidade é a **figura incriminadora autônoma**. Formas culposas, preterdolosas, qualificadas ou equiparadas só aparecem como registros separados quando o dispositivo apresenta elementos e pena próprios. Majorantes, minorantes, agravantes, atenuantes, regras de concurso e efeitos da condenação permanecem vinculados ao tipo-pai no campo de enriquecimento e não são contados autonomamente.

## Fonte canônica e derivados

`src/data/tiposPenais.json` é a fonte canônica. O CSV e o JSON público do site são derivados por `scripts/generate_tipos_penais.mjs`; não devem ser editados manualmente. `src/data/fontesPenais.json` preserva o inventário de URLs oficiais, inclusive fontes ainda pendentes.

## Estados de validação

`inventarioValidado` representa a confirmação da existência, dispositivo, conduta e pena na fonte primária. `enriquecimentoValidado` representa a conferência posterior de ação penal, rito, competência, tentativa, jurisprudência e demais campos jurídicos. O catálogo pode ser buscado com o primeiro estado, mas a calculadora aceita somente registros explicitamente marcados para cálculo.

## Vigência e tempo

O catálogo usa a data de corte **2026-08-17**. Alterações legislativas recentes, sobretudo aquelas cuja página foi bloqueada na consulta, ficam pendentes; não se presume vigência ou data inicial a partir de snippets de busca. Tipos revogados não entram na coleção ativa.

## Escopo do checkpoint

A carga inicial cobre uma seleção auditada do Código Penal e páginas oficiais acessadas de drogas, armas e organização criminosa. Ela não é um inventário nacional integral. O relatório de cobertura deve permanecer incompleto até que todos os módulos e dispositivos previstos estejam mapeados, auditados e justificados.
