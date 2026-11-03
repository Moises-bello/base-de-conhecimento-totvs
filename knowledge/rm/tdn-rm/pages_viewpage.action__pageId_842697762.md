---
content_hash: 8d8a59c18414dc7cb80c9ed088f524e87a04cba683860bd97e17366e59bfc6a8
fetched_at: '2026-06-29T00:11:50.554717+00:00'
page_id: '842697762'
product: rm
source: tdn-rm
title: DT - Evento de desconto de adiantamento 13° salário lançado na 2ª parcela horista
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=842697762
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | 13º salário |
| País: | Brasil |
| Ticket: | [Ticket #18640519](https://totvssuporte.zendesk.com/agent/tickets/18640519 "View ticket on the Zendesk portal") |
| Issue: | [DRHCALCRM-5743](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5743) |

## **02. SITUAÇÃO/REQUISITO**

Empresa possui funcionários horistas que recebem 13° salário pelas médias, ao lançar a primeira parcela de 13° salário o evento CC9 busca corretamente o valor de média, porém ao lançar a 2° parcela de 13° salário lança o evento de média com valor integral e não lança o evento de desconto de adiantamento de 13° salário CC35.

## **03. SOLUÇÃO**

Realizada a alteração no código para o desconto da primeira parcela 13° salário quando não existir no envelope o evento do grupo zero de 13o. salário 2a. Parcela.

Atenção:

O evento com código de cálculo 102 - 2ª parcela 13º Salário deve existir no cadastro de sindicatos pasta Eventos p/ Pag. de Médias de 13º na 2ª Parcela no grupo 0 (zero).

## **04. DEMAIS INFORMAÇÕES**

Aviso importante

Não poderá ser feito o recálculo direto no envelope de pagamento porque por não existir o evento do grupo zero de 13o. salário 2a. Parcela, então o envelope ficará sem os eventos lançados anteriormente.
