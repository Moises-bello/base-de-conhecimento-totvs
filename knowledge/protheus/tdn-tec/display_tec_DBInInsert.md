---
content_hash: 9b1f1736c1bfdd48ea73768ef1ff5ec064e77fe4c4f18f62eeb56d3c994ff886
fetched_at: '2026-07-02T19:24:23.176010+00:00'
page_id: '271156990'
product: protheus
source: tdn-tec
title: DBInInsert
type: documentation
url: https://tdn.totvs.com/display/tec/DBInInsert
version: 1
---

DBInInsert

Retorna se a tabela está em modo de inserção de registros ou não.

## Sintaxe

false

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Retorna **.T.** se estiver inserindo registros; caso contrário, **.F.**. |

## Observações

* Caso não haja tabela aberta, a função retornará **.F.**.

## Exemplos

O exemplo abaixo utiliza a RDD "**TOPCONN**", mas a função pode ser utilizada com qualquer uma das RDDs válidas.

cppEclipsetruefalseCPOC := "ABC"
(cTable1)->CPON := 99
DBCommit()
conout( DBInInsert() ) // Exibe: .F.
// Fecha a área de trabalho
DBCloseArea()
// Abre a tabela 1 em modo exclusivo criando uma área de trabalho
DBUseArea( .T., cRDD, cTable1, (cTable1), .F., .F. )
conout( DBInInsert() ) // Exibe: .F.
(cTable1)->CPOC := "DEF"
(cTable1)->CPON := 88
conout( DBInInsert() ) // Exibe: .F.
// Fecha a área de trabalho
DBCloseArea()
// Apaga a tabela
TCDelFile( cTable1 )
// Desconecta
TCUnlink( nHandle1 )
return
]]>

## Veja também
