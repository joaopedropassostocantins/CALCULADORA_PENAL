# Manifesto de fontes e dados

**Projeto:** Calculadora Penal — estudos sobre hiperinflação penal, encarceramento e populismo punitivo no Brasil  
**Data de consolidação:** 16 de agosto de 2026  
**Objetivo:** registrar, em um único documento, toda a informação utilizada ou coletada para os estudos versionados neste repositório.

## 1. Convenções de rastreabilidade

| Categoria | Significado |
|---|---|
| **Oficial** | Órgão público, base normativa oficial ou fonte institucional diretamente responsável pelo dado. |
| **Acadêmica** | Artigo, periódico, repositório ou estudo técnico com metodologia identificável. |
| **Imprensa/organização** | Reportagem, entidade da sociedade civil ou organização que reproduz/analisa dados de terceiros. |
| **Dado do usuário** | Planilha, PDF ou série fornecida pelo usuário; não foi tratada como dado oficial sem ressalva. |
| **Derivado** | Cálculo, gráfico, transcrição, cenário ou estimativa produzida pelos scripts deste projeto. |

> **Regra de interpretação:** dados oficiais, acadêmicos, de imprensa e estimativas não devem ser misturados como se tivessem a mesma autoridade. A fonte original, o conceito medido e a data de referência devem acompanhar cada número.

## 2. Dados brutos entregues pelo usuário

| Arquivo no repositório | Conteúdo | Uso |
|---|---|---|
| [`Catalogo_Normas_Penais_Brasil.xlsx`](raw-upload/Catalogo_Normas_Penais_Brasil.xlsx) | Planilha com catálogo de normas penais, súmulas e precedentes | Base do catálogo da aplicação e do prompt de catalogação nacional |
| [`serie_historica_auxilio_reclusao.pdf`](raw-upload/serie_historica_auxilio_reclusao.pdf) | Série estimada de benefícios ativos do auxílio-reclusão, 2016–2025 | Base do contrafactual; a própria página identifica a série como estimativa |
| [`extratos-web/`](extratos-web/) | Cópias dos documentos Markdown extraídos das páginas consultadas | Preservação do material textual coletado durante a pesquisa |

### Série do PDF fornecido pelo usuário

| Ano | Benefícios ativos estimados | Observação indicada no PDF |
|---|---:|---|
| 2016 | 26.585 | Regra antiga; semiaberto incluído e sem carência mínima |
| 2017 | 25.100 | Discussões de contenção |
| 2018 | 24.050 | Pente-fino nos benefícios federais |
| 2019 | 21.900 | MP 871/2019 e EC 103/2019 |
| 2020 | 15.400 | Reforma e pandemia |
| 2021 | 13.100 | Comprovação rígida de baixa renda |
| 2022 | 11.200 | Cruzamento automatizado de dados |
| 2023 | 8.900 | Mudança do cálculo e teto |
| 2024 | 7.800 | Rejeições automáticas no Meu INSS |
| 2025 | 7.329 | Estabilização no mínimo histórico |

## 3. Fontes oficiais e normativas

