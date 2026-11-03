---
content_hash: 8782ed47bbc1606912bb78e114923bdfb56bda4e37dd51e682186f7a261b619d
fetched_at: '2026-06-29T00:11:13.128762+00:00'
page_id: '656329904'
product: rm
source: tdn-rm
title: DT - FISCAL01-15581 - Associação de Lançamento de Saída
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=656329904
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Associação lanãamento de saída |
| País: | Brasil |
| Ticket: | 12900230 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15581 |

## **02. SITUAÇÃO/REQUISITO**

Ao executar o Processo de Associação de Lançamento de Saída, os lançamentos de saída que não é referente a Substituição Tributária ocorrem a seguinte mensagem:

Início do Processo

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*PROCESSADOS\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

O produto Orçamento Financeiro do lançamento 13186 e número do item 2 não foi associado por falta de quantidade.

Fim do Processo

O Cliente solicita que a mensagem seja melhorada. Pois este tipo de lançamento não atende ao processo de associação e torna o arquivo de log muito grande e confuso.

## **03. SOLUÇÃO**

Foi implementado a seguinte regra: 

**Se** Possui quantidade

**Então** ele não exibe a mensagem

**Se não**

**Então** ele exibe a mensagem

Com isso, o comportamento esperado ocorre.

**Disponível a partir da biblioteca 12.1.32**
