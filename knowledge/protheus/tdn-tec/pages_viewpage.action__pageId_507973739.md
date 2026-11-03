---
content_hash: 5cfbe6f972107a359db780ab4e0365e701cae876d0ac6a559a309dd3a07f8168
fetched_at: '2026-07-02T19:24:25.820170+00:00'
page_id: '507973739'
product: protheus
source: tdn-tec
title: Correção - Relatório TMSPrinter via Cliente truncando informações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=507973739
version: 1
---

Correção - Relatório TMSPrinter via Cliente truncando informações

|  |  |
| --- | --- |
| Situação | Quando solicitada a impressão de um relatório local (via Client) que utiliza a TMSPrinter (TReport), algumas informações não são apresentadas completamente pois apresentam um corte no último caractere. |
| Ocorrência | Ocorre em relatórios impressos via Client usando TReport. |
| Correção | Correção no cálculo do tamanho necessário para cada informação apresentada. |
| Informações adicionais | * Referente ao chamado: 6395239 * Referente à ocorrência: MTEC-3080 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.10 |
