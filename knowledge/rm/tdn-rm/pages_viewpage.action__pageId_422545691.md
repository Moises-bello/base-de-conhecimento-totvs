---
content_hash: e149bb55f0417d788d707a1eabf68fa1e8514d6f634acaed21521ce5d9423934
fetched_at: '2026-06-29T00:09:20.476202+00:00'
page_id: '422545691'
product: rm
source: tdn-rm
title: Dados do Modal do Lançamento Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545691
version: 3
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **De** | **Até** | **Tamanho** | **Tipo** | **Decimas** | **Tabela** | **Coluna** | **Descrição** | **Obrigatório** | **Observação** |
| 1 | 1 | 1 | 1 | Caracter |  |  | FIXO("M") | Tipo da linha | X | Letra M |
| 2 | 2 | 6 | 5 | Inteiro |  | DLAFCOMPLEMENTOCTRC | CODCOLIGADA | Coligada | X |  |
| 3 | 7 | 7 | 1 | Caracter |  | DLAFCOMPLEMENTOCTRC | TIPOVEICULO | Tipo do Veículo Tranportador |  | 0 - Embarcação, 1 - Empurrador/rebocador |
| 4 | 8 | 263 | 256 | Caracter |  | DLAFCOMPLEMENTOCTRC | IDENTVEICULO | Identificação do Veículo Tranportador |  |  |
| 5 | 264 | 264 | 1 | Caracter |  | DLAFCOMPLEMENTOCTRC | TIPONAVEGACAO | Tipo de Navegação |  | 0 - Interior, 1 - Cabotagem |
| 6 | 265 | 274 | 10 | Inteiro |  | DLAFCOMPLEMENTOCTRC | NUMEROVIAGEM | Número da viagem |  |  |
| 7 | 275 | 287 | 13 | Valor | 2 | DLAFCOMPLEMENTOCTRC | VALDESPPORTUARIA | Despesas Portuárias |  |  |
| 8 | 288 | 300 | 13 | Valor | 2 | DLAFCOMPLEMENTOCTRC | VALDESPCARGA | Despesas com carga e descarga |  |  |
| 9 | 301 | 313 | 13 | Valor | 2 | DLAFCOMPLEMENTOCTRC | VALFRETEMARINHA | Frete para Renovação da Marinha |  |  |
| 10 | 314 | 314 | 1 | Caracter |  | DLAFCOMPLEMENTOCTRC | TIPOTARIFA | Tipo de Tarifa |  | 0 - Exp., 1 - Enc., 2 - CI, 9 - Outra |
| 11 | 315 | 327 | 13 | Valor | 2 | DLAFCOMPLEMENTOCTRC | PESOTAXADO | Peso Taxado |  |  |
| 12 | 328 | 340 | 13 | Valor | 2 | DLAFCOMPLEMENTOCTRC | VALTAXATERRESTRE | Valor da Taxa Terrestre |  |  |
| 13 | 341 | 353 | 13 | Valor | 2 | DLAFCOMPLEMENTOCTRC | VALADVALOREM | Valor da Taxa "ad valorem" |  |  |
| 14 | 354 | 354 | 1 | Caracter |  | DLAFCOMPLEMENTOCTRC | NATUREZAFRETE | Indicador da Natureza do Frete |  | 0 - Negociável, 1 - Não Negociável |
| 15 | 355 | 367 | 13 | Valor | 2 | DLAFCOMPLEMENTOCTRC | VALGRIS | Valor dos Gris |  |  |
