---
content_hash: 12460cd831b8cd1500fd7f8814f4f2fbee9435ef80cc7a52dcb3ecd13689a916
fetched_at: '2026-07-02T19:24:20.582529+00:00'
page_id: '259555653'
product: protheus
source: tdn-tec
title: TMobile:findCalendarEvent
type: documentation
url: https://tdn.totvs.com/display/tec/TMobile%3AfindCalendarEvent
version: 2
---

TMobile:findCalendarEvent

Procura eventos no calendário do dispositivo por um período.

## Sintaxe

false, < dEndDate > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| dIniDate | data | Data de início da pesquisa. | X |  |
| dEndDate | data | Data final da pesquisa. | X |  |

trueImportante

Para melhor uso deste método é importante estudar a classe [TCalendarEvent](http://tdn.totvs.com/display/tec/TCalendarEvent), compreendendo sua utilização.

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aCalIds | vetor | Array contendo os Ids dos eventos do calendário encontrados |

## Observações

* Eventos recorrentes não são retornados pela função find.

## Exemplos

cppEclipsetruefalse
