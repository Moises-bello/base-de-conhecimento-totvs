---
content_hash: 66558a51ebc4243ddbcad51c174a1cdf96a408e18e8fd37cffe86d0b9a36ecd8
fetched_at: '2026-06-29T00:09:14.142942+00:00'
page_id: '421385139'
product: rm
source: tdn-rm
title: Alocação de Mão de Obra da Equipe 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385139
version: 5
---

---

O Anexo de Alocação de Mão de Obra é uma visão que tem por finalidade exibir a alocação de um determinado insumo para a equipe do projeto de mobilidade. Este anexo estará disponível no Menu | Controle | Minha Obra | Equipe de Mobilidade | Anexos | Alocação de Mão de Obra da Equipe.

**Observação:** Este anexo será utilizado somente para consulta, não sendo possível a sua edição.

Para melhor visualização e gerenciamento da alocação de cada equipe, o anexo "Alocação de Mão de Obra", disponibilizado no anexo da Folha Tarefa, juntamente com o anexo "Alocação de Mão de Obra da Equipe", disponibilizado no anexo da Equipe do Projeto, deverão estar dispostos lado a lado através do recurso de posicionamento automático de telas, acessando o menu Ambiente|Janelas|Lado a Lado.  
Para realizar a alocação de mão de obra à equipe do projeto, no anexo Alocação de Mão de Obra o usuário poderá selecionar a etapa da tarefa, selecionar a tarefa ou ainda selecionar o insumo, através do Drag-and-Drop.  
Após a associação da(s) tarefa(s) à equipe, os valores dos respectivos campos: Quantidade Alocada, Percentual Alocado e Saldo serão atualizados tanto no anexo "Alocação de mão de obra quanto no anex

* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Equipe de Mobilidade;
* Opção de Menu: Projetos \ Construção e Projetos \ Controle \ Básico \ Mobilidade \ Folhas Tarefa;
* O processo de Alocação de Mão de Obra tem por objetivo, planejar e gerenciar as tarefas de Mão de Obra relacionadas a uma Folha Tarefa. Consiste em posicionar os cadastros de Equipe do Projeto e Folha Tarefa lado a lado para que possa ser feito a alocação de cada equipe que atuará nas frentes de trabalho;
* No cadastro de Folha Tarefa, o anexo de Alocação de Mão de Obra deverá estar aberto. Com as devidas telas abertas, basta arrastar (Drag-and-Drop) a linha desejada para cima da equipe desejada para que a alocação possa ser processada;
* Várias linhas podem ser selecionadas no arraste. A seleção da linha para o arraste deve obedecer as seguintes regas:

  + Selecionar Etapa: Todas as tarefas itens da folha relacionadas com a etapa, serão processadas na alocação;
  + Selecionar Tarefa: Apenas a tarefa item selecionada será alocada;
  + Selecionar Insumo: Apenas a tarefa item correspondente ao insumo selecionado será alocada.
* Os passos para realizar a alocação de mão de obra são:

  + O usuário, estando na visão de Folha Tarefa, deverá selecionar a Folha Tarefa e acessar anexo Alocação de Mão de Obra;
  + Deverá abrir a visão das equipes e posicionar as duas telas lado a lado ou utilizar o recurso de posicionamento automático de telas;
  + Selecionar as Tarefas ou Etapas e arrastá-las para a equipe desejada.
  + Ao clicar em “Sim”, neste momento, o sistema faz as seguintes validações:

    - Verifica qual ou quais tarefas poderão ser executadas pela equipe onde o usuário soltou as tarefas;
    - Verificará quantos insumos são compatíveis com a(s) tarefa(s) selecionada(s);
    - Faz a associação da(s) tarefa(s) à equipe. Neste momento, é determinado qual ou quais tarefas a equipe escolhida ficarão responsável por executar;
    - Atualizará os valores de Quantidade Alocada, Percentual Alocado e Saldo nas visões de “Alocação de Mão de Obra” e “Alocação de Mão de Obra da Equipe”;
    - Fará uma carga na tabela de Alocação de Recursos do TOP, com os membros selecionados da equipe que farão a execução da tarefa na frente de obra.
