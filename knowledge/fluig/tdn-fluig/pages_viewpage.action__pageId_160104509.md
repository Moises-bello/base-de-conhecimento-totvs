---
content_hash: df8b342189c1cf93f5cbc803cd57060c9f6a6f4efbf9ffe04fee8da40113ed77
fetched_at: '2026-06-28T21:35:18.283903+00:00'
page_id: '160104509'
product: fluig
source: tdn-fluig
title: Componente Atualizar Arquivo Físico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=160104509
version: 24
---

# Índice

true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos do TOTVS Fluig Plataforma que desejam utilizar o componente **Atualizar arquivo físico**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

Conhecer os conceitos dos componentes de negócio da plataforma, disponíveis na página .

# Atualizar arquivo físico

---

O componente **Atualizar arquivo físico** tem como objetivo facilitar o processo de atualização de arquivos encapsulando todas as configurações básicas necessárias para essa atualização, restando para o desenvolvedor somente configurar o *plugin* e utilizar o *callback* para montar sua lógica de negócio.

## Estrutura Básica

---

jsEclipseEstrutura básica do componente

Como pode-se notar na estrutura básica, o componente recebe basicamente dois parâmetros, o primeiro, um objeto ***config*** com as configurações do componente e o segundo uma função ***callback*** contendo o erro e/ou o sucesso da atualização.

O primeiro parâmetro espera um objeto contendo três atributos: ***id***, ***version*** e ***types***, onde ***types*** não é obrigatório e os demais sim.

jsEclipseParâmetro config

O segundo parâmetro espera uma função que recebe dois valores: ***error*** e ***data***.

jsEclipseParâmetro callback

## Utilização Básica

---

jsEclipseminhawidget.js

No application.info de seu widget, adicione o componente como dependência:

bashEclipseapplication.info

### 1 - Tela exibida ao chamar o componente

### 2 - Tela exibida ao selecionar um arquivo para atualização

### 3 - Tela exibida quando o id do documento pertence a uma pasta
