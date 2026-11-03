---
content_hash: 2a3e13b3ca9b70fc7448c5545db13146f73ac1dbca169e835a37bbcf84a13f4a
fetched_at: '2026-06-29T00:08:22.282445+00:00'
page_id: '269418627'
product: rm
source: tdn-rm
title: Revisão de Programação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269418627
version: 194
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Revisão de Programação |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado** | TVQHPB | | |
| **País** | Brasil e demais países da América Latina | | |

  

## Objetivo

Essa ferramenta, que faz parte da rotina de Revisões Múltiplas, tem o objetivo de possibilitar o replanejamento do projeto, enquanto o projeto atual continua em andamento. Através da mesma, a empresa poderá criar uma revisão horizontal do projeto atual e replanejá-la conforme a sua necessidade, em um processo formalizado e sujeito à aprovação, que irá definir a aplicação desse replanejamento ou a sua negativa.

Quando um projeto se encontra em execução, isso significa que o seu orçamento e planejamento foram aprovados, a obra está acontecendo, e no TOTVS Obras e Projetos temos alguns módulos gerando valores realizados no projeto tais como: Contrato, Mobilidade, Plano de Compras, Apropriação entre outros.

Como o projeto não é paralisado quando é gerada uma Revisão de Programação, caso o usuário tenha uma solicitação para modificar o planejamento existente no momento da execução, o mesmo tem a possibilidade de realizar essa modificação e simulação através desta revisão. Ao realizar este procedimento o usuário seleciona os serviços e tarefas que deverão fazer parte do novo projeto, e então o Totvs Obras e Projetos, irá criar um novo projeto filho (revisão horizontal) do projeto selecionado, dando ao usuário a possibilidade de realizar modificações/inclusões nessa revisão horizontal criada.

Posteriormente, caso essa revisão horizontal de Revisão de Programação seja aprovada a mesma será atualizada sobre o projeto original de acordo com os critérios que serão descritos nesse documento.

## Definição da Regra de Negócio

### 

## 1. Aplicação da Funcionalidade

Para se utilizar a Revisão de Programação, que é uma das funcionalidades da Revisão Múltipla, é imprescindível que o projeto tenha controle de fases, sendo que a Revisão Horizontal de Revisão de Programação apenas poderá ser aplicada em projetos que estão nas fases de Venda, Planejamento ou Execução.

## 2. Entidades Envolvidas no Controle de Revisão de Programação

As entidades que serão controladas pela ferramenta de Gestão de Revisão de Programação são:

* Tarefas – Serviços e Atividades (com pert e cronograma);
* Composições (com os seus recursos);
* Insumos (com os seus preços);
* Grupos de Custo;
* Parâmetros do Projeto (normalmente, somente os parâmetros que determinam a data do projeto e consequentemente os períodos do cronograma devem ser alterados, mas esta restrição fica a cargo da configuração de segurança, que disponibiliza ao cliente o controle por acesso às abas de parâmetros, sendo que se os mesmos forem alterados e a Revisão de Programação aprovada, eles serão atualizados no projeto pai).

 

## 3. Parametrizações da Revisão Horizontal de Revisão de Programação

### 3.1. Permitir Revisão de Programação na Revisão Múltipla:

Para criar uma revisão horizontal de Revisão de Programação em primeiro lugar é necessário que o projeto permita a realização desse processo.

Para isso, dentro do Projeto, em ***"Projetos | Parâmetros | Construção e Projetos | Projetos (F6) | Projeto | Revisão de Programação"*** deve ser marcado o parâmetro 'Permitir Revisão de Programação na Revisão Múltipla', sendo que o mesmo não poderá ser desmarcado após ter sido criada alguma revisão horizontal de Venda, Planejamento ou Execução.

Com este parâmetro marcado, ao ser acessado o Processo ***"Revisões Múltiplas"***, o sistema permitirá ao usuário optar pela criação de uma Revisão Vertical ou de uma Revisão Horizontal de Revisão de Programação.

### 3.2. Consistências da Revisão de Programação:

Estes parâmetros irão definir se na Aplicação da Revisão de Programação, o TOTVS Obras e Projetos irá consistir quando a quantidade utilizada na atividade do projeto principal for diminuída na revisão de Revisão de Programação.

Para se garantir a integridade dos contratos do projeto pai, é necessário que o TOTVS Obras e Projetos se certifique que as quantidades contratadas não sejam desrespeitadas na aplicação da revisão de Revisão de Programação.

