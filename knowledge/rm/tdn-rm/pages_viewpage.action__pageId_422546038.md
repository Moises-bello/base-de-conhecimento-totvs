---
content_hash: 1fcf4660df2f09adbbb3de0b7b0b29a9f25c347978125199c259e917eeaf7821
fetched_at: '2026-06-29T00:09:23.011239+00:00'
page_id: '422546038'
product: rm
source: tdn-rm
title: Rateio Gerencial da Contabilização do Lançamento Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546038
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **De** | **Até** | **Tamanho** | **Tipo** | **Decimas** | **Tabela** | **Coluna** | **Descrição** | **Obrigatório** | **Observação** |
| 1 | 1 | 1 | 1 | Caracter |  |  | FIXO("R") | Tipo da linha | X | Letra R |
| 2 | 2 | 6 | 5 | Inteiro |  | DLAFRAT | CODCOLIGADA | Código da Coligada do Rateio | X |  |
| 3 | 7 | 7 | 1 | Inteiro |  | DLAFRAT | TIPO | Débito / Crédito | X | Nota 9 |
| 4 | 8 | 12 | 5 | Inteiro |  | DLAFRAT | CODCOLCONTA | Cód. Da Coligada. Da Conta Contábil | X |  |
| 5 | 13 | 52 | 40 | Caracter |  | DLAFRAT | CODCONTA | Código da Conta Contábil | X |  |
| 6 | 53 | 57 | 5 | Inteiro |  | DLAFRAT | CODCOLCONTAGER | Cód. Coligada Conta Gerencial | X |  |
| 7 | 58 | 97 | 40 | Caracter |  | DLAFRAT | CODCONTAGER | Cód. da Conta Gerencial | X |  |
| 8 | 98 | 112 | 15 | Valor | 4 | DLAFRAT | VALOR | Valor Conta Contábil |  |  |
| 9 | 113 | 117 | 5 | Inteiro |  | DLAFRAT | CODLOTE | Código Lote Contábil |  |  |
| 10 | 118 | 137 | 20 | Caracter |  |  |  | Código Reduzido da Conta Contábil |  |  |
