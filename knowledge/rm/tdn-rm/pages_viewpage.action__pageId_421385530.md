---
content_hash: 1734b21095f76379f3ce935dee368efe3a34d47d4c7c2925ffa3e4346cb5633d
fetched_at: '2026-06-29T00:09:16.399009+00:00'
page_id: '421385530'
product: rm
source: tdn-rm
title: Sincronismo entre Projeto Principal e Revisão de Reprogramação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385530
version: 4
---

Após terem sido efetuadas as alterações desejadas na Revisão de Revisão de Reprogramação, antes de aplicá-las, recomendamos fortemente que seja efetuado o sincronismo da revisão em uso, pois, dependendo das alterações realizadas em um projeto, as mudanças de planejamento podem durar vários dias ou até meses, e como o projeto origem não permaneceu parado, ou seja, continuou tendo o seu realizado em andamento, é necessário que o projeto filho consiga obter algumas informações do projeto pai, para que a situação desse projeto filho seja atualizada para a realidade antes que as suas modificações sejam aplicadas ao projeto pai.  
O sincronismo garante a integridade do cronograma realizado, pois é necessário que projetos em fase de execução tenham compatibilidade com suas revisões ao longo do tempo da obra. Neste momento é necessário que os projetos revisados da Revisão de Reprogramação recebam informações do projeto principal para que não fiquem desatualizados em relação à execução.  
Ao clicar no processo "Sincronizar Planejamento da Revisão de Reprogramação" o sistema apresentará em tela todas as revisões de Revisão de Reprogramação existentes e será necessário que o usuário selecione os projetos de Revisão de Reprogramação que receberão o sincronismo.   
Caso deseje incluir novas tarefas na Revisão de Revisão de Reprogramação, antes de solicitar o Avanço do processo, clique em "Incluir Novas Tarefas" e, se o projeto utilizar Planilha de Serviços o sistema apresentará em tela as atividades da Planilha de Serviços, sendo que o  sincronismo das tarefas já existentes na Revisão Horizontal de Revisão de Reprogramação será efetuado automaticamente, ou seja, deverão ser selecionadas apenas as novas tarefas que deseja sincronizar.  
Da mesma forma que na criação da Revisão de Reprogramação, também no sincronismo, ao selecionar um serviço, o sistema automaticamente irá selecionar todas as tarefas vinculadas a ele e estas tarefas serão sincronizadas para a revisão de Revisão de Reprogramação.  
Ao selecionar os serviços e clicar em Avançar, o sistema apresentará a tela com as tarefas da Planilha de Atividades do projeto pai, sendo que o  sincronismo das tarefas já existentes na Revisão Horizontal de Revisão de Reprogramação será efetuado automaticamente, ou seja, deverão ser selecionadas apenas as novas tarefas que deseja sincronizar..  
Na tela das tarefas da Planilha de Atividades o usuário poderá selecionar novas atividades a serem sincronizadas além das que já vieram marcadas, sejam elas vinculadas a serviços ou não, sendo que, se for selecionada alguma atividade vinculada a algum serviço que não foi marcado, o sistema automaticamente irá sincronizar também o serviço vinculado à mesma, bem como as demais atividades vinculadas a este serviço.  
No rodapé das telas de seleção de atividades da Planilha de Serviços e da Planilha de Atividades deverá ser apresentado um contador que informe ao usuário a quantidade de serviços e a quantidade de atividades selecionados.  
Caso o projeto não utilize a Planilha de Serviços, será apresentada somente a tela com as atividades da Planilha de Atividades do projeto pai seguindo as mesmas regras descritas acima.  
Se não for inserir nenhuma tarefa durante o sincronismo, ou seja, caso deseje somente sincronizar as tarefas já existentes no projeto de Revisão de Reprogramação, basta selecionar aquela que será sincronizada, clicar em Avançar e o sistema iniciará a execução do processo.  
Antes da execução da rotina de sincronismo o sistema deverá exibir em tela um resumo contendo todas as tarefas da Planilha de Serviços e da Planilha de Atividades que serão sincronizadas, solicitando a confirmação ou o cancelamento do processo por parte do usuário.  
Ao ser efetuado o sincronismo o sistema irá executar as seguintes atividades:  
   
·         Novas Tarefas: Caso o usuário selecione uma tarefa que não está no projeto de revisão de Revisão de Reprogramação; o processo de sincronismo irá adicioná-la à revisão com todas as suas relações (recursos, datas, cronograma);  
·         A quantidade planejada nas planilhas de Serviços e Atividades da Revisão de Reprogramação prevalecerá;  
·         Serão atualizados o travamento de períodos, os períodos travados dos cronogramas previsto, realizado e medido e o percentual concluído do PERT, sendo que o percentual do PERT será calculado através do somatório da quantidade do cronograma realizado do projeto origem dividido pela quantidade da revisão de Revisão de Reprogramação;  
·         Caso a quantidade total do cronograma realizado seja maior do que a quantidade da tarefa no projeto de destino, o processo será concluído com ressalvas, ou seja, irá finalizar o cálculo para as atividades que estão com quantidades condizentes com o projeto origem e para as demais tarefas não irá calcular, apresentando log de erro.   
Durante o sincronismo, o sistema poderá, ainda, realizar o replanejamento automático do cronograma, caso o usuário assim deseje. Descrevemos abaixo essa funcionalidade:   
   
