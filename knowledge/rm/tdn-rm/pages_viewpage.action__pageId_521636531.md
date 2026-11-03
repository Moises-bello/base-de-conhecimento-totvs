---
content_hash: ecf0cf5d6176d57fa47c885857042d0d1afcb7a8a266d7e6322f8fe2895771ba
fetched_at: '2026-06-29T00:10:31.299796+00:00'
page_id: '521636531'
product: rm
source: tdn-rm
title: FISCAL01-10383 DT - R-2099 Fechamento dos Eventos Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521636531
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Processo de Transmissão de Eventos da EFD-REINF R-2099 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10383 |

## **02. SITUAÇÃO/REQUISITO**

Ao final do período é necessário executar o fechamento do mesmo junto a RFB através do evento R-2099. 

Deverá ser criado um processo com nome "R-2099 Fechamento dos Eventos Periódicos" de controle do Evento R-5011 que será disponibilizado somente na lista de processos da visão do R-5011. Este processo será integrado com o TSS já no momento de sua inclusão. Ao ser executado com sucesso o status do Evento R-5011 deve ser alterado para Pendente. Durante a consulta do R-2099 se o mesmo for rejeitado o R-5011 voltará para o status de "Aberto" e se for autorizado o status será alterado para "Encerrado".

## **03. SOLUÇÃO**

Foi implementado o Evento R-2099 Fechamentos dos Eventos Periódicos. Este está disponível na lista de processos do Evento R-5011 e poderá ser executado somente para Eventos com Status Aberto.

Todas as execuções deste processo serão registradas no histórico do Evento R-2099 e as alterações de status do R-5011 serão registradas no histórico deste.

## **04. DEMAIS INFORMAÇÕES**

Quando houver um Evento Inconsistente ou Rejeitado o sistema irá reenviar este eventos com um novo XML e um novo Id. da Reinf devido a validação abaixo  
*"Código MS0037: Já existe na base de dados do Ambiente Nacional um evento com mesma identificação."*

A TAG compSemMovto não será gerada conforme a validação abaixo  
*"Código MS1217: tag compSemMovto não pode ser informada se o período de apuração é maior ou igual a 2018-11."*

A TAG evtPgtos não será gerada conforme a validação abaixo  
*"Validação: Só preencher este campo se {perApur} <= [2018-10]"*

## **05. ASSUNTOS RELACIONADOS**

* Especificação de Requisito:

div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
