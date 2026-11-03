---
article_id: 18170981581335
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 6cc7431a26131c138d8af124ef62486a0913ed86e2d93356081647d548086bee
fetched_at: '2026-06-28T22:38:42.491961+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Como reabrir pedido
  de compra após devolução de compras?
type: support-article
updated_at: '2023-10-10T18:52:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18170981581335-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Como-reabrir-pedido-de-compra-ap%C3%B3s-devolu%C3%A7%C3%A3o-de-compras
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18171007929879)***Tempo aproximado para leitura:**00:01:30 min**

**Dúvida**Como reabrir alterando o status do Pedido de Compra ao realizar a devolução da compra?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**No Protheus é possível a reabertura automática dos pedidos de compras quando vinculados a uma nota fiscal para a qual foi realizada uma devolução de Compra, para isso foi criado o parâmetro **"MV\_COMPCDV"** para alterar o status do pedido de compras para "Em Aberto" após a devolução da NF em que ele estava vinculado.

**MV\_COMPCDV = .F.**Ao devolver compra com pedido vinculado, não reabre o pedido de compra.

**MV\_COMPCDV = .T.**Ao devolver compra com pedido vinculado, reabre o pedido de compra.

**OBSERVAÇÃO:** Não serão considerados nesta reabertura do Pedido de Compras itens que foram Eliminado Resíduo.

**Saiba Mais:**

[MV\_COMPCDV - Parâmetro para alterar o status do pedido de compras para em aberto após a devolução](http://tdn.totvs.com/pages/viewpage.action?pageId=233753468)
