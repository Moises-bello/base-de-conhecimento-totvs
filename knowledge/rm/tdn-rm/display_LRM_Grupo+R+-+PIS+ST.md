---
content_hash: d1df25b6710b07173fd8d91a6a55712d40434cd1487bdb32f5386656b1d510ad
fetched_at: '2026-06-29T00:12:10.649609+00:00'
page_id: '953003395'
product: rm
source: tdn-rm
title: Grupo R - PIS ST
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+R+-+PIS+ST
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo R - PIS ST** | | | | | | | | | | |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocorrência | Tamanho | Observação | Mais Informações |
| 287 | R01 | PISST | Grupo PIS Substituição Tributária | G | M01 |  | 0-1 |  |  | NÃO SERÁ GERADO |
| 287.1 | R01.1 | -x- | Sequência XML | CG | R01 |  | 1-1 |  | Informar os campos R02 e R03 para cálculo do PIS em percentual. | NÃO SERÁ GERADO |
| 288 | R02 | vBC | Valor da Base de Cálculo do PIS | E | R01.1 | N | 1-1 | 13v2 | NÃO SERÁ GERADO |
| 289 | R03 | pPIS | Alíquota do PIS (em percentual) | E | R01.1 | N | 1-1 | 3v2-4 | NÃO SERÁ GERADO |
| 289.1 | R03.1 | -x- | Sequência XML | CG | R01 |  | 1-1 |  | Informar os campos R04 e R05 para cálculo do PIS em valor. | NÃO SERÁ GERADO |
| 290 | R04 | qBCProd | Quantidade Vendida | E | R031. | N | 1-1 | 12v0-4 | NÃO SERÁ GERADO |
| 291 | R05 | vAliqProd | Alíquota do PIS (em reais) | E | R03.1 | N | 1-1 | 11v0-4 | NÃO SERÁ GERADO |
| 292 | R06 | vPIS | Valor do PIS | E | R01 | N | 1-1 | 13v2 |  | NÃO SERÁ GERADO |
