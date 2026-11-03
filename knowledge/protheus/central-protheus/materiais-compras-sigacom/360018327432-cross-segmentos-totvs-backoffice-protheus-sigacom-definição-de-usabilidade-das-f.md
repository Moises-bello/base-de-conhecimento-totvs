---
article_id: 360018327432
category: Materiais - Compras (SIGACOM)
content_hash: 0c26f5a9f70c7b0172c46eccc26689a43cb971535f1ffe2596b3c89bfba66483
fetched_at: '2026-06-28T22:41:08.776863+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Definição de usabilidade
  das funcionalidades Rejeitar, Bloquear e Estornar da rotina Liberação de Documentos
type: support-article
updated_at: '2025-09-29T18:56:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018327432-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Defini%C3%A7%C3%A3o-de-usabilidade-das-funcionalidades-Rejeitar-Bloquear-e-Estornar-da-rotina-Libera%C3%A7%C3%A3o-de-Documentos
---

**Duvida**Definição de usabilidade das funcionalidades Rejeitar, Bloquear e Estornar da rotina Liberação de Documentos  
  
**Ambiente**Protheus – Compras – A partir da versão 12.17  
  
  
**Solução**

As opções Rejeitar, Bloquear e Estornar encontram-se no menu Outras Ações da rotina Liberação de Documentos - MATA094. Segue as definições da funcionalidades:

**Rejeitar:**

A opção Rejeitar tem a funcionalidade de negar a liberação do documento, ou seja, o usuário aprovador não irá atender a solicitação de liberação. A legenda do documento bloqueado e do documento que originou o bloqueio serão alteradas para a Legenda ![](http://tdn.totvs.com/download/thumbnails/420550366/image2018-10-9_8-8-37.png?version=1&modificationDate=1539087441783&api=v2) - Status "Documento Rejeitado pelo Usuário" - indicando que o aprovador rejeitou a liberação.

**As opções de documentos disponíveis para rejeição são:**

SA - Solicitação ao Armazém (SIGAEST)

ST - Solicitação de Transferência (SIGAEST

SC - Solicitação de Compras (SIGACOM)

PC - Pedido de Compras (SIGACOM)

IP - Item de Pedido de Compras (SIGACOM)

CT - Contrato (SIGAGCT)

IC - Item Contrato (SIGAGCT)

RV - Revisão Contrato (SIGAGCT)

IR - Item Revisão Contrato (SIGAGCT)

MD - Medição Contrato (SIGAGCT)

IM - Item Medição Contrato (SIGAGCT)

**Bloquear:**

A opção Bloquear tem a funcionalidade de "pausar" o processo de liberação do documento. O registro de liberação ficará aguardando a manipulação do usuário aprovador liberar ou rejeitar o documento (Rejeição apenas para os Tipos de Documentos citados acima).

A legenda do registro de liberação será alterada para a Legenda ![](http://tdn.totvs.com/download/thumbnails/420550366/image2018-10-9_8-31-45.png?version=1&modificationDate=1539087441750&api=v2) - Status "Documento Bloqueado pelo Usuário". A legenda do documento que originou o bloqueio não será alterada.

Todos os Tipos de Documentos podem ser bloqueados desde que estejam com a Legenda ![](http://tdn.totvs.com/download/thumbnails/420550366/image2018-10-9_8-36-39.png?version=1&modificationDate=1539087441680&api=v2) - Status "Aguardando Liberação do Usuário".

**Estornar:**

A opção **Estornar**tem a funcionalidade de desfazer o processo de liberação do documento, ou seja, o registro de liberação retornará para o Status de "Aguardando Liberação do Usuário" - Legenda ![](http://tdn.totvs.com/download/thumbnails/420550366/image2018-10-9_8-36-39.png?version=1&modificationDate=1539087441680&api=v2) e em casos de mais de um nível de aprovação - Legenda ![](http://tdn.totvs.com/download/thumbnails/420550366/image2018-10-9_8-50-10.png?version=1&modificationDate=1539087441623&api=v2).

Está opção está disponível para todos os documentos que estejam com a Legenda ![](http://tdn.totvs.com/download/thumbnails/420550366/image2018-10-9_8-53-46.png?version=1&modificationDate=1539087441590&api=v2) - Status "Documento Liberado pelo Usuário", desde que não estejam atendidos (Ex. Pedido de Compras / Solicitação de Compras) ou que tenham sido faturado (Ex. Nota Fiscal).

Ao clicar em Estornar será apresentada a tela abaixo informando como ocorrerá o processo de estorno.

![](http://tdn.totvs.com/download/attachments/420550366/image2018-10-9_8-56-53.png?version=1&modificationDate=1539087441550&api=v2)

***Saiba Mais :***

[PCOM09015 - Opções Rejeitar, Bloquear e Estornar](https://tdn.totvs.com/pages/releaseview.action?pageId=420550366)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
