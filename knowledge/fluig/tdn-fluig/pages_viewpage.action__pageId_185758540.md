---
content_hash: 05eb304bdce8e40f0fd50ea11d4bd2228bc35264df2f05d9287007bf27428a6d
fetched_at: '2026-06-28T21:35:18.959306+00:00'
page_id: '185758540'
product: fluig
source: tdn-fluig
title: Componente Resposta de formulário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185758540
version: 8
---

# Índice

true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos da plataforma que desejam utilizar o componente **Resposta de formulário**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

Conhecer os conceitos dos componentes de negócio do TOTVS Fluig Plataforma, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Resposta de formulário

---

O componente **Resposta de formulário** tem como objetivo facilitar o processo de resposta de formulário, encapsulando todas as configurações básicas necessárias para a resposta de formulário e permitindo sua resposta em qualquer parte da plataforma sem perder a navegação atual, restando para o desenvolvedor somente configurar o *plugin*.

## Estrutura Básica

---

A seguir é apresentada a estrutura básica do componente:

jsEclipseEstrutura básica do componente

O componente recebe um parâmetro, o id do formulário no ECM.

O parâmetro espera uma *string*.

jsEclipseParâmetro config

## Utilização Básica

---

A utilização básica do componente é apresentada a seguir:

jsEclipseminhawidget.js

No [application.info](http://application.info) de seu *widget*, adicione o componente como dependência:

bashEclipseapplication.info

**Tela exibida ao chamar o componente**
