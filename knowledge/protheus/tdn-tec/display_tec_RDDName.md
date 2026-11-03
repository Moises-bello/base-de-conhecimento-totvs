---
content_hash: 7b797d9cf689577179c8acf26ad621cd04607a2f689947d9141fee90ee755e1b
fetched_at: '2026-07-02T19:24:22.562682+00:00'
page_id: '270914377'
product: protheus
source: tdn-tec
title: RDDName
type: documentation
url: https://tdn.totvs.com/display/tec/RDDName
version: 1
---

RDDName

Retorna o nome da RDD utilizada.

## Sintaxe

false

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| cRet | caractere | Retorna o nome da RDD utilizada. |

## Observações

A função pode retornar um dos seguintes valores:

| RDD |
| --- |
| DBFCDX |
| DBFCDXTTS |
| DBFCDXAX |
| BTV |
| BTVCDX |
| CTREECDX |
| TOPCONN |
| CODEBCDX |
| CODEBCDXTTS |
| DBFCDXADS |
| MEMORY |
| SQLITE |
| CTREETMP |

* O valor padrão é "**DBFCDX**".
* Caso a RDD não esteja com um valor inválido, será retornado "**UNDEFINED**".
* Caso a função seja chamada sem uma área de trabalho aberta, o programa será encerrado com ocorrência de erro recuperável "*Work area not in use*" e retornará uma string vazia ("").

## Exemplos

O exemplo abaixo utiliza a RDD "**TOPCONN**", mas a função pode ser utilizada com qualquer uma das RDDs válidas.

cppEclipsetruefalse
