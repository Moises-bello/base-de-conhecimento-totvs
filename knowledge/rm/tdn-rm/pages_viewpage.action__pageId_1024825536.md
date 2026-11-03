---
content_hash: 71ed16e6bfc2e05ecba970c743ad02e3dad9fa7c48af83220826e9b3f68e9c46
fetched_at: '2026-06-29T00:05:48.482049+00:00'
page_id: '1024825536'
product: rm
source: tdn-rm
title: DT - Nota Técnica 04/2025 - Criação de novos campos nas tabelas PFPERFF e PFPERFFCOMPL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1024825536
version: 3
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha deIm Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Ficha Financeira e Ficha Financeira Complementar |
| País: | Brasil |
| Issue: | [DRHCALCRM-10597](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-10597) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2502
* 12.1.2506
* 12.1.2510 e posteriores

## **03. SITUAÇÃO/REQUISITO**

Foi solicitado a criação de novos campos na ficha financeira para a Nota Técnica do eSocial S-1.3

## **04. SOLUÇÃO**

Foi criado um campo nas tabelas PFPERFF e PFPERFFCOMPL, com o nome de **NOTAFT** que tem por função identificar lançamentos de valores que foram apurados pela [**Auditoria-Fiscal do Trabalho (AFT)**](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/escola/o-auditor-fiscal-do-trabalho-e-a-inspecao-do-trabalho "Seguir link").  Eventos que irão utilizar esta informação:  S-1200, S-2299 e S-2399.
