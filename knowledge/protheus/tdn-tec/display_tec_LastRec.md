---
content_hash: 6dfcd2da02de16fbac5a11ab853e8f89ae77cd0900127467615bea0a6586a297
fetched_at: '2026-07-02T19:24:22.517082+00:00'
page_id: '270898184'
product: protheus
source: tdn-tec
title: LastRec
type: documentation
url: https://tdn.totvs.com/display/tec/LastRec
version: 1
---

LastRec

Retorna o número do último registro inserido na tabela atual.

## Sintaxe

false

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Retorna o número do último registro inserido na tabela atual. |

## Observações

* Caso não haja área de trabalho aberta, o programa será encerrado com ocorrência de erro recuperável "*Work area not in use*".
* Se houver alguma ação pendente (inserção, atualização ou remoção de registros), as ações serão efetuadas. Caso haja erro nessa atualização, o programa será encerrado com ocorrência de erro recuperável "*Commit error: (RecCount/LastRec)*".
* Em caso de erro ou de criação da tabela, o retorno da função é 0 (zero).
* **LastRec** substitui as funções **RecCount** e **RecC**, as quais se tornaram obsoletas.
* **LastRec** retorna o valor do último registro inserido para uma tabela mesmo que haja troca da conexão ativa (no caso de mais de uma conexão com o mesmo SGBD na mesma thread).

## Exemplos

O exemplo abaixo utiliza a RDD "**TOPCONN**", mas a função pode ser utilizada com qualquer uma das RDDs válidas.

cppEclipsetruefalseMYFIELD := nI
DBCommit()
next nI
conout( LastRec() ) // Exibe: 3
// Vai para o primeiro registro
DBGoTop()
// Marca todos os registros para exclusão
while !eof()
DBDelete()
DBSkip()
enddo
// Apaga todos os registros marcados para exclusão
\_\_DBPack()
conout( LastRec() ) // Exibe: 3
// Fecha a área de trabalho
DBCloseArea()
// Abre uma outra conexão com o SGBD
nHandle2 := TCLink( "MSSQL/DSN1", "127.0.0.1", 7890 )
// Abre a tabela em modo exclusivo
DBUseArea( .T., cRDD, cTable, (cTable), .F., .F. )
conout( LastRec() ) // Exibe: 3
// Fecha a área de trabalho
DBCloseArea()
// Desconecta do SGBD
TCUnlink( nHandle2 )
TCUnlink( nHandle1 )
return
]]>
