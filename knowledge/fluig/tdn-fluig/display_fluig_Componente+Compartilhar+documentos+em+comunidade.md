---
content_hash: 331df3b1877734c6d99dbf4a57d62fe626bfa6e39b25d773b36c4200c748f524
fetched_at: '2026-06-28T21:35:29.783534+00:00'
page_id: '766954364'
product: fluig
source: tdn-fluig
title: Componente Compartilhar documentos em comunidade
type: documentation
url: https://tdn.totvs.com/display/fluig/Componente+Compartilhar+documentos+em+comunidade
version: 8
---

.\*ndice

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos da plataforma que desejam utilizar o componente **Compartilhar documentos em comunidade**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

Conhecer os conceitos dos componentes de negócio da plataforma, disponíveis na página [Componentes de negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Busca de documento em comunidade

---

O componente **Compartilhar documento em comunidade** tem como objetivo facilitar a busca e inserção de documentos em uma comunidade no Fluig plataforma, restando para o desenvolvedor somente configurar o *plugin* e utilizar o *callback* para montar sua lógica de negócio.

## Estrutura básica

---

Como pode-se notar na estrutura básica, o componente recebe basicamente dois parâmetros:

* o primeiro, um objeto ***config*** com as configurações do componente;
* e o segundo uma função ***callback*** contendo o erro e/ou o sucesso.

Veja o exemplo abaixo:

jsEclipseEstrutura básica do componente

O primeiro parâmetro espera um objeto contendo até dez atributos, onde nenhum é obrigatório:

jsEclipseParâmetro config

O segundo parâmetro espera uma função que recebe dois valores: ***error*** e ***data***. O valor data contém o objeto do arquivo/pasta selecionado.

jsEclipseParâmetro callback

## Utilização básica

---

Um exemplo da utilização básica abaixo:

jsEclipseminhawidget.js

* No arquivo [application.info](http://application.info/) de seu *widget*, adicione o componente como dependência. Como no exemplo abaixo:

bashEclipseapplication.info

**Tela exibida ao chamar o componente**
