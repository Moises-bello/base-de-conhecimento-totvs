---
article_id: 235301987
category: Gestão de Armazenagem (WMS)
content_hash: 169f6fb46da6d7f6e7ac43398e7846c4738bb8c3c78a5a080b672e9c28d64432
fetched_at: '2026-06-28T22:45:48.003973+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Definir a doca de destino no processo de
  expedição
type: support-article
updated_at: '2021-12-22T12:21:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235301987-Log%C3%ADstica-Linha-Protheus-WMS-Definir-a-doca-de-destino-no-processo-de-expedi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png) Tempo aproximado para leitura: **00:01:25 min  
  
Dúvida**Como definir a doca de destino no processo de expedição do **WMS *- Warehouse Management System?*****Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - Versão 12  
  
**Solução**Existem basicamente três formas de definir o endereço de doca no processo de expedição*,* são eles:

1. Informar diretamente no **pedido de venda** o endereço destino a ser utilizado para o processo **WMS**, no campo **End. Destino**.
2. Informar o endereço destino de uma carga durante o processo de **montagem da carga**. Para esta opção deve ser configurado o parâmetro **MV\_****WMSEOMS**. Caso este parâmetro esteja como sim, será solicitado o endereço destino do processo **WMS** quando não foram informados nos itens do pedido de venda ou quando dentre esses endereços existirem endereços diferentes.
3. Informar o endereço destino diretamente na execução da ordem de serviço do **WMS**. Nesta terceira opção será considerado o mesmo endereço destino para todo o documento, quando:  
   3.1 Não utilizar carga ou as ordens de serviço deste pedido tiverem sido geradas durante a liberação do pedido.  
   3.2 Utilizar carga e a geração das ordens de serviço tiverem sido geradas durante o processo de **montagem da carga**.

Na opção 2, durante a **montagem da carga**, somente será considerado o novo endereço informado como destino para os pedidos que não tenham suas ordens de serviço executadas no processo do **WMS**, ou seja, as ordens de serviço devem estar pendentes, pois quando as mesmas já foram executadas, os movimentos já foram direcionados para o endereço informado no pedido ou na execução da ordem de serviço. Portanto, não poderá ser alterado!  
  
**Importante**  
Caso todas as ordens de serviço dos pedidos que vão compor a carga tenham sido executadas, não será solicitado o endereço destino durante a montagem de carga.
