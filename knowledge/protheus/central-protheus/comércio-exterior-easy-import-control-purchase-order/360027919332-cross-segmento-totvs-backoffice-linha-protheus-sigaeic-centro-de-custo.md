---
article_id: 360027919332
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 4a99627137f02221698b4b46c688fa4ba26edb2a7b86917db6493c47f1d63d10
fetched_at: '2026-06-28T22:39:41.094232+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Centro de Custo
type: support-article
updated_at: '2022-06-10T18:51:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027919332-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Centro-de-Custo
---

**Dúvida**Como é preenchido o campo C7\_CC (Centro de Custo) quando realizada a inclusão através da Purchase Order?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**O cento de custo pode ser informado no campo W3\_CTCUSTO, caso este esteja em branco será levado a Unidade Requisitante campo W3\_CC, definido no parâmetro **MV\_GCUSTO** que permite manipular o envio do Centro de Custo para o pedido de compras.

Quando o parâmetro **MV\_GCUSTO** estiver ligado (.T.), se o campo W1\_CTCUSTO estiver preenchido o mesmo será enviado para o pedido de compra e caso esteja vazio será enviado o campo W1\_CC.

Se o parâmetro **MV\_GCUSTO** estiver desligado (.F.), o campo Centro de Custo será enviado em branco no pedido de compras.

**Observação:** Com a configuração do parâmetro **MV\_GCUSTO** (.F.).

Saiba mais: [Criação do parâmetro MV\_GCUSTO para manipular o envio do Centro de Custo para o pedido de compras](http://tdn.totvs.com/pages/releaseview.action?pageId=223163026)
