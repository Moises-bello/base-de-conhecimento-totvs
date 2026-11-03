---
content_hash: 772b8ccc8ed63c304a61f719b09db78e73a187806d41ca6f52f24893d83eeb8a
fetched_at: '2026-07-02T19:24:19.843643+00:00'
page_id: '244916565'
product: protheus
source: tdn-tec
title: TCCanOpen
type: documentation
url: https://tdn.totvs.com/display/tec/TCCanOpen
version: 5
---

TCCanOpen

Verifica se uma tabela e/ou índice existe.

## Sintaxe

false, [ cIndex ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cTable | caractere | Nome da tabela. | X |  |
| cIndex | caractere | Nome do índice. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Retorna **.T.** se a tabela e/ou índice existir, caso contrário, retorna **.F.** |

trueObservações

* Para verificar a existência de um índice, é necessário informar a tabela a que este índice pertence.

## Exemplos

cppEclipsetruefalse

## Veja também
