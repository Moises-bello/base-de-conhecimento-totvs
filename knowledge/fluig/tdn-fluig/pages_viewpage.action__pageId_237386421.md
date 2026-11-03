---
content_hash: 8847a1ff486e397cc5f05f48913be54d888184c7feddfe0b7b61426efd8695ae
fetched_at: '2026-06-28T21:35:22.507666+00:00'
page_id: '237386421'
product: fluig
source: tdn-fluig
title: WCM - Por que meu arquivo Javascript não carregou?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237386421
version: 11
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Por que meu arquivo Javascript não carregou?

# Solução

Verifique no [arquivo application.info](http://tdn.totvs.com/display/fluig/Arquivo+application.info) se existe a propriedade **application.resource.js.{número}={caminho/do/seu/javascript}**. Veja abaixo um exemplo dessa propriedade, tomando como base a atual estrutura criada pelo Studio:

* **application.resource.js.1=/resources/js/minhawidget.js**

Note que propriedades do tipo "application.resource.\*" não podem repetir o número. O [application.info](http://tdn.totvs.com/display/fluig/Arquivo+application.info) **não pode conter**, por exemplo, as propriedades:

* application.resource.js**.1**=...
* application.resource.css**.1**=...

O **correto** é:

* application.resource.js**.1**=...
* application.resource.css**.2**=...
