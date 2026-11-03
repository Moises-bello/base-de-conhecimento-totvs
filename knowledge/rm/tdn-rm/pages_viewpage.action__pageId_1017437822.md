---
content_hash: 5591fb6b4ec71282ba4478af3371f1f024559dff1dc795917c12682a287aa057
fetched_at: '2026-06-29T00:05:47.770373+00:00'
page_id: '1017437822'
product: rm
source: tdn-rm
title: DT - Crédito do Trabalhador - Portabilidade de Crédito do Trabalhador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1017437822
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Crédito do Trabalhador - Portabilidade de Crédito do Trabalhador |
| País: | Brasil |
| Ticket: | [25071549](https://totvssuporte.zendesk.com/agent/tickets/25071549 "View ticket on the Zendesk portal") |
| Issue: | [DRHCALCRM-10168](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-10168) |

## **02. VERSÕES**

A partir dos patches:

* + 12.1.2502.242
  + 12.1.2506.190
  + 12.1.2510.122
  + 12.1.2602 e superiores

## **03. SITUAÇÃO/REQUISITO**

Ao realizar a portabilidade de um Crédito do Trabalhador, o número do contrato permanece o mesmo, porém o banco é alterado. Nesse cenário, o sistema não está registrando essa mudança, nem mantendo um histórico das alterações no empréstimo original.

## **04. SOLUÇÃO**

Em casos de portabilidade do empréstimo do Crédito do Trabalhador, o número do contrato deverá ser mantido, contudo, o código do banco poderá ser alterado.

Nesse cenário, sempre que houver alteração do código do banco, essa informação deverá ser devidamente atualizada durante o processo de importação do arquivo da seguinte forma:

* + Dar baixa na linha do empréstimo atual  para manter o histórico do banco anterior.
  + Criar uma nova linha com data inicial conforme novo banco.

## **04.** **ASSUNTOS RELACIONADOS**

* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
