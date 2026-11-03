---
content_hash: e73271087258071896b7a7c157209c74fd2094f70456d3f77828e60873071367
fetched_at: '2026-06-28T21:35:27.432733+00:00'
page_id: '549487213'
product: fluig
source: tdn-fluig
title: Abrir documentos a partir de widgets mobile
type: documentation
url: https://tdn.totvs.com/display/fluig/Abrir+documentos+a+partir+de+widgets+mobile
version: 6
---

# Índice

4true.\*ndicenone

## Objetivo

Este guia tem por objetivo auxiliar usuários que queiram abrir documentos no mobile por meio de widgets utilizando uma chamada para a função "JSInterface.openDocument".

A partir da versão **1.16.16 do IOS** e da versão **1.6.5.28 do Android** é possível abrir documentos via widgets nos aplicativos Fluig Mobile. Veja o passo a passo abaixo.

## Abrir documentos via widgets mobile

---

Para abrirmos documentos via widgets, basta acrescentarmos uma chamada para a função **JSInterface.openDocument** passando como parâmetro e código do documento no GED, além disso é possível também passarmos o título que será utilizado na janela do documento. Como no exemplo abaixo:

sample1Passo 1

Será preciso checar se está no mobile realmente.

2Passo 2

Ao adicionar esta chamada os documentos no Fluig mobile serão abertos via widgets.