Caso o parâmetro de projeto esteja definido como **Avisa**, o TOTVS Obras e Projetos irá realizar a aplicação e, se caso encontrar a quantidade da tarefa inferior à quantidade contratada ou comprada o mesmo irá emitir uma alerta com todas as atividades que possuem essa característica e finalizará o sincronismo. Caso o parâmetro de projeto esteja habilitado com a opção **Barra**, o TOTVS Obras e Projetos irá interromper a execução da aplicação e irá emitir uma mensagem com todas as atividades que possuem quantidade inferior à contratada. Caso no parâmetro de projeto esteja informada a opção **Não Confere**, o TOTVS Obras e Projetos executará a aplicação sem a necessidade de consistir a quantidade da tarefa em relação ao contrato e ao plano de compras. 

Na aplicação o TOTVS Obras e Projetos irá verificar os seguintes tipos de contratos:

* Contrato de Serviço;
* Contrato de Parcela Fixa;
* Contrato de Insumo;
* Contrato Extra-Histograma (apenas caso também exista Contrato de Insumo para pelo menos um dos insumos da tarefa).

O contrato do tipo Serviço é um contrato cuja característica é a associação de atividades com quantidades e valores, podendo-se realizar a gestão de Terceirização de Mão-de-Obra e de Serviços. Por possuir essa característica acreditamos que o contrato do tipo Serviço não pode ter suas quantidades já contratadas desrespeitadas na planilha de atividades. A aplicação da revisão de Revisão de Programação irá analisar se a quantidade da tarefa na revisão está respeitando a quantidade já contratada neste tipo de contrato. Assim, caso o processo de aplicação não atenda a esta regra, o processo verificará qual será seu comportamento conforme o parâmetro definido, ou seja, se caso o parâmetro for diferente de Não Confere, o TOTVS Obras e Projetos poderá barrar o processo e listar ao usuário todas as atividades que estão desrespeitando a quantidade já contratada, ou poderá efetivá-lo, mas irá listá-las também. No caso da planilha de Serviços, deverá será feita a mesma consistência de quantidade, só que para os contratos a receber.

O contrato do tipo Parcela Fixa é um contrato que possui características similares ao contrato do tipo serviço, sendo que a diferença está na geração de parcelas com valores iguais, com períodos já medidos, a fim de simplificar e dar agilidade ao negócio. Como estes contratos possuem características similares suas consistências seguirão o mesmo comportamento, ou seja, o processo de aplicação verificará em seu parâmetro de projeto como o TOTVS Obras e Projetos ira se comportar ao verificar que a quantidade associada ao contrato está menor do que a quantidade na planilha de atividade, ou que a quantidade na planilha de serviços está menor do que a já associada nos contratos a receber.

Contrato do tipo Insumo é um contrato cuja característica é o consumo de insumos associados ao contrato. Os insumos possíveis de ser associados são os insumos utilizados no projeto, assim na associação de insumo ao contrato o usuário poderá associar quantidade parcial ou total dos insumos no projeto. O TOTVS Obras e Projetos, no momento de aplicação, irá verificar se a quantidade total associada ao contrato está mantida na planilha de atividades da revisão de Revisão de Programação, e caso a quantidade total associada ao contrato seja inferior ao total de uso do insumo no projeto o TOTVS Obras e Projetos irá verificar os parâmetros de projeto e assim definirá qual comportamento deverá assumir durante esta consistência. Caso o Parâmetro de Projeto seja diferente de Não Confere, o TOTVS Obras e Projetos irá listar ao usuário todos os insumos que estão desrespeitando a quantidade já associada. A mesma consistência será efetuada para o contrato Extra Histograma, nos casos em que o mesmo for validado. A mesma consistência será efetuada na planilha de serviços, mas somente para os contratos a receber.

O contrato de Fornecimento de Material será tratado na consistência de plano de compras e para o contrato de Marco Contratual não será necessária a validação por quantidade pois o mesmo é caracterizado por metas, e essas metas são percentuais concluídos das atividades que estarão compatibilizadas por causa do cronograma realizado sincronizado.

Para se garantir a integridade do plano de compras é necessário que o TOTVS Obras e Projetos verifique se a quantidade planejada na revisão de Revisão de Programação está maior ou igual à quantidade solicitada no módulo de Pedido de Material, (exceto Pedidos de Cotação). Para esta integridade o TOTVS Obras e Projetos irá analisar os Parâmetros de Projeto, e se caso o parâmetro esteja configurado para **Não Confere**  o TOTVS Obras e Projetos não irá realizar esta validação, caso contrário será exibido um Log com todas as tarefas para as quais esta regra foi desrespeitada.