| Fonte | Dados ou afirmações utilizados | Arquivo/estudo relacionado |
|---|---|---|
| [Planalto — Lei n. 14.532/2023](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14532.htm) | Alterações sobre injúria racial e racismo; usada apenas na análise histórica, não na versão de slides que retirou a agenda identitária | `estudos/estudo_hiperinflacao_penal_brasil.md`, notas |
| [INSS — Auxílio-reclusão](https://www.gov.br/inss/pt-br/direitos-e-deveres/auxilio-reclusao/auxilio-reclusao) | Requisitos, dependentes, regime de cumprimento e natureza previdenciária do benefício | Nota contrafactual |
| [INSS — Valor-limite do auxílio-reclusão](https://www.gov.br/inss/pt-br/direitos-e-deveres/auxilio-reclusao/valor-limite-para-direito-ao-auxilio-reclusao) | Limite de baixa renda e atualização do valor-limite | Nota contrafactual |
| [SENAPPEN](https://www.gov.br/senappen/pt-br) | Estatísticas prisionais e referência institucional ao SISDEPEN/Infopen | Estudos carcerários e correlacionais |
| [CNJ — auxílio-reclusão e famílias de segurados presos](https://www.cnj.jus.br/auxilio-reclusao-ajuda-no-sustento-de-familias-de-405-mil-presos-segurados-do-inss/) | 40.519 famílias em junho de 2013 | Nota contrafactual |
| [CNJ — réus primários por tráfico](https://www.cnj.jus.br/estudo-aponta-que-mais-de-100-mil-reus-primarios-por-trafico-poderiam-ter-pena-ajustada-pela-lei/) | Mais de 100 mil condenados sem outras condenações potencialmente alcançados pela revisão do tráfico privilegiado | Análise correlacional |
| [STF — enquadramento de homofobia/transfobia](https://noticias.stf.jus.br/postsnoticias/stf-enquadra-homofobia-e-transfobia-como-crimes-de-racismo-ao-reconhecer-omissao-legislativa/) | Marco jurisprudencial de 2019; preservado nas notas históricas, não usado na versão revisada dos slides | Notas históricas |
| [Lei Seca — TJDFT](https://www.tjdft.jus.br/institucional/imprensa/campanhas-e-produtos/direito-facil/edicao-semanal/lei-seca) | Explicação institucional dos marcos de trânsito | Artigo jurídico e gráfico de trânsito |
| [IPC — Transparência Internacional](https://transparenciainternacional.org.br/ipc/) | Índice de percepção da corrupção e comparação temporal | Estudo principal |
| [SENAPPEN — estudo de reincidência 2022 (PDF)](https://www.gov.br/senappen/pt-br/assuntos/noticias/depen-divulga-relatorio-previo-de-estudo-inedito-sobre-reincidencia-criminal-no-brasil/reincidencia-criminal-no-brasil-2022.pdf) | Métricas de reincidência penitenciária e limites de comparação | Análise correlacional |

## 4. Fontes acadêmicas e técnicas

| Fonte | Tema/dado | Arquivo/estudo relacionado |
|---|---|---|
| [SciELO — Revista Katálysis: auxílio-reclusão](https://www.scielo.br/j/rk/a/GzNr7HFxVkGLRpHjWzhtGNB/?format=html&lang=pt) | Cobertura histórica restrita do benefício e perfil de proteção social | Nota contrafactual |
| [SciELO — tráfico, encarceramento e tendências](https://www.scielo.br/j/trends/a/5PwpZnH5ksJdpmRKw9XjNrC/?lang=en) | Relação entre política de drogas e encarceramento | Estudos carcerários |
| [SciELO Saúde Pública — estudo de trânsito](https://www.scielosp.org/article/csc/2025.v30n10/e15372025/en/) | Mortalidade/lesões e dados de trânsito | Artigo jurídico e análise de trânsito |
| [PLoS ONE — estudo de trânsito, DOI 10.1371/journal.pone.0288288](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0288288) | Série temporal e efeitos de fiscalização/legislação de trânsito | Artigo jurídico e gráfico de trânsito |
| [PLoS/PMC — estudo de trânsito 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC8971401/) | Evidência acadêmica sobre mortalidade e políticas de segurança viária | Artigo jurídico |
| [PLoS/PMC — estudo de trânsito 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC9038143/) | Evidência acadêmica complementar sobre acidentes fatais e intervenção | Artigo jurídico |
| [Scientific/Elsevier — artigo sobre Lei Seca](https://www.sciencedirect.com/science/article/abs/pii/S0001457512002357) | Relação entre legislação, álcool e sinistros | Análise de trânsito |
| [Ipea — estudo técnico](https://repositorio.ipea.gov.br/bitstreams/f6cc1ce0-eeba-4dd8-8140-896950c9747a/download) | Segurança pública, encarceramento ou trânsito conforme citado nos estudos | Estudo principal |
| [RBSP — descumprimento de medida protetiva](https://revista.forumseguranca.org.br/rbsp/article/view/1894) | Perfil e contexto do art. 24-A/descumprimento de medida protetiva | Análise correlacional |
| [Revista UNAERP — produção/expansão penal](https://revistas.unaerp.br/rcd/article/view/1471/1510) | Discussão acadêmica sobre política criminal e produção legislativa | Estudo principal |
| [Câmara — e-Legis](https://e-legis.camara.leg.br/cefor/index.php/e-legis/article/download/540/732/2733) | Produção legislativa e racionalidade penal | Estudo principal |

## 5. Fontes de imprensa, organizações e bases secundárias

| Fonte | Dado ou contexto coletado | Observação |
|---|---|---|
| [BBC Brasil — perfil da população prisional](https://www.bbc.com/portuguese/articles/c0k4nmd3e2xo) | 663 mil presos em celas físicas; 888 mil incluindo domiciliar/monitoramento; 173 mil por tráfico; 30% provisórios; composição dos crimes | Reportagem baseada em dados SENAPPEN; não substitui a base oficial |
| [Poder360 — auxílio-reclusão na pandemia](https://www.poder360.com.br/governo/numero-de-beneficiarios-do-auxilio-reclusao-sobe-264-na-pandemia/) | 44.533 beneficiários em outubro de 2020 e alta de 26,4% | Reportagem que atribui os dados ao INSS; conceitos diferem da série do usuário |
| [CNM — caso Petrobras](https://cnm.org.br/comunicacao/noticias/petrobras-e-o-segundo-maior-caso-de-corrupcao-do-mundo) | Contexto do caso Petrobras/Lava Jato | Fonte secundária; usar com cautela em afirmações comparativas |
| [Conectas — Lei de Drogas](https://conectas.org/noticias/nova-lei-de-drogas-penaliza-mais-negros-e-pobres/) | Seletividade e impacto social da política de drogas | Organização da sociedade civil |
| [ConJur — consolidação de tipos penais](https://www.conjur.com.br/2024-ago-23/o-ninho-de-mafagafos-dos-tipos-penais-no-brasil-consolidacao-normativa-urgente/) | Estimativa e debate sobre quantidade de tipos penais | Não é um inventário oficial exaustivo |
| [Direito Penal Brasileiro — direito penal simbólico](https://www.direitopenalbrasileiro.com.br/direito-penal-simbolico/) | Conceito de direito penal simbólico | Fonte doutrinária/explicativa secundária |
| [Migalhas — produção legislativa penal](https://www.migalhas.com.br/coluna/informacao-privilegiada/375382/as-problematicas-da-producao-legislativa-penal-brasileira) | Críticas à produção legislativa penal e ao simbolismo | Fonte jurídica secundária |
| [FBSP/Fontes Seguras — elucidação de homicídios](https://fontesegura.forumseguranca.org.br/brasil-esclarece-apenas-4-em-cada-10-homicidios/) | Estimativa de elucidação de homicídios | Fonte secundária baseada em dados públicos |
| [FBSP — violência doméstica/medidas protetivas](https://www.mpmt.mp.br/portalcao/news/723/117950/maria-da-penha-quase-13-mil-homens-sao-presos-por-violencia-domestica/464) | Operações e prisões por violência doméstica | Reportagem institucional; não confundir prisões em operação com estoque anual |
| [ONSV — análise DATASUS 2024](https://www.onsv.org.br/estudos/analise-datasus-2024) | Óbitos no trânsito e série recente | Organização setorial; conferir sempre com SIM/DATASUS |
| [Pesquisa FAPESP/ONSV — mortes no trânsito](https://www.onsv.org.br/estudos/analise-datasus-2024) | Tendência recente de mortalidade viária | URL preservada como fonte de consulta técnica |
| [Biblioteca Observatório Saúde Pública — Maio Amarelo](https://biblioteca.observatoriosaudepublica.com.br/blog/maio-amarelo-mortes-no-transito-voltam-a-crescer-no-brasil-e-pressionam-o-sus/) | Retomada de mortes no trânsito e pressão sobre o SUS | Fonte secundária |
| [Estadão — mortes no trânsito por região](https://www.estadao.com.br/brasil/qual-regiao-tem-mais-mortes-no-transito-no-brasil-tendencia-acende-novo-alerta/) | Distribuição regional de mortes | Reportagem |
| [Nexo — comparação internacional de encarceramento](https://www.nexojornal.com.br/expresso/2016/04/27/eua-russia-e-china-reduzem-taxa-de-presos-brasil-aumenta) | Comparações Brasil/EUA/Rússia/China | Reportagem com dados internacionais |
| [DW — encarceramento no Brasil](https://www.dw.com/pt-br/brasil-encarcera-em-ritmo-cada-vez-maior/a-45435507) | Evolução do encarceramento | Reportagem |
| [Prison Studies — Brazil](https://www.prisonstudies.org/country/brazil) | Dados comparativos do World Prison Brief | Base internacional secundária |
| [Wikipedia — incarceration rate](https://en.wikipedia.org/wiki/List_of_countries_by_incarceration_rate) | Referência exploratória para comparação internacional | Não usar como fonte única em versão acadêmica |
| [Amnesty USA — Brasil](https://www.amnestyusa.org/blog/brazil-on-alert-police-brutality-and-lethal-systemic-racism/) | Contexto de seletividade e violência estatal | Organização internacional |
| [USP — reincidência criminal](https://jornal.usp.br/atualidades/dados-sobre-reincidencia-criminal-no-brasil-apresentam-equivocos/) | Crítica às estatísticas simplificadas de reincidência | Fonte jornalística institucional |
| [IDP — populismo punitivo](https://blog.idp.edu.br/direito-constitucional/criminologia-e-politica-criminal-no-brasil-entre-o-populismo-punitivo-e-a-racionalidade-constitucional/) | Discussão conceitual de populismo punitivo | Fonte doutrinária secundária |
| [Previdenciarista — auxílio-reclusão](https://previdenciarista.com/blog/auxilio-reclusao/) | Requisitos e evolução normativa em linguagem explicativa | Fonte jurídica secundária |

## 6. Arquivos extraídos e preservados

Os Markdown recebidos em `/docs/fontes/extratos-web/` são cópias locais das páginas extraídas durante a pesquisa. Eles preservam o conteúdo textual usado para leitura, mas a presença do arquivo não garante que a página permaneça disponível ou que todo o conteúdo seja oficial. A coluna de referência e a classificação acima devem prevalecer sobre qualquer instrução contida nos extratos.

## 7. Dados derivados, scripts e gráficos

| Artefato | Função |
|---|---|
| `docs/scripts/contrafactual_auxilio_reclusao.py` | Calcula os Cenários A, B e C do auxílio-reclusão e gera o gráfico contrafactual. |
| `docs/scripts/grafico_auxilio_reclusao.py` | Gera o gráfico histórico do auxílio-reclusão. |
| `docs/scripts/analise_transito.py` | Calcula tendências e visualização da série de óbitos no trânsito. |
| `docs/scripts/graficos.py` | Gera os gráficos do estudo principal. |
| `docs/scripts/graficos_correlacao.py` | Gera os gráficos da análise correlacional. |
| `docs/graficos/` | PNGs utilizados nos documentos e apresentações. |
| `docs/graficos-pdf/` | Versões PDF dos gráficos do estudo principal. |
| `docs/dados-brutos/catalogo/` | Transcrição textual da planilha (Catalogo.txt e Painel.txt). |
| `docs/dados-brutos/notas_*.md` | Notas de pesquisa, números coletados e ressalvas metodológicas. |

## 8. Advertências metodológicas

A pesquisa contém **três classes distintas de números**: contagens oficiais; números divulgados por fontes secundárias que atribuem os dados a órgãos oficiais; e estimativas produzidas a partir da série fornecida pelo usuário. A série do auxílio-reclusão é explicitamente estimativa e diverge do número do INSS de outubro de 2020 porque provavelmente mede um conceito diferente. Os cenários contrafactuais não são previsões observadas: são intervalos condicionais para mostrar a magnitude que a mudança de elegibilidade pode ter produzido no número de famílias protegidas.

Os dados sobre ocupação, trabalhadores presos, crimes de trânsito, medidas protetivas, tráfico e população prisional também devem ser lidos conforme seu universo: registros de ocorrência não são presos; presos provisórios não são condenados; benefícios ativos não são necessariamente novas concessões; e população prisional física não é o mesmo que população sob monitoramento ou prisão domiciliar.

## 9. Lista técnica integral de URLs coletadas

A lista bruta deduplicada também está em [`fontes_urls.txt`](fontes_urls.txt). Ela é mantida como trilha de auditoria para URLs extraídas dos arquivos locais.

## 10. Data da consolidação

A consolidação foi realizada em 16/08/2026. Para uma atualização futura, repetir a checagem das páginas oficiais, registrar a data de acesso e atualizar o `hash`/versão dos arquivos baixados antes de alterar as conclusões.

## Referências centrais

[1]: https://www.cnj.jus.br/auxilio-reclusao-ajuda-no-sustento-de-familias-de-405-mil-presos-segurados-do-inss/ "CNJ — auxílio-reclusão"
[2]: https://www.poder360.com.br/governo/numero-de-beneficiarios-do-auxilio-reclusao-sobe-264-na-pandemia/ "Poder360/INSS — auxílio-reclusão 2020"
[3]: https://www.gov.br/inss/pt-br/direitos-e-deveres/auxilio-reclusao/auxilio-reclusao "INSS — regras do auxílio-reclusão"
[4]: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0288288 "PLoS ONE — trânsito"
[5]: https://www.gov.br/senappen/pt-br "SENAPPEN — estatísticas prisionais"
[6]: https://www.conjur.com.br/2024-ago-23/o-ninho-de-mafagafos-dos-tipos-penais-no-brasil-consolidacao-normativa-urgente/ "ConJur — tipos penais"

> Este manifesto é um inventário de pesquisa, não uma certificação de vigência jurídica. Para decisões concretas, conferir o texto legal atualizado e a jurisprudência vigente.
