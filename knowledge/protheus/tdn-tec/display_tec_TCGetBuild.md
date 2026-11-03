---
content_hash: eecbcbb13838ab79f2205440da9726a2dd7d9060d9686fbf9a9ef6d776835d37
fetched_at: '2026-07-02T19:24:22.355567+00:00'
page_id: '269425901'
product: protheus
source: tdn-tec
title: TCGetBuild
type: documentation
url: https://tdn.totvs.com/display/tec/TCGetBuild
version: 2
---

TCGetBuild

Retorna a build do DBAccess em que está conectado.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| lDate | lógico | Indica se incluirá ou não a data de geração da build no valor que será retornado. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| cRet | caractere | Retorna uma string contendo a build do DBAccess em que está conectado. |

## Observações

* Em caso de erro, a função retornará a string "**V40f-**".
* O parâmetro **lDate** estará disponível em builds superiores a **7.00.131227A**.
* O valor padrão para **lDate** é **.F.**.
* **lDate** só incluirá a data de geração caso a build do DBAccess seja superior a **20150725**.

## Exemplos

cppEclipsetruefalse

## Veja também
