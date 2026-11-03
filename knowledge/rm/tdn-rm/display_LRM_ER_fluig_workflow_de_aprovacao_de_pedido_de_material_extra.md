---
content_hash: 16d55e5c9347033f55ae81217acb41ab749c726f72201f36143b81930b707ac2
fetched_at: '2026-06-29T00:06:01.084725+00:00'
page_id: '198935848'
product: rm
source: tdn-rm
title: ER_fluig_workflow_de_aprovacao_de_pedido_de_material_extra
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_fluig_workflow_de_aprovacao_de_pedido_de_material_extra
version: 29
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## 

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOP (Totvs Obras e Projetos) |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto** | R\_C&P\_TOP007 | **IRM** | PCREQ-2617 |
| **Requisito** | PCREQ-6026 | **Subtarefa** | PDR\_CP\_TOP007-1455 |
| **Chamado** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colômbia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  |  | | --- | --- | --- | | 1 | [Pedido de material extra](http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.GeracaoPedExtra.aspx) | *<http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.GeracaoPedExtra.aspx>* | |  | Workflow - Aprovação Pedido de Material Extra | <http://tdn.totvs.com.br/pages/releaseview.action?pageId=179700033> | | | |

## Objetivo

 O Pedido de material extra tem a finalidade de controlar os gastos de material extra, ou seja, material além do planejado, onde são controladas todas as movimentações de pedidos, autorização do pedido, quantidade pedida para determinada tarefa e principalmente as pessoas envolvidas no processo. O workflow de aprovação de pedidos de material extra via Fluig irá incorporar ao TOP (TOTVS Obras e Projetos) a opção de realizar a aprovação de pedidos de material extra através de um novo caminho, além do próprio TOP, o ambiente Fluig. Esse novo caminho para a aprovação irá seguir os mesmo passos da aprovação já existente, tentando ao máximo manter o elementos já presentes nela.

## Definição da Regra de Negócio

Através do pedido de material extra com aprovação via TOP os operadores do sistema tem a opção de elaborar um pedido de material ao sistema de Backoffice, sendo que este deverá ser aprovado por algum gestor com permissões para exercer tal ação. Neste pedido o operador irá incorporar itens que serão solicitados em quantidades de acordo com a necessidade descrita. Ao termino da elaboração do pedido o operador irá submeter esse pedido a aprovação, e neste momento o pedido será encaminhado a quem deverá analisa-lo e aprovar/reprovar o mesmo.

O passo seguinte ao  envio do pedido para aprovação, é a aprovação propriamente dita. Neste ponto um operador com permissões de aprovar o pedido e seus itens, irá manifestar seu consentimento ou não diante dos dados apresentados. Neste momento ele poderá:

* Aprovar completamente todo o pedido;
* Reprovar completamente todo o pedido;
* Aprovar item a item:
  + Aprovar completamente o item;
  + Aprovar parcialmente o item (informando a quantidade ou o percentual de aprovação);
  + Reprovar o item;

Este será o ponto o qual o workflow irá atuar fornecendo informações via Fluig para que o seja possível realizar a aprovação dentro da sua plataforma. O operador aprovador munido de um usuário com permissões para aprovar o workflow irá visualizar no Fluig as mesmas informações visualizadas no TOP, tanto do pedido quanto de seus itens. 

### Parâmetros Gerais

Será incluído na aba “Fluig” nos parâmetros gerais TOTVS Obras e Projetos dois novos parâmetros para esta nova funcionalidade. Esses parâmetros indicarão qual será o processo relativo ao workflow de aprovação de contratos e também quais serão os estados que indicarão que o workflow está “Aprovado” e “Reprovado”. Veja protótipo de tela Parâmetros Gerais.

### Parâmetros de Projeto

Na aba “Integração Fluig” em “Parâmetros de Projetos -> Integração -> Integração Fluig” (veja a tela  Parâmetros de Projeto) será adicionado os seguintes parâmetros, “Utilizar workflow de aprovação de pedido de material extra”, que indica ao TOP que os pedidos de material extra serão avaliados no Fluig.

