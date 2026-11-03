---
content_hash: d32684ce35107da230c07879ada6c52237d7245bc2dcba63fbf2c3613dc3fb49
fetched_at: '2026-07-02T19:24:21.401482+00:00'
page_id: '267780966'
product: protheus
source: tdn-tec
title: TCGetSID
type: documentation
url: https://tdn.totvs.com/display/tec/TCGetSID
version: 4
---

TCGetSID

Retorna o número do processo em uso no TOTVS | DBAccess para a conexão atual.

## Sintaxe

false

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nRet | numérico | Retorna o número da thread da conexão atual com o DBAccess. |

## Observações

* Caso não exista conexão com o DBAccess, será retornado o valor **-1**.

## Exemplos

cppEclipsetruefalse

## Abrangência

Este recurso requer um TOTVS | Application Server com build igual ou superior a **7.00.100812P**, bem como um TOTVS | DBAccess com build igual ou superior a **20100927**.

## Veja também