* Realiza uma consistência para garantir que somente uma tarefa poderá ser associada a uma equipe caso ela ainda possua saldo na Folha Tarefa. Caso não exista mais saldo nesta tarefa, é emitida uma mensagem informativa ao usuário. Por exemplo, se a tarefa 001.01.01 possuir, na Folha Tarefa, a quantidade de 100 horas e esta tarefa já estiver associada a uma equipe que apontará 50% (cinquenta por cento) dessas horas, o usuário poderá associá-la a outra equipe com a capacidade que esta equipe possui para apontamento desta tarefa. Caso ela já esteja 100% (cem por cento) associada a uma equipe, no final do processo de Drag-and-Drop o sistema emite uma mensagem ao usuário informando as tarefas que não puderam ser associadas, devido ao fato de não possuírem saldo na Folha. Porém, antes mesmo do usuário realizar a alocação, ele poderá verificar no anexo de “Alocação de Mão de Obra” o “% Alocado”, se a tarefa já está 100% (cem por cento) alocada;
* Após a finalização do processo, a quantidade alocada fica disponível para alteração no anexo “Tarefas da Equipe” presente no cadastro de Equipes do Projeto. Porém essa alteração só poderá ser feita se os dados ainda não tiverem sido exportados para um coletor. O usuário poderá cancelar a Folha Tarefa como um todo, caso não queira por algum motivo receber os apontamentos da equipe ou do insumo;
* O usuário, acessando tanto o anexo “Equipes Associadas à Folha Tarefa” quanto o anexo “Tarefas Associadas à Equipe”, poderá visualizar a(s) tarefa(s) que foi associada à(s) equipe(s) da Folha Tarefa. Nestes anexos poderá desalocar utilizando o processo de “Excluir Alocação de Mão de Obra”;
* Após a montagem do planejamento da Alocação de Mão de Obra, caso o usuário queira visualizar quais os funcionários foram alocados para a tarefa, estas informações estarão disponíveis no cadastro de "Alocação de Recursos", que é uma funcionalidade já existente no TOTVS Construção Obras e Projetos;
* Quem define qual recurso da equipe fará cada tarefa é o encarregado. O usuário responsável pelo planejamento apenas definirá qual será a equipe responsável pela execução das tarefas;
* As tarefas somente poderão ser associadas às equipes que estejam “Ativas” e à Folha Tarefa que não tenha sido enviada ao coletor. Caso deseje-se desativar uma equipe, deve-se desmarcar o campo “Ativa” no cadastro da equipe;
* Caso a equipe não esteja composta com a quantidade de insumos necessários para realização da tarefa, com a quantidade informada, o sistema permitirá que o usuário inclua mais membros à equipe ou vincular outra equipe que contenha insumos aptos a realizar a tarefa selecionada. Para inclusão de novos membros à equipe, o usuário deverá finalizar o processo, para que o sistema salve todas as alterações já feitas no processo da montagem do seu planejamento de alocação de mão de obra para que nenhuma informação seja perdida. Caso o usuário resolva cancelar o processo, nenhuma informação será salva.
* Exemplo:
  + Se um projeto precisar de dez funcionários e o usuário associar uma equipe que possui apenas sete, o usuário terá que associar outra equipe para executar a tarefa. Ao associar outra equipe, pode acontecer desta equipe possuir recursos que não serão necessários, como por exemplo, engenheiro, pintor etc. A equipe ficará com homens que, teoricamente, não possuem nenhum vínculo com a tarefa. Neste caso é de responsabilidade do usuário enquanto planejamento, realocar estes funcionários ou o encarregado, na frente de obra, redistribuir os mesmos de forma a não deixar nenhum insumo ocioso. Para o caso do encarregado optar por fazer a redistribuição dos recursos na frente de obra, o sistema do coletor móvel deverá permitir, através da matrícula do funcionário, da tarefa e/ou centro de custo, está realocação de mão de obra, enviando os funcionários para outra frente de trabalho e realizando check-out deste membro de sua equipe no coletor.
  + **Importante:**

    - * **A equipe que possui associação só poderá ser excluída se a mesma estiver associada a uma folha tarefa que ainda não foi enviada a um coletor;**
      * **A equipe só poderá ser desativada se a mesma ainda não tiver sido associada a uma folha tarefa.**
