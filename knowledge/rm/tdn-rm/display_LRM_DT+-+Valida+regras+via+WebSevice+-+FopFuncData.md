---
content_hash: 8f321a79f1fd8bfdbd9b7998a8cc77388abd26a0c296a43f36be69f27447b402
fetched_at: '2026-06-29T00:11:05.395849+00:00'
page_id: '630839505'
product: rm
source: tdn-rm
title: DT - Valida regras via WebSevice - FopFuncData
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Valida+regras+via+WebSevice+-+FopFuncData
version: 5
---

## ****01. DADOS GERAIS****

Linha RM​

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | Totvs Folha de Pagamento |
| Função: | SaveRecord FopFuncData |
| País: | Brasil |
| Ticket: | 11198404 |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-207](https://jiraproducao.totvs.com.br/browse/DRHROTRM-207) |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar uma admissão via webservice wsDataServer, método SaveRecord, não está realizando a validação de obrigatoriedade de requisições.

## **03. SOLUÇÃO**

Realizado o tratamento para validar a obrigatoriedade das requisições na admissão.

Parametro "Valida regras via WebSevice" deve estar marcado.

Ao tentar realizar a inclusão do funcionario sem a inclusão de uma requisição sistema apresentará erro no processo.

## **04. ASSUNTOS RELACIONADOS**
