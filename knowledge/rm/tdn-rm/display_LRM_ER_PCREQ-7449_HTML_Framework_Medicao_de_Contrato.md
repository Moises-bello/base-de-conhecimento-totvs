---
content_hash: b96d8db787d3164ec87030557a73777e90f53e7b1da69988239b10c38237f71d
fetched_at: '2026-06-29T00:06:10.377062+00:00'
page_id: '203762468'
product: rm
source: tdn-rm
title: ER_PCREQ-7449_HTML_Framework_Medicao_de_Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-7449_HTML_Framework_Medicao_de_Contrato
version: 23
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contrato |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP008 | **IRM1** | PCREQ-5473 |
| **Requisito1** | PCREQ-7449 | **Subtarefa1** | PDR\_CP\_TOP008-98 |
| **Chamado2** | Não se aplica. | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:  TOTVS HTML Framework - [tec:TOTVS](http://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&title=HTML+Framework&linkCreation=true&fromPageId=196053421)  Fluig - <http://tdn.totvs.com/display/public/fluig/Sobre+o+Fluig>  Projetos - <http://wikihelp.totvs.com.br:1210/WikiHelp/PRJ/PRJ.Projetos.aspx>  Contrato - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Contrato.aspx>  Períodos de Contrato - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.PeriodosContrato.aspx>  Medindo o Contrato - <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.MedicaoContrato.aspx> | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Migração da funcionalidade de Medição de Contrato para o ambiente Fluig utilizando o TOTVS HTML Framework.

## Definição da Regra de Negócio

### **TOTVS HTML *Framework***

O TOTVS | HTML *Framework* foi concebido para tratar apenas a camada de interface das aplicações, confiando que os produtos por trás da interface irão conceder a infraestrutura e a implementação mínima dos serviços para utilização do*framework*. 

Ela tem como objetivo:

* + Fornecer uma Infraestrutura de componentes visuais e de serviços (de interface) HTML5;

* + Prover uma IDE de desenvolvimento HTML5, baseada no TDS ([TOTVS Developer Studio](http://ds.totvs.com/));

* + Disponibilizar um Template de CRUD responsivo com respectivo acelerador no TDS, baseado em Serviços providos pelos produtos;

* + Estruturar um ambiente de desenvolvimento compatível com o Fluig e que possa ser utilizados por todos os produtos TOTVS.

A arquitetura pode ser resumida de acordo com a imagem a baixo:

Mais informações sobre o TOTVS HTML Framework: [tec:TOTVS](http://tdn.totvs.com/pages/createpage.action?spaceKey=LRM&title=HTML+Framework&linkCreation=true&fromPageId=196053421)

### Fluig

No mundo dos negócios, onde as empresas precisam ter controle sobre suas operações e, ao mesmo tempo, agilidade para atender aos diversos processos que acontecem simultaneamente, a forma de interação mudou. A comunicação e os procedimentos são determinados, mas não rígidos, e a única constância é justamente a mudança e tudo precisa estar em nossas mãos.

Entendendo a mudança no comportamento dos indivíduos no ambiente corporativo e as demandas tecnológicas, a TOTVS criou a plataforma fluig com o objetivo de centralizar em uma única tela todos os processos, documentos e sistemas com um único login em uma interface de comunicação colaborativa.

Em resumo Fluig é uma plataforma de produtividade e colaboração que unifica a gestão de processos, documentos e identidades.

Mais informações sobre o Fluig nos links:

* <http://tdn.totvs.com/display/public/fluig/Sobre+o+Fluig>
* <http://www.fluig.com/>

### Medição de Item de Contrato

A medição de contrato consiste, resumidamente, em informar a quantidade que um serviço foi executado em um determinado período de um contrato.

#### Pré-Requisitos para realizar Medição de Item de Contrato no TOTVS HTML

* Ter um contrato criado com a finalidade de: Prestação de Serviços.
* Ter itens (serviços) associados.
* Ter Períodos gerados para o contrato.

#### Migração

Para a funcionalidade de Medição de Contrato do TOTVS Obras e Projetos serão desenvolvidas páginas Web utilizando o TOTVS HTML Framework.

Uma vez que as páginas Web forem desenvolvidas, estas serão inserida na plataforma Fluig para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.

Serão desenvolvidas três páginas para a Medição de Contrato da seguinte forma:

* + Página com a listagem dos Contratos e seus respectivos Períodos salvos na base de dados com opções para realizar uma Medição por período;
  + Página com os detalhes de um Contrato, com informações dos itens associados, períodos gerados e itens medidos.
  + Página com um formulário para Incluir, editar e excluir medições para um período de contrato.

##### Página de Listagem de Contrato e Períodos

Na página de listagem dos Contratos serão mostradas as seguintes informações (vide Protótipo 1):

* + Número do Contrato (será um link que ao clicar será redirecionado para a página com os detalhes do Contrato e suas medições);
  + Finalidade do Contrato;
  + Tipo (à pagar ou à receber)
  + Cliente/Fornecedor;
  + Data do Contrato;
  + Data de Início do Contrato;
  + Data de Término do Contrato;
  + Periodicidade;
  + Total do Contrato;
  + Total de Medição;
  + Posição Atual;
  + Saldo Contratual.

Ainda na listagem dos Contratos ao clicar no link "Exibir detalhes..." serão exibidos as seguintes informações:

* + Código do Período (será um link para realizar a medição para o período);
  + Data Início
  + Data Fim
  + Data da Liberação da Medição
  + Quem liberou a medição
  + Total Medido no Período
  + Valor Retido no Período

Para cada período terá um botão chamado "Medir" para realizar a medição para o período. Ao clicar nesse botão será redirecionado para a página de Incluir/Editar/Excluir medições para um período de Contrato. Caso o período já esteja liberado o botão irá se chamar "Visualizar" e levará para a mesma página porém nenhuma informação poderá ser editada.

A lista de Contratos poderá ser filtrada pelo número do contrato e pelo Cliente/Fornecedor no campo "Pesquisar". Terá também um filtro para exibir todos os períodos ou somente os períodos em aberto. Por padrão serão exibidos somente os períodos em aberto, ou seja, períodos que podem realizar medição pois não se encontram liberados.

##### Página de Detalhes de Contrato

A página de detalhes de um Contrato conterá os mesmos dados de contrato da página de listagem e conterá três pastas (abas) (vide Protótipo 2):

* Períodos
  + Dados dos Períodos de Contrato com um botão chamado "Medir" ou "Visualizar para cada período que leva para a página de Incluir/Editar/Excluir Medição de Período do Contrato.
* Itens Associados ao Contrato
  + Uma lista com as informações dos itens que foram associados ao contrato
* Itens Medidos
  + Uma lista com informações de medições que já foram realizadas no Contrato

##### Página de Incluir/Editar/Excluir Medição de Item de Contrato

A página para incluir/editar/excluir medições de um determinado período de Contrato será composta por uma lista contendo os itens (serviços) associados ao contrato que serão medidos. Será mostrado também as etapas e obras dos itens para medição, porém obras e etapas não serão medidos, apenas itens (serviços). Haverá também um filtro para filtrar por item (serviço) chamado "Pesquisar Tarefa".

Para cada item haverá um formulário onde poderá ser definido qual o percentual, quantidade ou valor que deseja informar para o item, além do valor retido para o período.

Ao informar um percentual, a quantidade e valor já será calculado automaticamente. Ao informar a quantidade, o percentual e o valor será calculado automaticamente. E, não menos importante, ao informar o valor, o percentual e quantidade serão calculado automaticamente. O cálculo tem como base a quantidade e o valor total contratado para o item.

Para cada item haverá um botão salvar, editar e excluir a medição.

Cada item de contrato é mostrado como um item de uma lista. O Código e Nome do item é o título. Terá um link "Exibir detalhes..." que ao clicar irá mostrar mais informações do item  (vide Protótipo 3):

* + Código, Nome, Descrição e Unidade do Item (Serviço)
  + Quantidade, Valor e Percentual Medido
  + Valor Retido do item
  + Quantidade, Valor e Percentual Medido acumulado
  + Quantidade e Valor Contratado
  + Saldo de Quantidade e Valor
  + Valor unitário atual e Valor unitário liberado no período

Ao clicar no botão Editar de um item, uma janela (modal) será aberta com informações da medição e um campo para informar o novo valor, quantidade ou percentual daquela medição, além do valor retido para o item  (vide Protótipo 4).

Nessa janela de edição serão exibidas também três abas para Rateio de Produtos, Centro de Custo e Estado/Município.

Para informar um Rateio haverá um campo para escolher o item de Rateio e um campo para definir o Valor do Rateio. Esse campo de Valor será correspondente ao campo medido do item.

**Exemplo**: Se o campo medido for percentual o campo irá se chamar Percentual. E assim para cada campo que pode ser medido (Percentual, Quantidade e Valor).

Para cada item de Rateio definido será mostrado em uma lista sua descrição e valor informado além de um botão para exclusão.

### Consumir Objetos do Contrato

#### Pré-Requisitos para realizar Consumo de Objetos de Contrato no TOTVS HTML

* Para a realização do consumo de objeto pelo ambiente Totvs HTML é necessário que o contrato esteja cadastrado com a finalidade de contrato de insumo ou contrato extra Histograma.
* Para a realização do consumo de objeto pelo ambiente Totvs HTML é necessário que o contrato tenha seus períodos gerados pelo processo de “Geração de Períodos”
* Para a realização do consumo de objeto pelo ambiente Totvs HTML é necessário que os insumos estejam associados ao contrato.

#### Migração

Uma vez que as telas Web forem desenvolvidas, estas serão inserida na plataforma Totvs HTML para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.

Para esta funcionalidade serão desenvolvidas 3 páginas da seguinte forma:

* + Pagina com a Listagem de Contratos e períodos em aberto.
  + Pagina com a Listagem dos insumos associadas ao contrato, para consumo.
  + Pagina de consumo dos objetos

Na 1º pagina com a listagem de contratos e períodos em aberto, serão exibidos os seguintes campos (vide Protótipo 4):

* + Data Inicio
  + Data de Termino
  + Data de Termino com Adiantamento
  + Posição atual do contrato
  + Cliente/Fornecedor
  + Tipo
  + Periodicidade
  + Total do contrato
  + Detalhes
    - No menu oculto de detalhes será exibido os períodos em aberto do contrato. É caracterizado período em aberto aqueles que ainda não foram liberados.
    - Neste campo é necessário que o usuário clique no período correspondente que ele deseja realizar o consumo.

Na 2º Pagina com a Listagem dos insumos associadas ao contrato, para consumo, serão exibidos a visão com todos os insumos associados ao contrato e os períodos em aberto para consumo (Protótipo 5):

* + Código do Insumo
  + Descrição do Insumo
  + Unidade
  + Quantidade
  + Valor unitário
  + Saldo de Quantidade
  + Saldo de Valor
  + Quantidade Consumida

Na 3º Pagina de consumo de objetos será possível o usuário realizar vários consumos para o período do contrato. O usuário deverá informar insumo, tarefa, tipo de consumo e o valor para o consumo do Objeto, essas informações serão salvas a cada solicitação de consumo.  O usuário terá a possibilidade de editar ou excluir um consumo do período. (Protótipo 6):

* + Insumo
    - Será disponibilizado no Lookup os insumos que possuem associação ao contrato.
    - Tarefas
    - Será disponibilizado todas as tarefas da planilha de atividades.
    - Consumo Utilizado
      * Usuário tem a possibilidade de informar, qual será a grandeza de consumo.
      * Consumo
        + Valor a ser consumido, respeitando a grandeza informada.

É importante lembrar que a cada solicitação de consumo as regras e consistências definidas, serão verificadas, no botão consumir. Caso o consumo respeite todas as consistências o mesmo irá aparecer na tabela de insumos Consumidos e o usuário terá a possibilidade de Editar ou excluir o consumo.

## Protótipo de Página

**Protótipo 01**

**Protótipo 02**

****Protótipo 03****

******Protótipo 04******

******Protótipo 05******

********Protótipo 06********

**********Protótipo 07**********

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
