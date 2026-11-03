---
content_hash: b72922585d6da36b91fa21a5484902423f2e8aac1d00aad06400541eb9ed17aa
fetched_at: '2026-07-02T19:24:25.799443+00:00'
page_id: '506790663'
product: protheus
source: tdn-tec
title: Correção - Foco em Janelas MDI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506790663
version: 1
---

|  |  |
| --- | --- |
| Situação | Em situações que ocorre um pedido de foco em uma janela que não esteja acima das outras (visível), faz com que a janela visível fique "escondida" por trás de outra. |
| Ocorrência | Problema começou a ocorrer no QT5 que aceita a troca de foco mesmo em caso de janela modal |
| Correção | Correção efetuada para não permitir a troca de foco caso a janela pai do widget não esteja visível. |
| Informações adicionais | * Referente ao chamado: [6441486](https://totvssuporte.zendesk.com/agent/tickets/6441486 "View ticket on the Zendesk portal") * Referente à ocorrência: MTEC-3079 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.10 |