A consistência desses tipos de contratos e das requisições será feita separadamente, exceto quando nos Parâmetros do Projeto, em ***"Contratos | Liberação"*** o campo "Consistência entre Pedidos de Material e Contratos" esteja marcado, pois dessa forma a consistência será efetuada pela soma das quantidades dos contratos e Pedidos. Assim, neste caso em que o parâmetro da Consistência estiver marcado o sistema automaticamente preencherá os parâmetros de consistência da Revisão de Programação com Barra e não permitirá a alteração dos mesmos.

Estes parâmetros serão definidos no projeto principal e não poderão ser alterados na Revisão de Revisão de Programação.

## 4. Criando uma Revisão Horizontal de Revisão de Programação:

Estando na visão de projetos, ao selecionar determinado projeto e entrar em ***"Processos | Revisões Múltiplas"*** o usuário poderá incluir uma Descrição para a Revisão que será criada e optar pelo Recálculo do Projeto (recomendamos que este recálculo seja efetuado, garantindo que a revisão horizontal de Revisão de Programação seja criada com os dados atualizados). Ao Avançar, irá optar por gerar uma Revisão Vertical transformando a fase do projeto ou por gerar uma Revisão Horizontal de Revisão de Programação.

Tendo optado pela Revisão Horizontal de Revisão de Programação deverá informar quem será o projeto mandatário, se o projeto original ou a revisão de Revisão de Programação, para a determinação da codificação das tarefas quando houver qualquer conflito entre eles.

Essa informação será utilizada pelo sistema nas rotinas "Sincronizar Planejamento" e "Aplicar Revisão de Programação" para definições quanto aos códigos das tarefas, devido à criação de novas tarefas e aos processos de renumeração e alteração de código que podem ser efetuados em ambos os projetos.

Se definirmos que o projeto mandatário é o projeto pai e na Revisão de Programação for criada uma tarefa com um código que já exista nele, no momento do Sincronismo ou da Aplicação da Revisão de Programação a tarefa será automaticamente renumerada. Assim, quando da aplicação da revisão de Revisão de Programação, a tarefa será transferida  com um novo código, ou seja, independente do que foi definido na Revisão de Programação, a ordenação dos códigos do projeto pai prevalecerá. Além disso, caso o projeto mandatário seja o projeto Origem, na Revisão de Revisão de Programação não será permitido executar os processos "Trocar Código" e "Reorganizar Código".

Por outro lado, se for definido que o projeto mandatário é a Revisão Horizontal de Revisão de Programação, se nela for criada uma tarefa cujo código já exista no projeto pai, no momento do Sincronismo ou da Aplicação da Revisão de Programação a tarefa do projeto pai terá seu código alterado para o próximo código disponível, o mesmo ocorrendo se na Revisão de Programação for realizada a renumeração das tarefas, ou seja, independente do que existia no projeto pai, a ordenação dos códigos da Revisão de Programação prevalecerá.

Dando continuidade ao processo, o sistema irá verificar em ***"Projetos | Parâmetros | Construção e Projetos | Projetos (F6) | Planilha de Serviços"*** se o parâmetro 'Utiliza Planilha de Serviço' está marcado, e caso o projeto utilize Planilha de Serviço, o sistema apresentará em tela as atividades da Planilha de Serviços para que sejam selecionadas aquelas que farão parte do Projeto Horizontal de Revisão de Programação.

Ao ser selecionado um serviço, o sistema automaticamente irá selecionar também todas as tarefas a ele vinculadas e estas tarefas farão parte da Planilha de Atividades da revisão de Revisão de Programação. Assim, ao selecionar os serviços e clicar em Avançar o sistema apresentará a tela com as tarefas da Planilha de Atividades do projeto pai, sendo que as tarefas vinculadas aos serviços selecionados virão automaticamente marcadas.

Na tela das tarefas da Planilha de Atividades o usuário poderá selecionar outras atividades além das que já vieram marcadas, sejam elas vinculadas a serviços ou não, sendo que, se for selecionada alguma atividade vinculada a algum serviço que não havia sido marcado, o sistema automaticamente irá gerar para a revisão de Revisão de Programação o serviço vinculado à mesma, bem como as demais atividades vinculadas a este serviço.

