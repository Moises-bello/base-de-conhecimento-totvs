---
content_hash: a2ee11b666505a683b8f6b7fb781117a728711976855ebe707c27c46f670ef01
fetched_at: '2026-06-29T00:09:21.140366+00:00'
page_id: '422545821'
product: rm
source: tdn-rm
title: Outros Tributos do Item do Lançamento Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545821
version: 4
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **De** | **Até** | **Tamanho** | **Tipo** | **Decimas** | **Tabela** | **Coluna** | **Descrição** | **Obrigatório** | **Observação** |
| 1 | 1 | 1 | 1 | Caracter |  |  | FIXO("B") | Tipo da linha | x | Letra B |
| 2 | 2 | 6 | 5 | Inteiro |  | DTRBITEM | CODCOLIGADA | Código da Coligada | x |  |
| 3 | 7 | 16 | 10 | Caracter |  | DTRBITEM | CODTRB | Código do Tributo | x |  |
| 4 | 17 | 31 | 15 | Valor | 4 | DTRBITEM | BASETRB | Base de Cálculo |  |  |
| 5 | 32 | 46 | 15 | Valor | 4 | DTRBITEM | VALORTRB | Valor do Tributo |  |  |
| 6 | 47 | 61 | 15 | Valor | 4 | DTRBITEM | VLRISENTO | Valor Isento |  |  |
| 7 | 62 | 62 | 1 | Caracter |  | DTRBITEM | TIPOTRIBUTACAO | Tipo de Tributação |  | 0 = Nenhum 1 = Tributado, 2 = Alíquota Zero, 3 = Isento, 4 = Substituição Tributária |
| 8 | 63 | 77 | 15 | Valor | 4 | DTRBITEM | ALIQTRB | Aliquota |  |  |
| 9 | 78 | 79 | 2 | Caracter |  | DTRBITEM | SITTRIBUTARIA | Situação Tributária |  |  |
| 10 | 78 | 92 | 15 | Valor | 4 | DTRBITEM | DEDUCAOTRB | Valor Dedução |  |  |
| 11 | 93 | 107 | 15 | Valor | 4 | DTRBITEM | ALIQUOTAPORVALOR | Aliquota por Valor |  |  |
| 12 | 108 | 109 | 2 | Caracter |  | DTRBITEM | CODCONTRIBSOCIAL | Código da Contribuição Social |  |  |
| 13 | 110 | 129 | 20 | Caracter |  | DTRBITEM | NATOPERNFSE | Natureza de Operação NFS-e |  | Somente para ISS |
| 14 | 110 | 111 | 2 | Caracter |  | DTRBITEM | CODRECEITA | Código da Receita |  |  |
