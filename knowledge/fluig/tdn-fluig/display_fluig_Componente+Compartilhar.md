---
content_hash: c4a97817ae62cf739d7d8a4f849aa18a98872647600f75165958e95582191651
fetched_at: '2026-06-28T21:35:18.910655+00:00'
page_id: '185751355'
product: fluig
source: tdn-fluig
title: Componente Compartilhar
type: documentation
url: https://tdn.totvs.com/display/fluig/Componente+Compartilhar
version: 20
---

# Índice

true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos da plataforma que desejam utilizar o componente **Compartilhar**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

* Conhecer os conceitos dos componentes de negócio do TOTVS Fluig Plataforma, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Compartilhar

---

O componente **Compartilhar** tem como objetivo facilitar o processo de compartilhamento de conteúdo encapsulando todas as configurações básicas necessárias para o compartilhamento, restando para o desenvolvedor somente configurar o *plugin*.

## Estrutura Básica

---

A seguir é apresentada a estrutura básica do componente:

jsEclipseEstrutura básica do componente

O componente recebe dois parâmetros:

* o primeiro, um objeto ***target*** que pode ser um objeto ou uma *string;*
* e o segundo as configurações para o componente.

O primeiro parâmetro espera um objeto ou uma *string*:

jsEclipseParâmetro config

O segundo parâmetro espera um objeto com os valores: ***showOnlyLink**, **sourceType**, **type**, **preview**, **link*** e ***paramId***.

jsEclipseParâmetro callback

## Utilização Básica

---

A utilização básica do componente é apresentada a seguir:

jsEclipseminhawidget.jsMiniatura
