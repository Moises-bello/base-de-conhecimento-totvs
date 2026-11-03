---
content_hash: efbbe2b760bcabda03348b5d83960c414425abcffcf71bf9c227e5102f55efdc
fetched_at: '2026-06-29T00:11:54.586438+00:00'
page_id: '855353925'
product: rm
source: tdn-rm
title: DT - Rescisão Complementar Tipo F - Base de IRRF PLR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=855353925
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Rescisão Complementar |
| País: | Brasil |
| Ticket: | [13908107](https://totvssuporte.zendesk.com/agent/tickets/13908107 "View ticket on the Zendesk portal") |
| Issue: | [DRHCALCRM-2247](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2247) |

## **02. SITUAÇÃO/REQUISITO**

Quando o colaborador tem o direito de receber o valor pago a titulo de PLR mesmo estando demitido, o mesmo deve ser pago como verba de natureza salarial ou não salarial após o desligamento. Pode ocorrer casos em que após o pagamento desta verba o colaborar tenha direito a algum complemento relacionado a dissídio, onde se faz necessário executar o cálculo de rescisão complementar. Porém quando este cálculo era executado, estava considerando esta verba de PLR paga no mesmo caixa da rescisão complementar, fazendo com o valor de desconto de IRRF PLR fosse lançado. 

## **03. SOLUÇÃO**

Adequado o cálculo para não somar a base da rescisão quando existir PLR paga como verba de natureza salarial ou não salarial após o desligamento. 

## **04.** **ASSUNTOS RELACIONADOS**

* [Rescisão Complementar](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718921)
