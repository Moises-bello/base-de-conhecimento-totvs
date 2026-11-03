---
content_hash: ebeaa375ab14b2fd9c00069315cb5d936d1bb3268a8568b631f9c7ce214afa11
fetched_at: '2026-06-29T00:09:23.056594+00:00'
page_id: '422546039'
product: rm
source: tdn-rm
title: Referências do Item
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546039
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **De** | **Até** | **Tamanho** | **Tipo** | **Decimas** | **Tabela** | **Coluna** | **Descrição** | **Obrigatório** | **Observação** |
| 1 | 1 | 1 | 1 | Caracter |  |  | FIXO("G") | Tipo da linha | X | Letra G |
| 2 | 2 | 6 | 5 | Inteiro |  | DITEMREFERENCIA | CODCOLIGADA | Coligada | X |  |
| 3 | 7 | 11 | 5 | Inteiro |  |  |  | Codigo Filial | X |  |
| 4 | 12 | 12 | 1 | Caracter |  |  |  | Tipo Lançamento Fiscal | X | Nota 1: NF de aquisição da mercadoria exportada (Tipo NF = "E") |
| 5 | 13 | 13 | 1 | Caracter |  |  |  | FLAG Identificador Cliente/Fornecedor | X | Nota 2: Fornecedor da mercadoria exportada (Flag = "C") |
| 6 | 14 | 18 | 5 | Inteiro |  |  |  | Coligada do Cliente/Fornecedor | X |  |
| 7 | 19 | 43 | 25 | Caracter |  |  |  | Código do Cliente/Fornecedor | X |  |
| 8 | 44 | 53 | 10 | Data |  |  |  | Data Entrada/Saida | X |  |
| 9 | 54 | 63 | 10 | Caracter |  |  |  | Especie Documento | X |  |
| 10 | 64 | 67 | 4 | Caracter |  |  |  | Serie | X |  |
| 11 | 68 | 79 | 12 | Caracter |  |  |  | Número Documento | X |  |
| 12 | 80 | 94 | 15 | Valor | 4 | DITEMREFERENCIA | QTDEPRD | Quantidade |  |  |