Como você pôde perceber os vínculos entre as Planilhas de Serviços e de Atividades serão sempre mantidos, assim, caso seja desmarcado um serviço, todas as atividades vinculadas ao mesmo serão desmarcadas, e caso seja desmarcada uma atividade, o sistema irá desmarcar o serviço vinculado a essa atividade, bem como todas as demais atividades vinculadas a este serviço.

No canto esquerdo do rodapé das telas de seleção de atividades da Planilha de Serviços e da Planilha de Atividades será apresentado um contador que informará ao usuário a quantidade de serviços e a quantidade de atividades selecionadas.

Caso o projeto não utilize a Planilha de Serviços, será apresentada somente a tela com as atividades da Planilha de Atividades para que sejam selecionadas aquelas que farão parte da revisão de Revisão de Programação.

Antes da execução do processo de criação da Revisão Horizontal de Revisão de Programação o sistema deverá exibir em tela um resumo contendo todas as tarefas da Planilha de Serviços e da Planilha de Atividades que farão parte da Revisão de Programação a ser criada, solicitando a confirmação ou o cancelamento por parte do usuário.

Na geração de uma Revisão Horizontal de Revisão de Programação o sistema seguirá as seguintes regras:

* Quando for selecionada uma tarefa, as etapas e obras superiores a esta tarefa serão copiadas, mesmo que não estejam selecionadas;
* Quando for selecionada uma etapa ou obra, as tarefas abaixo da mesma automaticamente selecionadas e consequentemente copiadas;
* Será mantido o mesmo identificador da tarefa na nova revisão, pois ele será utilizado mais tarde para identificar o vínculo da revisão de Revisão de Programação com o projeto pai;
* As composições, insumos, cronogramas e preços associados às tarefas selecionadas também serão copiados;
* Antes de realizar a cópia das tarefas, os parâmetros do projeto serão copiados para a nova revisão automaticamente;
* Não levará para a revisão de Revisão de Programação os Contratos e suas Medições, Riscos, Apontamentos, Mobilidade e Planos de Compras realizados no projeto pai;
* Os novos projetos de Revisão de Programação criados a partir da versão 12.1.18 do TOP Obras e Projetos contemplarão os processos de Incluir/Alterar/Excluir Grupos de Custo, portanto, caso existam na base Projetos de Revisão de Programação criados em versões anteriores, será necessário realizar um Sincronismo para atualização dos Grupos de Custo nesses Projetos.

## 5. Ações da Revisão Horizontal de Revisão de Programação:

Após ter sido gerada a Revisão Horizontal de Revisão de Programação o usuário poderá alterá-la, efetuando assim o replanejamento do projeto.

Descrevemos abaixo as restrições, possibilidades e o fluxo do processo para a Revisão Horizontal de Revisão de Programação, determinando, assim, o funcionamento da mesma.

### 5.1. Ações Não Permitidas na Revisão Horizontal de Revisão de Programação

Algumas funcionalidades não serão permitidas na Revisão Horizontal de Revisão de Programação, a saber:

* Alocação de Recursos (liberado apenas Interprojetos);
* Alteração em períodos do cronograma que já vieram travados do projeto pai;
* Alterações no quadro de permanência;
* Apontamentos de Equipamento;
* Apontamento Manual e por Período (validação ao selecionar o projeto no lookup e ao salvar o apontamento);
* Apropriação de Serviços/Insumos;
* Associa Calendário de Turno;
* Backup/Restore de Projeto;
* Ciclos de Transporte;
* Contratos;
* Custos Diretos;
* Custos Indiretos;
* Diário de Projeto;
* Equipamentos Associados ao Projeto;
* Equipe de Mobilidade;
* Equipes de Timesheet;
* Exclusão de Composições não utilizadas;
* Exclusão de Insumos não utilizados;
* Exclusão de tarefas, composições e/ou insumos que vieram do projeto pai;
* Execução de Tarefas(Monitor e Tray Icon);
* Folhas Tarefa;
* Gerar Lançamento Financeiro;
* Gerar Projeto de Licitação;
* Importação da PINI;
* Importação de arquivo TXT;
* Importação via MS Project;
* Importar EMOP;
* Importar FGV;
* Importar Insumo do Suprimento/Faturamento;
* Integração Orçamento;
* Mapa de Apontamentos de Equipamento;
* Mobilidade;
* Pedido de Material;
* Pedido de Material Extra;
* Quadro de permanência;
* Redução do número de períodos do cronograma;
* Relatório Ciclo de Transporte;
* Relatório Cronograma Mensal;
* Relatório de Folha Tarefa;
* Relatório de Medição Completa;
* Relatório de Plano de Ação;
* Relatório Feedback;
* Relatório Membros de Equipe;
* Relatórios Periódicos;
* Saldo para fluxo de desembolso;
* Sincronização com MS Project;
* Sincronizar Folha de Ponto;
* Timesheet;
* Transformar Recursos Globais em Locais.

