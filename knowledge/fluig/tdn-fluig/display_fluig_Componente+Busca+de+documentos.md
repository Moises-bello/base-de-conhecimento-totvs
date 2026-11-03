---
content_hash: ab9b45811b00532aeb1d921762fa88a7ee47a7da8f67e256edcf27ad5226a36d
fetched_at: '2026-06-28T21:35:27.200659+00:00'
page_id: '505770336'
product: fluig
source: tdn-fluig
title: Componente Busca de documentos
type: documentation
url: https://tdn.totvs.com/display/fluig/Componente+Busca+de+documentos
version: 26
---

# Índice

true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos da plataforma que desejam utilizar o componente **Busca de documentos**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

Conhecer os conceitos dos componentes de negócio da plataforma, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Busca de documentos

---

O componente **Busca de documentos** tem como objetivo facilitar a busca de documentos e pastas da plataforma, restando para o desenvolvedor somente configurar o ***plugin*** e utilizar o ***callback*** para montar sua lógica de negócio.

## Estrutura Básica

---

Como pode-se notar na estrutura básica, o componente recebe basicamente dois parâmetros:

* o primeiro, um objeto ***config*** com as configurações do componente;
* e o segundo uma função ***callback*** contendo o erro e/ou o sucesso.

Veja o exemplo abaixo:

jsEclipseEstrutura básica do componente

O primeiro parâmetro espera um objeto contendo até dez atributos, onde nenhum é obrigatório:

jsEclipseParâmetro config

O parâmetro "form" deve ser passado nas opções da chamada ECMBC.searchDocument, como true ou false, para que funcione trazendo as opções antigas de busca.

jsEclipseParâmetro configTipos de documento

O tipo de documento, no campo docTypeId, segue o padrão:

1 - Pasta  
2 - Documento normal  
3 - Documento externo  
4 - Formulário  
5 - Registro de formulário  
7 - Anexo Workflow  
8 - Novo conteúdo  
9 - Aplicativo  
10 - Relatório

O segundo parâmetro espera uma função que recebe dois valores: ***error*** e ***data***. O valor data contém o objeto do arquivo/pasta selecionado.

jsEclipseParâmetro callback

## Utilização Básica

---

Um exemplo da utilização básica abaixo:

jsEclipseminhawidget.js

* No arquivo application.info de seu *widget*, adicione o componente como dependência. Como no exemplo abaixo:

bashEclipseapplication.info

**Tela exibida ao chamar o componente**
