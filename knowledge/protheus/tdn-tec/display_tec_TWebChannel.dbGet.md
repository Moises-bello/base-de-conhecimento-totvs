---
content_hash: a05da7958422cbadf96d84c1695cd259d10d066b034ece86902b67d75d50cbfe
fetched_at: '2026-07-02T19:24:23.157931+00:00'
page_id: '270914995'
product: protheus
source: tdn-tec
title: TWebChannel.dbGet
type: documentation
url: https://tdn.totvs.com/display/tec/TWebChannel.dbGet
version: 1
---

TWebChannel.dbGet

Recupera registros do banco SQLite definido no AppServer.ini a partir de uma Query. Os registros serão retornados no formato JSON para uma função callback Javascript.

## Sintaxe

false, < callback > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cQuery | caractere | Query no formato SQL para retorno dos registros. | X |  |
| callback | caractere | Função JavaScript (callBack) para retorno dos dados no formato JSON. | X |  |

## Observações

* Função disponível em builds superiores a 7.00.131227A.

## Exemplos

cppEclipsetruefalse
