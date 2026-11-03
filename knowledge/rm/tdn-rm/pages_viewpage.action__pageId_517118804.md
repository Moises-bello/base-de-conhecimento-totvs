---
content_hash: d1d69df49df5d7302f118b28d5cc875d70214ba42b7a020822c4e9dbe8384892
fetched_at: '2026-06-29T00:10:27.910819+00:00'
page_id: '517118804'
product: rm
source: tdn-rm
title: S-2230-Gatilhos após 2.5.00 NT -15/2019
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=517118804
version: 14
---

A **Nota Técnica nº 15/2019** divulgada pelo Governo no dia 02/08/2019 tem como objetivo implantar as primeiras medidas de **simplificação e modernização do eSocial**, conforme disposto no art. 9º da Portaria nº 300, de 13/06/2019.

## Data de entrada nos ambientes do eSocial

* Produção restrita (testes): **08/10/2019**
* Produção: **11/11/2019**

## Releases que contemplam a Nota Técnica nº 15/2019

* 12.1.23.274
* 12.1.24.224
* 12.1.25.154
* 12.1.26.104
* E superiores

| ATENÇÃO: |
| --- |
| No parametrizador teremos a opção de dois leiautes.    De acordo com o leiaute selecionado teremos alterações na forma da geração do gatilhos. |

 Alteração ao gerar gatilho:

 

| Casos | Resultado do gatilho no leiaute 2.5 | Resultado do gatilho no leiaute 2.5.00 Nota técnica |
| --- | --- | --- |
| Afastamentos maiores de 15 dias em que seu cadastro foi feito preenchendo a data de início e fim. | Gera 2 gatilhos: um com o tipo de operação "Início", e outro com tipo de operação "Término". | Gera 1 gatilho com o tipo de operação "Inclusão". |

Observação:

Para os afastamentos gerados anteriormente a nota técnica, qualquer alteração ou retificação referente a estes gatilhos seguirão a regra do "leiaute 2.5"  
A regra do "leiaute 2.5 nota técnica" é valida apenas para os novos afastamentos.
