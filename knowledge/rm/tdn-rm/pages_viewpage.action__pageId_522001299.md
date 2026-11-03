---
content_hash: 7c3c0e00f15fdb81c5d601b7d081dee8dd36bf86aa237e70b2c5cb28ea8c935a
fetched_at: '2026-06-29T00:10:31.721957+00:00'
page_id: '522001299'
product: rm
source: tdn-rm
title: FISCAL01-10382 DT - R-2098 Reabertura dos Eventos Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=522001299
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Processo de Transmissão e Consulta de Eventos da EFD-REINF R-2098 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10382  FISCAL01-11542 |

## **02. SITUAÇÃO/REQUISITO**

Conforme necessário o período da EFD-REINF poderá ser reaberto através do Evento R-2098

Transmissão

Deverá ser criado um processo com nome "R-2098 Reabertura dos Eventos Periódicos" de controle do Evento R-5011 que será disponibilizado somente na lista de processos da visão do R-5011. Este processo será integrado com o TSS já no momento de sua inclusão.

Consulta

Se o Evento R-2098 for autorizado com sucesso o status do R-5011 deverá ser alterado para Aberto e os dados de encerramento do R-5011 devem ser apagados sendo necessário executar novamente o encerramento em outro momento.

## **03. SOLUÇÃO**

Foi implementado o Evento R-2098 Reabertura dos Eventos Periódicos.

Transmissão

A transmissão deste Evento está disponível na lista de processos do Evento R-5011 com o nome "R-2098 Reabertura dos Eventos Periódicos" e poderá ser executado somente para Eventos com Status Encerrado.

Durante a transmissão podem ocorrer as seguintes situações:

* Erro de validação do Status do Evento: Este caso ocorrerá sempre que o processo for executado para um Evento com o status diferente de Encerrado. Neste caso o processo apresentará um log de erro e nada será salvo;
* Erro na conexão com o TSS: Este caso ocorrerá sempre que por motivo qualquer o TSS não esteja preparado para receber a conexão com o RM. Neste caso o processo apresentará um log de erro e nada será salvo;
* R-2098 Enviado com sucesso: Este caso ocorrerá quando o RM enviar ao TSS o Evento R-2098 com sucesso. Neste caso o R-2098 será salvo com o status Pendente e o R-5011 será alterado para Pendente.
* R-2098 Com erro de schema: Este caso ocorrerá quando ao Enviar o Evento ao TSS o mesmo apresentar erros de validação no schema xml do Evento. Neste caso o Evento R-2098 será salvo como inconsistente e nenhuma alteração ocorrerá no Evento R-5011;

Consulta

Já a consulta deverá ser realizada selecionando o próprio Evento R-2098, no Anexo de Eventos do R-5011, e então executando o processo "*Consultar Evento*".

Durante a consulta do Evento R-2098 podem ocorrer as seguintes situações:

* Erro de validação do Status do Evento: Este caso ocorrerá sempre que o processo for executado para um Evento com o status diferente de Pendente. Neste caso o processo apresentará um log de erro e nada será salvo;
* Erro na conexão com o TSS: Este caso ocorrerá sempre que por motivo qualquer o TSS não esteja preparado para receber a conexão com o RM. Neste caso o processo apresentará um log de erro e nada será salvo;
* R-2098 Autorizado: Este caso ocorre quando através da consulta o TSS retornar para o RM o campo Status com o valor **6**. Neste caso o R-2098 será salvo com status autorizado e o Evento R-5011 será alterado para Aberto sendo que os campos "*Data da Última Transmissão*", "*Recibo de Entrega*", "*Xml de Envio*" e "*Xml de Retorno*" serão limpos;
* R-2098 Pendente: Este caso ocorre quando através da consulta o TSS retornar para o RM o campo Status com o valor **1, 2** ou **4**. Neste caso nenhuma alteração ocorrerá nos Eventos.
* R-2098 Rejeitado: Este caso ocorre quando através da consulta o TSS retornar para o RM o campo Status com o valor **5**. Neste caso o R-2098 será salvo com status rejeitado e o Evento R-5011 será alterado para Encerrado e nenhum outro campo será alterado.

Em todas as execuções deste processo serão registradas no histórico do Evento R-2098 e as alterações de status do R-5011 serão registradas no histórico deste.

## **04. DEMAIS INFORMAÇÕES**

Quando houver um Evento Inconsistente ou Rejeitado o sistema irá reenviar este eventos com um novo XML e um novo Id. da Reinf devido a validação abaixo  
*"Código MS0037: Já existe na base de dados do Ambiente Nacional um evento com mesma identificação."*

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
