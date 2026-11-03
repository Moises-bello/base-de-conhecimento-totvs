---
content_hash: 68059644096752254716e2fd3b71570d8dafbc78d89d10f4e7eefada3e85c4b6
fetched_at: '2026-06-29T00:09:21.163274+00:00'
page_id: '422545826'
product: rm
source: tdn-rm
title: Notas Fiscais de Terceiros associadas ao Lançamento Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545826
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Ordem** | **De** | **Até** | **Tamanho** | **Tipo** | **Decimas** | **Tabela** | **Coluna** | **Descrição** | **Obrigatório** | **Observação** |
| 1 | 1 | 1 | 1 | Caracter |  |  | FIXO("P") | Tipo da linha | X | Letra P |
| 2 | 2 | 6 | 5 | Inteiro |  | DNFTERCEIROS | CODCOLIGADA | Coligada | X |  |
| 3 | 7 | 16 | 10 | Caracter |  | DNFTERCEIROS | CODTDO | Espécie do Documento | X |  |
| 4 | 17 | 31 | 15 | Caracter |  | DNFTERCEIROS | DOCINI | Nº do Documento | X |  |
| 5 | 32 | 35 | 4 | Caracter |  | DNFTERCEIROS | SERIEDOC | Série do Documento | X |  |
| 6 | 36 | 38 | 3 | Caracter |  | DNFTERCEIROS | SUBSERIE | Sub-série do Documento |  |  |
| 7 | 39 | 58 | 20 | Caracter |  | DNFTERCEIROS | CNPJCPFCEI | CNPJ/CPF/CEI | X |  |
| 8 | 59 | 60 | 2 | Caracter |  | DNFTERCEIROS | UF | UF |  |  |
| 9 | 61 | 80 | 20 | Caracter |  | DNFTERCEIROS | INSCRESTADUAL | Inscrição Estadual |  |  |
| 10 | 81 | 82 | 2 | Caracter |  | DNFTERCEIROS | MOTIVOREF | Motivo Referência | X |  |
| 11 | 83 | 232 | 150 | Caracter |  | DNFTERCEIROS | OBSERVACAO | Observação |  |  |
| 12 | 233 | 247 | 15 | Valor | 2 | DNFTERCEIROS | VALORTOTAL | Valor Total |  |  |
| 13 | 248 | 257 | 10 | Data |  | DNFTERCEIROS | DATAEMISSAO | Data Emissão |  |  |
