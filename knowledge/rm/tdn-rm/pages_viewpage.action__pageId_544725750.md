---
content_hash: 526b8905e7054871d0777b5499fe027bb0a182419dac10d18468264bc3724b68
fetched_at: '2026-06-29T00:10:38.764663+00:00'
page_id: '544725750'
product: rm
source: tdn-rm
title: LGPD - Serviços SOAP e Rest - Processo Seletivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544725750
version: 2
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Lista de dataservers com restrições**

## **01. VISÃO GERAL**

Com base na [Lei Nº 13.709/18](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm) , implementamos algumas regras de restrição a dados consumidos através de dataservers por meio dos serviços SOAP e Rest. 

Estas restrições se aplicam aos registros retornados (restrição de linha) ao consultar dados através destes serviços e implicam que um usuário só poderá ter acesso às informações que lhe pertencem, ou seja, informações que fazem referência a sua pessoa. 

Para os serviços via SOAP as restrições de aplicam aos métodos "ReadView" e "ReadRecord" e para os serviços Rest por meio da função "Get".

Estas restrições serão aplicadas aos dataservers listados abaixo (item 02) e para que o usuário tenha acesso a todas as informações do sistema através destes serviços, será necessário conceder permissão através dos perfis do sistema para cada dataserver de acordo com sua funcionalidade no menu do TOTVS Processo Seletivo.

## **02. LISTA DE DATASERVERS COM RESTRIÇÕES**

| Funcionalidade | Nome do DataServer | Item de permissão |
| --- | --- | --- |
| Usuário | EduPsUsuarioData | [02.01.06.04] Visualizar informações de 'Usuário' sem restrição por Webservice |
| Inscrição de candidato | EduPsInscricaoAreaOfertadaData | [03.01.01.03] Visualizar informações de 'Inscrição do candidato' sem restrição por Webservice |
