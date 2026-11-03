---
content_hash: 401dbb28c2b5001e1aaba0c3b3a480616cb718901f8bdd8320308d1ebcf48212
fetched_at: '2026-07-02T19:24:24.201259+00:00'
page_id: '465387085'
product: protheus
source: tdn-tec
title: GetLinesProg
type: documentation
url: https://tdn.totvs.com/display/tec/GetLinesProg
version: 2
---

GetLinesProg

Retorna o numero de linhas executáveis do fonte onde ela foi chamada, ou GetLinesProg("fonte.extensao") para retornar de um outro fonte.

## Sintaxe

false )
]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| cFile | caractere | Caso presente, procura o arquivo indicado no RPO atual e ve qual o numero de linhas dele. | X |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nLines | numérico | Numero de linhas do fonte |

trueObservações

* O fonte precisá estar previamente compilado no mesmo RPO que foi chamada a função

## Exemplos

cppEclipsetruefalsesuposto fonte dummy.prw.
return
]]>

## Abrangência

TOTVS Application Server 17.3.0.8
