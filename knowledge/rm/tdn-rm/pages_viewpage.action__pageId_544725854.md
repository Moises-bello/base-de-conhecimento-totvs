---
content_hash: eec7882a0ac2068a09bd8b03bfdf95c9edb2dddbc1856a242baf74ec132cc204
fetched_at: '2026-06-29T00:10:38.767185+00:00'
page_id: '544725854'
product: rm
source: tdn-rm
title: LGPD - Serviços SOAP e Rest - Biblioteca
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544725854
version: 1
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Lista de dataservers com restrições**

## **01. VISÃO GERAL**

Com base na [Lei Nº 13.709/18](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm) , implementamos algumas regras de restrição a dados consumidos através de dataservers por meio dos serviços SOAP e Rest. 

Estas restrições se aplicam aos registros retornados (restrição de linha) ao consultar dados através destes serviços e implicam que um usuário só poderá ter acesso às informações que lhe pertencem, ou seja, informações que fazem referência a sua pessoa. 

Para os serviços via SOAP as restrições de aplicam aos métodos "ReadView" e "ReadRecord" e para os serviços Rest por meio da função "Get".

Estas restrições serão aplicadas aos dataservers listados abaixo (item 02) e para que o usuário tenha acesso a todas as informações do sistema através destes serviços, será necessário conceder permissão através dos perfis do sistema para cada dataserver de acordo com sua funcionalidade no menu do TOTVS Gestão Bibliotecária.

## **02. LISTA DE DATASERVERS COM RESTRIÇÕES**

| Funcionalidade | Nome do DataServer | Item de permissão |
| --- | --- | --- |
| Usuários | BibUsuarioData | [02.04.01.10] Visualizar informações de 'Usuários' sem restrição por Webservice |
