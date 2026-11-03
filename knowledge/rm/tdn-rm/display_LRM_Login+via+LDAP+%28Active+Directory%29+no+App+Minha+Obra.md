---
content_hash: 973893aab24822461891f75dc8cbf4aed976bd6ac973fcaa83541b4a8f002be4
fetched_at: '2026-06-29T00:10:32.931444+00:00'
page_id: '528455089'
product: rm
source: tdn-rm
title: Login via LDAP (Active Directory) no App Minha Obra
type: documentation
url: https://tdn.totvs.com/display/LRM/Login+via+LDAP+%28Active+Directory%29+no+App+Minha+Obra
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Construção e Projetos |
| Módulo: | TOP |
| Função: | Login no App Minha Obra via LDAP (Active Directory) |
| Ticket: | [TOPORCAPLAN001-9978](https://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-9978) |
| Requisito/Story/Issue (informe o requisito relacionado) : | [TOPORCAPLAN001-9887](https://jiraproducao.totvs.com.br/browse/TOPORCAPLAN001-9887) |

## **02. SITUAÇÃO/REQUISITO**

Permitir que o App Minha Obra funcione com a autenticação de usuários via LDAP (Active Directory).

Pré-requisitos:

* É necessário que a integração com LDPA esteja configurado conforme documentação:
  + [https://tdn.totvs.com/pages/releaseview.action?pageId=451277985](https://tdn.totvs.com/pages/releaseview.action?pageId=451277985 "Seguir link")

## **03. SOLUÇÃO**

* No primeiro login via LDAP (off-line), caso não exista internet, o aplicativo deve avisar o usuário que para no primeiro login é necessário internet.
* Ao fazer o Login via LDAP (on-line) e a senha for válida, o aplicativo deve gravar a senha no aparelho do App Minha Obra, para que seja possível utilizar o App Minha Obra off-line nos próximos logins.
* Se utilizar LDAP e tiver on-line, sempre deve validar a senha do usuário, caso a senha seja alterada no servidor LDAP e atualizar no aparelho.
