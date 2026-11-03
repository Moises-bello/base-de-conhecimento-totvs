---
article_id: 11535799142295
category: Faturamento - Cadastros
content_hash: 88e52913adeeb4919f7c161b8b844b75d49e1465504096dec924d133a5251803
fetched_at: '2026-06-28T22:38:36.898348+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos – TOTVS Backoffice (Linha Protheus) – Faturamento (SIGAFAT)
  – Preenchimento do campo  "Cond. Pagto" (EC_COND)
type: support-article
updated_at: '2023-01-12T18:05:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535799142295-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Preenchimento-do-campo-Cond-Pagto-EC-COND
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Como realizar o preenchimento do campo "Cond. Pagto" (EC\_COND)?

**Ambiente**Cross Segmentos – TOTVS Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões  
**Solução**

Ao realizar o cadastro de uma condição de pagamento do tipo B, ou seja, preenchendo o campo "Tipo" (E4\_TIPO) como B, é possível utilizar duas ou mais condições de pagamento de forma conjunta.

O campo "Cond. Pagto" (EC\_COND) indica a regra a ser aplicada, no percentual da venda, indicado no campo "% Rateio" (EC\_RATEIO), ele determina a geração das duplicatas, caso o pedido de venda gere títulos (F4\_DUPLIC = “S – Sim”):

![Cond_PGTO_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11625665779735)

No exemplo acima, 20% do valor da venda, "% Rateio" (EC\_RATEIO) igual a 20, será pago em 00 dias, ou seja, "à vista", 30% do valor da venda, "% Rateio" (EC\_RATEIO) igual a 30, será pago em 30 dias e 50% será pago em 60 dias.

**Saiba mais:** [Condições de Pagamento (MATA360)](https://tdn.totvs.com/x/PdpSDg)
