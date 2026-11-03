---
content_hash: 47055c37500a3ce489ac702b3c6ccb2c9b91200a7063a285caab633c1e8dc59b
fetched_at: '2026-06-28T21:35:19.128143+00:00'
page_id: '192091701'
product: fluig
source: tdn-fluig
title: Identity | Por que o usuário recebe um e-mail de convite mesmo quando seleciono
  a opção Senha Temporária durante a criação?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=192091701
version: 14
---

**Dúvida**

Por que o usuário recebe um e-mail de convite mesmo quando seleciono a opção Senha Temporária durante a criação?

**Solução**

Este tipo de situação ocorre quando o usuário que foi adicionado já estava cadastrado em outra empresa do Identity com o mesmo e-mail. Nesse caso, mesmo selecionando a opção de ativação por senha temporária, o e-mail de convite será enviado.

Ao receber o e-mail de convite, o recomendado é que usuário faça a autenticação utilizando a senha pessoal (ou seja, a senha própria do Identity):

1. Acessar o Identity através do *link* enviado na mensagem de e-mail.
2. Informar a senha pessoal para acessar o Identity.

A conta do usuário será vinculada a ambas as empresas e ele poderá alternar entre elas utilizando o menu localizado no canto superior direito, conforme explicado na documentação de .

Atenção

Caso o administrador do novo contexto permita a autenticação utilizando a senha do Active Directory, e esta seja informada pelo usuário, a conta será vinculada a ambas as empresas, mas ele não poderá fazer a troca de contextos pelo menu, apenas pela URL.
