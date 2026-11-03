---
content_hash: 8e37a7c67e576e8656bed463fcb8205173e6186ced02cb08983682f9f8fae1bc
fetched_at: '2026-07-02T19:24:23.219237+00:00'
page_id: '271187899'
product: protheus
source: tdn-tec
title: FieldWBlock
type: documentation
url: https://tdn.totvs.com/display/tec/FieldWBlock
version: 1
---

FieldWBlock

Retorna um bloco de código para um campo de uma área de trabalho aberta.

## Sintaxe

false, < nWokArea > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cField | caractere | Indica o nome do campo que será retornado o bloco de código. | X |  |
| nWokArea | numérico | Indica o número da área de trabalho que será retornado o bloco de código. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| bRet | bloco de código | Retorna o bloco de código para o campo da área de trabalho informada. |

## Observações

Essa função é utilizada para retornar um bloco de código executável com o campo de uma área de trabalho especificada.

Quando o bloco de código resultante é executado sem parâmetro, recupera o valor armazenado no campo. Mas, quando executado com um valor, define esse valor no determinado campo.

Portanto, o bloco de código retornado é similar a:

falsefalseCampo, cAlias->Campo := Valor ) }" )
]]>

Sendo:

Area = Parâmetro **nWokArea** da função FieldWBlock  
 cAlias = Alias correspondente ao número informado em **Area**  
 Campo = Parâmetro **cField** da função FieldWBlock  
 Valor = Valor executado no bloco de código

Se o número da área de trabalho informada for inválido ou a área de trabalho não estiver aberta, o programa será encerrado com ocorrência de erro recuperável "*Work area does not exist*" e retornará **Nil**.

Caso haja erro na criação do bloco de código, o programa será encerrado com ocorrência de erro recuperável "*CodeBlock definition error*" e retornará **Nil**.

Caso o nome informado não exista no alias aberto, o bloco de código será criado, mas ocorrerá erro na execução do mesmo.

## Exemplos

O exemplo abaixo utiliza a RDD "**TOPCONN**", mas a função pode ser utilizada com qualquer uma das RDDs válidas.

cppEclipsetruefalse( DBAppend( .F. ) )
// Faz o Eval do bloco de código informando o valor
// Isso irá fazer a atribuição do valor ao campo
for nK := 1 to nLen
Eval( aBlocks[nI][nK], aValues[nI][nJ][nK] )
next nK
(aNames[nI])->( DBCommit() )
next nJ
// Vai para o primeiro registro
(aNames[nI])->( DBGoTop() )
while !(aNames[nI])->( eof() )
// Exibe o conteúdo de cada campo do registro
for nJ := 1 to nLen
conout( Eval( aBlocks[nI][nJ] ) )
next nI
(aNames[nI])->( DBSkip() )
enddo
// Fecha a área de trabalho
(aNames[nI])->( DBCloseArea() )
// Apaga a tabela no SGBD
TCDelFile( aNames[nI] )
next nI
// Desconecta
TCUnlink( nHandle1 )
return
]]>

## Veja também
