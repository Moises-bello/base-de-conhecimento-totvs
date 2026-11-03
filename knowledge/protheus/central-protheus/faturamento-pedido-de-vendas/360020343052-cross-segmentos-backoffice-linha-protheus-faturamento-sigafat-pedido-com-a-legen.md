---
article_id: 360020343052
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 009ddb11abff7cabc7065a03daa879598818753d2178f944cc21d6d48f819764
fetched_at: '2026-06-28T22:38:38.693375+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Pedido
  com a legenda "bloqueado"
type: support-article
updated_at: '2022-09-28T13:58:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020343052-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Pedido-com-a-legenda-bloqueado
---

**Dúvida**

Uma vez que o pedido de venda está liberado e é feito uma analise sobre o mesmo, neste momento verifica-se que o pedido não pode ser liberado.

Como eu faço para aparecer a **LEGENDA de Pedido bloqueado** e também como faço para desbloqueá-lo depois?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.  
  
**Solução**

Na legenda de pedido de venda (**MATA410**), o pedido somente será gerado como bloqueado caso exista uma regra de negócio ou bloqueio de verba de venda, no qual o pedido seja enquadrado, conforme **FAQ:** **[FAT0242 Liberações / Bloqueios do Pedido de Vendas](http://tdn.totvs.com/pages/viewpage.action?pageId=330839110)**

Para estes tipos de bloqueios, existe a rotina Liberação de regras (**FATA210**) para visualizar o tipo de bloqueio que o pedido sofreu e efetuar a sua liberação.  
  
Agora, se o pedido foi liberado via rotina de Liberação de Pedido (**MATA440**) e sofreu bloqueio de crédito e estoque, devido ao parâmetro **MV\_BLOQUEI** estar como T, esta legenda de bloqueio somente poderá ser vista na rotina de Liberação de crédito (**MATA450**) ou liberação de estoque (**MATA455**), a **FAQ** acima também explica como pode ser visualizado e liberado estes tipos de bloqueios.
