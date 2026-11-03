---
content_hash: f6354da7ae679afc24452d1f6de4daf876ed4696d6dca0ab206913af720d3029
fetched_at: '2026-06-29T00:11:55.958783+00:00'
page_id: '864987269'
product: rm
source: tdn-rm
title: FISCAL01-23725 - ECD - Diferença de valores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864987269
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Fiscal |
| Processo | Evento Tributário - Simulação Regra de Apuração |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-23725 |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar a simulação do evento tributário ao encerrar o período anual o valor do lucro da exploração do período anual não coincide  com o período do mês de dezembro,

## **03. SOLUÇÃO**

Alteração para buscar Poeb de acordo com a data fim do período Informado no processo do Evento Tributário: Simulação - Regra de Apuração.

Disponível à partir da biblioteca 12.1.2406
