---
article_id: 360016127411
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d2d3ca20aff47aa104f228657b82810820edfab1e5ee4ce9e5af81f8c9bb8004
fetched_at: '2026-06-28T22:38:29.982284+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Funcionamento
  dos parâmetros MV_RESAUT, MV_DELRES e MV_DELRES2
type: support-article
updated_at: '2023-08-02T19:41:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016127411-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Funcionamento-dos-par%C3%A2metros-MV-RESAUT-MV-DELRES-e-MV-DELRES2
---

**Dúvida**

Qual é o comportamento dos parâmetros **MV\_RESAUT, MV\_DELRES** e **MV\_DELRES2** no pedido de venda?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - A partir da versão 11.80

**Solução**

Segue as indicações dos Parâmetros:

**MV\_DELRES**

Este parâmetro permite que a reserva seja excluída de um Pedido de Venda automaticamente, ao estornar a liberação do Pedido.

**MV\_DELRES = .T.**

Na exclusão do Pedido de Vendas o Sistema excluirá a reserva.

Na alteração do pedido de Vendas o Sistema limpará o campo "Num.Reserva" (C6\_RESERVA), excluirá a reserva e criará uma nova reserva, colocando-a no campo "Num.Reserva" (C6\_RESERVA).

**MV\_DELRES = F.**

Na exclusão do Pedido de Vendas o Sistema não excluirá a reserva, apenas alterará o status para não baixada.

Na alteração do Pedido de Vendas o Sistema manterá a reserva no pedido.

**Observações:**

* O estorno deverá ser feito através da rotina de Prep. Documento de Saída (MATA460A), através da opção "Estor. Docs.". (.T. - Exclui / .F. - Não exclui, apenas deixa a reserva como não baixada)

**MV\_DELRES2** - Indica se as reservas incluídas por meio de do parâmetro **MV\_RESAUT** podem ser excluídas manualmente, após o estorno da liberação do pedido de venda.

**MV\_RESAUT** - Indica se após a inclusão de um item de pedido de venda com lote (rastreabilidade) deve-se efetuar automaticamente a reserva de estoque.

**Saiba mais:**

Exemplos de uso: **[Comportamento dos parâmetros MV\_DELRES e MV\_DELRES2](http://tdn.totvs.com/pages/viewpage.action?pageId=389546972)**
