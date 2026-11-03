---
content_hash: 8f55f1cdf5ab2d53525425e020e9d992642c0d884f794044569965a482d6a472
fetched_at: '2026-06-28T21:35:18.914881+00:00'
page_id: '185751362'
product: fluig
source: tdn-fluig
title: Componente Listar compartilhamentos
type: documentation
url: https://tdn.totvs.com/display/fluig/Componente+Listar+compartilhamentos
version: 10
---

# Índice

# true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos da plataforma que desejam utilizar o componente **Listar compartilhamentos**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

* Conhecer os conceitos dos componentes de negócio do TOTVS Fluig Plataforma, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Listar compartilhamentos

---

O componente **Listar compartilhamentos** tem como objetivo facilitar o processo de listagem de compartilhamentos de um conteúdo encapsulando todas as configurações básicas necessárias, restando para o desenvolvedor somente configurar o *plugin* e utilizar o *callback* para montar sua lógica de negócio.

## Estrutura Básica

---

A seguir é apresentada a estrutura básica do componente:

jsEclipseEstrutura básica do componente

O componente recebe dois parâmetros:

* o primeiro, um objeto ***config*** com as configurações do componente;
* e o segundo uma função ***callback*** contendo o erro e/ou o sucesso da listagem.

O primeiro parâmetro espera um objeto contendo três atributos: ***sociableId**, **title** e **instanceId**,* onde ***sociableId*** é o único obrigatório.

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
