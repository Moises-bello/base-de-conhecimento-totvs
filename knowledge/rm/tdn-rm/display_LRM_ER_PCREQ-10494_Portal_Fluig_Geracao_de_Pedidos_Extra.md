---
content_hash: f00d9f9783795908553d4c5567c7bc6afad6d8dd7a4a5139f918fda4e7cf58d5
fetched_at: '2026-06-29T00:08:03.508184+00:00'
page_id: '235323483'
product: rm
source: tdn-rm
title: ER_PCREQ-10494_Portal_Fluig_Geracao_de_Pedidos_Extra
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10494_Portal_Fluig_Geracao_de_Pedidos_Extra
version: 146
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Pedido de Material Extra |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP011 | **IRM1** | PCREQ-10493 |
| **Requisito1** | PCREQ-10494 | **Subtarefa1** | PDR\_CP\_TOP011-94 |
| **Chamado2** | Não se aplica. | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colômbia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  | | --- | --- | | **Pré-requisitos para melhor entendimento da especificação** | | | **Entidade** | **Link para o Wikihelp** | | Pedidos de Material Extra | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.GeracaoPedExtra.aspx> | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Migração da funcionalidade de Geração de Pedido de Material Extra para o ambiente Web utilizando o TOTVS HTML Framework.

## Definição da Regra de Negócio

### **TOTVS HTML Framework**

O TOTVS | HTML *Framework* foi concebido para tratar apenas a camada de interface das aplicações, confiando que os produtos por trás da interface irão conceder a infraestrutura e a implementação mínima dos serviços para utilização do *Framework*.

 Ela tem como objetivo:

