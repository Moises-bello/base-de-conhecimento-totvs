---
content_hash: a6b300a2d5c7dfe653aa0f20103e590fcf73206e028746202c7500fe05bc4ac4
fetched_at: '2026-06-28T21:35:18.893513+00:00'
page_id: '185748563'
product: fluig
source: tdn-fluig
title: Criar uma biblioteca personalizada
type: documentation
url: https://tdn.totvs.com/display/fluig/Criar+uma+biblioteca+personalizada
version: 14
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar as ações necessárias para a criação de uma biblioteca personalizada.

# Visão Geral

Uma biblioteca personalizada é um arquivo com *snippets* de códigos que podem ser reaproveitados na criação de *layouts*. A  é parte integrante da plataforma, porém, existe a possibilidade do desenvolvedor criar a sua própria biblioteca.

# Como criar a biblioteca?

Para criar a própria biblioteca, é necessário efetuar os seguintes passos:

11Passo 1Passo 1

* Acessar a pasta de *templates* que fica localizada em [Instalação do fluig]/repository/wcmdir/templates.

2Passo 2Passo 2

* Dentro da pasta templates, criar um arquivo com a extensão ftl. Por exemplo: "custom.ftl".

O arquivo da biblioteca pode conter vários *snippets* de código.

# Como criar *snippets* novos?

Para criar *snippets* novos é necessário inserir uma macro nova no arquivo ftl da biblioteca, conforme mostrado a seguir:

xml


 
<#macro helloWorld>

# Hello world!

]]>

## *Snippet* com parâmetros

Abaixo segue um exemplo de *snippet* que utiliza um parâmetro:

# ${param1}!

 ]]>

# Como utilizar a biblioteca?

A importação da biblioteca personalizada segue o mesmo exemplo da importação da .

No *layout*, inserir o seguinte código:

]]>

Após importar, a utilização é similar ao da Biblioteca WCM.

 
<@wcm.helloWorld/>
<@wcm.funcao param1="Exemplo de importação da biblioteca customizada"/>]]>

# Material para referência

Para mais informações sobre como criar *snippets* de código, acessar a [documentação do FreeMarker](http://freemarker.org/docs/dgui_misc_userdefdir.html) e/ou utilizar o código abaixo como exemplo:

xmlAbrir Exemplotrue

<#list (pageRender.getInstancesIds("SlotChat"))! as id>
${pageRender.renderInstanceNoDecorator(id)}

<#macro header public="false">

[<#if '${imageLogo}'=='true'>
![](${serverContextURL}/resources/images/${pageRender.user.tenantId}/logo_image.png)
<#else>
![](${serverContextURL}/resources/images/logo.png)](home "${i18n.getTranslation('layout.label.pagetitle')}")

<#if "${public}" == "false">

<#list (pageRender.getInstancesIds("SlotInstantSearch"))! as id>
${pageRender.renderInstanceNoDecorator(id)}

<#list (pageRender.getInstancesIds("SlotGlobalAlert"))! as id>
${pageRender.renderInstanceNoDecorator(id)}



<#list (pageRender.getInstancesIds("SlotLogin"))! as id>
${pageRender.renderInstanceNoDecorator(id)}

<#macro menu>
<#macro renderSlot id decorator="false" editableSlot="false" class=" ">
<#assign slot = id>
<#assign computedClass = class>
<#if editableSlot == "true">
<#assign computedClass = computedClass + " slotint sortable">

<#list (pageRender.getInstancesIds(slot))! as id>
${pageRender.renderInstanceNoDecorator(id)}

<#nested>
<#macro footer layoutuserlabel>

<#if pageRender.isUserLogged() >
<#if "${wcmVersionInfo.getStatus()}" == "1">

![](${contextPath}/resources/images/icon_toast_alert.png)

${i18n.getTranslation('warninVersion.user.title')}

${i18n.getTranslation('warninVersion.user1')}

<#elseif "${wcmVersionInfo.getStatus()}" == "2">

![](${contextPath}/resources/images/icon_toast_alert.png)

${i18n.getTranslation('warninVersion.user.title')}

${i18n.getTranslationP1('warninVersion.user2', wcmVersionInfo.getStatusInfo())}

<#elseif "${wcmVersionInfo.getStatus()}" == "3">

![](${contextPath}/resources/images/icon_toast_erro.png)

${i18n.getTranslation('warninVersion.user.title')}

${i18n.getTranslation('warninVersion.user3')}


${wcmVersionInfo.getVersionName()}
${wcmVersionInfo.getVersionBuild()}
- ${i18n.getTranslation('${layoutuserlabel}')}: ${user.fullName}


<#list (pageRender.getInstancesIds("SlotUsePolicy"))! as id>
${pageRender.renderInstanceNoDecorator(id)}

<#nested>
 ]]>
