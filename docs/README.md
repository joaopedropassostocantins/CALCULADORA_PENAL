# Documentação de pesquisa — dados e estudos

Este diretório reúne os estudos, notas de pesquisa, gráficos e o prompt técnico produzidos durante a investigação sobre a hiperinflação legislativa penal e o encarceramento no Brasil. Os arquivos são independentes da aplicação (site) e servem como base de conhecimento para o projeto.

## Estrutura

| Caminho | Conteúdo |
|---|---|
| `estudos/estudo_hiperinflacao_penal_brasil.md` | Estudo principal: tipos penais em vigor, evolução carcerária 1988–2025, populismo punitivo e direito penal simbólico (22 referências, 6 gráficos). |
| `estudos/analise_correlacional_penal_brasil.md` | Análise correlacional: perfil da população carcerária, tráfico privilegiado, medidas protetivas e crimes de trânsito (15 referências, 6 gráficos). |
| `estudos/resumo_executivo_artigo_juridico.md` | Resumo executivo em formato de artigo jurídico: trânsito (preterdolo, mortes 2007–2024) e impacto das tipificações na esfera privada e familiar. |
| `dados-carcerarios/nota_contrafactual_auxilio_reclusao.md` | Nota técnica do cenário contrafactual do auxílio-reclusão (2016–2025): o que aconteceria se as regras de 2019 não tivessem sido endurecidas. |
| `dados-carcerarios/notas_de_pesquisa.md` | Notas de pesquisa consolidadas com séries, fontes e verificações metodológicas. |
| `graficos/` | Gráficos em alta resolução citados nos estudos (auxílio-reclusão, contrafactual, trânsito, carcerário). |
| `prompt-claude/README-prompt-catalogacao.md` | Prompt técnico para uso em um projeto do Claude: baixar todas as normas penais especiais vigentes e compilar o catálogo nacional de tipos penais em vigor, em ordem alfabética, com norma, conduta, bem jurídico, ação penal, procedimento, rito, pena e demais campos. |

## Sobre a nota do contrafactual do auxílio-reclusão

A nota apresenta três cenários para 2025, todos ancorados na taxa de cobertura observada em 2016 (~4% da população carcerária) e calibrados no ponto oficial do INSS (44.533 beneficiários em out/2020). Sob a premissa mais conservadora (regra antiga mantida, sem nenhum impulso adicional), haveria cerca de **36,4 mil benefícios** — quase cinco vezes o valor observado (7.329). Se a tendência de crescimento pré-reforma (13,8% a.a.) tivesse continuado, a estimativa sobe para **~84,9 mil**; somando o choque da pandemia (+26,4%), para **~107,3 mil**. A divergência de conceitos entre as séries (benefícios ativos vs. famílias atendidas no mês) é explicitada na nota, que também registra os limites da estimativa (teto de renda, carência de 24 contribuições, exclusão do regime semiaberto e rejeição automática pelo Meu INSS).
