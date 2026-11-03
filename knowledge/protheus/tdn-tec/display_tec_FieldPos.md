---
content_hash: e5f9425f7c1557d0e71d7a524047cf0ad7ee79aebe6d715fb61387b356e8fca8
fetched_at: '2026-07-02T19:24:23.190679+00:00'
page_id: '271162195'
product: protheus
source: tdn-tec
title: FieldPos
type: documentation
url: https://tdn.totvs.com/display/tec/FieldPos
version: 1
---

FieldPos

Retorna a posição de um determinado campo dentro da área de trabalho corrente.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cField | caractere | Nome do campo. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Retorno a posição do campo, caso não exista retorna 0. |

## Exemplos

cppEclipsetruefalse(FieldPos("FIELD\_NAME") > 0
conout("Campo existe!")
endif
DBCloseArea()
TCUnlink()
RETURN
]]>

## Veja também
