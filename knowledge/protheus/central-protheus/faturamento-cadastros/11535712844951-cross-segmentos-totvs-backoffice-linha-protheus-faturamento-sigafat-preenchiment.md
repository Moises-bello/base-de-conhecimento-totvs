---
article_id: 11535712844951
category: Faturamento - Cadastros
content_hash: 9ac1e9ea0db6ce1db05f15572dabc63249d0c331dbdec5d01cb0b9a0fd23e4d1
fetched_at: '2026-06-28T22:38:36.911365+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos – TOTVS Backoffice (Linha Protheus) – Faturamento (SIGAFAT)
  – Preenchimento do campo "Tipo" (EC_TIPO)
type: support-article
updated_at: '2023-01-12T19:16:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11535712844951-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Preenchimento-do-campo-Tipo-EC-TIPO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**

Como realizar o preenchimento do campo "Tipo" (EC\_TIPO)?

**Ambiente**Cross Segmentos – TOTVS Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Ao realizar o cadastro de uma condição de pagamento do tipo B, ou seja, preenchendo o campo "Tipo" (E4\_TIPO) como B, é possível utilizar duas ou mais condições de pagamento de forma conjunta.

O campo "Tipo" (EC\_TIPO) indica o tipo da condição de pagamento que será aplicada, no percentual da venda, indicado no campo "% Rateio" (EC\_RATEIO):

![Cond_PGTO_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11628005801367)

No exemplo acima, na linha destacada, será aplicada uma condição de pagamento do Tipo 1, campo "Tipo" (EC\_TIPO) preenchido como 1, em 20% do valor da venda, campo "% Rateio" (EC\_RATEIO) preenchido como 20, e será pago "à vista", campo "Cond. Pagto" (EC\_COND) preenchido como 00.

O Help **Tipo** será apresentado, caso seja informado no campo "Tipo" (EC\_TIPO) um tipo de condição de pagamento que seja inválido:

![Tipo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11628239458583)

**Saiba mais:** [Condições de Pagamento (MATA360)](https://tdn.totvs.com/x/PdpSDg)
