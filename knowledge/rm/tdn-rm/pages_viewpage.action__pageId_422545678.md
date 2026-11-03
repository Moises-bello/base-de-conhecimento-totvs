---
content_hash: eac0035b4e6222a99a4d83bdb8c8a4885de62dad92ed7ea6fd23d1f2f2c459ea
fetched_at: '2026-06-29T00:09:20.200129+00:00'
page_id: '422545678'
product: rm
source: tdn-rm
title: Importação da Contabilização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545678
version: 5
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **De** | **Até** | **Tamanho** | **Tipo** | **Decimas** | **Tabela** | **Coluna** | **Descrição** | **Obrigatório** | **Observação** |
| 1 | 1 | 1 | 1 | Caracter |  |  | FIXO("C") | Tipo da linha | X | Letra C |
| 2 | 2 | 6 | 5 | Inteiro |  | DLAFCONT | CODCOLIGADA | Código da Coligada | X |  |
| 3 | 7 | 7 | 1 | Inteiro |  | DLAFCONT |  | Débito / Crédito (1,2) | X | Nota 9 |
| 4 | 8 | 12 | 5 | Inteiro |  | DLAFCONT |  | Cód. da Coligada. da Conta Contábil | X |  |
| 5 | 13 | 52 | 40 | Caracter |  | DLAFCONT |  | Código da Conta Contábil | X |  |
| 6 | 53 | 67 | 15 | Valor | 4 | DLAFCONT |  | Valor Conta Contábil |  |  |
| 7 | 68 | 92 | 25 | Inteiro |  | DLAFCONT |  | Cód. Da Filial | X |  |
| 8 | 93 | 117 | 25 | Caracter |  | DLAFCONT |  | Cód. Do Departamento |  |  |
| 9 | 118 | 142 | 25 | Caracter |  | DLAFCONT |  | Cód. Do Centro de Custos |  |  |
| 10 | 143 | 152 | 10 | Caracter |  | DLAFCONT |  | Cód. Do Histórico Padrão |  |  |
| 11 | 153 | 402 | 250 | Caracter |  | DLAFCONT |  | Complemento do Histórico |  |  |
| 12 | 403 | 407 | 5 | Inteiro |  | DLAFCONT |  | Código Lote Contábil |  |  |
| 13 | 408 | 427 | 20 | Caracter |  |  |  | Código Reduzido da Conta Contábil |  |  |
