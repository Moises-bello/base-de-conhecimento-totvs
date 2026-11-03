---
content_hash: 45daad778ef5f33fe0503c2b009e3e21a6453c2b927fafc6a981a3f5c6ced8bb
fetched_at: '2026-06-28T21:35:22.724886+00:00'
page_id: '239026841'
product: fluig
source: tdn-fluig
title: BPM 038 - Como faço para utilizar somente o último complemento de uma atividade?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=239026841
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

**Versão:** 1.5.X

# Ocorrência

Gostaríamos de usar somente a última observação (complemento) da atividade com o campo WKUserComment. Isto funciona na versão 1.4. Na versão 1.5 está aparecendo mais de um complemento.

# Causa

Foi alterado o comportamento.

# Solução

Esse é o real comportamento do produto. Houveram mudanças com a parte de complementos e todo histórico é retornado ao movimentar uma atividade, porém existe um desenvolvimento sobre a plataforma em que é executado um filtro trazendo somente o último complemento:

js
