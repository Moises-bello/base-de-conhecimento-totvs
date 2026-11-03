---
content_hash: 0500a8fc339bb814c6292eb24e26d3eeed64191c5c845181bb294877f064e419
fetched_at: '2026-07-02T19:24:19.535384+00:00'
page_id: '223172281'
product: protheus
source: tdn-tec
title: TMSGraphic:CreateSerie
type: documentation
url: https://tdn.totvs.com/display/tec/TMSGraphic%3ACreateSerie
version: 3
---

CreateSerie

Cria uma série para o gráfico.

## Sintaxe

, [cLegenda], [nDecimals], [lShowValues] )]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório |
| --- | --- | --- | --- |
| nSerieType | Numérico | Indica o tipo do gráfico, sendo:  1 = GRP\_LINE 2 = GRP\_AREA 3 = GRP\_POINT 4 = GRP\_BAR 10 = GRP\_PIE | x |
| cLegenda | Caracter | Indica a legenda da série. |  |
| nDdecimais | Numérico | Indica o número de casas decimais dos valores. |  |
| lShowValues | Lógico | Indica, se os valores será apresentados:  (.T.) - Os valores são apresentados (.F.) - Os valores não são apresentados. |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| nRet | Numérico | Retorna a quantidade de séries criadas. |

## Exemplos

GRP\_LINEGRP\_AREAGRP\_POINTGRP\_BARGRP\_PIE
