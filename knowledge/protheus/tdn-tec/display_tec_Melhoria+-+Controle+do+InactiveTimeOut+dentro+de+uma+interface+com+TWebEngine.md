---
content_hash: afd135f4c19ec5f36cd3029b7abf87d0582a066c6161a8616da089eb041eb713
fetched_at: '2026-07-02T19:24:27.769690+00:00'
page_id: '680249982'
product: protheus
source: tdn-tec
title: Melhoria - Controle do InactiveTimeOut dentro de uma interface com TWebEngine
type: documentation
url: https://tdn.totvs.com/display/tec/Melhoria+-+Controle+do+InactiveTimeOut+dentro+de+uma+interface+com+TWebEngine
version: 1
---

|  |  |
| --- | --- |
| Situação | Dentro de uma interface TWebEngine, caso existisse inactivetimeout ligado na seção, a mesma acabava caindo devido a inatividade. |
| Ocorrência | Queda por inatividade ocorre porque dentro do TWebEngine o Smartclient não troca mensagens com o appserver, causando a queda por inatividade |
| Melhoria | Alteração feita para capturar eventos de clique e keypress dentro do TWebEngine e enviar mensagem para o appserver reiniciar os timers de inatividade e impedir a queda. Mesmo assim, após um tempo sem receber clique/keypress e o Smartclient estiver com o TWebengine em foco, uma mensagem será exibida (antes do tempo limite), avisando que o tempo de inatividade está quase no limite e se o usuário não clicar em OK o Appserver irá derrubar a conexão por inatividade. |
| Informações adicionais | * Referente ao chamado: [#12799225](https://totvssuporte.zendesk.com/agent/tickets/12799225 "View ticket on the Zendesk portal") [#12509111](https://totvssuporte.zendesk.com/agent/tickets/12509111 "View ticket on the Zendesk portal") * Referente à ocorrência: DTCLIENT01-3062 e DTCLIENT01-2993 * Disponível em builds iguais ou superiores a 7.00.210324P - 20.3.1.0 |
