---
content_hash: 8e722ec9dff173ea39da6bc8d12a3553077549d3f7e0ae9e606ee85ef0bf09a0
fetched_at: '2026-07-02T19:24:20.466313+00:00'
page_id: '249956477'
product: protheus
source: tdn-tec
title: TCIsView
type: documentation
url: https://tdn.totvs.com/display/tec/TCIsView
version: 8
---

TCIsView

Função para verificar por nome se um objeto é uma view.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cName | caractere | Nome da tabela/view a ser verificada. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Retorna **.T.** se o nome informado pertece a uma view, caso contrário, retorna **.F.** |

## Observações

* Se for informado o nome de uma tabela ou a view não existir, o retorno é **.F.**

## Exemplos

cppEclipsetruefalse

## Abrangência

Esta função está disponível no Application Server - build 7.00.131227A, com data de geração superior a 09/08/2016 e depende de um DBAccess com build superior a 20160402.

## Veja também
