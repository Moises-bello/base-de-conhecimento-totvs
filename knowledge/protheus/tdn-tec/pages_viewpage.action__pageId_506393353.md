---
content_hash: 2c8426eddca35c6ad4d042f7b1af560bc5264da766d4b5e31e43686109ee1cc8
fetched_at: '2026-07-02T19:24:25.785225+00:00'
page_id: '506393353'
product: protheus
source: tdn-tec
title: Correção - Margem de janela ocultando barra de rolagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506393353
version: 1
---

|  |  |
| --- | --- |
| Situação | Em algumas telas do Protheus, por exemplo inclusão do pedido de compra, está ocultando parte da barra de rolagem do TGetDados |
| Ocorrência | Problema começou a ocorrer no Lobo Guara devido a diferença de comportamento do tamanho da margem da janela no QT5. |
| Correção | Correção feita no estilo para respeitar o tamanho da margem da janela e não ocultar a barra de rolagem |
| Informações adicionais | * Referente ao chamado: [5901584](https://totvssuporte.zendesk.com/agent/tickets/5901584 "View ticket on the Zendesk portal") * Referente à ocorrência: MTEC-2659 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.10 |
