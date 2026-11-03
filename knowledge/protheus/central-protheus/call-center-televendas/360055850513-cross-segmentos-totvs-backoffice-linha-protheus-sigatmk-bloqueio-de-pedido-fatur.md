---
article_id: 360055850513
category: Call Center - Televendas
content_hash: 82eacf9a126211161b5d0f48121db17cd15dfb4eb76d8f9280b8a064c9e44d8e
fetched_at: '2026-06-28T22:41:30.319484+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK-Bloqueio de pedido
  faturado via TMK
type: support-article
updated_at: '2022-06-22T19:04:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055850513-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Bloqueio-de-pedido-faturado-via-TMK
---

**Dúvida**

O pedido efetuado pelo atendimento Call center (**TMKA271**), encontra-se faturado e ainda sim, é permitido a alteração, existe uma forma de bloquear a alteração?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - todas as versões.  
  
**Solução**

Da mesma forma que no pedido de venda (**MATA410**) do módulo Faturamento, para o pedido gerado pelo atendimento TMK, é necessário  que o parâmetro **MV\_ALTPED** esteja configurado como N para não permitir alteração.

O pedido tem que estar 100% faturado para que o parâmetro funcione, em caso de faturamento parcial, seguirá a mesma regra do módulo Faturamento e permitirá a alteração.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093063573/mceclip0.png)

![mv_altped_tmk.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360093061493/mv_altped_tmk.gif)
