---
content_hash: 46c8b8d26c6dabd7ddaa3174367a496e5e80284b0738f2f173723d6a16f52b38
fetched_at: '2026-06-29T00:11:11.506164+00:00'
page_id: '647460774'
product: rm
source: tdn-rm
title: DT – eSocial - Valor INSS Folha com R$ 0,01 maior que o Valor INSS Governo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=647460774
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Cálculo INSS e INSS Outro Emprego |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-977](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-977) |

## **02. SITUAÇÃO/REQUISITO**

Mesmo com o parâmetro 'Calcula INSS conforme o Esocial' MARCADO, o sistema calculou o evento INSS com R$ 0,01 a maior que o governo (Esocial). O sistema calculou com o valor de R$ 339,20 e o governo calculou e nos devolveu o valor de R$ 339,19.

## **03. SOLUÇÃO**

Como a inconsistência acontece quando há lançamento de INSS Outro Emprego, foi alterado para que no lançamento de evento com código de cálculo 29 – INSS Outro Emprego no envelope de pagamento onde já exista o evento de salário normal seja calculado o código de cálculo 29 primeiro nas faixas de INSS quando o cálculo do INSS for executado.

## **04. DEMAIS INFORMAÇÕES**

[EXEMPLO LANÇAMENTO CC 29 – INSS Outro Emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=647459982)
