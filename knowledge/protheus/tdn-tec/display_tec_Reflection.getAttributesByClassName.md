---
content_hash: 02fca8d8cf62228a26afb88b6ea709a95ce90dd958798708430851c889898199
fetched_at: '2026-07-02T19:24:28.755236+00:00'
page_id: '849562666'
product: protheus
source: tdn-tec
title: Reflection.getAttributesByClassName
type: documentation
url: https://tdn.totvs.com/display/tec/Reflection.getAttributesByClassName
version: 2
---

Reflection.getDataAnnotation

Retorna uma lista com a(s ) propriedade(s) e seu(s) respectivo(s) tipo(s) em cada posição da lista.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| ``` cClassName ``` | caractere | Nome da classe a serem obtidas as propriedades. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aRet | array | Retorna uma array multidimensional onde em cada posição sera retornada a propriedade e o tipo da mesma.   * aRet[1][1] =  propriedade * aRet[2][1] = tipo da propriedade   Caso não encontre o retorno é vazio. |

## Exemplos

cppEclipseclassProgram.tlpptruecppEclipseexemplo.tlpptrue 0)
Conout(aRet[1][1], aRet[1][2], aRet[2][1], aRet[2][2])
endIf
Return
]]>

## Resultado do Exemplo

data1  
numeric  
data2  
character

## Abrangência

24.3.0.0

## Veja também
