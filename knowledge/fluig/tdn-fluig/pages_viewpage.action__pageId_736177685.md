---
content_hash: b42914912f2ed458734d36bc49c3c1c183389cf190d01dfdc286a4366719b082
fetched_at: '2026-06-28T21:35:29.082520+00:00'
page_id: '736177685'
product: fluig
source: tdn-fluig
title: Componente de visualização de artigos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=736177685
version: 1
---

# Índice

true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos da plataforma que desejam utilizar o componente de **visualização de artigos**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

* Conhecer os conceitos dos componentes de negócio do TOTVS Fluig Plataforma, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Visualização de artigos

---

O componente de **visualização de artigos** tem como objetivo facilitar o processo de visualização de artigos encapsulando todas as configurações básicas necessárias para essa visualização, restando para o desenvolvedor somente configurar o *plugin* e utilizar o *callback* para montar sua lógica de negócio.

## Estrutura Básica

---

jsEclipseEstrutura básica do componente

Como pode-se notar na estrutura básica, o componente recebe basicamente dois parâmetros:

* o primeiro, um objeto ***config*** com as configurações do componente;
* e o segundo uma função ***callback*** contendo o erro e/ou o sucesso da atualização.

O primeiro parâmetro espera um objeto contendo sete atributos: **articleId, alias, version, title, instanceId**, onde os parâmetros são opcionais*.*

jsEclipseParâmetro config

O segundo parâmetro espera uma função que recebe dois valores: ***error*** e ***data***.

jsEclipseParâmetro callback

## Utilização Básica

---

jsEclipseminhawidget.js

No [application.info](http://application.info) de seu *widget*, adicione o componente como dependência:

bashEclipseapplication.info

### Tela exibida ao chamar o componente
