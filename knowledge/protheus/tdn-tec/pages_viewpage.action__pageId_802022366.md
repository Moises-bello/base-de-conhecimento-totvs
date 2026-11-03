---
content_hash: 576867612b8b9835fb0ef763df8fea0cdbdf7403fca8f7618b236d298030264a
fetched_at: '2026-07-02T19:24:28.628009+00:00'
page_id: '802022366'
product: protheus
source: tdn-tec
title: Correção - Ctrl-Alt-N não abre SCPing (NetTest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=802022366
version: 1
---

|  |  |
| --- | --- |
| Situação | Ao pressionar a tecla de atalho Ctrl-Alt-N a tela de gráficos do SCPing não está aparecendo, ou está derrubando o Smartclient |
| Ocorrência | Dois problemas foram detectados, com o teclado configurado em Inglês o atalho não estava sendo reconhecido pelo Smartclient (impedindo a abertura da tela). Com teclado em PT-BR (ABNT ou ABNT2) ao pressionar o atalho, derrubava o Smartclient |
| Correção | Duas correções aplicadas, primeiro para reconhecer o atalho mesmo com o teclado em Ingês e outra para não derrubar o Smartclient na abertura da tela |
| Informações adicionais | * Referente ao chamado: [Ticket #18373946](https://totvssuporte.zendesk.com/agent/tickets/18373946 "View ticket on the Zendesk portal") * Referente à ocorrência: DTCLIENT01-4362 * Disponível em builds iguais ou superiores a 7.00.210324P - 20.3.2.1 |