**Replanejamento do Cronograma da Revisão de Reprogramação**  
Na análise do cronograma o TOTVS Obras e Projetos irá verificar se houve alguma alteração e travamento do período do cronograma da Planilha de Atividades. Caso exista algum período travado na Planilha de Atividades do projeto principal  , o TOTVS Obras e Projetos irá realizar o travamento e alteração do cronograma planejado, realizado e medido automaticamente igualando os valores do projeto principal e da revisão de Revisão de Reprogramação nestes períodos. Esta analise ocorrerá apenas na Planilha de Atividades, pois como a Planilha de Serviços é utilizada para orçamento, caso tenha alguma informação de realizado no seu cronograma esta informação será ignorada. No processo de sincronismo há a possibilidade do usuário realizar o replanejamento de cronograma e ao selecionar esta opção o TOTVS Obras e Projetos irá verificar o avanço físico do período e replanejá-lo de acordo com os exemplos abaixo:  
Vamos supor um projeto A que está em execução e deste projeto foram geradas 2 revisões de Revisão de Reprogramação A.1 e A.2. No momento desta revisão o projeto possuía andamento apenas no 1º período e consequentemente o mesmo está travado. Os usuários que geraram as revisões realizaram as modificações de cronograma como demonstrado abaixo:  
   
  
Com o andamento da obra, foi realizado o 2º período do projeto principal A, assim, o usuário tornou-se obrigado a sincronizar os projetos de Revisão de Reprogramação. No momento que o usuário solicitou o sincronismo ele não marcou o replanejamento automático e o sistema irá se comportar da seguinte forma:  
·         Se o parâmetro de projeto "Não emitir aviso se o cronograma não fechar em 100%" estiver selecionado, o TOTVS Obras e Projetos deixará o lançamento ser realizado se o percentual total do cronograma previsto for inferior a 100%;  
·         Se o parâmetro "Somente avisar se o cronograma previsto não fechar em 100%" estiver selecionado, o TOTVS Obras e Projetos deixará o lançamento ser realizado se o percentual total do cronograma previsto for inferior a 100%;  
·         Se o Parâmetro de projeto "Obriga o fechamento do cronograma previsto em 100%" estiver selecionado, O TOTVS Obras e Projetos não deixará o sincronismo ser concluído se todas as tarefas não fecharem em 100%.   
Vamos supor ainda que, para o cenário anterior, o parâmetro selecionado foi "Obriga o fechamento do cronograma previsto em 100%" e o usuário não selecionou a opção de replanejamento. Com essas parametrizações, o seguinte cenário irá ocorrer:  
   
  
Neste cenário o TOTVS Obras e Projetos não realizará o sincronismo de nenhum dos projetos pois, sem o replanejamento automático todos os lançamentos em cronograma estarão com valores diferentes de 100%.  
Em uma outra situação, caso o parâmetro selecionado tenha sido "Não emitir aviso se o cronograma não fechar em 100%" e o usuário não selecionou a opção de replanejamento, o TOTVS Obras e Projetos irá emitir um Log de Atenção, pois o Projeto A.1 que possui percentual planejado superior a 100% não será sincronizado e o Projeto A.2 que possui percentual planejado inferior a 100% irá receber a atualização. O mesmo cenário se repetirá caso o usuário selecione o parâmetro "Somente avisar se o cronograma previsto não fechar em 100%".  
Vamos supor agora que o usuário na execução do processo selecione o replanejamento automático do cronograma. Neste caso, o TOTVS Obras e Projetos irá realizar a o replanejamento de acordo com o lançamento travado no cronograma, conforme abaixo:  
   
  
Neste cenário com o parâmetro de replanejamento selecionado, o TOTVS Obras e Projetos realizou uma redistribuição no cronograma dos projetos A.1 e A.2 de acordo com o realizado do projeto principal, deixando os projetos de Revisão de Reprogramação atualizados em relação ao projeto principal.  
É importante salientar que a opção de replanejamento apenas será realizada pelo processo se os cronogramas das tarefas estiverem planejados em 100%, pois apenas desta forma o Totvs Obras e Projetos consegue replanejar a atividade  
Todas as validações de cronograma serão feitas pela dimensão de quantidade, na relação quantidade / tarefa e quantidade no cronograma, pois outras dimensões poderão causar erros.  
Ao final do Sincronismo, o sistema irá gerar um resumo com tudo o que foi sincronizado, bem como um log com o que não foi possível efetuar na sincronização. É importante que você verifique este log antes de passar ao processo de Aplicação da Revisão Horizontal de Revisão de Reprogramação.

Como Fazer

Revisão Múltipla
