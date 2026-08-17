# Calculadora Penal

> **Aviso importante:** esta aplicação é um simulador informativo. Ela não presta consultoria jurídica, não substitui a análise do caso concreto e não deve ser usada como fundamento exclusivo para decisões processuais ou estratégicas. A revisão por profissional habilitado é indispensável.

## O que está incluído

A interface oferece uma simulação aritmética por fases, busca no catálogo de normas enviado pelo usuário e consulta avulsa/pacotes por quantidade de consultas. Os valores comerciais são **sugestões hipotéticas**, centralizados em `src/data/pricing.ts`.

| Recurso | Estado |
| --- | --- |
| Simulação aritmética por parâmetros inseridos | Implementado |
| Catálogo de normas, súmulas e precedentes | Importado de planilha fornecida |
| Checkout Mercado Pago para PIX e cartão | Preferência validada; exige credencial privada no ambiente |
| Webhook de confirmação | Implementado; consulta o pagamento na API antes de classificar o evento |
| Confirmação de pagamento via webhook verificador | Implementada; persistência de créditos ainda pendente |
| Liberação de créditos persistentes | Próxima etapa recomendada |

## Documentação de pesquisa

O diretório `docs/` reúne os estudos, dados e o prompt técnico produzidos na investigação sobre a hiperinflação legislativa penal e o encarceramento no Brasil. Inclui a nota técnica do cenário contrafactual do auxílio-reclusão ("e se as regras de 2019 não tivessem mudado?"), os estudos correlacionais completos, os gráficos em alta resolução e o prompt para catalogação nacional de tipos penais vigentes em um projeto do Claude. Ver `docs/README.md`.

## Verificação realizada

Em 15/08/2026, a interface local foi revisada com êxito. A página exibiu a simulação paramétrica, **88 normas catalogadas**, 15 súmulas vinculantes, 25 súmulas STF/STJ e 12 precedentes vinculantes importados da planilha fornecida. O endpoint de checkout permanece propositalmente indisponível até a inclusão de uma credencial privada válida do Mercado Pago.

## Catálogo de tipos penais

O inventário de figuras incriminadoras fica separado do catálogo de diplomas normativos. A fonte canônica é `src/data/tiposPenais.json`, acompanhada de `src/data/tiposPenais.schema.json`; `src/data/tiposPenais.csv`, `src/data/fontesPenais.json` e `sites/calculadora-penal/data/tiposPenais.public.json` são derivados. Execute `pnpm run catalog:generate` para regenerá-los e `pnpm run catalog:validate` para verificar IDs, dispositivos, referências a tipos-pai, penas, datas, URLs e bloqueio de registros pendentes no cálculo.

O checkpoint atual é deliberadamente **incompleto**: contém 119 registros ativos, dos quais 88 têm inventário conferido e 31 permanecem pendentes. O relatório de cobertura, as decisões metodológicas, as pendências jurídicas e o registro de fontes estão em `docs/catalogo/`. A aplicação publica os registros do checkpoint com o estado de conferência visível; somente os registros com inventário validado podem ser enviados à calculadora. O aviso de que a coleção não representa ainda todos os tipos penais vigentes permanece ativo.

## Execução local

Instale as dependências com `pnpm install`, copie `.env.example` para `.env` e preencha `MERCADO_PAGO_ACCESS_TOKEN` com a credencial privada do seu aplicativo Mercado Pago. Depois, execute `pnpm dev`.

O endpoint de checkout cria uma preferência no Checkout Pro. Em ambiente local, URLs de retorno não públicas são omitidas para evitar rejeição da API; em produção, defina `APP_URL` como uma URL HTTPS pública. Os meios de pagamento exibidos (PIX e cartão) dependem da conta e das configurações comerciais do vendedor no Mercado Pago. Consulte a documentação oficial antes de disponibilizar o serviço em produção: <https://www.mercadopago.com.br/developers/pt/docs/checkout-pro/overview>.

### Como obter as chaves

No painel de desenvolvedores do Mercado Pago, acesse **Suas integrações → sua aplicação → Credenciais**. Use o **Access Token** somente no servidor, como `MERCADO_PAGO_ACCESS_TOKEN`; nunca o inclua no frontend, no README ou em um commit. A **Public Key** é destinada a componentes de pagamento executados no navegador e não substitui o Access Token para criar preferências. Mantenha credenciais de teste e produção separadas e gere um novo token se uma credencial produtiva tiver sido compartilhada.

A tentativa de gravar o segredo como GitHub Actions Secret foi bloqueada pela permissão atual do token do repositório (`Resource not accessible by integration`). Portanto, o deploy ainda precisa configurar `MERCADO_PAGO_ACCESS_TOKEN` no ambiente privado da hospedagem antes de operar em produção. A credencial não foi adicionada a este repositório.

### Webhook e liberação de acesso

O endpoint `POST /api/webhooks/mercadopago` recebe a notificação, consulta o pagamento diretamente na API do Mercado Pago e só classifica o evento como verificado quando o status é `approved` e há `external_reference`. O retorno do navegador com `pagamento=sucesso` não libera créditos por si só. Antes da operação real, conecte o evento verificado a uma tabela persistente de créditos, implemente idempotência por `paymentId` e configure a URL HTTPS do webhook no painel do Mercado Pago.
