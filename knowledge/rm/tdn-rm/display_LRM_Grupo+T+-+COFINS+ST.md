---
content_hash: 887dbcf756b583785c495b89c56188c6c8cef7e1c9a9fde0afbd1464ffcd9a3c
fetched_at: '2026-06-29T00:12:10.674242+00:00'
page_id: '953003409'
product: rm
source: tdn-rm
title: Grupo T - COFINS ST
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+T+-+COFINS+ST
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo T - COFINS ST** | | | | | | | | | | |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocorrência | Tamanho | Observação | Mais Informações |
| 313 | T01 | COFINSST | Grupo COFINS Substituição Tributária | G | M01 |  | 0-1 |  |  | NÃO SERÁ GERADO |
| 313.1 | T01.1 | -x- | Sequência XML |  | T01 |  | 1-1 |  | Informar os campos T02 e T03 para cálculo da COFINS Substituição Tributária em percentual. | NÃO SERÁ GERADO |
| 314 | T02 | vBC | Valor da Base de Cálculo da COFINS | CG | T01.1 | N | 1-1 | 13v2 | NÃO SERÁ GERADO |
| 315 | T03 | pCOFINS | Alíquota da COFINS (em percentual) | E | T01.1 | N | 1-1 | 3v2-4 | NÃO SERÁ GERADO |
| 315.1 | T03.1 | -x- | Sequência XML | E | T01 |  | 1-1 |  | Informar os campos T04 e T05 para cálculo da COFINS Substituição Tributária em valor. | NÃO SERÁ GERADO |
| 316 | T04 | qBCProd | Quantidade Vendida | CG | T03.1 | N | 1-1 | 12v0-4 | NÃO SERÁ GERADO |
| 317 | T05 | vAliqProd | Alíquota da COFINS (em reais) | E | T03.1 | N | 1-1 | 11v0-4 | NÃO SERÁ GERADO |
| 318 | T06 | vCOFINS | Valor da COFINS | E | T01 | N | 1-1 | 13v2 |  | NÃO SERÁ GERADO |