* **Fator de Produtividade**
  + Após a montagem da Folha Tarefa, o usuário do planejamento poderá informar um fator de produtividade (percentual), que aumenta a quantidade a ser executada no período. Ao ser informado, o campo irá calcular a quantidade planejada para o período: Quantidade prevista para a tarefa X Fator de Produtividade. Desta forma, se uma tarefa possui quantidade = 20 M de muro a ser executada, caso o usuário informe um Fator de produtividade = 1,5 espera-se que seja executada no mesmo período a quantidade total de 30 M de muro contando com os mesmos recursos (20 M x Fator 1,5 = 30 M);
  + Por padrão, o fator de produtividade será 1(um), e para o cálculo da quantidade de recursos necessários à execução do processo será considerada a quantidade programada (sem aplicar o fator de produtividade). O objetivo é demonstrar o quanto se deseja que seja executado no período (além do programado). A quantidade programada não poderá ser superior ao saldo da tarefa a executar.

o "Alocação de Mão de Obra da Equipe". Sendo assim, através do anexo de Alocação de Mão de Obra da Equipe será possível verificar a disponibilidade, o saldo restante para novas associações com determinado insumo, possibilitando melhor gerenciamento da periodicidade do cronograma e das folhas tarefas.  
O controle, em relação ao percentual alocado do insumo para aquela equipe, é definido de acordo com o período do cronograma do projeto. Sendo assim, para verificar a disponibilidade, o percentual alocado e o saldo disponível de determinado insumo da folha tarefa para a equipe, deve informar no filtro a periodicidade correspondente àquela folha.

 Inicialmente as datas iniciais e finais serão as datas do cronograma do projeto e a partir do momento em que forem alteradas sempre será armazenado o último intervalo informado.  
Uma Folha Tarefa pode estar associada a uma ou mais tarefas. Esta alocação é realizada diariamente. Cada insumo possui um ciclo de vida que caracteriza a sua jornada. Sendo assim, estes dados ficarão disponíveis para consulta, de modo que se possa controlar o quanto já foi alocado na tarefa e quanto ainda precisa ser alocado, ou mesmo se houve superalocação de horas na tarefa.  
Mais de uma tarefa poderá ser alocada na equipe do projeto. Caso a equipe não esteja composta com a quantidade de insumos necessários da tarefa o sistema permitirá incluir mais um membro à equipe, ou vincular outra equipe que contenha insumos aptos a realizar a tarefa selecionada.  
Fluxo de execução da funcionalidade do Anexo de Mão de Obra:  
1) Acessar o menu Controle|Mobilidade|Equipe do Projeto|Anexos|Alocação de Mão de Obra da Equipe;

2) Acessar o menu Controle|Minha Obra|Folha Tarefa|Anexos|Alocação de Mão de Mão de Obra;

3) Para melhor visualização e execução do Drag-and-Drop, selecionar o modelo de visualização em janelas através do menu Ambiente|Exibição em Janelas|Janelas|Janelas lado a lado;

4) Selecionar uma tarefa no anexo de alocação de mão de obra e "arrastar" para a janela Equipe de Mobilidade;

5) No anexo de Alocação de Mão de Obra da Equipe, os valores serão atualizados de acordo com a disponibilidade da tarefa;

6) Informar o período do cronograma que deseja visualizar;

7) O sistema atualizará os dados do Anexo de Alocação de Mão de Obra.
