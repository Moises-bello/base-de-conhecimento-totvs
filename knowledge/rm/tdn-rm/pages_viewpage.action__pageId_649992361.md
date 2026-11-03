---
content_hash: a2b408aca45a28cdb6c19b6e84c26bd9152ba80319c29594117e67816ec65d8a
fetched_at: '2026-06-29T00:11:11.778963+00:00'
page_id: '649992361'
product: rm
source: tdn-rm
title: DT – Rescisão Retificadora – Lançar evento de líquido retificação para a opção
  "Calcular somente o eventos informados"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=649992361
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Rescisão Complementar |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-974](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-974) |

## **02. SITUAÇÃO/REQUISITO**

Calcular a rescisão retificadora, marcando a opção "Calcular somente eventos informados", o sistema não lança o evento código de cálculo 383 - Líquido retificação. Se não marcar esse parâmetro, o sistema realiza o lançamento do líquido no movimento atual, porém o cliente não deseja recalcular toda a rescisão. Somente informar um evento específico que deixou de pagar.

## **03. SOLUÇÃO**

Calcular a rescisão retificadora, marcando a opção "Calcular somente eventos informados", o sistema lança o evento código de cálculo 383 - Líquido retificação.

## **04. DEMAIS INFORMAÇÕES**

[S-2299/S-2399 - Como gerar Retificação de desligamento?](https://tdn.totvs.com/pages/viewpage.action?pageId=417700835#Calculo-3-2)
