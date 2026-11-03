---
content_hash: e877d286a3bcfef088346fcd3edb365fb67e764fc8c1b4a2ff72017992e6a348
fetched_at: '2026-06-28T21:35:19.877154+00:00'
page_id: '224120968'
product: fluig
source: tdn-fluig
title: Identity | Por que um usuário importado do Active Directory foi adicionado
  à lista de Rejeitados?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224120968
version: 13
---

**Dúvida**

Por que um usuário importado do Active Directory foi adicionado à lista de Rejeitados?

**Solução**

Um usuário importado do Active Directory é enviado para a lista de Rejeitados em duas situações:

1. Um dos administradores do contexto intencionalmente rejeitou o usuário a partir da lista de Pendentes.
2. O usuário foi previamente excluído do mesmo contexto em que está sendo importado.

Para provisionar um usuário nesta situação, basta aceitá-lo a partir da lista de .
