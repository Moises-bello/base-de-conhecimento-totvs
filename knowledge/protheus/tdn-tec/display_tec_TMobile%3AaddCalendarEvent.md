---
content_hash: ce8013a734c17c4258e07b8276dc87540290cee1f57187100e5836ca1e20675a
fetched_at: '2026-07-02T19:24:20.576809+00:00'
page_id: '259555644'
product: protheus
source: tdn-tec
title: TMobile:addCalendarEvent
type: documentation
url: https://tdn.totvs.com/display/tec/TMobile%3AaddCalendarEvent
version: 3
---

TMobile:addCalendarEvent

Utiliza o API do sistema (Android/IOS) para adicionar um evento ao calendário do dispositivo.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| oCalEv | objeto | Instância da classe TCalendarEvent com os dados que devem ser inseridos no calendário. | X |  |

trueImportante

Para melhor uso deste método é importante estudar a classe [TCalendarEvent](http://tdn.totvs.com/display/tec/TCalendarEvent), compreendendo sua utilização.

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| cID | caractere | Retorna o ID do evento criado. Se o usuário cancelou a criação do evento, retorna um ID "0". |

## Exemplos

cppEclipsetruefalse
