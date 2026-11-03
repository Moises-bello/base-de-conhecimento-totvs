---
content_hash: 3b4ed77db45e3a131e760f1dd4b0a107109ecb9b66a528b0c4f29374a2864c30
fetched_at: '2026-06-29T00:11:16.964693+00:00'
page_id: '674902939'
product: rm
source: tdn-rm
title: 13756599 FISCAL01-17623 - DT - C100 - ajuste valor campo 12
type: documentation
url: https://tdn.totvs.com/display/LRM/13756599+FISCAL01-17623+-+DT+-+C100+-+ajuste+valor+campo+12
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED FISCAL |
| País: | Brasil |
| Ticket: | [13756599](https://totvssuporte.zendesk.com/agent/tickets/13756599 "Visualizar o Ticket no portal do Zendesk") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17623 |

## **02. SITUAÇÃO/REQUISITO**

O campo 12 do registro C100 esta gerando um valor incorreto e não foi possível rastrear a origem da diferença , a inconsistência ocorre apenas em lançamentos que possuem duas situações tributárias.

## **03. SOLUÇÃO**

Realizado ajuste no cálculo que é realizado quando o Lançamento possui Desconto Condicional para que não ocorram diferenças no campo 12 do SPED FISCAL mesmo que o lançamento possua várias situações tributárias e itens.

Disponível a partir da biblioteca 12.1.33
