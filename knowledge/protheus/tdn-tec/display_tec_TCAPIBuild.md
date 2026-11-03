---
content_hash: 518da4d59fbc6536b9d2bf3bd0993663b4b126ab5003a18d7e729021b5b02b20
fetched_at: '2026-07-02T19:24:22.363695+00:00'
page_id: '269428458'
product: protheus
source: tdn-tec
title: TCAPIBuild
type: documentation
url: https://tdn.totvs.com/display/tec/TCAPIBuild
version: 2
---

TCAPIBuild

Retorna a build do biblioteca client do DBAccess, a DBAPI.

## Sintaxe

false

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| cRet | caractere | Retorna uma string contendo a build e a data de geração da DBAPI. |

## Observações

* O formato de retorno é **YYYYMMDD-YYYYMMDD**, onde **YYYY** é o ano com 4 dígitos, **MM** o mês com 2 dígitos e **DD** o dia com 2 dígitos. A primeira data refere-se à **build** da DBAPI e a segunda à **data de geração** da build.
* Em caso de erro, a função retornará a string "**00000000**".
* A data de geração da DBAPI é retornada a partir de build **42.20160402** do DBAccess com data de geração superior a 25/11/2016.

## Exemplos

cppEclipsetruefalse

## Veja também
