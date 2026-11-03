---
content_hash: 78f3439cf1e64210a4a304f42097b339287f67b6c57dbbfbcc2aa8d05c0cd2d7
fetched_at: '2026-06-29T00:05:47.289130+00:00'
page_id: '1010257226'
product: rm
source: tdn-rm
title: DT - Crédito do Trabalhador - Novos campos na tabela de Importação do Crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1010257226
version: 5
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Crédito do Trabalhador - Importação |
| País: | Brasil |
| Ticket: | [24291124](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%2224291124%22 "24291124") |
| Issue: | [DRHCALCRM-8100](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-8100) |

## **02. VERSÕES**

A partir dos patches:

* + 12.1.2410.319
  + 12.1.2502.229
  + 12.1.2506.179
  + 12.1.2510.112
  + 12.1.2602 e superiores

## **03. SITUAÇÃO/REQUISITO**

Criar novos campos na tabela PFEMPRT para conter informações de Mês competência e Ano competência em que o empréstimo está sendo importado.

## **04. SOLUÇÃO**

Foram criados dois novos campos para a tabela de empréstimos:

* **PFEMPRT.MESCOMPATUAL**
* **PFEMPRT.ANOCOMPATUAL**

## **05.****ASSUNTOS RELACIONADOS**
