---
article_id: 360020838191
category: NFe - Nota Fiscal Eletrônica
content_hash: 7c462ee99b91f85e93c5b9c4a969f54ff5e20163e052a5f4a18aa657f86c19aa
fetched_at: '2026-06-28T22:40:05.229313+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 690 Rejeição :
  Pedido de cancelamento para NF-e com CT-e ou MDF-e.'
type: support-article
updated_at: '2025-07-14T14:20:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020838191-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-690-Rejei%C3%A7%C3%A3o-Pedido-de-cancelamento-para-NF-e-com-CT-e-ou-MDF-e
---

**Dúvida**690 Rejeição : Pedido de cancelamento para NF-e com CT-e ou MDF-e.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

Uma NF-e pode estar referenciada em diferentes CT-es ou MDF-es, nos grupos de documentos referenciados deste modelos. Quando uma NF-e está vinculada a ***um CT-e ou MDF-e,*** esta não poderá ser cancelada. Caso o emitente da NF-e tente registar um evento de cancelamento, quando há um vinculo desta com um CT-e ou MDF-e a Sefaz retornará a rejeição *"**690 - Pedido de cancelamento para NF-e com CT-e ou MDF-e**".*

Para que a NF-e possa ser cancelada, o emitente do CT-e ou MDF-e deve cancelar o seu documento fiscal que está referenciando a NF-e. A partir do momento que o ***CT-e ou MDF-e forem cancelados, a NF-e poderá também ser cancelada.***

1. Cancelar o ***CT-e ou MDF-e vinculados*** a NF-e

2. Após o cancelamento do ***CT-e ou MDF-e, transmita novamente a NF-e***, conforme o link abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como cancelar (cancelamento) uma nota fiscal eletrônica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018751111)
