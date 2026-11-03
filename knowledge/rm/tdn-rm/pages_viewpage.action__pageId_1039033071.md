---
content_hash: 27196fe05f62754feea32fc0ab564368a71a96339b2bc7ee18fa6afd8659f31a
fetched_at: '2026-06-29T00:05:49.304720+00:00'
page_id: '1039033071'
product: rm
source: tdn-rm
title: DT - Crédito do Trabalhador - CC 487 e 488 lançados em período diferente da
  folha - Provisionamento Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1039033071
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Crédito do Trabalhador - Cálculo |
| País: | Brasil |
| Ticket: | [#24456726](https://totvssuporte.zendesk.com/agent/tickets/24456726) |
| Issue: | [DRHCALCRM-9657](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-9657) |

## **02. VERSÕES**

A partir dos patches:

* + 12.1.2502.277
  + 12.1.2506.242
  + 12.1.2510.166
  + 12.1.2602 e superiores

## **03. S****ITUAÇÃO/REQUISITO**

No provisionamento de Férias, o evento de [CC 487 - Provisão Crédito Trab. Férias 1º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707675) e [488 - Provisão Crédito Trab. Férias 2º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707680) são lançados no envelope no mesmo período das férias. Contudo, a proposta do provisionamento é auxiliar no líquido do envelope para o desconto do empréstimo e, nesse cenário, ele influencia apenas no líquido do envelope de férias, deixando de realizar sua real função já que o desconto é feito em período diferente.

## **04.****SOLUÇÃO**

        No Parametrizador, aba Férias / Empréstimo, foi criado o campo "Período para lançar o provisionamento do empréstimo crédito do trabalhador nas férias".

Quando informado este período, os processos de Lançar e Finalizar as férias irão inserir os eventos de [CC 487 - Provisão Crédito Trab. Férias 1º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707675) e [488 - Provisão Crédito Trab. Férias 2º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707680) no período selecionado pelo usuário. Caso não tenha nenhum conteúdo neste campo, os eventos de CC's 487 e 488 serão inseridos no mesmo envelope dos eventos de férias, assim como já está hoje.

## **05. ASSUNTOS RELACIONADOS**

* [Empréstimo - Folha de pagamento](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719223)
* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
