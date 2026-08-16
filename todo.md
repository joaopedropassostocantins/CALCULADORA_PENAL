# Project TODO

- [x] Inspecionar a estrutura do repositório e identificar a tecnologia utilizada.
- [x] Analisar o catálogo de normas penais enviado e definir sua importação segura.
- [x] Traduzir e adaptar toda a interface para português brasileiro.
- [x] Informar claramente que resultados e valores são estimativas/sugestões hipotéticas, não aconselhamento jurídico.
- [x] Implementar consulta avulsa pelo valor hipotético de R$ 3,99.
- [x] Modelar planos apenas por quantidade de consultas, sem cobrança por assinatura implícita.
- [x] Preparar o fluxo de pagamento com PIX e cartão pelo Mercado Pago.
- [ ] Guardar credenciais do Mercado Pago exclusivamente como segredo do ambiente de execução do repositório.
- [x] Validar regras de cálculo, fluxo de acesso pago e responsividade.
- [x] Criar testes automatizados e documentação de configuração.
- [x] Verificar visualmente a interface local e a renderização do catálogo normativo importado.

- [x] Armazenar o Access Token produtivo somente como segredo do ambiente de execução, sem incluí-lo no repositório.
- [x] Validar a criação de uma preferência Mercado Pago usando o segredo configurado, sem efetuar cobrança real.
- [x] Documentar como obter Public Key e Access Token e como alternar entre credenciais de teste e produção.
- [x] Recomendar a rotação do token produtivo após seu compartilhamento na conversa.
- [x] Implementar confirmação de pagamento via webhook antes de liberar créditos de consulta.
- [x] Revisar a proteção contra criação repetida de preferências e o tratamento de estados pendente/aprovado.

## Registro de segurança

O Access Token produtivo foi recebido em mensagem do usuário e não será reproduzido, versionado ou escrito em arquivos do projeto. A Public Key pode ser usada no navegador apenas em componentes que dependam dela; a criação de preferências permanece exclusivamente no servidor.

### Referências operacionais

- Mercado Pago Developers: https://www.mercadopago.com.br/developers/pt/docs/checkout-pro/overview
- Painel de credenciais: https://www.mercadopago.com.br/developers/panel/app
- Credenciais de teste e produção devem ser mantidas separadas.

> O token deve ser rotacionado no painel do Mercado Pago porque foi compartilhado nesta conversa.

### Status de segurança

- [ ] O token produtivo foi armazenado em um secret manager da hospedagem.
- [x] O token não foi gravado no código-fonte, README, `.env.example` ou histórico do Git.
- [x] O servidor responde com erro controlado quando `MERCADO_PAGO_ACCESS_TOKEN` não está configurado.
- [x] PIX e cartão ficam sob a disponibilidade/configuração da conta Mercado Pago no Checkout Pro.

> Não executar uma cobrança real como teste. A validação deve usar credencial de teste ou uma requisição controlada de criação de preferência sem concluir o pagamento.

> A liberação de créditos deve aguardar confirmação confiável do Mercado Pago; redirecionamento de retorno, sozinho, não comprova pagamento aprovado.

### Critérios de pronto da integração

- [ ] `MERCADO_PAGO_ACCESS_TOKEN` chega por variável de ambiente no processo do servidor.
- [ ] `POST /api/checkout` cria uma preferência com preço centralizado e `external_reference` único.
- [ ] A resposta nunca devolve o Access Token ao navegador.
- [ ] O webhook valida a notificação e registra o estado da preferência/pagamento.
- [ ] A aplicação não libera consulta apenas porque a URL voltou com `pagamento=sucesso`.
- [x] Testes cobrem validação do segredo, estados aprovados/pendentes e ausência de criação de cobrança.

### Validação

- [x] Rodar `pnpm check` após os ajustes.
- [x] Rodar `pnpm test` após os ajustes.
- [x] Rodar `pnpm build` após os ajustes.
- [x] Fazer revisão visual desktop/mobile sem iniciar cobrança real.

### Entrega pendente

- [ ] Solicitar ao usuário a rotação do token produtivo e a confirmação de onde o segredo será hospedado.
- [ ] Informar claramente que o checkout real permanece bloqueado até o segredo estar configurado no ambiente de execução.
- [x] Criar uma versão Git depois dos testes finais.

### Nota

Os arquivos gerados anteriormente já cobrem a interface em português, o catálogo importado e o endpoint inicial de Checkout Pro. A próxima implementação deve priorizar webhook, idempotência e persistência dos créditos antes de declarar o pagamento operacional.

## Pacote local HTML/JavaScript para teste

- [x] Criar uma página HTML independente com interface da Calculadora Penal.
- [x] Criar CSS responsivo com formulário, resultado, catálogo resumido e opções de consulta.
- [x] Criar JavaScript do navegador para cálculo, busca, validação e interação com o checkout.
- [x] Criar proxy/servidor local que mantenha o Access Token apenas no backend.
- [x] Testar criação de preferência Mercado Pago sem concluir cobrança.
- [x] Documentar execução local e cuidados com credenciais.
