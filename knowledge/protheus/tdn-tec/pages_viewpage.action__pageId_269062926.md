---
content_hash: 6debfe8cd87c38ab63cf6a282b596927b71e1f77c636abe17f225a0a559926a4
fetched_at: '2026-07-02T19:24:22.205778+00:00'
page_id: '269062926'
product: protheus
source: tdn-tec
title: DBCreateIndex (New)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269062926
version: 1
---

DBCreateIndex

Cria um indice para Tabela/View

## Sintaxe

false, < cExprKey >, [ bExprKey ], [ lUnique ] )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cName | caractere | Indica o nome do arquivo de índice que será criado | X |  |
| cExprKey | caractere | Expressão das chaves do índice que será criado na forma de string. | X |  |
| bExprKey | bloco de código | Expressão das chaves do índice que será criado na forma executável. |  |  |
| lUnique | lógico | Valor lógico para especificar que o indice será unico. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| uRet | nil | Retorno sempre é nulo. |

## Observações

Caso exista um arquivo com o mesmo nome, definido no parâmetro <cNome>, ele será excluído e o novo criado. No entanto, são realizados os seguintes passos:

1. Salva fisicamente as alterações realizadas na tabela corrente.
2. Fecha todos os arquivos de índice abertos.
3. Cria o novo índice.
4. Posiciona o novo índice como ordem corrente.
5. Posiciona a tabela corrente no primeiro registro do índice.

Com exceção do RDD C-Tree, a tabela corrente não precisa estar aberta em modo exclusivo para a criação do índice, pois na criação de índices, no c-tree, é alterada a estrutura da tabela, mas é necessário que a tabela esteja aberta em modo exclusivo.

## Exemplos

cppEclipsetruefalse(DBCreateIndex('T2\_IND', 'FIELD\_NAME', { || 'FIELD\_NAME' }))
IIF(TCCanOpen('T2', 'T2\_IND'), CONOUT('TRUE'), CONOUT('FALSE')) // retorna .T., ou seja, tabela e índice existem
DBCloseArea()
// Criação de Indice na View
DBUseArea(.F., 'TOPCONN', cView1, (cView1), .F., .F.)
TCSetVIdx( .T. )
(cView1)->(DBCreateIndex('VIEW1\_IND', 'FIELD\_NAME'))
TCSetVIdx( .F. )
IIF(TCCanOpen('VIEW1', 'VIEW1\_IND'), CONOUT('TRUE'), CONOUT('FALSE')) // retorna .T., ou seja, view e índice existem
DBCloseArea()
TCUnlink()
RETURN
]]>

## Abrangência

Esta função está disponível no Application Server - build 7.00.131227A, com data de geração superior a 09/08/2016 e depende de um DBAccess com build superior a 20160402.

## Veja também
