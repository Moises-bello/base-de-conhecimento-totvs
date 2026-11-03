---
article_id: 360042530834
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f135dd3bcf7b7aac85d9daf0a3eec50b63a723d39a77e93294bbff1d90420936
fetched_at: '2026-06-28T22:38:41.106433+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como gerar
  e excluir o registro na tabela SDC a partir do Pedido de Vendas?
type: support-article
updated_at: '2023-08-31T21:39:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042530834-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-gerar-e-excluir-o-registro-na-tabela-SDC-a-partir-do-Pedido-de-Vendas
---

**Dúvida**

Como gerar e excluir o registro na tabela **SDC** a partir do pedido de vendas (**MATA410**)?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT – todas as versões.  
  
**Solução**

Quando um produto possui controle de **Endereçamento (B1\_LOCALIZ)**, ao incluir um pedido de vendas e **liberá-lo**, o sistema deve gerar um registro na tabela **SDC**. Assim como, ao **estornar** a liberação do pedido, esta linha da tabela **SDC** deve ser deletada.

Caso o pedido gere **bloqueio** por falta de saldo de **estoque** ou **crédito**, a tabela **SDC não é gerada** até que realizadas as **liberações**.

Ao gerar a reserva através da rotina **Controle de Reservas** (**MATA430**), o sistema gera automaticamente o registro na tabela **SDC**, quando informada a reserva no pedido de vendas e liberado o pedido, o sistema deve **deletar** a linha da **SDC** gerada (que contém o **DC\_ORIGEM** igual a **SC0**) e criar uma nova linha (com o **DC\_ORIGEM** igual a **SC6**).

Quando gerada uma **ordem de produção** vinculada ao pedido, o sistema **não irá gerar** a tabela **SDC** até que **encerrada** a Ordem de Produção e liberado o bloqueio de estoque do pedido. Por regra do sistema, quando o produto possui controle de endereçamento, o apontamento da OP não irá libera-lo automaticamente, a liberação do estoque deve ser realizada selecionando o produto a ser vinculado ao pedido.  
  
O registro também é excluído da tabela SDC após gerar a Nota Fiscal.
