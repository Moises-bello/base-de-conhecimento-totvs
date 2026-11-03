---
content_hash: d23fd496fd70c75729564c71991542e679847dbdacd0a324596cf718b56982d7
fetched_at: '2026-06-28T21:35:24.954723+00:00'
page_id: '272716205'
product: fluig
source: tdn-fluig
title: Identity | Por que ocorre erro de permissão ao tentar utilizar o método email
  da API REST v2?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272716205
version: 8
---

**Ocorrência**

Estou tentando utilizar o método rest/v2/users/email para obter usuários cadastrados no meu contexto do Identity através do e-mail e está dando erro de falta de permissão para usar o mesmo:

**Causa**

Este método da API REST v2 é restrito a parceiros.

**Solução**

Utilizar o método GET [/rest/v2/companies/{companyId}/users/email/{email}](https://app.fluigidentity.com/rest/swagger-ui/index.html#!/companies/getUserInCompanyByEmail_get_56).

O companyId (ID da Empresa) pode ser obtido na aba **Segurança** do menu de **Configurações** do Identity. Para saber mais, consulte o help .
