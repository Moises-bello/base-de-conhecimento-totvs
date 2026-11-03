---
content_hash: 99bd49a704b0e93ec4acfa67f32f98de6bce5d01576513b4b3db30822aff8964
fetched_at: '2026-06-28T21:35:18.808063+00:00'
page_id: '185739196'
product: fluig
source: tdn-fluig
title: Modo de visualização vs. modo de edição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185739196
version: 13
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar as características dos modos de visualização e edição de *widgets*.

# Modo de visualização vs. modo de edição

No que poderíamos chamar de "camada de apresentação" de um *widget* (ou seja, as telas), existe a concepção inicial de que ela é formada por dois arquivos FreeMarker (.ftl): um para visualização e outro para edição. Geralmente esta estrutura é composta por um único arquivo JavaScript (.js). A seguir, veremos cada um dos componentes.

## Modo de Visualização

Por padrão, o renderizador de páginas da plataforma Fluig seleciona o arquivo "view.ftl" dentro do *widget* para a renderização do modo de visualização. Caso o desenvolvedor deseje especificar um outro arquivo .ftl como padrão para o modo de visualização, é necessário informá-lo na propriedade [view.file](http://tdn.totvs.com/display/fluig/Arquivo+application.info#Arquivoapplication.info-view.file) no arquivo [application.info](http://tdn.totvs.com/display/fluig/Arquivo+application.info). Por exemplo:

text

## Modo de Edição

Por padrão, o renderizador de páginas da plataforma Fluig seleciona o arquivo "edit.ftl" dentro do *widget* para a renderização do modo de edição. Caso o desenvolvedor deseje especificar um outro arquivo .ftl como padrão para o modo de edição, é necessário informá-lo na propriedade [edit.file](http://tdn.totvs.com/display/fluig/Arquivo+application.info#Arquivoapplication.info-edit.file) no arquivo [application.info](http://tdn.totvs.com/display/fluig/Arquivo+application.info). Por exemplo:

textImportante

Caso não exista uma propriedade [edit.file](http://tdn.totvs.com/display/fluig/Arquivo+application.info#Arquivoapplication.info-edit.file) no application.info e nem um arquivo "edit.ftl" na estrutura do *widget*, o renderizador entenderá que esse *widget* não possui modo de edição.

# Variáveis de ambiente FTL & JS

Quando é utilizada a extensão de [Super Widget](http://style.fluig.com/javascript.html#super-widget) em um arquivo **\*.js** (JavaScript), existe uma função herdada chamada *"*isEditMode". Veja o exemplo abaixo:

js

Já no arquivo **\*.ftl** (FreeMarker), pode-se usar o seguinte código:

xml
 
<#if pageRender.isEditMode()=true>
<#else>
