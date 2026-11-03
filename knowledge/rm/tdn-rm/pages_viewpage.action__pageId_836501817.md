---
content_hash: 7ed6c82b00d27bc925917b90b37d583ed175643eb9348f00d84ca8e80092b634
fetched_at: '2026-06-29T00:11:49.675787+00:00'
page_id: '836501817'
product: rm
source: tdn-rm
title: DT - Código de cálculo 130/131/132 - Prioridade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=836501817
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Prioridade no cadastro de eventos |
| País: | Brasil |
| Ticket: | [Ticket #19124952](https://totvssuporte.zendesk.com/agent/tickets/19124952) |
| Issue: | [DRHCALCRM-5986](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5986) |

## **02. SITUAÇÃO/REQUISITO**

Ao cadastrar algum dos eventos com os códigos de cálculo 130,131 ou 132, a prioridade está sendo setada como 80 e no TDN [Eventos de Cálculo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719284) informa que deve ser 81.  
 

## **03. SOLUÇÃO**

Alterado para cadastrar a prioridade 81 nos eventos que tenham a seleção dos códigos de cálculos:

130 - INSS Férias Próximo Mês

131 - INSS Férias Desconto Mês Anterior

132 - Diferença INSS Férias Próximo Mês

## **04. DEMAIS INFORMAÇÕES**

IMPORTANTE

Para alterar o evento já cadastrado com a prioridade 80 basta editar o evento selecionar o código de cálculo 0 - Sem Código de Cálculo Existente, retornar com o código de cálculo retirado anteriormente e salvar.

**DICA:** Utilize o processo de cópia entre coligadas no cadastro de eventos para o caso de existir mais coligadas e o código do evento nelas for o mesmo, ou seja, DEVE COINCIDIR CÓDIGO DO EVENTO COM O CÓDIGO DE CÁLCULO NAS COLIGADAS para copiar o evento cadastrado e alterado sobrepondo nas outras coligadas,