As demais funcionalidades serão permitidas, mas somente serão refletidas na revisão em uso as alterações realizadas nas entidades citadas no tópico “2. Entidades Envolvidas no Controle de Revisão de Programação”.

### 5.2. Ações Permitidas na Revisão Horizontal de Revisão de Programação

Serão permitidas durante a Revisão Horizontal de Revisão de Programação as seguintes ações:

* Alterações na Tarefa (inclusive código);
* Alterações nas Composições e Recursos de Composição;
* Alterações no Cronograma;
* Alterações nos Grupos de Custo;
* Alterações nos Insumos e Preços de Insumos;
* Alterações nos Parâmetros (sendo que serão aplicadas somente alterações relativas a aumento do número de períodos do cronograma) ;
* Cópia de Itens;
* Equalização de Insumos;
* Importação via MS Excel para insumos, composições e tarefas;
* Inclusão de novas Tarefas tanto no projeto original como na revisão de Revisão de Programação;
* Inclusão de novas Composições (somente serão consideradas se tiverem associação com alguma tarefa da revisão de Revisão de Programação – direta ou indiretamente);
* Inclusão de novos Insumos: (somente serão consideradas se tiverem associação com alguma tarefa da revisão de Revisão de Programação – direta ou indiretamente);
* Renumeração e Alteração do Código das Tarefas (serão aplicados conforme a revisão definida como mandatária);
* Uso do Comparador de Projetos para comparar as alterações realizadas com a revisão de escopo atual.

## 6. Sincronismo entre Projeto Principal e Revisão de Programação

Após terem sido efetuadas as alterações desejadas na Revisão de Revisão de Programação, antes de aplicá-las, recomendamos fortemente que seja efetuado o sincronismo da revisão em uso, pois, dependendo das alterações realizadas em um projeto, as mudanças de planejamento podem durar vários dias ou até meses, e como o projeto origem não permaneceu parado, ou seja, continuou tendo o seu realizado em andamento, é necessário que o projeto filho consiga obter algumas informações do projeto pai, para que a situação desse projeto filho seja atualizada para a realidade antes que as suas modificações sejam aplicadas ao projeto pai.

O sincronismo garante a integridade do cronograma realizado, pois é necessário que projetos em fase de execução tenham compatibilidade com suas revisões ao longo do tempo da obra. Neste momento é necessário que os projetos revisados da Revisão de Programação recebam informações do projeto principal para que não fiquem desatualizados em relação à execução.

Ao clicar no processo “Sincronizar Planejamento da Revisão de Programação” o sistema apresentará em tela todas as revisões de Revisão de Programação existentes e será necessário que o usuário selecione os projetos de Revisão de Programação que receberão o sincronismo.

Caso deseje incluir novas tarefas na Revisão de Revisão de Programação, antes de solicitar o Avanço do processo, clique em "Incluir Novas Tarefas" e, se o projeto utilizar Planilha de Serviços o sistema apresentará em tela as atividades da Planilha de Serviços, sendo que o  sincronismo das tarefas já existentes na Revisão Horizontal de Revisão de Programação será efetuado automaticamente, ou seja, deverão ser selecionadas apenas as novas tarefas que deseja sincronizar.

Da mesma forma que na criação da Revisão de Programação, também no sincronismo, ao selecionar um serviço, o sistema automaticamente irá selecionar todas as tarefas vinculadas a ele e estas tarefas serão sincronizadas para a revisão de Revisão de Programação.

Ao selecionar os serviços e clicar em Avançar, o sistema apresentará a tela com as tarefas da Planilha de Atividades do projeto pai, sendo que o  sincronismo das tarefas já existentes na Revisão Horizontal de Revisão de Programação será efetuado automaticamente, ou seja, deverão ser selecionadas apenas as novas tarefas que deseja sincronizar..

Na tela das tarefas da Planilha de Atividades o usuário poderá selecionar novas atividades a serem sincronizadas além das que já vieram marcadas, sejam elas vinculadas a serviços ou não, sendo que, se for selecionada alguma atividade vinculada a algum serviço que não foi marcado, o sistema automaticamente irá sincronizar também o serviço vinculado à mesma, bem como as demais atividades vinculadas a este serviço.

