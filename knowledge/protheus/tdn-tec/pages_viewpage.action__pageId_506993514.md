---
content_hash: 8fc689ffab58a01b7b775f385d856b326e2d1a12d9b26ff8d972b2c7c9760e63
fetched_at: '2026-07-02T19:24:25.805171+00:00'
page_id: '506993514'
product: protheus
source: tdn-tec
title: Correção - TSay por cima de outros widgets
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506993514
version: 1
---

|  |  |
| --- | --- |
| Situação | Em situações que o tamanho do TSay for maior que o necessário e esse espaço "em branco" ficasse por cima de outro widget, era impossível clicar nesse outro widget. |
| Ocorrência | Problema já estava resolvido porém apenas para o componente TGet, falhando no caso de outros componentes, por exemplo: TComboBox |
| Correção | Agora qualquer componente com a mesma hierarquia que o TSay ficará por cima dele. |
| Informações adicionais | * Referente ao chamado: [6344259](https://totvssuporte.zendesk.com/agent/tickets/6344259 "View ticket on the Zendesk portal") * Referente à ocorrência: NTEC-2925 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.10 |
