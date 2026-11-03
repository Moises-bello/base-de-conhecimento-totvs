---
content_hash: 9b51d2b1027663a45f56e8c2208006dc1e0eb5c6d6b52240c0561cd785bf5af9
fetched_at: '2026-06-29T00:09:20.464119+00:00'
page_id: '422545690'
product: rm
source: tdn-rm
title: Dados do Exterior
type: documentation
url: https://tdn.totvs.com/display/LRM/Dados+do+Exterior
version: 3
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **De** | **Até** | **Tamanho** | **Tipo** | **Decimas** | **Tabela** | **Coluna** | **Descrição** | **Obrigatório** | **Observação** |
| 1 | 1 | 1 | 1 | Caracter |  |  | FIXO("A") | Tipo da linha | X | Letra A |
| 2 | 2 | 6 | 5 | Inteiro |  | DLAFEXTERIOR | CODCOLIGADA | Coligada | X |  |
| 3 | 7 | 17 | 11 | Caracter |  | DLAFEXTERIOR | NUMERODE | Número DE |  |  |
| 4 | 18 | 27 | 10 | Data |  | DLAFEXTERIOR | DATADE | Data DE |  |  |
| 5 | 28 | 32 | 5 | Inteiro |  | DLAFEXTERIOR | NATUREZAEXPORTACAO | Natureza exportação |  | preencher com 1, 2 ou em branco |
| 6 | 33 | 57 | 25 | Caracter |  | DLAFEXTERIOR | CONHECIMENTOEMBARQUE | Conhecimento Embarque |  | Antes do patch 11.52.20 o tamanho do campo conhecimento Embarque é 16 |
| 7 | 58 | 67 | 10 | Data |  | DLAFEXTERIOR | DATACONHECIMENTO | Data Conhecimento |  |  |
| 8 | 68 | 72 | 5 |  |  | DLAFEXTERIOR | TIPOCONHECIMENTO | Tipo Conhecimento |  | Conforme tabela de Tipos de Conhecimento SISCOMEX |
| 9 | 73 | 82 | 10 | Data |  | DLAFEXTERIOR | DATAAVERBACAO | Data Averbação |  |  |
| 10 | 83 | 93 | 11 | Caracter |  | DLAFEXTERIOR | NUMDESPACHO | Numero Despacho |  |  |
| 11 | 94 | 108 | 15 | Valor | 4 | DLAFEXTERIOR | VALORDESPACHO | Valor Despacho |  |  |
| 12 | 109 | 120 | 12 | Caracter |  | DLAFEXTERIOR | NUMERODI | Número DI |  |  |
| 13 | 121 | 130 | 10 | Data |  | DLAFEXTERIOR | DATADI | Data DI |  |  |
| 14 | 131 | 140 | 10 | Data |  | DLAFEXTERIOR | DATADESEMBARACO | Data Desembaraço |  |  |
| 15 | 141 | 145 | 5 | Inteiro |  | DLAFEXTERIOR | NATUREZAIMPORTACAO | Natureza de Importação |  |  |