No rodapé das telas de seleção de atividades da Planilha de Serviços e da Planilha de Atividades deverá ser apresentado um contador que informe ao usuário a quantidade de serviços e a quantidade de atividades selecionados.

Caso o projeto não utilize a Planilha de Serviços, será apresentada somente a tela com as atividades da Planilha de Atividades do projeto pai seguindo as mesmas regras descritas acima.

Se não for inserir nenhuma tarefa durante o sincronismo, ou seja, caso deseje somente sincronizar as tarefas já existentes no projeto de Revisão de Programação, basta selecionar aquela que será sincronizada, clicar em Avançar e o sistema iniciará a execução do processo.

Antes da execução da rotina de sincronismo o sistema deverá exibir em tela um resumo contendo todas as tarefas da Planilha de Serviços e da Planilha de Atividades que serão sincronizadas, solicitando a confirmação ou o cancelamento do processo por parte do usuário.

Ao ser efetuado o sincronismo o sistema irá executar as seguintes atividades:

* Novas Tarefas: Caso o usuário selecione uma tarefa que não está no projeto de revisão de Revisão de Programação; o processo de sincronismo irá adicioná-la à revisão com todas as suas relações (recursos, datas, cronograma);
* A quantidade planejada nas planilhas de Serviços e Atividades da Revisão de Programação prevalecerá;
* Serão atualizados o travamento de períodos, os períodos travados dos cronogramas previsto, realizado e medido e o percentual concluído do PERT, sendo que o percentual do PERT será calculado através do somatório da quantidade do cronograma realizado do projeto origem dividido pela quantidade da revisão de Revisão de Programação;
* Caso a quantidade total do cronograma realizado seja maior do que a quantidade da tarefa no projeto de destino, o processo será concluído com ressalvas, ou seja, irá finalizar o cálculo para as atividades que estão com quantidades condizentes com o projeto origem e para as demais tarefas não irá calcular, apresentando log de erro.

Durante o sincronismo, o sistema poderá, ainda, realizar o replanejamento automático do cronograma, caso o usuário assim deseje. Descrevemos abaixo essa funcionalidade:

### 6.1. Replanejamento do Cronograma da Revisão de Programação

Na análise do cronograma o TOTVS Obras e Projetos irá verificar se houve alguma alteração e travamento do período do cronograma da Planilha de Atividades. Caso exista algum período travado na Planilha de Atividades do projeto principal  , o TOTVS Obras e Projetos irá realizar o travamento e alteração do cronograma planejado, realizado e medido automaticamente igualando os valores do projeto principal e da revisão de Revisão de Programação nestes períodos. Esta analise ocorrerá apenas na Planilha de Atividades, pois como a Planilha de Serviços é utilizada para orçamento, caso tenha alguma informação de realizado no seu cronograma esta informação será ignorada. No processo de sincronismo há a possibilidade do usuário realizar o replanejamento de cronograma e ao selecionar esta opção o TOTVS Obras e Projetos irá verificar o avanço físico do período e replanejá-lo de acordo com os exemplos abaixo:

Vamos supor um projeto **A** que está em execução e deste projeto foram geradas 2 revisões de Revisão de Programação A.1 e A.2. No momento desta revisão o projeto possuía andamento apenas no 1º período e consequentemente o mesmo está travado. Os usuários que geraram as revisões realizaram as modificações de cronograma como demonstrado abaixo:

Com o andamento da obra, foi realizado o 2º período do projeto principal **A**, assim, o usuário tornou-se obrigado a sincronizar os projetos de Revisão de Programação. No momento que o usuário solicitou o sincronismo ele não marcou o replanejamento automático e o sistema irá se comportar da seguinte forma:

* Se o parâmetro de projeto “Não emitir aviso se o cronograma não fechar em 100%” estiver selecionado, o TOTVS Obras e Projetos deixará o lançamento ser realizado se o percentual total do cronograma previsto for inferior a 100%;
* Se o parâmetro “Somente avisar se o cronograma previsto não fechar em 100%” estiver selecionado, o TOTVS Obras e Projetos deixará o lançamento ser realizado se o percentual total do cronograma previsto for inferior a 100%;
* Se o Parâmetro de projeto “Obriga o fechamento do cronograma previsto em 100%” estiver selecionado, O TOTVS Obras e Projetos não deixará o sincronismo ser concluído se todas as tarefas não fecharem em 100%.

