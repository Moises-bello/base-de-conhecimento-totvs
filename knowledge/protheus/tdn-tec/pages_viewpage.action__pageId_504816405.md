---
content_hash: 308a31dc88e0215a0441c1551b948fd0ef89a01ff8a8387f8f656d7924d97bfb
fetched_at: '2026-07-02T19:24:25.702705+00:00'
page_id: '504816405'
product: protheus
source: tdn-tec
title: Correção - Problema com foco em janela aberta pelo bValid
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=504816405
version: 1
---

|  |  |
| --- | --- |
| Situação | Quando uma janela é aberta pelo bValid de um tGet, além da janela ficar em segundo plano (sendo necessário alternar com alt+tab para retornar para o primeiro plano), a função ReadVar() não informa corretamente qual o campo está em "foco". |
| Ocorrência | Problema começou a ocorrer devido a troca de mensagem de MS\_UPDATEGETSERVERVALUE para MS\_UPDATESERVERVALUE que passou a ser do tipo SendAndWait e fez com que a ordem de algumas mensagens ficasse diferente. |
| Correção | Mensagem voltou a não ser do tipo SendAndWait para não inverter a ordem de troca de mensagens, fazendo com que o foco fique corretamente na janela aberta pelo bValid. |
| Informações adicionais | * Referente ao chamado: [5752577](https://totvssuporte.zendesk.com/agent/tickets/5752577 "View ticket on the Zendesk portal") [5955176](https://totvssuporte.zendesk.com/agent/tickets/5955176 "View ticket on the Zendesk portal") [6035569](https://totvssuporte.zendesk.com/agent/tickets/6035569 "View ticket on the Zendesk portal") [6225547](https://totvssuporte.zendesk.com/agent/tickets/6225547 "View ticket on the Zendesk portal") [6230485](https://totvssuporte.zendesk.com/agent/tickets/6230485 "View ticket on the Zendesk portal") * Referente à ocorrência: MTEC-2645 MTEC-2673 MTEC-2791 MTEC-2854 MTEC-2881 * Disponível em builds superiores a 7.00.170117A - 17.3.0.9 |
