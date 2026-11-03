---
content_hash: c9301d752b2956bc4aeabe9eaf28552404c59c574fc4da07cb135ed40ee81556
fetched_at: '2026-07-02T19:24:20.484120+00:00'
page_id: '252510230'
product: protheus
source: tdn-tec
title: TCViewStruct
type: documentation
url: https://tdn.totvs.com/display/tec/TCViewStruct
version: 3
---

TCViewStruct

Função que recebe o nome da view como parâmetro e retorna o nome da tabela master e a estrutura da view, no formato (table,field,table,field,...)

## Sintaxe

false, < @cTable >, < @cStruct > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cView | caractere | Nome da view. | X |  |
| cTable | caractere | Variável que será preenchida com nome da tabela master. | X | X |
| cStruct | caractere | Variável que será preenchida com a estrutura da view informada em cView. | X | X |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Retorna **.T.** em caso de sucesso, caso contrário, retorna **.F.** e o motivo do erro pode ser verificado com a função . |

## Exemplos

cppEclipsetruefalse " + cTable)
CONOUT("Estrutura da VIEW1 -> " + cStruct)
ENDIF
TCUnlink()
RETURN
]]>

## Abrangência

Esta função está disponível no Application Server - build 7.00.131227A, com data de geração superior a 09/08/2016 e depende de um DBAccess com build superior a 20160402.

## Veja também