Vamos supor ainda que, para o cenário anterior, o parâmetro selecionado foi “Obriga o fechamento do cronograma previsto em 100%” e o usuário não selecionou a opção de replanejamento. Com essas parametrizações, o seguinte cenário irá ocorrer:

Neste cenário o TOTVS Obras e Projetos não realizará o sincronismo de nenhum dos projetos pois, sem o replanejamento automático todos os lançamentos em cronograma estarão com valores diferentes de 100%.

Em uma outra situação, caso o parâmetro selecionado tenha sido “Não emitir aviso se o cronograma não fechar em 100%” e o usuário não selecionou a opção de replanejamento, o TOTVS Obras e Projetos irá emitir um Log de Atenção, pois o Projeto **A.1** quepossui percentual planejado superior a 100% não será sincronizado e o Projeto **A.2** que possui percentual planejado inferior a 100% irá receber a atualização. O mesmo cenário se repetirá caso o usuário selecione o parâmetro “Somente avisar se o cronograma previsto não fechar em 100%”.

Vamos supor agora que o usuário na execução do processo selecione o replanejamento automático do cronograma. Neste caso, o TOTVS Obras e Projetos irá realizar a o replanejamento de acordo com o lançamento travado no cronograma, conforme abaixo:

Neste cenário com o parâmetro de replanejamento selecionado, o TOTVS Obras e Projetos realizou uma redistribuição no cronograma dos projetos A.1 e A.2 de acordo com o realizado do projeto principal, deixando os projetos de Revisão de Programação atualizados em relação ao projeto principal.

É importante salientar que a opção de replanejamento apenas será realizada pelo processo se os cronogramas das tarefas estiverem planejados em 100%, pois apenas desta forma o Totvs Obras e Projetos consegue replanejar a atividade

Todas as validações de cronograma serão feitas pela dimensão de quantidade, na relação quantidade / tarefa e quantidade no cronograma, pois outras dimensões poderão causar erros.

Ao final do Sincronismo, o sistema irá gerar um resumo com tudo o que foi sincronizado, bem como um log com o que não foi possível efetuar na sincronização. É importante que você verifique este log antes de passar ao processo de Aplicação da Revisão Horizontal de Revisão de Programação.

## 7. Aplicação da Revisão Horizontal de Revisão de Programação:

Após a conclusão da análise da revisão de Revisão de Programação, o usuário deverá escolher a revisão que atualizará a versão de execução.

Ao acessar o processo ***"Aplicar Revisão de Programação"*** o usuário poderá optar poraprová-la ou rejeitá-la, salientando que ambas as opções referem-se à Revisão de Revisão de Programação como um todo, ou seja, não existe aprovação parcial ou rejeição parcial de uma Revisão de Programação.

Antes de proceder com a aprovação ou rejeição o sistema exibirá duas mensagens solicitando ao usuário que confirme se deseja prosseguir, já que este processo é irreversível.

Caso o usuário opte por Rejeitar o projeto de Revisão de Programação, sua posição será modificada para Cancelado e ficarão registrados, na observação do histórico, a rejeição e o usuário que a rejeitou, além de um texto que o usuário poderá informar para detalhar a rejeição. Nesta situação o projeto original não sofre nenhuma alteração.

No caso de Aprovação, a posição do projeto de Revisão de Reprogramação será modificada para Concluído e ficarão registrados, na observação do histórico, a aprovação e o usuário que a aprovou, além de um texto que o usuário poderá informar para detalhar a aprovação. Nesta situação o projeto original passa para a posição Revisado, sendo criada uma nova revisão que passa a ser o projeto em vigor.

No caso de aprovação da Revisão Horizontal de Revisão de Programação, o sistema efetuará as seguintes ações para aplicar as alterações efetuadas:

* Para as tarefas incluídas, renumeradas ou que tiveram seu código alterado, ao serem aplicadas na nova revisão ativa, irão prevalecer as informações do projeto mandatário (vide item 3.2. desta especificação);
* Para as tarefas que sofreram qualquer outro tipo de alteração, elas serão aplicadas na nova revisão ativa, lembrando que nas alterações para quantidade inferior serão verificados os parâmetros de consistência da Revisão de Programação (vide item 3.3. desta especificação);
* As alterações ao Cronograma Previsto serão replicadas para a nova revisão ativa. Já os cronogramas realizado e medido, mesmo que tenham sido modificados não serão aplicados, visto sua edição ser permitida na Revisão de Programação, apenas para efeito de simulações;
* Composições e Insumos alterados serão replicados para a nova revisão ativa;
* Composições e Insumos criados também serão criados na nova revisão ativa;
* Se no projeto pai existir algum insumo ou composição cujo código entre em conflito com algum cadastrado na Revisão de Programação, o processo será abortado e emitirá um aviso com os insumos e/ou composições que devem ser ajustados antes de se aplicar a Revisão de Programação;
* Preços ativos de insumos da Revisão de Programação deverão prevalecer em relação aos preços dos insumos do projeto pai;
* Se no projeto pai uma tarefa existente na revisão de Revisão de Programação, for excluída, ela não será recriada através do processo de Aplicação.

