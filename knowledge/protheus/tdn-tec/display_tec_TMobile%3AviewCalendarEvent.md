---
content_hash: 9bebe842d41c64721787ca393d147d7ba5cf8cb7711dd8e6fd7f306c0a99453c
fetched_at: '2026-07-02T19:24:20.590393+00:00'
page_id: '259555658'
product: protheus
source: tdn-tec
title: TMobile:viewCalendarEvent
type: documentation
url: https://tdn.totvs.com/display/tec/TMobile%3AviewCalendarEvent
version: 3
---

TMobile:viewCalendarEvent

Utiliza o API do sistema (Android/IOS) para mostrar o evento à partir da aplicação padrão do Dispositivo Móvel.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cID | caractere | Identificador do calendário. | X |  |

trueImportante

Para melhor uso deste método é importante estudar a classe [TCalendarEvent](http://tdn.totvs.com/display/tec/TCalendarEvent), compreendendo sua utilização.

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lSuccess | lógico | Retorna .T. se achou o evento e .F. se o evento não existe (ou não foi possível acessar). |

## Exemplos

cppEclipsetruefalse
