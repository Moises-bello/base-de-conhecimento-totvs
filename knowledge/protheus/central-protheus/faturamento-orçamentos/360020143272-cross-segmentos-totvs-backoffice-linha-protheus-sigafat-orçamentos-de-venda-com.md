---
article_id: 360020143272
category: Faturamento - Orçamentos
content_hash: 68d71292c72645d45bb5fa4c6b8ff888c228f0f6d2881207efbcab4ab7447ff4
fetched_at: '2026-06-28T22:38:24.978945+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Orçamentos
  de Venda com Situação Tributária
type: support-article
updated_at: '2022-08-29T17:44:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020143272-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Or%C3%A7amentos-de-Venda-com-Situa%C3%A7%C3%A3o-Tribut%C3%A1ria
---

**Dúvida**

Como utilizar o preenchimento automático da situação tributária no orçamento (mata415)?

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGAFAT – todas as versões

**Solução**

Implementação de um gatilho no campo **Tipo de Operação** (**CK\_OPER**) com a finalidade de realizar o preenchimento automático da situação tributária do produto no campo "**Sit.Tribut.**" (**CK\_CLASFIS**) na *grid* do Orçamento de Vendas.

Para a implementação, crie o gatilho do campo CK\_OPER e configure a tes inteligente para utilização no orçamento. Consulte a documentação técnica para efetuar processos informados: **[1717256 DSERFAT-3378 DT Orçamentos de Venda com Situação Tributária](http://tdn.totvs.com/pages/viewpage.action?pageId=337352443)**
