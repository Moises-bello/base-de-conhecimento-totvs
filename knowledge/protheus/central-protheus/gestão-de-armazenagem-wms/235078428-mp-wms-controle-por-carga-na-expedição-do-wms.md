---
article_id: 235078428
category: Gestão de Armazenagem (WMS)
content_hash: 1f27fe77edd94f3f050503ecb2d15b18e63f1ff80ec7cff0a18ba1e16fcf0e8d
fetched_at: '2026-06-28T22:45:48.189243+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: MP - WMS - Controle por carga na expedição do WMS
type: support-article
updated_at: '2019-12-27T12:51:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235078428-MP-WMS-Controle-por-carga-na-expedi%C3%A7%C3%A3o-do-WMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como efetuar o controle por carga na expedição do **WMS *- Warehouse Management System***?  
  
**Ambiente**  
Microsiga Protheus – Gestão de Armazenagem – A partir da versão 11.80  
  
**Solução**1. Configure o parâmetro **MV\_WMSACAR - Permite aglutinar Produto + Carga -** igual a **S**.  
2. Informe no pedido de venda que utiliza carga - **C5\_TPCARGA** - e que gera ordem de serviço **WMS** na montagem da carga - **C5\_GERAWMS**.   
  
Com base nisto, a geração da ordem de serviço para iniciar o processo **WMS** ocorrerá apenas na montagem da carga e os produtos iguais, mesmo que de pedidos diferentes, serão aglutinados em uma única ordem de serviço de expedição.  
  
**Importante**  
Caso o parâmetro **MV\_WMSACAR** esteja como **N**, mesmo que as ordens de serviço sejam geradas apenas na montagem da carga, nenhum item de pedido será aglutinado.  
  
Além disto, se o pedido de venda utilizar carga e gerar ordem de serviço **WMS** na liberação do pedido, todo o processo do **WMS** seguirá com a separação dos pedidos de forma individual, sem aglutinação.
