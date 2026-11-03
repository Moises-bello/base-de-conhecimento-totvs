---
article_id: 25950530257815
category: Financeiro
content_hash: 8229902acf74f619d7094990e1da00024e17ccdef3970ecd69d92f3519850350
fetched_at: '2026-06-28T22:38:03.060926+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Como é demonstrado
  o Saldo em Aplicações no Novo Painel Gestor > Movimentações Financeiras > Saldo
  em Aplicações?
type: support-article
updated_at: '2024-08-29T14:06:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25950530257815-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Como-%C3%A9-demonstrado-o-Saldo-em-Aplica%C3%A7%C3%B5es-no-Novo-Painel-Gestor-Movimenta%C3%A7%C3%B5es-Financeiras-Saldo-em-Aplica%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25950530225943) Tempo aproximado para leitura: **00:15:00 min****Dúvida**FINA710 - Como é demonstrado o "saldo em aplicações" no Novo Painel Gestor > Movimentações Financeiras > Saldo em Aplicações?  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - A partir P22.1.10]  
  
**Solução**

**Exemplo 1:**

Ao incluir uma aplicação CDB feita no inicio do ano no valor de R$ 1.000.000,00

No final do ano, sem resgatar ou apropriar, emitir o FINA710 - Novo Painel Gestor > Movimentações Financeiras > Saldo em Aplicações

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25950491890327)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25950491891863)

Hoje será demostrado no quadrante "**Saldo em Aplicações**" o valor inicial da aplicação.

Não sendo considerado os juros compostos do período em uma aplicação com o cenário acima

**Exemplo 2:**

Ao incluir uma **empréstimo** com taxa 80% no valor de R$ 1.000.000,00 hoje, onde será gerado 2 parcelas de 30 dias entre os títulos, com amortização **SAC**.

Serão gerados as parcelas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25951271116823)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25951271119127)

Serão gerado as parcelas do tipo:PR no **FINA050 - Contas a Pagar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25951287754519)

Como foi gerado as parcelas, serão considerados a primeira parcela no quadrante de "**Saídas**" que estão dentro dos 30 dias

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25951271125911)

E na visão consolidado também serão provisionados

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25951287760407)
