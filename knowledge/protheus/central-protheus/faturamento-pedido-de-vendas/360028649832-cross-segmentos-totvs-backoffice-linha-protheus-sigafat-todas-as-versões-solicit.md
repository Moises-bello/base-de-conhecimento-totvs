---
article_id: 360028649832
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b62933b4fb3c7e32f003b615356e95828428376f9b73a4c5a36dd6713a49956a
fetched_at: '2026-06-28T22:38:41.194622+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGAFAT – todas as versões-Solicitação
  de Pedido De Vendas
type: support-article
updated_at: '2022-08-29T17:42:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028649832-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-todas-as-vers%C3%B5es-Solicita%C3%A7%C3%A3o-de-Pedido-De-Vendas
---

**Dúvida**

Existe uma rotina de Solicitação de Pedido de Vendas no módulo de Faturamento, parecida com Solicitação de Compras do módulo de Compras?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGAFAT – todas as versões

**Solução**

Hoje, não há um tratamento no módulo de Faturamento de solicitação de pedido de vendas como é feito no módulo de Compras através da rotina Solicitação de Compras (**MATA110**) .

No módulo Faturamento, o que poderia ser considerado um pré-pedido seria a rotina de orçamento (**MATA415**) e através dela, posteriormente, aprovar e gerar o pedido de venda (**MATA410**), fora disso, é só a inserção direta do pedido.

A rotina de Orçamento apenas trabalha com a entidade Cliente (**MATA030**), não trata a entidade Fornecedor (**MATA020**).

No módulo Faturamento, e entidade Fornecedor , somente é utilizada no momento de um pedido de venda, do tipo **Devolução de Compra** ou envio para **Beneficiamento**.
