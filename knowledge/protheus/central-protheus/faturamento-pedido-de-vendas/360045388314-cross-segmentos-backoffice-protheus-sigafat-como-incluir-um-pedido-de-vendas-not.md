---
article_id: 360045388314
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 9c9dee09dde3d7edaf184325c69e62326b40bb398c62a3c2ebbf636c0125dbe0
fetched_at: '2026-06-28T22:38:39.720144+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como incluir um pedido de
  vendas / nota fiscal com a quantidade zerada
type: support-article
updated_at: '2026-04-02T19:01:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045388314-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-incluir-um-pedido-de-vendas-nota-fiscal-com-a-quantidade-zerada
---

**Dúvida**

Como incluir um pedido de vendas / nota fiscal com a quantidade zerada?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**

Ao incluir um pedido com o Tipo (**C5\_TIPO**) complemento, o sistema automaticamente exige que a quantidade fique zerada, exceto se o complemento for de quantidade.

Caso necessite inserir a quantidade zerada nos demais tipos de pedido de venda, é necessário preencher o campo, do TES, “Qtd.Zerada” (**F4\_QTDZERO**) como “1 – Sim”.
