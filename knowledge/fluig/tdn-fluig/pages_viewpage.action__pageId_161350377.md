---
content_hash: de59caef250fec483b729984537095bf21d2ac72d69891babc6363f233840ced
fetched_at: '2026-06-28T21:35:18.522070+00:00'
page_id: '161350377'
product: fluig
source: tdn-fluig
title: Atualização 1.3.7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=161350377
version: 54
---

Confira abaixo as novidades na atualização 1.3.7 do Fluig:

# BPM

**************Processos com mais rastreabilidade**************

As informações das solicitações estão mais completas. No histórico de solicitações, dentro da consulta da solicitação, é possível saber o que aconteceu nos subprocessos e se possui alguma observação.

**************Novo componente BPMN 2.0 - Tarefa de Usuário**************

Agora seus diagramas estão mais ricos, defina claramente que atividades serão executadas por pessoas (*user tasks*) usando o padrão definido na notação BPMN.

**************Movimentação de processos com mais integridade**************

Foi aprimorada a movimentação de processos para garantir a integridade do fluxo e das informações referentes a eles. Agora não é permitido enviar o fluxo diretamente de um *fork* para um *join*.

**************Utilização de *datasets* aperfeiçoada e mais íntegra**************

A  utilização de *datasets* está mais eficiente a partir dessa atualização:

* a consulta está mais íntegra quando são utilizadas *constraints* no SQL *Server;*
* *zoom* de *datasets* internos está mais completo.

**************Retorno de datas mais preciso em formulários**************

Foram aprimoradas as regras de formatação de data, tornando-as mais precisas nos retornos em formulários.

**************Movimentação em blocos melhorada**************

A movimentação de solicitações em blocos quando elas possuem formulários ou validações está mais eficiente.

**************Encontrar tarefas está mais rápido**************

A busca de tarefas está mais ágil. Agora o Fluig permite alternar a visualização entre as tarefas em *pool* na central de tarefas, proporcionando mais agilidade para encontrá-las.

******************Mais precisão no *dataset* de anexos******************

Fizemos com que o *dataset* de anexos *"processAttachment*" apresente em qual movimentação da tarefa foi incluído anexo em processos que possuem fluxo de retorno.

NotaInformações adicionais podem ser obtidas em Customização de *Datasets*.

 

****************Mais qualidade na exportação de processos****************

A exportação da documentação ou da imagem do processo conta com mais qualidade, gerando os artefatos desejados com maior precisão.

Nota

Agora é necessário salvar o diagrama antes de efetuar a exportação para garantir a qualidade dos artefatos.

******************Método aperfeiçoado****************** 

O método "*setCardValue"* foi aprimorado, garantindo o correto funcionamento independente da forma de armazenamento dos formulários.

# Social

**************Inclusão de usuários em comunidades**************

Aumentamos a confiabilidade no processo de inclusão de usuários em comunidades quando essas e os participantes estão na mesma nuvem de acesso.

# Arquitetura

**************Conversão de base ECM/Fluig mais segura**************

Foi aperfeiçoada a conatualização de base do ECM para o Fluig para aceitar caracteres especiais, aumentando a abrangência e, também, validando caracteres inválidos.

**************Atualização mais simples**************

A partir dessa atualização, o instalador durante a atualização detecta e mantém as configurações de portas utilizadas previamente. A configuração das portas *Realtime* e *Chat* agora não são perdidas durante a atualização.

**************Criação de empresas com mais integridade**************

O procedimento de criação de empresas está mais íntegro. Quando o *Identity* está habilitado, os procedimentos corretos para a criação de empresas são:

* Nova empresa no Fluig:

1. Solicite a criação do contexto no *Identity*;
2. Crie a empresa no Fluig;
3. Configure a integração entre o contexto do *Identity* e a empresa do Fluig.

* Empresa já existente no Fluig:

1. Crie a empresa no *Identity;*
2. Integre com a empresa do Fluig;
3. Envie os usuários do Fluig para o *Identity*.

NotaMais informações podem ser obtidas em [Integração do Fluig com o *Identity*](http://tdn.totvs.com/x/Tx1bB)*.*

# WCM

****************************Mensagens de eventos mais claras e objetivas****************************

As mensagens de validação de eventos existentes no Fluig foram aprimoradas, tornando-se mais claras e objetivas para facilitar o entendimento do usuário.

*****************************Widget* Editor de Conteúdo - *Link Popup*****************************

A *widget* Editor de Conteúdos agora permite configurar *links* para abrirem o conteúdo em uma janela *popup*.

# Fluig Studio

**************Cliente de *Webservices* maiscustomizado**************

Agora é possível alterar algumas configurações do cliente *Webservices* utilizado para fazer requisições aos serviços cadastrados no Fluig.

Nota

Mais informações sobre o funcionamento podem ser obtidas em [Integração com Aplicativos Externos](http://tdn.totvs.com/x/lCVbB), no item ***Webservice* com *Client* Customizado**.

**************Cadastro de *Webservices* independente de servidor**************

Para facilitar a utilização do mesmo código fonte em servidores de teste e produção, agora é possível especificar o nome dos pacotes inseridos. Recomenda-se, ao cadastrar um serviço no Fluig Studio, colocar um *package* igual para todos os servidores.

# Mobile

**************Listagem de comunidades aprimorada**************

Foi aperfeiçoada a apresentação de comunidades para que sejam apresentadas as comunidades ocultas em que o usuário participa no Fluig Mobile.

**************Formulário mais confiável**************

Agora o registro do formulário é exibido em mais situações na movimentação de processos.

Também foi aprimorada a integração entre o movimento de solicitações Web x Mobile quando elas possuem formulários pai x filho, tornando o procedimento mais eficiente.
