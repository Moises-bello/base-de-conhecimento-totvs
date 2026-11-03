---
content_hash: 1abae7b47cbbcbc92fcdd8cdad4edd73c713dcb64821d1d3d65dde35d2a8ff15
fetched_at: '2026-06-29T00:09:22.815280+00:00'
page_id: '422546036'
product: rm
source: tdn-rm
title: Referências do Lançamento Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546036
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **De** | **Até** | **Tamanho** | **Tipo** | **Decimas** | **Tabela** | **Coluna** | **Descrição** | **Obrigatório** | **Observação** |
| 1 | 1 | 1 | 1 | Inteiro |  |  | FIXO("E") | Tipo da linha | X | Letra E |
| 2 | 2 | 6 | 5 | Inteiro |  | DLAFREFERENCIA | CODCOLIGADA | Código Coligada | X |  |
| 3 | 7 | 11 | 5 | Inteiro |  |  |  | Código Filial | X |  |
| 4 | 12 | 12 | 1 | Caracter |  |  |  | Tipo Lançamento Fiscal | X |  |
| 5 | 13 | 13 | 1 | Caracter |  |  |  | FLAG identificador Cliente/ Fornecedor /  Empresa | X |  |
| 6 | 14 | 18 | 5 | Inteiro |  |  |  | Código Coligada do Cliente/Fornecedor | X |  |
| 7 | 19 | 43 | 25 | Caracter |  |  |  | Fornecedor/ Empresa | X |  |
| 8 | 44 | 53 | 10 | Data |  |  |  | Data Entrada/Saída | X |  |
| 9 | 54 | 63 | 10 | Data |  |  |  | Data Emissão | X |  |
| 10 | 64 | 73 | 10 | Caracter |  |  |  | Espécie do Documento | X |  |
| 11 | 74 | 77 | 4 | Caracter |  |  |  | Série | X |  |
| 12 | 78 | 89 | 12 | Caracter |  |  |  | Nº do Documento | X |  |
| 13 | 90 | 91 | 2 | Caracter |  | DLAFREFERENCIA | MOTIVOREF | Motivo Referência |  |  |
| 14 | 92 | 241 | 150 | Caracter |  | DLAFREFERENCIA | OBSERVAÇÃO | Observação |  |  |
| 15 | 242 | 246 | 5 | Inteiro |  | DLAFREFERENCIA | TIPOREFERENCIA | Tipo Referencia |  | Nota 28 |
| 16 | 247 | 251 | 5 | Inteiro |  | DLAFREFERENCIA | TIPODEDUCAO | Tipo Dedução |  | Nota 29 |
| 17 | 252 | 266 | 15 | Valor | 4 | DLAFREFERENCIA | VALORDEDUCAO | Valor Dedução |  | Nota 30 |
