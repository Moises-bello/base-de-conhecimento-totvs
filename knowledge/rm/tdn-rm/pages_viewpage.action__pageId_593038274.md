---
content_hash: 60fa7d847cc52c3bca08019aa0e978d528f74b74ee4c0295fbfeebf40d8ee2ee
fetched_at: '2026-06-29T00:10:56.766163+00:00'
page_id: '593038274'
product: rm
source: tdn-rm
title: Segurança WebService
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593038274
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | RH |
| Módulo: | Automação de ponto |
| Função: | Parâmetro de segurança |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [PONTO01-9833 Segurança API Rest](https://jiraproducao.totvs.com.br/browse/PONTO01-9833) |

## **02. SITUAÇÃO/REQUISITO**

Ao acessar o WebService POSTMAN ou SOAPUI,  foi encontrada uma falha de segurança, onde um usuário que tem permissão em apenas uma coligada dentro do RM, consegue visualizar informações de outras coligadas, na qual não tem permissão, através do WebService.

## **03. SOLUÇÃO**

Foi criado um parâmetro **"Desconsiderar filtro de produto em WebService"**, junto com as classes de segurança para validar o acesso do usuário.
