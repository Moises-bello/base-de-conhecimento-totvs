---
content_hash: d8d9157b2772ee7056819d8fa4488ba8472e638f6d376c4d25d06f54005f064d
fetched_at: '2026-06-28T21:35:22.509707+00:00'
page_id: '237386447'
product: fluig
source: tdn-fluig
title: WCM - Por que meu arquivo CSS não carregou?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237386447
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Por que meu arquivo CSS não carregou?

# Solução

Da mesma forma que acontece quando o , verifique se existe a propriedade **application.resource.css.{número}={caminho/do/seu/css}**. Na atual estrutura do Studio é esperado que propriedade seja algo como o exemplo abaixo:

* **application.resource.css.1=/resources/css/minhawidget.css**

Da mesma forma que o JavaScript, verifique se os números não se repetem.
