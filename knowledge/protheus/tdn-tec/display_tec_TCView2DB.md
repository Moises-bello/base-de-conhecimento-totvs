---
content_hash: fa50c6893aa715a8e2f7c61b66e2eb5f20865364fbeed6e0f349c61af8bf45e6
fetched_at: '2026-07-02T19:24:20.489169+00:00'
page_id: '252510242'
product: protheus
source: tdn-tec
title: TCView2DB
type: documentation
url: https://tdn.totvs.com/display/tec/TCView2DB
version: 3
---

TCView2DB

Função para materializar uma view e seus dados em uma tabela física.

## Sintaxe

false, < cTable > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cView | caractere | Nome da view a ser materializada. | X |  |
| cTable | caractere | Nome da tabela a ser criada no SGBD. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Retorna **.T.** se tabela cTable foi criada, caso contrário, retorna **.F.** e o motivo do erro pode ser verificado com a função . |

## Observações

* As operações são realizadas em uma única etapa, que envolve a criação da nova tabela com a estrutura da view e o insert de todas as linhas da view na nova tabela física.

## Exemplos

cppEclipsetruefalse

## Abrangência

Esta função está disponível no Application Server - build 7.00.131227A, com data de geração superior a 09/08/2016 e depende de um DBAccess com build superior a 20160402.

## Veja também
