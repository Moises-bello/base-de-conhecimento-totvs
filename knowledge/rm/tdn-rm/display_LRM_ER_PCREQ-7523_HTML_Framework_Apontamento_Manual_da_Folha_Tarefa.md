---
content_hash: 21b7baf156f5f551cd9697ee0335de6dd1acdc88ceb11ba3d68580c0c37fc6ac
fetched_at: '2026-06-29T00:06:10.453680+00:00'
page_id: '203763162'
product: rm
source: tdn-rm
title: ER_PCREQ-7523_HTML_Framework_Apontamento_Manual_da_Folha_Tarefa
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-7523_HTML_Framework_Apontamento_Manual_da_Folha_Tarefa
version: 14
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Apontamento Manual de Folha Tarefa |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP008 | **IRM1** | PCREQ-7522 |
| **Requisito1** | PCREQ-7523 | **Subtarefa1** | PDR\_CP\_TOP008-74 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:  TOTVS HTML Framework - http://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&title=HTML+Framework&linkCreation=true&fromPageId=196053421  Fluig - <http://tdn.totvs.com/display/public/fluig/Sobre+o+Fluig>  Mobilidade - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Mobilidade.aspx>  Folha Tarefa - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.FolhaTarefa.aspx>  Apontamento Manual - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.InterfaceColetaLeituraCodigoBarrasFolhaTarefa.aspx> | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Migração da funcionalidade de Apontamento manual de avanço físico da folha tarefa para o ambiente Fluig utilizando o TOTVS HTML Framework. 

## Definição da Regra de Negócio

**TOTVS HTML *Framework***

          O TOTVS | HTML *Framework* foi concebido para tratar apenas a camada de interface das aplicações, confiando que os produtos por trás da interface irão conceder a infraestrutura e a implementação mínima dos serviços para utilização do *framework*.

Ela tem como objetivo:  

* + Fornecer uma Infraestrutura de componentes visuais e de serviços (de interface) HTML5;

* + Prover uma IDE de desenvolvimento HTML5, baseada no TDS ([TOTVS Developer Studio](http://ds.totvs.com/));

* + Disponibilizar um Template de CRUD responsivo com respectivo acelerador no TDS, baseado em Serviços providos pelos produtos;

* + Estruturar um ambiente de desenvolvimento compatível com o Fluig e que possa ser utilizados por todos os produtos TOTVS.

**Apontamento manual para folha tarefa**

A entrada dos percentuais de completude das tarefas de uma Folha deve ser realizada de forma ágil e dinâmica então sua interface deve fornecer recursos para tal.

Após a associação das tarefas a Folha tarefa é necessário que o usuário realize os apontamentos de avanço físico das tarefas associadas. O apontamento de avanço físico pode ser realizado pelo Coletor ou de forma manual pelo Totvs Obras e Projetos, iremos abordar nesta especificação a migração do apontamento manual para a plataforma web, utilizando o HTML Framework Totvs.

Para execução do processo é necessário existir Folhas Tarefas cadastradas com status Pronta para Impressão.  
O processo consiste em acessar o  formulário de Interface de Coleta via Leitura de Códigos de Barras da Folha Tarefa, marcar (ou desmarcar) o indicador de 100%, efetuar a leitura do código de barras (ou digitar), selecionar o percentual de completude da tarefa (somente se o indicador de 100% estiver desmarcado) e salvar. O sistema interpreta o código de barras identificando a tarefa e atualiza o seu apontamento de acordo com o percentual selecionado.

**Migração para TOTVS HTML Framework**

Para a funcionalidade de Apontamentos Manual de folha tarefa  do TOTVS Obras e Projetos serão desenvolvidas telas Web utilizando o TOTVS HTML Framework

Uma vez que as telas Web forem desenvolvidas, estas serão inserida na plataforma Fluig para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.

Será desenvolvida três paginas para o apontamento Manual de Folha Tarefa da seguinte forma:

* Tela com a listagem de Folhas Tarefa do Projeto
* Tela com detalhamento da folha e seus itens associados
* Tela com função de apontamento e listagem das tarefas associadas a  folha tarefa

Na pagina de listagem de folha tarefa serão listadas apenas as folhas tarefas com status de "Pronta para Impressão". As seguintes informações serão exibidas de acordo com o Protótipo 01:

* Descrição da Folha Tarefa
* Numero da Folha
* Data de Inicio
* Data Fim
* Periodicidade

Na pagina de detalhamento da folha e seus itens as seguintes informações (Protótipo 02):

* Folha Tarefa
  + Descrição da Folha Tarefa
  + Numero da Folha
  + Data de Inicio
  + Data Fim
  + Periodicidade
* Itens Associados a Folha
  + Código da Tarefa concatenado ao nome.
  + Quantidade programada
  + Quantidade da tarefa
  + Saldo a executar
  + Percentual apontado

Na pagina de Apontamento serão mostradas as seguintes informações (Protótipo 03):

* Forma de apontamento
  + Será disponibilizado uma opção para o usuário selecionar qual será a forma de apontamento. (código de barras ou código da tarefa)
* Código de Barras da Tarefa ou código da Tarefa
  + O usuário poderá informar o código de barras do item associado a Folha ou código da Tarefa.
* Percentual Aplicado  
  + O usuário informara o percentual aplicado ao item informado no campo "Código de Barras da Tarefa ou código da Tarefa".
  + O percentuais aplicados serão em memoria e apenas serão gravados no momento em que o usuário clicar em salvar.
* Itens Associados a Folha
  + Código da Tarefa concatenado ao nome.
  + Quantidade programada
  + Quantidade da tarefa
  + Saldo a executar
  + Percentual apontado

O processo migrado para Framework HTML, consistirá em acessar o formulário de Apontamento de manual de folha tarefa, informar no campo "Código de Barras ou Código de Tarefa" o código de Barras ou o código da tarefa e aplicar. O sistema interpreta o código de barras identificando a tarefa e atualiza o seu apontamento de acordo com o percentual informado.

### Opcional

## Protótipo de Tela

**Protótipo 01**

**Protótipo 02**

****Protótipo 03****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
