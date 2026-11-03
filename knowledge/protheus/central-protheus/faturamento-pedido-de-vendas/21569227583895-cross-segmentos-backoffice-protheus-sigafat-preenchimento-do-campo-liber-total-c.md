---
article_id: 21569227583895
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 3692a1183dc2b46c0c186c339a00eaa0695dcdee2a1e81df4aace2834d5cfe84
fetched_at: '2026-06-28T22:38:39.986862+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Preenchimento do campo "Liber.
  Total (C5_LIBEROK)"
type: support-article
updated_at: '2025-02-17T11:19:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21569227583895-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Preenchimento-do-campo-Liber-Total-C5-LIBEROK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21569211883415) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**

Como é preenchido o campo "Liber. Total (C5\_LIBEROK)"?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

O campo "Liber. Total (C5\_LIBEROK)" é preenchido com "S" quando o pedido de venda foi completamente submetido a liberação para análise, independente de bloqueios posteriores.

Também não depende da rotina que liberou para a análise o item. Pode ser a rotina "MATA410 - Pedido de venda" ou "MATA440 - Liberação do pedido de venda".

O pedido de venda é completamente liberado quando a legenda fica amarela ou, existe na tabela "SC9 - Liberações do pedido de venda" linhas do pedido de venda com quantidade suficiente para ser igual ao total do pedido de venda no campo "Quantidade (C6\_QTDVEN)", assim o sistema sabe que ele foi todo liberado.

Esse campo interage com as legendas do pedido de venda abertos (cor verde), encerrados (cor vermelha) ou liberados (cor amarela).

* Se o contéudo do campo "Liber. Total (C6\_LIBEROK)", "Nota Fiscal (C5\_NOTA)" e "Blq Regras (C5\_BLQ)" estiverem vazios, a legenda do pedido de venda será verde (pedido de venda em aberto)
* Se o contéudo do campo "Blq Regras (C5\_BLQ)" estiver nulo e ou o campo "Nota Fiscal (C5\_NOTA)" não for nulo ou o campo "Liber. Total (C6\_LIBEROK)" estiver igual a "E", a legenda do pedido de venda será vermelha (pedido de venda faturado)
* Se o contéudo do campo "Liber. Total (C6\_LIBEROK)" não for vazio e o conteúdo dos campos "Nota Fiscal (C5\_NOTA)" e "Blq Regras (C5\_BLQ)" forem vazios,  a legenda do pedido de venda será amarela (pedido de venda totalmente liberado)
