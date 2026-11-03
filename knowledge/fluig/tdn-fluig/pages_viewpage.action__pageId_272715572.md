---
content_hash: b88a49f3d7b2f6d4c0de9009635db8757ef6cfe1fd537b19a6ea112d369324b2
fetched_at: '2026-06-28T21:35:24.952588+00:00'
page_id: '272715572'
product: fluig
source: tdn-fluig
title: WCM - Por que o erro "403 Forbidden" é exibido ao consultar a API do Fluig
  em widgets de páginas públicas?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272715572
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Erro "403 forbidden" ao consultar API REST do Fluig em widgets de páginas públicas, ou seja, sem usuário autenticado.

# Causa

Ao fazer uma requisição REST é necessário passar a URL completa do servidor no parâmetro URL da requisição.

# Solução

Concatenar a URL do servidor com a URL da API REST que deseja consumir.

jsExemplo