#### Alterações em parâmetros existentes

No TOP já existem parâmetros de projeto para a aprovação de pedido de material extra, que no contexto Fluig, não fazem muito sentido. Por tanto tais parâmetros serão agrupados, com o indicativo que serão validos somente quando a aprovação estiver sendo realizada via TOP, para o Fluig esse não terão efeito.

 **Workflow para Aprovação de Contratos**

No contexto do Fluig, a execução da aprovação será executada via workflow, e isso traz algumas particularidades não existentes na aprovação via TOP, como por exemplo estados da aprovação, que em comparativa se assemelham aos estados do pedido, mas não são idênticos. Para que o comportamento seja semelhante a observação dessa particularidades é muito importante, e a saída a ser adotada é o estudo e adequação do workflow, para que seus dispositivos e mecanismo sejam moldados de forma a aderir o processo já existente .

A aprovação do pedido de material extra no TOP possui duas etapas, a avaliação dos itens e do pedido e a finalização da aprovação. Na avaliação o operador observa todos os dados dos itens, podendo aprovar ou reprovar cada um individualmente, ou até mesmo aprovar parcialmente a quantidade de um item. Feita a etapa de avaliação o pedido deverá ser finalizado, que nada mais é que o fechamento da aprovação, do pedido e dos itens e disponibilização do pedido no formato em que está para ser enviado ao back-office, isso na prática irá disponibilizar para o pedido apenas os itens aprovados ou aprovados parcialmente, levando sempre em consideração as quantidades aprovadas.

O workflow será elaborado de forma a manter ao máximo a semelhança com o processo já existente. Neste sentido teremos alguns pontos a observar:

* Aprovação total do pedido;
* Reprovação total do pedido;
* Aprovação parcial do pedido;
* Aprovação parcial dos itens;

#### Apresentação do workflow no Fluig

No Fluig o workflow com os dados do pedido de material extra e dos seus itens será exibido de forma a apresentar apenas as informações relevantes, mas sem deixar de lado informações importantes. Neste sentido a apresentação do formulário será como exibido na Figura **Protótipo 04 - Visão Fluig dos dados do pedido** e na Figura **Protótipo 05 - Visão Fluig dos itens do pedido**, com duas abas sendo a primeira para apresentação dos dados do pedido e segunda a listagem dos itens.

Na tela do pedido o usuário será capaz apenas de visualizar dados, nenhuma informação poderá ser alterada, já que essas informações não serão alteradas no TOP e não deverão ser enviadas de volta a ele.

Na tela dos itens, assim como na tela do pedido, todos os campos serão bloqueados, porém o campo "Quantidade aprovada" poderá ser editado, pois é esse o campo que irá refletir a aprovação do item. Como dito anteriormente o Fluig irá manter o comportamento já existente, mas nem todos poderão ser iguais, e a edição do campo quantidade é um deles, pois ele será o ponto central da aprovação do workflow, a analise do campo irá indicar ser o item foi aprovado, aprovado parcialmente ou reprovado. Essa avaliação será simples, fazendo as seguintes validações:

* Item com Quantidade aprovada igual a Quantidade Pedida, será considerado aprovado;
* Item com Quantidade aprovada menor que a Quantidade Pedida, será considerado aprovado parcialmente;
* Item com Quantidade aprovada igual a zero será considerado reprovado;

Para facilitar a aplicação estarão disponíveis botões para aprovar ou reprovar item, permitindo também a execução destas ações ou a aplicação de um percentual de aprovação para todos os itens.

Além das visualizações, o Fluig irá seguir o fluxo de operação do workflow conforme a Figura **Fluxo do workflow 01 - Fluxo de execução do workflow de aprovação de pedido de material extra**, existindo dois estados finais "Finalizado (Final)" e "Reprovado (Final)".

#### Aprovação total do pedido

