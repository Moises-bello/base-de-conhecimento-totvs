---
content_hash: 569fc34a3fb928716c872a4aac9aebd12a40bef9899c0f4010af3a197407cf95
fetched_at: '2026-07-02T19:24:23.206280+00:00'
page_id: '271178275'
product: protheus
source: tdn-tec
title: DBSelectArea
type: documentation
url: https://tdn.totvs.com/display/tec/DBSelectArea
version: 1
---

DBSelectArea

Define a área de trabalho especificada como ativa.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| xArea | qualquer | Indica a área de trabalho que ficará ativa. | X |  |

## Observações

* **xArea** pode ser do tipo **numérico**, indicando o número da área de trabalho, ou do tipo **caractere**, indicando o alias de uma área de trabalho.
* Após a seleção de uma área de trabalho, todas as operações subsequentes serão realizadas nesta área de trabalho, a menos que outra área seja informada ou que se utilize alias para se referenciar a outra área de trabalho.
* Se **xArea** contiver uma string com uma alias que não foi aberto, o programa será encerrado com ocorrência de erro recuperável "*Alias does not exist: AAA*", onde **AAA** indica o alias informado.
* Se **xArea** contiver um número menor ou igual a 0 (zero) ou for maior que o número de áreas de trabalho informado pela chave "**MaxWorkAreas**" da seção do ambiente no arquivo ini do AppServer, o programa será encerrado com ocorrência de erro recuperável "*Work area does not exist*".
* Se for informado em **xArea** um número de área de trabalho válido, mas não aberto, ou uma string com um alias inexistente, ou o valor nulo (**Nil**), a área de trabalho atual será desativada.
* Cada área de trabalho corresponde às informações de um único alias.

## Exemplos

O exemplo abaixo utiliza a RDD "**TOPCONN**", mas a função pode ser utilizada com qualquer uma das RDDs válidas.

cppEclipsetruefalse( DBAppend( .F. ) )
(cTable2)->CPOC := "CC"
(cTable2)->( DBCommit() )
// Fecha todas as áreas de trabalho
DBCloseAll()
// Apaga a tabela 1
TCDelFile( cTable1 )
// Apaga a tabela 2
TCDelFile( cTable2 )
// Desconecta
TCUnlink( nHandle1 )
return
]]>

## Veja também
