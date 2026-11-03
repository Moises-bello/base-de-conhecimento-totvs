---
article_id: 24797140106391
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d0d4d5eabaee2ed63781cb0674d52e9fd4c0ea52bbf4ac32ae74b4f1016ccd1e
fetched_at: '2026-06-28T22:38:42.558911+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help A410PRODFA no faturamento
type: support-article
updated_at: '2024-07-10T19:01:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24797140106391-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A410PRODFA-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24797140043031) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como solucionar e por qual motivo ocorre o Help A410PRODFA?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

**Entendendo a causa do erro:**

O Help ocorre em dois momentos no pedido de venda:

* "Qtd. Entregue C6\_QTDENT" maior ou igual a "Qtd. Vendida (C6\_QTDVEN)" com o campo da TES do pedido de venda "Qtd. Zero (F4\_QTDZERO)" sendo diferente de "1 - Não".
* "Qtd. Entregue C6\_QTDENT" igual a "Qtd. Vendida (C6\_QTDVEN)" com o campo da TES do pedido de venda "Qtd. Zero (F4\_QTDZERO)" sendo igual a "1 - Não" e a linha desse item estiver com o campo "Nota fiscal (C6\_NOTA)" preenchido.

**Solução:**

* Informar uma quantidade no item maior do que já foi anteriormente faturada, nunca a menor, pois não há como estar no pedido de venda para vender 5 itens e já ter sido vendido 10, por exemplo.
