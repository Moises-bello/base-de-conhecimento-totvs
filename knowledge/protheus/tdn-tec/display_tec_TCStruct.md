---
content_hash: 7c9b3be74f330f01fe4972cd36be27dec5d0aaaab9a016a3a0c5c144acb71cc9
fetched_at: '2026-07-02T19:24:22.448969+00:00'
page_id: '269554517'
product: protheus
source: tdn-tec
title: TCStruct
type: documentation
url: https://tdn.totvs.com/display/tec/TCStruct
version: 4
---

TCStruct

Retorna um array contendo a estrutura da tabela ou view no SGBD.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cName | caractere | Indica o nome da tabela ou view no SGBD. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| aRet | vetor | Retorna um array contendo a estrutura de **cName** no SGBD. |

## Observações

Cada elemento do retorno da função contém as seguintes informações sobre as colunas da tabela ou view indicada em **cName** como criado no SGDB:

| Posição | Tipo | Descrição |
| --- | --- | --- |
| 1 | C | Nome da coluna |
| 2 | C | Tipo da coluna |
| 3 | L | Indica se é a coluna aceita valor nulo |
| 4 | N | Tamanho da coluna |
| 5 | N | Número de casas decimais da coluna |
| 6 | C | Tipo AdvPL da coluna |

* Caso **cName** não exista, será retornado um array vazio.
* A função retorna dados para os SGBDs: SQL Server, DB2, Informix, Oracle, MySQL, PostgreSQL.
* O índice 6 está disponível em builds do DBAccess superiores a 20171117. Caso a DBAPI não seja atualizada, o DBAccess não enviára o tipo AdvPL das colunas.

## Exemplos

cppEclipsetruefalse

## Abrangência

Essa função está disponível em build do **Application Server** superior a **7.00.131227A** e build do **DBAccess** superior a **20161016**.

## Veja também
