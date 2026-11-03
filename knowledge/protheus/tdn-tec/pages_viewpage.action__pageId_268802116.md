---
content_hash: 50975d9b9a9efa8cad3abfed9a56f2075db1e9571d4d7f9dfc912ef6ba143903
fetched_at: '2026-07-02T19:24:21.610468+00:00'
page_id: '268802116'
product: protheus
source: tdn-tec
title: TCDelFile (New)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268802116
version: 2
---

TCDelFile

Exclui uma tabela ou view de um banco relacional, através do DBAccess.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cName | caractere | Nome da Tabela/View a ser excluida. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Retorna **.T.** se excluiu com sucesso, caso contrário, retorna **.F.** |

## Observações

* Se for informado o nome de uma tabela/view ou a view não existir, o retorno é **.F.**. Geralmente, o retorno falso **.F.**, ocorre quando a tabela/view está sendo utilizada por outro processo ou a tabela/view não existe no banco de dados.

## Exemplos

cppEclipsetruefalse

## Veja também
