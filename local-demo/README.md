# Demo local HTML/JavaScript — Calculadora Penal

Esta pasta contém uma interface independente em HTML, CSS e JavaScript para testar localmente a calculadora e o Checkout Pro do Mercado Pago. O navegador chama apenas `/api/checkout`; o `MERCADO_PAGO_ACCESS_TOKEN` permanece no processo Node e nunca é incluído no HTML, no JavaScript do navegador ou na resposta da API.

## Execução

Na raiz do repositório, execute:

```bash
MERCADO_PAGO_ACCESS_TOKEN='SEU_ACCESS_TOKEN' PORT=3002 node local-demo/server.js
```

Depois, abra <http://localhost:3002>. Para verificar o servidor, clique em **Testar servidor**. Para validar a criação da preferência sem efetuar cobrança, escolha um dos pacotes. A página será redirecionada ao Checkout Pro apenas quando o Mercado Pago retornar uma preferência válida.

Em ambiente local, o servidor não envia `back_urls` nem `auto_return`, porque `localhost` não é uma URL HTTPS pública adequada para os retornos automáticos. Para testar retornos em um ambiente público, defina `APP_URL` com uma URL HTTPS acessível:

```bash
MERCADO_PAGO_ACCESS_TOKEN='SEU_ACCESS_TOKEN' APP_URL='https://seu-dominio.example' PORT=3002 node local-demo/server.js
```

## Segurança

Use credencial de teste sempre que possível. Não cole o token no `app.js`, no `index.html`, em `styles.css`, no README, em um commit ou em uma variável `VITE_`. Para produção, configure o token no secret manager da hospedagem. A Public Key não é necessária para este fluxo de Checkout Pro; ela só deve ser usada no frontend em integrações que explicitamente dependam dela.

> Esta demo não confirma pagamentos nem libera créditos. O próximo passo de produção é adicionar o webhook verificador, persistência idempotente dos pagamentos e a liberação controlada das consultas após status `approved` confirmado pela API do Mercado Pago.

## Arquivos

| Arquivo | Função |
| --- | --- |
| `index.html` | Estrutura da interface e formulário |
| `styles.css` | Identidade visual e responsividade |
| `app.js` | Cálculo no navegador, estado da interface e chamada do checkout |
| `server.js` | Servidor local e proxy privado para o Mercado Pago |
