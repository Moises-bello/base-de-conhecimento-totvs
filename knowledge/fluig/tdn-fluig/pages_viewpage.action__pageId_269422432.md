---
content_hash: d0f988e1862490fcf922a28ab692901c50af2db689fef872050bfb7ca08589e2
fetched_at: '2026-06-28T21:35:24.409835+00:00'
page_id: '269422432'
product: fluig
source: tdn-fluig
title: ARQ - Por que ao tentar logar na plataforma, utilizando autenticação integrada,
  é apresentada tela em branco?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269422432
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Por que ao tentar logar na plataforma, utilizando  (sem TOTVS Identity), é apresentada tela em branco?

# Causa

Esse erro normalmente é ocasionado pela fato de algum campo no cadastro do usuário no AD (Active Directory) não estar preenchido.

# Solução

Deve-se verificar as seguintes informações: *username, firstname, lastname*e *e-mail* e preencher os campos que estiverem vazios no Active Directory.
