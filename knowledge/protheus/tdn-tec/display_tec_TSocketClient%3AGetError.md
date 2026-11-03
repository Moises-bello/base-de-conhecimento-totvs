---
content_hash: ce25aa25fcafcebba14a0209de4d145501f02d06f6a927afc7b049e43038faf2
fetched_at: '2026-07-02T19:24:18.639036+00:00'
page_id: '219121397'
product: protheus
source: tdn-tec
title: TSocketClient:GetError
type: documentation
url: https://tdn.totvs.com/display/tec/TSocketClient%3AGetError
version: 1
---

TSocketClient:GetError

Permite recuperar um código e uma string correspondendo à ultima ocorrência do Socket client registrada em caso de falha.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cDesc | caractere | Retorna um código e uma string que corresponde à última ocorrência de SocketClient registrada em caso de falha. Caso não haja nenhuma falha registrada, a função retorna 0 (zero). | X | X |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Retorna o código do último erro ocorrido. |
