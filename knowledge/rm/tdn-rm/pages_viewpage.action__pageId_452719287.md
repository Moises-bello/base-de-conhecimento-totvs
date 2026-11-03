---
content_hash: 2bcf49163e7f928b832c0dd00cda8ef391956686ca480334298591df4f1042bd
fetched_at: '2026-06-29T00:10:05.391794+00:00'
page_id: '452719287'
product: rm
source: tdn-rm
title: Layout Período da Ficha Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719287
version: 3
---

Para que a importação do Período da Ficha Financeira seja realizado corretamente, é necessário que o arquivo siga o seguinte layout:

|  |  |  |  |
| --- | --- | --- | --- |
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **CAMPO** |
| Chapa do Funcionário | String | 16 | 1 |
| Ano de Competência | Inteiro | 5 | 2 |
| Mês de Competência | Inteiro | 2 | 3 |
| Número do Período | Inteiro | 2 | 4 |
| Mês Caixa Comum | Inteiro | 2 | 5 |
| Salário Comissão (Formato 999999999999,99) | Real | 15 | 6 |
| Valor lançado de férias no mês (Formato 999999,99) | Real | 9 | 7 |
| Base INSS (Formato 999999,99) | Real | 9 | 8 |
| Base INSS de outro emprego (Formato 999999,99) | Real | 9 | 9 |
| INSS (Formato 999999,99) | Real | 9 | 10 |
| INSS de Férias (Formato 999999,99) | Real | 9 | 11 |
| INSS de outro emprego (Formato 999999,99) | Real | 9 | 12 |
| Base INSS do 13º (Formato 999999,99) | Real | 9 | 13 |
| Base INSS do 13º de outro emprego (Formato 999999,99) | Real | 9 | 14 |
| INSS do 13º (Formato 999999,99) | Real | 9 | 15 |
| Base de salário família (Formato 999999,99) | Real | 9 | 16 |
| Salário família (Formato 999999,99) | Real | 9 | 17 |
| Base de vale transporte (Formato 999999,99) | Real | 9 | 18 |
| Vale transporte entregue (Formato 999999,99) | Real | 9 | 19 |
| Vale transporte descontado (Formato 999999,99) | Real | 9 | 20 |
| Base de IRRF (Formato 999999,99) | Real | 9 | 21 |
| IRRF (Formato 999999,99) | Real | 9 | 22 |
| INSS caixa (Formato 999999,99) | Real | 9 | 23 |
| INSS Calculado pelo Usuário | Real | 9 | 24 |
| Dedutível em IRRF (Formato 999999,99) | Real | 9 | 25 |
| Base de IRRF participação (Formato 999999,99) | Real | 9 | 26 |
| IRRF participação (Formato 999999,99) | Real | 9 | 27 |
| Base IRRF férias (Formato 999999,99) | Real | 9 | 28 |
| IRRF férias (Formato 999999,99) | Real | 9 | 29 |
| Indicativo de INSS com CPMF | Real | 9 | 30 |
| Descrição do Período | String | 250 | 31 |
| Base de FGTS (Formato 999999,99) | Real | 9 | 32 |
| Base de FGTS de 13º Salário (Formato 999999,99) | Real | 9 | 33 |
| Salário pago (Formato 999999999999,99) | Real | 15 | 34 |
| Base de IRRF de 13º Salário (Formato 999999,99) | Real | 9 | 35 |
| IRRF sob 13 | Real | 9 | 36 |
| Inss de férias com Cpmf | Real | 9 | 37 |
| INSS de diferença salarial (Formato 999999,99) | Real | 9 | 38 |
| INSS de diferença salarial de 13 (Formato 999999,99) | Real | 9 | 39 |
| INSS de diferença salarial de férias (Formato 999999,99) | Real | 9 | 40 |
| Base FGTS Dif salarial (Formato 999999,99) | Real | 9 | 41 |
