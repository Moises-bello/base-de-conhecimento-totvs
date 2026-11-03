---
content_hash: 9eaa5b07c9595235bc397c7b0f2f6f0f6eba9de93256440906e4e0411352b547
fetched_at: '2026-06-28T21:35:26.029415+00:00'
page_id: '330826453'
product: fluig
source: tdn-fluig
title: IDE - Mensagem "Usuário está desativado" ao tentar acessar a plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330826453
version: 8
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma integrado ao TOTVS Identity

**Versão:** 1.6

# Ocorrência

Ao tentar acessar a plataforma, é exibida a mensagem "Usuário está desativado". No Identity seu status está ativo.

# Causa

Esta mensagem não diz respeito ao Identity, mas à plataforma Fluig. O status do usuário no Identity está ativo, mas no Painel de controle da plataforma está *BLOCKED*. Os status dos usuários no Identity e na plataforma são independentes e não estão integrados. Um usuário pode estar desativado na plataforma e ativo no Identity, pois precisa acessar os demais aplicativos que estão integrados, mas não a plataforma especificamente.

# Solução

Acessar o Painel de Controle, opção [Usuários](http://tdn.totvs.com/pages/viewpage.action?pageId=234455411), buscar pelo usuário e reativa-lo.
