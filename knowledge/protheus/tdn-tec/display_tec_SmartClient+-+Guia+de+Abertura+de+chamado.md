---
content_hash: 80f62e9320e469f4c4c858b9f460c8be9ca6c6374b21750a3ad35be39ace5ed3
fetched_at: '2026-07-02T19:24:25.731379+00:00'
page_id: '505759808'
product: protheus
source: tdn-tec
title: SmartClient - Guia de Abertura de chamado
type: documentation
url: https://tdn.totvs.com/display/tec/SmartClient+-+Guia+de+Abertura+de+chamado
version: 38
---

Guia de Abertura de chamado

Guia de abertura de issues no Jira para atendimento do time de Tecnologia Clients, no projeto TOTVS | Platform - Clients.

Abaixo são descritos o padrão, os requisitos e informações necessários por tipo de Issue:

FieldTab,nFeedFieldTab,nFeedyesFieldTabManutenção,Melhoria,Apoio,Documentação,Teste SistêmicoManutenção,Melhoria,Apoio,Documentação,Teste SistêmicoyesManutenção

Para abertura de chamados manutenção é obrigatório seguir o Guia abaixo. Caso exista a falta de alguns dos itens a Issue ira retornar para Atendimento.

**Guia de Abertura de manutenção:**

* Resumo (Summary) :

  ---
* Descrição (Description) :

  1. Para recuperar as versões de Smartclient utilize o [parâmetro de linha](http://tdn.totvs.com.br/pages/viewpage.action?pageId=6066051) "SmartClient -t".
  2. Para descobrir a versão AppServer e da Lib do Framework utilize as teclas [Shift +F6](http://tdn.totvs.com.br/pages/viewpage.action?pageId=440840402), dentro de Protheus.
  3. Para recuperar a versão do SmartClient HTML, acesse a página de Parâmetros Iniciais e verifique no canto inferior direito.

* ---

* Componente (Component/s) :  

  ---
* Anexos (Attachment) :

Conteúdo dos anexos

console.log: Geração do [console.log](http://tdn.totvs.com.br/display/tecen/ConsoleLog) com o [Ativação do logMessages](http://tdn.totvs.com.br/display/tecen/Section+%5Bgeneral%5D%2C+key+logMessages).

evidencia.pm4: Gravação de um vídeo com o procedimento para reproduzir o problema. Necessário evidencia do local dos clicks .

evidencia.doc: Evidencia com o processo para reproduzir o problema, de preferencia sem a camada de negocio.

error.log: Copiar o conte udo do error.log em um arquivo.

cppModelo de POCnoMelhoria

Para abertura de chamados melhoria é obrigatório seguir o Guia abaixo. Caso exista a falta de alguns dos itens a Issue ira retornar para Atendimento.

Requisitos de RoadMap

* Para solicitações internas de Segmento: Existência de RoadMap de produto com a necessidade da melhoria.
* Para solicitações de Clientes: Existência de no minimo 1 ticket de cliente, associado ou vinculada direto a issue.

**Guia de Abertura de melhoria:**

* Resumo (Summary) :

  ---
* Descrição (Description) :

  ---
* Componente (Component/s) :  

  ---

* Anexos (Attachment) :

Especificação.doc: Especificação da sugestão de melhoria com Prints.

POC.prw:

cppModelo de POCnoApoionoTeste SistêmiconoDocumnetaçãononFeedDevolução para Atendimento

As issues que não atenderem o padrão descrito neste guia serão rejeitadas para atendimento.

20/04/2017
