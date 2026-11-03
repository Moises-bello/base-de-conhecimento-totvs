---
content_hash: 4270774295fdf253506390f141ebd8626d104ab8f8cfc42728553bf09a355cbd
fetched_at: '2026-06-28T21:35:18.553812+00:00'
page_id: '161352230'
product: fluig
source: tdn-fluig
title: Componente de recorte de imagem
type: documentation
url: https://tdn.totvs.com/display/fluig/Componente+de+recorte+de+imagem
version: 13
---

# Índice

true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos da plataforma que desejam utilizar o componente de **recorte de imagem**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

* Conhecer os conceitos dos componentes de negócio do TOTVS Fluig Plataforma, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Recorte de imagem

---

O componente de **recorte de imagem** tem como objetivo facilitar o processo de atualização de imagens encapsulando todas as configurações básicas necessárias para essa atualização, restando para o desenvolvedor somente configurar o *plugin* e utilizar o *callback* para montar sua lógica de negócio.

## Estrutura Básica

---

jsEclipseEstrutura básica do componente

Como pode-se notar na estrutura básica, o componente recebe basicamente dois parâmetros:

* o primeiro, um objeto ***config*** com as configurações do componente;
* e o segundo uma função ***callback*** contendo o erro e/ou o sucesso da atualização.

O primeiro parâmetro espera um objeto contendo sete atributos: ***alias***, ***title**,* ***types**, **imageShape**, **imageSrc**, **saveCallback** e **cancelCallback***, onde os parâmetros são opcionais*.*

jsEclipseParâmetro config

O segundo parâmetro espera uma função que recebe dois valores: ***error*** e ***data***.

jsEclipseParâmetro callback

## Utilização Básica

---

jsEclipseminhawidget.js

No [application.info](http://application.info) de seu *widget*, adicione o componente como dependência:

bashEclipseapplication.info

### Tela exibida ao chamar o componente