* + Fornecer uma Infraestrutura de componentes visuais e de serviços (de interface) HTML5;
  + Prover uma IDE de desenvolvimento HTML5, baseada no TDS ([TOTVS Developer Studio](http://ds.totvs.com/));
  + Disponibilizar um Template de CRUD responsivo com respectivo acelerador no TDS, baseado em Serviços providos pelos produtos;
  + Estruturar um ambiente de desenvolvimento compatível com o Fluig e que possa ser utilizado por todos os produtos TOTVS.

A arquitetura pode ser resumida de acordo com a imagem a baixo: 

Mais informações sobre o TOTVS HTML Framework: [tec:TOTVS](http://tdn.totvs.com.br/pages/createpage.action?spaceKey=LRM&title=HTML+Framework&linkCreation=true&fromPageId=196053421)

### Fluig

No mundo dos negócios, onde as empresas precisam ter controle sobre suas operações e, ao mesmo tempo, agilidade para atender aos diversos processos que acontecem simultaneamente, a forma de interação mudou. A comunicação e os procedimentos são determinados, mas não rígidos, e a única constância é justamente a mudança e tudo precisa estar em nossas mãos.

Entendendo a mudança no comportamento dos indivíduos no ambiente corporativo e as demandas tecnológicas, a TOTVS criou a plataforma fluig com o objetivo de centralizar em uma única tela todos os processos, documentos e sistemas com um único login em uma interface de comunicação colaborativa.

Em resumo Fluig é uma plataforma de produtividade e colaboração que unifica a gestão de processos, documentos e identidades. 

Mais informações sobre o Fluig nos links:  

* <http://tdn.totvs.com/display/public/fluig/Sobre+o+Fluig>
* <http://www.fluig.com/>

### Pedido de Material Extra

O pedido de Material Extra tem a finalidade de controlar os gastos de material extra, ou seja, material além do planejado.

São controladas todas as movimentações de pedidos, autorização do pedido, quantidade pedida para determinada tarefa e principalmente as pessoas envolvidas no processo.

### Migração

Para a funcionalidade de cadastro do Pedido de Material Extra no TOTVS Obras e Projetos serão desenvolvidas telas Web utilizando o TOTVS HTML Framework.

Uma vez que as telas Web forem desenvolvidas, estas serão inserida na plataforma Fluig para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.

Serão desenvolvidas todos os cadastros e visões de anexo para o Pedido de Material Extra da seguinte forma:

* + Tela com a listagem dos pedidos de materiais extras salvos na base de dados com opções para Adicionar, editar, visualizar e excluir ;
  + Tela com os detalhes do Pedido Material Extra;
    - Item de Pedido de Material Extra
    - Movimento
  + A páginacom um formulário para criar novo Pedido de Material Extra e Editar os itens do Pedido.

#### Página de Listagem de Pedido de Material Extra

Na tela de listagem dos Pedidos serão mostradas as seguintes informações ():

* + Código do Pedido
  + Data da Requisição
  + Status do Pedido
  + Código e Nome do Usuário Requerente

Todas as informações na listagem estarão ordenadas pela Data da Requisição de forma decrescente e haverá um campo para pesquisar pelo campo Código do Pedido, Data da Requisição ou Status do Pedido. A partir da página de listagem de pedidos será possível adicionar novos pedidos, assim como editar ou visualizar pedidos já criados.

Ao clicar no link "Exibir detalhes..." será mostrado os itens do pedido de material extra.

Para cada pedido de material haverá um botão para editar e outro para excluir o pedido.

De acordo com o status do pedido haverá um botão para executar os processos:

* + **Retornar para criação:** Quando o pedido está no status "Em aprovação" e deseja-se realizar alterações no pedido.
  + **Enviar para Aprovação:** Quando o pedido está no status "Em criação" e pronto para ser analisado e aprovado.
  + **Finalizar Aprovação:** Quando o pedido está no status "Em aprovação" e houve alguma alteração individual em algum item, ou seja foi aprovado parcialmente.
  + **Aprovar Pedido Extra:** Quando o pedido está no status "Em aprovação" e deseja aprovar o pedido por completo, sem nenhuma ressalva.
  + **Reprovar Pedido Extra:** Quando o pedido está no status "Em aprovação" e deseja reprovar o pedido por completo.

#### Página de Detalhes do Pedido de Material Extra

Quando o usuário estiver visualizando um Pedido de Material Extra haverá os seguintes Anexos na própria página de detalhes:

* + - Item de Pedido de Material ()
    - Movimento ()

A página de detalhes mostra as informações do Pedido de Material Extra, observando que em nenhum anexo, a priori, terá a execução de processo como é feito na versão Desktop.

#### Página de Criar, Editar ou Apagar um Pedido de Material Extra

Essa página contém o formulário para criar ou editar um Pedido de Material Extra ().

Ela irá conter uma lista com os itens do pedido extra vinculados ao pedido e um botão para incluir novos itens.

Nesta lista irá conter um botão para editar ou excluir um item. Ao clicar no botão Editar, uma janela (tipo modal) será aberta para alterar o item do pedido. ().

Na janela de modal para edição do item também irá conter uma aba para aprovação, aprovação parcial ou reprovação do item de pedido extra. ()

Terá também os botões para aprovação, aprovação parcial ou reprovação do pedido.

**Rotina de Pedido de Material Extra - Processos**

Para os processos do Pedido de Material no TOTVS Obras e Projetos serão desenvolvidas telas Web utilizando o TOTVS HTML Framework. Não será possível selecionar múltiplos registros para execução dos processos, seguindo o padrão de uso da framework, devendo executar item a item.

Serão migados todos os processos que envolvem o Pedido de Material:

* + Pedido de Material
    - Processo: Retornar para criação
    - Processo: Enviar Pedido Extra para Aprovação
    - Processo: Finalizar Aprovação de Pedido Extra
    - Processo: Aprovar Pedidos Extra
    - Processo: Reprovar Pedidos Extra
    - Processo: Gerar 1 Movimento
    - Processo: Gerar Movimento por Data de Entrega
    - Processo: Excluir Movimento
  + Anexo Item do Pedido de Material  
    - Processo: Aprovar item
    - Processo: Reprovar Item
    - Processo: Aprovar Item Parcialmente
    - Processo: Colocar Itens em Análise
  + Movimento
    - Anexo: Rastreamento de movimento

**Migração dos Processos da rotina de Pedido de Material Extra**

Conforme padrão definido na TOTVS HTML Framework, a visão não apresenta seleção de múltiplos registros e assim sendo os processos deverão neste requisito ser executados registro a registro. Caso haja modificação nos padrões esta tela também deve ser adequada ao novo comportamento.

**Retornar para criação**

O processo "Retornar para criação" manterá o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

Para tal execução será trafegado automaticamente (sem necessidade de solicitar ao usuário em tela) os dados de identificação do Pedido.

**Enviar Pedido Extra para Aprovação**

O processo "Enviar Pedido Extra para Aprovação" manterá o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

Para tal execução será trafegado automaticamente (sem necessidade de solicitar ao usuário em tela) os dados de identificação do Pedido.

**Finalizar Aprovação de Pedido Extra**

O processo "Finalizar Aprovação de Pedido Extra" manterá o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

Para tal execução será trafegado automaticamente (sem necessidade de solicitar ao usuário em tela) os dados de identificação do Pedido.

**Aprovar Pedidos Extra**

O processo "Aprovar Pedidos Extra" manterá o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

Para tal execução será trafegado automaticamente (sem necessidade de solicitar ao usuário em tela) os dados de identificação do Pedido.

**Reprovar Pedidos Extra**

O processo "Reprovar Pedidos Extra" manterá o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

Para tal execução será trafegado automaticamente (sem necessidade de solicitar ao usuário em tela) os dados de identificação do Pedido.

**Gerar 1 Movimento**

O processo "Gerar 1 Movimento" manterá o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

Para tal execução será trafegado automaticamente (sem necessidade de solicitar ao usuário em tela) os dados de identificação do Pedido.

**Gerar Movimento por Data de Entrega**

O processo "Gerar Movimento por Data de Entrega" manterá o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

Para tal execução será trafegado automaticamente (sem necessidade de solicitar ao usuário em tela) os dados de identificação do Pedido.

**Excluir Movimento**

O processo "Excluir Movimento" manterá o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

Para tal execução será trafegado automaticamente (sem necessidade de solicitar ao usuário em tela) os dados de identificação do Movimento.

**Migração dos Processos da rotina de Item de Pedido de Material Extra**

**Aprovar Item de Pedido Extra**

O processo "Aprovar Item" manterá o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

Para tal execução será trafegado automaticamente (sem necessidade de solicitar ao usuário em tela) os dados de identificação do Item de Pedido.

**Reprovar **Item de Pedido Extra****

O processo "Reprovar Item" manterá o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

Para tal execução será trafegado automaticamente (sem necessidade de solicitar ao usuário em tela) os dados de identificação do Item de Pedido.

**Aprovar Item Parcialmente**

O processo "**Reprovar Item**" manterá o comportamento similar ao da interface WinForms, onde o usuário poderá informar a quantidade ou o percentual que deseja aprovar e recebe como retorno a mensagem com o status de processamento.

Para tal execução será apresentada uma tela () para que o usuário informe as duas informações citadas acima e após confirmação estas serão enviadas ao serviço juntamente com os dados de identificação do Item de Pedido.

Somente deve ser permitido que o usuário informe um dos campos (Quantidade ou Percentual), devendo limpar e bloquear o outro campo caso o outro seja selecionado.

**Colocar Itens em Análise**

O processo "**Colocar Itens em Análise**" manterá o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

Para tal execução será trafegado automaticamente (sem necessidade de solicitar ao usuário em tela) os dados de identificação do Item de Pedido.

**Migração do Anexo de Rastreabilidade de Movimento**

Inicialmente este anexo será migrado com layout diferente do WinForms, tendo seu layout orientado em formato de arvore (TreeView), apresentando todos os movimentos relacionados encadeados por seu parentesco.

Esta rotina apresenta as informações do movimento, dos itens de movimento, relacionamento entre eles e demais informações que sejam pertinentes. Para visualizar as informações dos movimentos relacionados deve-se clicar na lupa apresentada a direita da sua descrição.

Vide .

## Protótipo de Tela

### **Protótipo 01 -  Página de Listagem de Pedidos de Material Extra**

### **Protótipo 02 -  Página de Detalhes de um Pedidos de Material Extra**

### **Protótipo 03 -  Página de Criar/Editar e Aprovar um Pedido de Material Extra**

### **Protótipo 04 -  Página de Criar/Editar e Aprovar um Item de Pedido de Material Extra**

### **Protótipo 05 - Tela para informação de parâmetros do processo "Aprovar Itens Parcialmente"**

### **Prototipo\_06Protótipo 06 - Tela de rastreabilidade de Movimentos**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
