---
content_hash: 624835b8048914f5729ac83629fba168d24f2d33841c34530d36c454b9a3fff7
fetched_at: '2026-07-02T19:24:23.143350+00:00'
page_id: '270914990'
product: protheus
source: tdn-tec
title: TWebChannel.dbExec
type: documentation
url: https://tdn.totvs.com/display/tec/TWebChannel.dbExec
version: 1
---

TWebChannel.dbExec

Executa uma query no banco SQLite definido no AppServer.ini.

## Sintaxe

false, < callback > )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cQuery | caractere | Query no formato SQL para retorno dos registros. | X |  |
| callback | caractere | Função JavaScript (callBack) disparada como retorno da execução da Query, seja ela bem bem sucedida ou não. | X |  |

## Observações

* Função disponível em builds superiores a 7.00.131227A.

## Exemplos

cppEclipsetruefalse
