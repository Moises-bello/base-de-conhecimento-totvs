---
content_hash: 37d1211c2ab5bff6327f7e4c81c15405c02833eeb1b663759dabc38923aa1aca
fetched_at: '2026-06-28T21:35:23.884295+00:00'
page_id: '267788725'
product: fluig
source: tdn-fluig
title: IDE - Por que novos usuários não são provisionados na plataforma?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267788725
version: 10
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma integrado ao TOTVS Identity

# Ocorrência

Após logar no Identity, os novos usuários tentam usar o aplicativo Fluig, porém recebem a mensagem de que o acesso não é permitido. O que fazer para corrigir esta situação?

# Causa

A opção **Provisionamento "Just in Time"**do cadastro da empresa está desabilitada. Esta opção realiza a criação automática dos usuários no momento do primeiro acesso a partir do aplicativo Fluig do Identity.

# Solução

Para habilitar o provisionamento, seguir as instruções abaixo:

**01.** Acessar a plataforma com o usuário wcmadmin (http://[endereço\_fluig]:[porta]/wcmadmin).

**02.** Editar o cadastro da empresa com a qual o Identity está integrado (**Painel de Controle → WCM → Empresas**).

**03.** Na aba **Autenticação**, marcar a opção **Provisionamento "Just in Time"**.

**04.** Acionar **Salvar**.

Após a alteração, fazer um novo teste de acesso com um dos usuários afetados.

Atenção!

Cada usuário vinculado ao Identity será criado automaticamente na plataforma após autenticar-se pela primeira vez.
