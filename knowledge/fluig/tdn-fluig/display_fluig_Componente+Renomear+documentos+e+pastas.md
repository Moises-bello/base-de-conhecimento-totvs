---
content_hash: 4c26af10da4ab740a107c7642115a644c92ed955ee8e6d5ec825a00064211d27
fetched_at: '2026-06-28T21:35:18.549081+00:00'
page_id: '161352228'
product: fluig
source: tdn-fluig
title: Componente Renomear documentos e pastas
type: documentation
url: https://tdn.totvs.com/display/fluig/Componente+Renomear+documentos+e+pastas
version: 24
---

# Índice

true.\*ndicenone

# Objetivo

---

Este guia é destinado aos desenvolvedores internos e externos da plataforma que desejam utilizar o componente **Renomear documento**. O objetivo é apresentar o seu funcionamento e o detalhamento de todos os parâmetros de configuração.

# Pré-requisitos

---

* Conhecer os conceitos dos componentes de negócio do TOTVS Fluig Plataforma, disponíveis na página [Componentes de Negócio](http://tdn.totvs.com/pages/viewpage.action?pageId=160104507).

# Renomear documento

---

O componente **Renomear documento** tem como objetivo facilitar o processo de renomear documentos encapsulando todas as configurações básicas necessárias para essa atualização, restando para o desenvolvedor somente configurar o *plugin* e utilizar o *callback* para montar sua lógica de negócio.

## Estrutura Básica

---

jsEclipseEstrutura básica do componente

Como pode-se notar na estrutura básica, o componente recebe basicamente dois parâmetros:

* o primeiro, um objeto ***config*** com as configurações do componente;
* e o segundo uma função ***callback*** contendo o erro e/ou o sucesso da atualização.

O primeiro parâmetro espera um objeto contendo três atributos: ***id***, ***version*** e ***types***, onde ***types*** não é obrigatório e os demais sim.

jsEclipseParâmetro config

O segundo parâmetro espera uma função que recebe dois valores: ***error*** e ***data***.

jsEclipseParâmetro callback

## Utilização Básica

---

jsEclipseminhawidget.js

No [application.info](http://application.info) de seu *widget*, adicione o componente como dependência.

bashEclipseapplication.info

## Tela exibida ao chamar o componente

oculto

**Observação importante:** Liberar esses itens após a liberação do recurso. Alinhado com Anderson Graper.

Liberar essa documentação também: <https://tdn.totvs.com/x/TnTdKQ>

Estrutura Básica

---

jsEclipseEstrutura básica do componente

Como pode-se notar na estrutura básica, o componente recebe basicamente dois parâmetros:

* o primeiro, um objeto ***config*** com as configurações do componente;
* e o segundo uma função ***callback*** contendo o erro e/ou o sucesso da atualização.

O primeiro parâmetro espera um objeto contendo três atributos: ***id***, ***version*** e ***title***, onde ***title*** não é obrigatório e os demais sim.

jsEclipseParâmetro config

O segundo parâmetro espera uma função que recebe dois valores: ***error*** e ***data***.

jsEclipseParâmetro callback

Utilização Básica

---

jsEclipseminhawidget.js

No [application.info](http://application.info) de seu *widget*, adicione o componente como dependência.

bashEclipseapplication.info

Tela exibida ao chamar o componente

$("b:contains('oculto')").parent().parent().hide();
]]>
