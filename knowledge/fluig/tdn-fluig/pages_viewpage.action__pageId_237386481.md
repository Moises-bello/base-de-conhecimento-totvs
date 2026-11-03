---
content_hash: 256c20ea00797179b6127f0dfeab5564b11b30a60e4918b32d19de3d67ce3bcc
fetched_at: '2026-06-28T21:35:22.513559+00:00'
page_id: '237386481'
product: fluig
source: tdn-fluig
title: WCM - Por que meu arquivo FTL de edição não carregou?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237386481
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Por que meu arquivo FTL de edição não carregou?

# Solução

Verifique no [arquivo application.info](http://tdn.totvs.com/display/fluig/Arquivo+application.info) se existe a propriedade **edit.file={arquivo-edit.ftl}**. Na atual estrutura do Studio é esperado que propriedade seja algo como o exemplo abaixo:

* **edit.file=minhawidgetedit.ftl**
