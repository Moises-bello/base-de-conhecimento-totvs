---
article_id: 235302607
category: Gestão de Armazenagem (WMS)
content_hash: 4ec6cc9550dc56a07c882352359e04b29c1c2abf4e423838c8fe8b5af11a71e0
fetched_at: '2026-06-28T22:45:47.873130+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Distribuição - Linha Protheus - WMS - Aglutinação de itens do mesmo Lote e
  Sub-lote na nota fiscal de saída
type: support-article
updated_at: '2024-03-04T13:49:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235302607-Distribui%C3%A7%C3%A3o-Linha-Protheus-WMS-Aglutina%C3%A7%C3%A3o-de-itens-do-mesmo-Lote-e-Sub-lote-na-nota-fiscal-de-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16431745913751) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**É possível a aglutinação de itens do mesmo **Lote** e **Sub-lote** na nota fiscal de saída?  
  
**Ambiente**  
TOTVS Distribuição - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS)  – A partir da versão 11.80  
  
**Solução**Sim. Quando o pedido de venda utiliza carga e gera ordem de separação **WMS - Warehouse Management System** no pedido, o Sistema considera a parametrização de aglutinação de itens do mesmo lote e sub-lote na nota fiscal de saída.  
  
Para isto, é necessário configurar o parâmetro **MV\_WMSAGLU - Aglutina item da Nota Fiscal de Saída do mesmo Lote e Sub-Lote na execução de serviço do WMS** igual a **.T.**.  
  
Utilização no Sistema:

1. Gerar pedidos de venda que utilizem carga, gerar as ordens de serviço no pedido e solicitar várias normas de um mesmo produto.
2. Montar uma carga com os pedidos gerados.
3. Executar as ordens de serviço.
4. Efetuar o processo de separação por meio do coletor de rádio frequência.
5. O **WMS** aglutinará as quantidades em um único registro da tabela **SC9 - Pedidos Liberados** -para itens de cada pedido com mesmo lote e sub-lote.
