---
content_hash: 42423bbe91c29023e7d5b0366f96bcfa9991bcef9eb34f0910884fe0e50a47b4
fetched_at: '2026-07-02T19:24:21.457524+00:00'
page_id: '267798807'
product: protheus
source: tdn-tec
title: TCViewRen
type: documentation
url: https://tdn.totvs.com/display/tec/TCViewRen
version: 2
---

TCViewRen

Permite renomear uma View do SGBD, criada através das funções TCViewOne() e/ou TCViewMulti().

## Sintaxe

false, < cViewNewName > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cViewName | caractere | Indica o nome da View existente a ser renomeada. | X |  |
| cViewNewName | caractere | Indica o novo nome da View a ser renomeada. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| lRet | lógico | Retorna .T. em caso de sucesso na operação de renomear a View. Caso contrário retorna .F., e maiores informações sobre a falha na operação podem ser obtidas através da função TCSqlError() |

## Observações

* Essa função verifica as condições mínimas para a execução da operação, e internamente recupera as definições da View informada, remove a View do SGDB, e recria a View com o novo nome informado.
* Esta funcionalidade está disponível a partir do TOTVS | Application Server build 7.00.131227A, com data de geração igual ou superior a 14/10/2016.
* Esta funcionalidade também requer a atualização da DBAPI.DLL / SO do DBAccess atualizada, bem como o DBAccess Build 20160913 ou superior, com data de geração superior a 14/10/2016.

## Exemplos

cppEclipsetruefalse

## Abrangência

Esta função está disponível no Application Server - build 7.00.131227A, com data de geração superior a 14/10/2016 e depende de um DBAccess com build superior a 20160402.

## Veja também
