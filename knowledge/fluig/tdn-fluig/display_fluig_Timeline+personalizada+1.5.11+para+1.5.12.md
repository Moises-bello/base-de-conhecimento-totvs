---
content_hash: f8fc0579ace9f715d537ad686aa5f1858bd66305685c53f24291eaea21e66cec
fetched_at: '2026-06-28T21:35:23.919240+00:00'
page_id: '267798804'
product: fluig
source: tdn-fluig
title: Timeline personalizada 1.5.11 para 1.5.12
type: documentation
url: https://tdn.totvs.com/display/fluig/Timeline+personalizada+1.5.11+para+1.5.12
version: 4
---

# Índice

true.\*ndicenone

# Objetivo

Este guia é destinado aos desenvolvedores internos e externos do fluig. O objetivo é identificar e mapear todas as diferenças da *Timeline* personalizada entre as versões 1.5.11 e 1.5.12.

Dica

Sugerimos que ao seguir este guia seja utilizado um programa de comparação (diff), que permita visualizar as diferenças entre as versões.

# application.info

Na versão 1.5.12 não foi realizada nenhuma modificação nesse arquivo.

# view.ftl

Nas linhas,

42: SUBSTITUIR o conteúdo da linha 42 por:

xml

]]>

80: ADICIONAR o conteúdo:

xml -
{{/editionDate}}
{{^editionDate}}{{/editionDate}}]]>

91: SUBSTITUIR o conteúdo da linha 91 por:

xml{{{text}}}]]>

100: ADICIONAR o conteúdo:

xml

{{/allowsEditActions}}
