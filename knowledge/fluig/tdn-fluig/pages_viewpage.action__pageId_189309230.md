---
content_hash: 1401f6f0f8af1d78430ded7a4d8eedc1fac822f6a1dc774692aa552c5d47c982
fetched_at: '2026-06-28T21:35:19.056456+00:00'
page_id: '189309230'
product: fluig
source: tdn-fluig
title: Componente Seleção de comunidades
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=189309230
version: 17
---

# Índice

true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos do fluig que desejam utilizar o componente **Seleção de comunidades** para recuperar a comunidade desejada e utilizá-la em seu componente ou *widget*. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

Conhecer os conceitos dos componentes de negócio do fluig, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Seleção de comunidades

---

O componente **Seleção de comunidades** tem como objetivo facilitar a etapa de seleção de uma ou mais comunidades, encapsulando todas as configurações básicas necessárias para essa operação, restando para o desenvolvedor somente configurar o *plugin* e utilizar o *callback* para montar sua lógica de negócio.

## Estrutura Básica

---

A seguir é apresentada a estrutura básica do componente:

jsEclipseEstrutura básica do componente

O componente recebe dois parâmetros:

* o primeiro, um objeto ***config*** com as configurações do componente;
* e o segundo, uma função ***callback*** contendo o erro e/ou o sucesso da seleção.

O primeiro parâmetro espera um objeto contendo dois atributos: ***multiselect***, e ***required***, sendo os dois opcionais*.*

jsEclipseParâmetro config

O segundo parâmetro espera uma função que recebe dois valores: ***error*** e ***data***.

jsEclipseParâmetro callback

## Utilização Básica

---

A utilização básica do componente é apresentada a seguir:

jsEclipseminhawidget.js

No [application.info](http://application.info/) de seu *widget*, adicione o componente como dependência:

bashEclipseapplication.info

**Tela exibida ao chamar o componente**