Como no TOP a aprovação total do pedido irá refletir a definição de 100% da quantidade aprovada dos itens do pedido. No caso do workflow de aprovação de pedido de material extra essa irá acontecer quando o usuário Fluig selecionar prosseguir o workflow para o estado "Finalizar Aprovação" com todos os itens da listagem do formulário com suas quantidades aprovadas em 100% da quantidade pedida. Para aprovar todos os itens de uma só vez pode-se utilizar o botão de aprovação (verde) disponível no cabeçalho da grid de Itens.

Caso seja zerada a quantidade aprovada de todos os itens, ou seja, 0% da quantidade pedida, e o workflow prosseguir ao estado "Finalizar Aprovação", automaticamente o mesmo irá atribuir ao workflow o estado Reprovado, já que este é real estado refletido pelas quantidades aprovadas dos itens.

#### Reprovação total do pedido

Semelhante à Aprovação, a Reprovação do pedido irá se comportar conforme as regras já existentes no TOP, sendo assim ele irá atribuir a todos os itens do pedido o percentual associado de 0% e o status de reprovado. No workflow de aprovação de pedido de material extra esse comportamento será representado pelo estado "Reprovar todos os Itens". Ao entrar neste estado o workflow automaticamente atribuirá quantidade 0 a todos os itens e solicitará o a finalização da aprovação no RM..

#### Aprovação parcial do pedido e Aprovação parcial dos itens

A Aprovação parcial de um pedido é a situação em que nem todos os itens do mesmo são aprovados integralmente (100% da quantidade solicitada) ou então podendo ter alguns itens reprovados e outros aprovados (integral ou parcialmente). Resumidamente a aprovação parcial de um item é o processo já descrito, no qual o item pode não ter sua quantidade aprovada integralmente (menos de 100% da quantidade solicitada).

No workflow de aprovação de pedido de material extra esse comportamento será representado pelo estado "Finalizar Aprovação", que irá encaminhar ao TOP os itens do pedido no estado que o aprovador os deixou. Para manter o comportamento já existente no TOP, ao visualizar o workflow de aprovação de pedido de material extra existirá uma aba que irá exibir os dados dos itens, e nesta aba será possível atribuir a quantidade aprovada a um item. Existirá também nesta a opção de aplicar um percentual de aprovação em sobre a quantidade pedida, bastando apenas informar esse percentual e aplicar.

Na prática a informação que irá dizer se um item e subsequentemente um pedido está aprovado é a quantidade aprovada dos itens. Se todos os itens estiverem com a quantidade aprovada no valor de 100% da quantidade solicitada, irá indicar que todos os itens estão com o estado aprovado e o pedido também, bem como o valor da quantidade aprovada em 0% da quantidade solicitada presente em todos os itens do pedido irá indicar que aqueles itens estão todos reprovados e por consequência o pedido. Qualquer percentual de quantidade aprovada em um ou mais itens fora dos descritos acima indicará que o pedido está aprovado parcialmente.

### Comportamento na tela de Aprovação de pedido de material extra Fluig

Como o ambiente no qual o workflow está inserido existem particularidades, as telas de aprovação do workflow não serão espelhos das telas existentes no TOP. Alguns processos e campos serão eliminados, afim de tornar a visualização mais limpa e objetiva, deixando a vista somente dados relevantes da aprovação. Por tanto processos como os de aprovar, reprovar e aprovar parcialmente não existirão, e os seus comportamentos serão absorvidos por interações mais eficientes em um ambiente web e de workflow.

Continuando nesta linha de raciocínio, a aprovação ou reprovação de um item poderá ser feita a partir dos botões de ação à esquerda do Grid , conforme Figura **Protótipo 05 - Visão Fluig dos itens do pedido**, a partir da aplicação de percentuais de aprovação ou inserção manual da quantidade aprovada na caixa de texto correspondente.

Nenhum outro campo a não ser a quantidade aprovada (e automaticamente o status) estará disponível para edição. A qualquer momento o usuário poderá salvar o formulário, usando-se do botão presente no workflow para tal ação.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros de projeto | Alteração | Projeto -> Selecionar Projeto -> Projeto -> Construção e Projetos | Inclusão de parâmetro para habilitar a utilização do workflow de aprovação de pedido de material extra |
| Pedido de material extra | Alterada | Projeto -> Selecionar Projeto -> Planejamento -> Geração de pedido de material extra | O envio e as aprovações/reprovações de pedidos e itens será repassada ao Fluig, sendo bloqueada a execução no TOP |

