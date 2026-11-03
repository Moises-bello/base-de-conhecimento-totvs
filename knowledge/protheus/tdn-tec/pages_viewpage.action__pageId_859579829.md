---
content_hash: 33b14fab93e363376b84ac00ff45bd1e3d18527913c10282e079dcb2510c08ee
fetched_at: '2026-07-02T19:24:28.825075+00:00'
page_id: '859579829'
product: protheus
source: tdn-tec
title: Correção - Problemas no controle do checkbox
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=859579829
version: 1
---

|  |  |
| --- | --- |
| Situação | Ao clicar para alterar a seleção do checkbox, por vezes não mudava o estado |
| Ocorrência | Em ambientes com um pouco mais de latência, causava problemas na seleção dos campos CheckBox, fazendo a mudança de estado não ser efetiva |
| Correção | Correção feita para controlar melhor o estado do checkbox mesmo em ambiente com alta latência |
| Informações adicionais | * Referente ao chamado: [#19546678](https://totvssuporte.zendesk.com/agent/tickets/19546678 "View ticket on the Zendesk portal") * Referente à ocorrência: DTCLIENT01-4648 * Disponível em builds iguais ou superiores a 20.3.2.8 |
