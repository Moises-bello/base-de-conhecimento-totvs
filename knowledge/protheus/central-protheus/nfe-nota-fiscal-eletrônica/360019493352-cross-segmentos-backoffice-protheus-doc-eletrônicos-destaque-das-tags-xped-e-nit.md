---
article_id: 360019493352
category: NFe - Nota Fiscal Eletrônica
content_hash: 2557a5a7df7b55f8b597730f91ee232fbe341e9bd5f323c25519e88ea5aeaaf8
fetched_at: '2026-06-28T22:40:06.823244+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Destaque das TAGS
  XPED E NITEMPED
type: support-article
updated_at: '2025-11-04T21:35:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019493352-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Destaque-das-TAGS-XPED-E-NITEMPED
---

**Dúvida**Como destacar as tags **xPed e nItemPed** no **xml** das notas

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

1- Para gerar as TAGS XPED e nItemPed em ***Produtos** **e Serviços / Pedido de Compra <xprod>** utilizar os campos do pedido de venda **Item.Ped.Com "C6\_ITEMPC"  e Num.Ped.Com  "C6\_NUMPCOM"***

**![](https://totvssuporte.zendesk.com/attachments/token/lFMKB6FNO6eF054JtYsc5Z6DT/?name=inline1402531613.png)**2- Para gerar as TAGS XPED ***Informações de Compras <compra>*** utilizar o campo do pedido de venda ***Ped. Cliente*** **C6\_PEDCLI**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4527491648663)**

* **Saiba mais:**

Se preencher os campos ***C6\_ITEMPC e o C6\_NUMPCOM*** gerará as TAGS no bloco de ***<PROD>*** e se preencher também o campo ***C6\_PEDCLI*** irá gerar mais uma TAG do ***XPED*** no bloco de ***<compra>***

Conforme o Manual *de* Orientação *Contribuinte* v\_6.00.pdf página 187. ***A Tag xPed***  de 1 até 15 caracteres, ***a TAG nItemPed***  6 números.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16540416182807)
