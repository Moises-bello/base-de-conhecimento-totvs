---
article_id: 9451155463831
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1a062681981a7b6c76328973216ec1f25c20d0cc4a4c35a57964ce861b5bda3a
fetched_at: '2026-06-28T22:38:42.742299+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help A410CROSWMS
type: support-article
updated_at: '2022-10-10T19:44:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9451155463831-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-A410CROSWMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao realizar a tentativa de exclusão ou alteração de um Pedido de Vendas (MATA410), o sistema apresenta o help A410CROSWMS.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Causa**

Este help é apresentado sempre que o parâmetro **MV\_WMSNEW** estiver habilitado (.T.) e houver um Pedido de Compras vinculado ao Pedido de vendas através do campo "Ped.Compra" (**C6\_PEDCOM**).

**Solução**Para solucionar a ocorrência, retire o vínculo do pedido de compras no campo "Ped.Compra" (**C6\_PEDCOM**), caso não utilize o a integração com o WMS, desabilite o parâmetro MV\_WMSNEW,  ou entre em contato com o Suporte do módulo WMS para maiores informações.
