---
content_hash: 3104eff9e2dca17916b85d69990eac7524062dbdc57134db08ee1024be7fa8ec
fetched_at: '2026-06-29T00:11:54.534994+00:00'
page_id: '853915277'
product: rm
source: tdn-rm
title: DT - Smart View - Gerar relatórios do Smart View usando o TAE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=853915277
version: 5
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração TOTVS Folha de Pagamento X TOTVS Assinatura Eletrônica |
| País: | Brasil |
| Épico | [DRHCALCRM-5735](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-5735) |

## **02. VERSÃO**

A solução estará disponível a partir dos patchs/release abaixo:

* 12.1.2402.181
* 12.1.2406.113
* 12.1.2410

## **03. SITUAÇÃO/REQUISITO**

Disponibilizar  na integração do TOTVS Folha de Pagamento X TAE a opção onde o usuário possa, além de enviar documentos gerados pelo RM Reports, enviar documentos gerados pelo recurso do SmartView

## **04. SOLUÇÃO**

Foi implementado a flag "Usa Recurso SmartView" na tela Tipo de relatório. Marcando esta opção será listado os relatórios existentes na base de dados criados no SmartView conforme o tipo de relatório. Além disso, se o parâmetro estiver desmarcado, o usuário poderá continuar utilizando seu recurso RM Reports.

## **05. DEMAIS INFORMAÇÕES**

[TOTVS Assinatura Eletrônica - Definições e Parametrizações](https://tdn.totvs.com.br/pages/viewpage.action?pageId=607590749)