A aplicação da Revisão Horizontal de Revisão de Programação, possui ainda as seguintes características:

* Antes de iniciar o processo, o projeto pai será revisado para que seja mantida uma versão com o projeto que estava em execução;
* Todas as revisões de Revisão de Programação que estavam pendentes serão vinculadas à nova revisão ativa. São consideradas revisões pendentes, aquelas para as quais não foram aplicados nem o processo de Rejeição nem o de Aprovação;
* Depois de aplicada uma Revisão de Programação o sistema não irá mais permitir que a mesma seja excluída, já que ela documenta as alterações realizadas ao longo do projeto.
* O log de usuários irá registrar o usuário responsável pelas alterações na revisão de escopo atual, da mesma forma que registraria se fosse uma alteração normal.

Além disso, como a Revisão de Programação quando criada não leva para o projeto os Contratos e suas Medições, Riscos, Apontamentos, Mobilidade e Planos de Compras realizados no projeto pai, faz-se necessário que no momento da Aplicação, o TOTVS Obras e Projetos realize consistências garantindo a integridade do projeto que está em execução. Para isso é necessário realizar uma conferência e tratar as consistências dos seguintes módulos:

* Travamento de Períodos;
* Contrato;
* Plano de compras.

Para as consistências dos módulos de contrato e plano de compras o sistema irá levar em consideração o que foi parametrizado em Consistências da Revisão de Programação (vide item 3.3. desta especificação) e irá desprezar, somente avisar sobre as divergências encontradas ou barrar a aplicação da Revisão de Programação, conforme parametrizado.

Já no caso do travamento dos períodos do cronograma, como o sincronismo é um processo dependente do usuário, a rotina de aplicação de revisão de Revisão de Programação irá analisar se existe compatibilidade entre o projeto aprovado e o projeto principal que se encontra em execução. Caso os projetos sejam incompatíveis o TOTVS Obras e Projetos irá abortar a rotina, informando ao usuário a necessidade de se executar o processo de sincronização de projetos. As consistências analisadas pelo TOTVS Obras e Projetos serão feitas pela dimensão de quantidade e irão garantir que a quantidade da tarefa no projeto de revisão esteja lançada no cronograma planejado respeitando os parâmetros do projeto definidos para o cronograma;

Será garantido também que no processo de Aplicação da Revisão de Programação, não se percam informações dos processos que envolvam integrações, tais como: 

* Mobilidade: Apontamentos, Folhas, Associações de Bens, funções, Equipes, Alocação de Mão de Obra, custo improdutivo e produtivo;
* Apropriação;
* TimeSheet: Apontamento, Alocação;
* Pedido de Material;
* Contratos.

É importante que ao final do processo de aplicação de Revisão de Programação o usuário realize uma conferência dos processos que envolvem integrações com o BackOffice como Integração com Orçamento e Fluxo de Caixa, pois como o planejamento pode ter sofrido alteração é importante que estes processos sejam atualizados pelos usuários.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros do Projeto | Alteração | Projetos | Parâmetros | Construção e Projetos | Projetos (F6) | Projeto | Revisão de Programação | Conforme descrito neste documento |
| Parâmetros do Projeto | Alteração | Projetos | Parâmetros | Construção e Projetos | Projetos (F6) | Projeto | Conforme descrito neste documento |
| Revisão Horizontal de Revisão de Programação | Alteração | Projetos | Processos | Revisões Múltiplas | Revisão Horizontal de Revisão de Programação | Conforme descrito neste documento |
| Sincronizar Planejamento | Alteração | Projetos | Processos | Sincronizar Planejamento | Conforme descrito neste documento |
| Aplicar Revisão de Programação | Alteração | Projetos | Anexos | Projetos de Revisão Múltipla | Processos | Aplicar Revisão de Programação | Conforme descrito neste documento |

## Tabelas Utilizadas:

* MPARAMETRO - Parâmetros do Projeto

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