#### Tabelas envolvidas

|  |  |  |
| --- | --- | --- |
| **Tabelas de banco de dados utilizadas** | | |
| **Tabela** | **Descrição** | **Utilização** |
| MPAR | Parâmetros Gerais | Inclusão de colunas indicando qual o identificador do workflow no Fluig responsável pela aprovação de pedido de material extra bem como colunas indicando quais os estados referentes a Aprovar item, Reprovar item, Aprovar Parcialmente; |
| MPEDIDOMATEXTRA | Pedido de material extra | Inclusão de coluna de identificação do workflow no Fluig. Consulta de dados. Alteração de dados. |
| MITEMPEDIDOMATEXTRA | Item do pedido de material extra | Consulta de dados. Alteração de dados. |
| MPEDIDOEXTRASTATUS | Cadastros de Status do pedido de material extra | Consulta de dados. |
| MAPROVACAOPEDIDOSTATUS | Cadastros de Status do item do pedido de material extra | Consulta de dados. |

## Definição de Regras de Integridade

Para que o Workflow de aprovação de pedido material extra é necessário observar algumas regras e algumas validações. A principio um fato básico é a não existência de dois fluxos na aprovação do pedido, ou seja, a aprovação ser realizada via Fluig e via TOP, para não permitir tal situação alguns processos serão desabilitados ao se optar por utilizar a aprovação via Fluig. São eles:

* Finalizar Aprovação de pedido de material extra;
* Aprovar Pedido Extra;
* Reprovar Pedido Extra;

Além dos processo desabilitados alguns processos irão sofre alterações no seus fluxo normal de execução. O processo de "Retornar para criação" ira executar sua funcionalidade normalmente, mas como adicional ao seu fluxo de execução quando utilizada a aprovação via Fluig o processo irá cancelar qualquer workflow que esteja em aberto para aquele pedido. Assim não se corre o risco de abrir dois workflows para o mesmo pedido com informações diferentes. O processo de "Enviar pedido extra para aprovação" por outro lado irá sofrer mais alterações, ele será o responsável por elaborar o workflow e envia-lo ao Fluig, sua execução internamente no TOP irá continuar inalterada, mas com o adicional de gerar o workflow para o Fluig.

Outra validação que existirá é a não existência de dois workflows para um mesmo pedido de material ao mesmo tempo. Sendo que toda vez que de alguma forma for solicitado a elaboração de um novo workflow essa regra será validada.

Ao optar por executar a aprovação de pedidos de material extra via Fluig, o processo de aprovação só será concluído quando não houver nenhum erro ou exceção. Ao chegar a qualquer estado final no wokflow o Fluig agrupa os dados e chama um processo no TOP passando como informação os dados colhidos da tela, se por ventura durante a finalização da aprovação do pedido de material extra no TOP ocorrer erros ou exceções o procedimento será abortado. O TOP irá tentar buscar os dados da aprovação consultando o servidor Fluig, nenhum novo workflow será gerado e o pedido já em estado final não poderá gerar novo workflow.

## Protótipo de Tela

**Protótipo 01 - Parâmetros Gerais (Parametrização do workflow e estados do workflow**

```
 Protótipo 02 - Parâmetros de projeto ( Parâmetro utilizar Aprovação de pedido de material extra)
```

**Protótipo 03 - Visão Pedido de material extra ( Em destaque os processo alterados para que o workflow funcione)**

******Protótipo 04 - Visão Fluig dos dados do pedido******

********Protótipo 05 - Visão Fluig dos itens do pedido********

### Fluxo do Processo

### ****Caso de uso 01 - Funcionalidades TOP****

### *****Caso de uso 01 - Funcionalidades Fluig*****

 

### *****Fluxo do workflow 01 - Fluxo de execução do workflow de aprovação de pedido de material extra*****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
