---
article_id: 360034579773
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a4a7553af22e40a8fea066878e56ed8f508eef18bff9f03cc7d3187ce6168239
fetched_at: '2026-06-28T22:38:41.048092+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - O frete da nota fiscal de entrada/compra não é preenchido na devolução via pedidos
  de venda
type: support-article
updated_at: '2022-11-30T14:12:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034579773-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-O-frete-da-nota-fiscal-de-entrada-compra-n%C3%A3o-%C3%A9-preenchido-na-devolu%C3%A7%C3%A3o-via-pedidos-de-venda
---

**Dúvida**

Por que o valor do frete da nota fiscal de compras/entrada não é carregado na Devolução de compras (via pedido de vendas)?  
  
**Ambiente**

Microsiga Protheus – A partir da versão 12.  
  
**Solução**

Ao informar um valor de **frete** em uma **nota de compra** / **entrada** e realizar uma **devolução** da nota pelo pedido de vendas, o **valor do frete** por padrão **não é carregado**.

Isso porque o valor do frete aplicado pela transportadora contratada pelo fornecedor não é necessariamente o valor a ser aplicado na devolução do material.

A transportadora contratada na devolução pode aplicar preços e condições diferentes dos aplicados na compra, por isso, na devolução é **necessário** **informar** o valor do frete no campo **C5\_FRETE** (Frete) **manualmente**.

**Saiba mais**:  
**<http://tdn.totvs.com/pages/releaseview.action?pageId=225264003>**
