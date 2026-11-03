---
content_hash: 3db93bd127a5b431160e83fc932cb239282ba1c6e54150b3a8aebca837869e29
fetched_at: '2026-06-29T00:05:48.266401+00:00'
page_id: '1024357862'
product: rm
source: tdn-rm
title: DT - Crédito do Trabalhador - Importação para Funcionários com categoria 721
  eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1024357862
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Importação para Funcionários com categoria 721 eSocial |
| País: | Brasil |
| Ticket: | [25259392](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%2225259392%22 "25259392") |
| Issue: | [DRHCALCRM-10334](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-10334) |

## **02. VERSÕES**

A partir dos patches:

* + 12.1.2502.252
  + 12.1.2506.210
  + 12.1.2510.139
  + 12.1.2602 e superiores

## **03. SITUAÇÃO/REQUISITO**

Necessário tratar a importação para casos em que o funcionário não tenha Matricula do eSocial e que o mesmo utilize a categoria 721 do eSocial

## **04. SOLUÇÃO**

Agora é possível importar os dados de empréstimo para funcionários que estejam na categoria 721 do eSocial, utilizamos o campo CPF que já vinha no Layout de importação para identificar e realizar essa importação.

## **05. ASSUNTOS RELACIONADOS**
