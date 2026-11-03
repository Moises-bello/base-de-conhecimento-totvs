---
content_hash: 19c13f324e8331f7576606dfd45c08c4669e09d60eca44a115a6bf21adf12254
fetched_at: '2026-07-02T19:24:18.646383+00:00'
page_id: '219121433'
product: protheus
source: tdn-tec
title: TSocketClient:Send
type: documentation
url: https://tdn.totvs.com/display/tec/TSocketClient%3ASend
version: 1
---

TSocketClient:Send

Transmite o buffer pela conexão TCP genérica ativa.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cData | caractere | Indica a buffer que contém os dados que serão transmitidos pela conexão. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Retorna o número de bytes transmitidos. Caso o número seja diferente do tamanho especificado, no parâmetro cBuffer, algum erro aconteceu. |
