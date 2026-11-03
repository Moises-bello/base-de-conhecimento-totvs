---
content_hash: f68d0b54e28ed8dcbb5d35dd654dfef935a86910c4e64009097a0ce058c9db4b
fetched_at: '2026-06-29T00:10:26.061502+00:00'
page_id: '510505247'
product: rm
source: tdn-rm
title: DEDUMOBILE-2362 DT Remoção de alterar senha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=510505247
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | eduCONNECT |
| Função: | Alteração de Senha |
| Ticket: | [#6553885](https://totvssuporte.zendesk.com/agent/tickets/6553885 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUMOBILE-2315](https://jiraproducao.totvs.com.br/browse/DEDUMOBILE-2315) |

## **02. SITUAÇÃO/REQUISITO**

A conexão  do cliente é efetuada através de integração com o AD, ao tentar alterar a senha pelo eduCONNECT é apresentado erro de LDAP, ou seja, a alteração de senha pelo app não efetua a alteração de senha no AD da empresa.

## **03. SOLUÇÃO**

Otimizado o parâmetro: "Permite alterar senha no novo portal do aluno/eduCONNECT" onde se o mesmo estiver desmarcado não será exibido a opção: "Alterar senha" para o usuário do app eduCONNECT.

* Parâmetro marcado: É exibido a opção: "Alterar senha" no menu: Perfil.
* Parâmetro desmarcado: Não é exibido o item: "Alterar senha" no menu: Perfil.

## **04. DEMAIS INFORMAÇÕES**

Para que a funcionalidade seja efetiva, a parametrização deverá ser a mesma para todas as Coligadas.
