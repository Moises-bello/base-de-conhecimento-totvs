---
content_hash: 2b8d9f81570c0b82e6d771789931eedb89811828a1f7a2cad6b0f72b6f2dd1ef
fetched_at: '2026-06-28T21:35:22.515554+00:00'
page_id: '237386495'
product: fluig
source: tdn-fluig
title: WCM - Por que meu widget não aparece na lista para ser adicionado a uma página?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237386495
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Meu *widget* não aparece na lista para ser adicionado a uma página

# Solução

Verifique no [arquivo application.info](http://tdn.totvs.com/display/fluig/Arquivo+application.info) se existe a propriedade **application.uiwidget** e se o valor dela é *"true"*. Caso não exista, adicione-a com valor *"true"*. Se já existir e o valor for *"false"*, apenas mude-o para *"true"*.
