---
content_hash: fea0e10beadded6c9ceffe2f3643fb04ab88f4094d89765d2d99a507aeeda3df
fetched_at: '2026-06-29T00:09:20.299166+00:00'
page_id: '422545685'
product: rm
source: tdn-rm
title: Dados dos Itens Cancelados do Cupom Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/Dados+dos+Itens+Cancelados+do+Cupom+Fiscal
version: 3
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **De** | **Até** | **Tamanho** | **Tipo** | **Tabela** | **Coluna** | **Decimas** | **Descrição** | **Obrigatório** | **Observação** |
| 1 | 1 | 1 | 1 | Caracter |  | FIXO("H") |  | Tipo da linha | X | Letra H |
| 2 | 2 | 6 | 5 | Inteiro | DITEMCUPOMCANC | CODCOLIGADA |  | Coligada | X |  |
| 3 | 7 | 16 | 10 | Inteiro | DITEMCUPOMCANC | NUMITEM |  | Número do Item | X |  |
| 4 | 17 | 46 | 30 | Caracter | DITEMCUPOMCANC | IDPRD |  | Código do Produto | X |  |
| 5 | 47 | 61 | 15 | Valor | DITEMCUPOMCANC | QTDEPRD | 4 | Quantidade |  |  |
| 6 | 62 | 82 | 21 | Valor | DITEMCUPOMCANC | PRECOPRD | 10 | Preço |  | Para versões abaixo da versão 11.82 o tamanho é 15 e Decimais é igual a 4 |
| 7 | 83 | 97 | 15 | Valor | DITEMCUPOMCANC | DESCONTOS | 4 | Desconto |  |  |
| 8 | 98 | 112 | 15 | Valor | DITEMCUPOMCANC | DESPESAS | 4 | Despesas |  |  |
| 9 | 113 | 122 | 10 | Caracter | DITEMCUPOMCANC | CUPOMFISCAL |  | Cupom Fiscal |  |  |
