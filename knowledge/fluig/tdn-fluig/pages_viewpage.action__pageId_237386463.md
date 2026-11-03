---
content_hash: e021d502d89d72621d70d478fdcf867779cdcef5f37c96624f1a3dab9a9a74ce
fetched_at: '2026-06-28T21:35:22.511555+00:00'
page_id: '237386463'
product: fluig
source: tdn-fluig
title: WCM - Por que meu arquivo FTL de visualização não carregou?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237386463
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Por que meu arquivo FTL de visualização não carregou?

# Solução

Verifique no [arquivo application.info](http://tdn.totvs.com/display/fluig/Arquivo+application.info) se existe a propriedade **view.file={arquivo-view.ftl}**. Na atual estrutura do Studio é esperado que propriedade seja algo como o exemplo abaixo:

* **view.file=minhawidget.ftl**
