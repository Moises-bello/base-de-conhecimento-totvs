---
content_hash: b846043ec9ec25c309fc80a9c3177b12aa70b574ac8eaa4b1194da26c01bafee
fetched_at: '2026-07-02T19:24:28.482276+00:00'
page_id: '707385448'
product: protheus
source: tdn-tec
title: Melhoria - Controle do InactiveTimeOut dentro de uma interface com TWebEngine
  (Harpia)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=707385448
version: 1
---

|  |  |
| --- | --- |
| Situação | Dentro de uma interface TWebEngine, caso existisse inactivetimeout ligado na seção, a mesma acabava caindo devido a inatividade. |
| Ocorrência | Queda por inatividade ocorre porque dentro do TWebEngine o Smartclient não troca mensagens com o appserver, causando a queda por inatividade |
| Melhoria | Alteração feita para capturar eventos de clique e keypress dentro do TWebEngine e enviar mensagem para o appserver reiniciar os timers de inatividade e impedir a queda. |
| Informações adicionais | * Referente ao chamado: [#12799225](https://totvssuporte.zendesk.com/agent/tickets/12799225 "View ticket on the Zendesk portal") [#12509111](https://totvssuporte.zendesk.com/agent/tickets/12509111 "View ticket on the Zendesk portal") * Referente à ocorrência: DTCLIENT01-3062 e DTCLIENT01-2993 * Disponível em builds iguais ou superiores a 7.00.210324P - 20.3.0.5 |
