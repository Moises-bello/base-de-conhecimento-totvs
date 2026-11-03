---
content_hash: 73f726f1d6d11a2738ca0d56dd9fdb3f1c65288bc44d8476dd1168245caa9e9e
fetched_at: '2026-06-29T00:10:16.525829+00:00'
page_id: '471940217'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1131 DT Criação da dimensão de histórico contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=471940217
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional (Fast Analytics) |
| Função: | Extração da fato contabilidade |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUANALYTICS-1131 |

## **02. SITUAÇÃO/REQUISITO**

Os valores contábeis do mês de dezembro estão sendo afetados pelo processo de fechamento da conta contábil. Quando cliente "zera" a conta contábil utilizando a própria conta, o valor retornado para o mês de dezembro fica negativo.

## **03. SOLUÇÃO**

O campo que identifica a execução do processo de fechamento contábil foi incluído na fato de contabilidade. Além disso, foi criado uma nova dimensão chamada "Histórico Contábil" com as informações das execuções do processo de fechamento e uma variável no Gooddata com mesmo nome que deve conter todos os históricos que deverão ser desconsiderados ao retornar os valores da fato contabilidade.
