---
content_hash: 284cbba3beb68a5cfedee803899bdd1fb6e5a3c62b4fb862a35b8071ce89d44e
fetched_at: '2026-06-29T00:09:14.180173+00:00'
page_id: '421385144'
product: rm
source: tdn-rm
title: Alocação de Mão de Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385144
version: 8
---

---

O objetivo desse Rotina e realizar um processo que realiza a Alocação de Mão de Obra entre Itens de Folha Tarefa e Equipes de Projeto que posteriormente irá gerar uma visão panorâmica na Rotina Programado x Alocado em "Cadastro | Mobilidade | Folha Tarefa | Anexos | Alocação de Mão de Obra". (No caso aqui eu deveria falar que esse anexo é só para planilha atividade?? visto que o executiva não vai existir)

O processo de Alocação de Mão de Obra tem por objetivo, planejar e gerenciar as tarefas de Mão de Obra relacionadas a uma Folha Tarefa. O processo consiste em posicionar os cadastros de Equipe do Projeto e Folha Tarefa lado a lado para que possa ser feito a alocação de cada equipe que atuará nas frentes de trabalho.

A exibição e utilização do processo Alocar Mão de obra na folha Tarefa estão condicionadas à seleção do **[parâmetro de projeto](https://tdn.totvs.com/pages/viewpage.action?pageId=421385196)** referente ao tipo de planilha utilizada:

* **Planilha de Atividades:** O processo Alocar Mão de obra na folha Tarefa é exibido.
* **Planilha Executiva:** O processo Alocar Mão de obra na folha Tarefa NÃO é exibido e não pode ser utilizado.

   
Para melhor visualização e gerenciamento da alocação de cada equipe, os anexos "Alocação de Mão de Obra" na Folha tarefa e "Alocação de Mão de Obra de Equipe" na Equipe de projeto deverão estar posicionados lado a lado. Para realizar a alocação de mão de obra na equipe do projeto o usuário pode realizar o Drag-and-Drop entre os anexos ou executar o processo "Alocar Mão de Obra na Folha Tarefa".

Passo a passo para associação via Drag-and-Drop:

1. Acessar o menu "Controle | Mobilidade | Equipe do Projeto | Anexos | Alocação de Mão de Obra da Equipe";
2. Acessar o menu "Controle | Mobilidade | Folha Tarefa | Anexos | Alocação de Mão de Mão de Obra";
3. Para melhor visualização e execução do Drag-and-Drop, selecionar o modelo de visualização em janelas através do menu "Ambiente | Exibição em Janelas | Janelas | Janelas lado a lado";
4. Selecionar uma tarefa no anexo de alocação de mão de obra e "arrastar" para a janela Equipe de Mobilidade;
5. No anexo de Alocação de Mão de Obra da Equipe, os valores serão atualizados de acordo com a disponibilidade da tarefa;
6. Informar o período do cronograma que deseja visualizar;
7. O sistema atualizará os dados do Anexo de Alocação de Mão de Obra.

Esta tela deverá apenas exibir os insumos do tipo mão de obra, que serão necessários para a execução da tarefa, ou seja, não será exibido alocações de insumos diferentes do tipo "mão de Obra";  
Haverá a Validação pelo o sistema qual ou quais tarefas poderão ser executadas pela equipe Selecionada;  
Haverá a Validação pelo o sistema de quantos insumos são compatíveis com a(s) tarefa(s) selecionada(s), No caso de incompatibilidade o sistema emitirá uma mensagem informativa;  
Havendo a compatibilidade o sistema fará a associação da(s) tarefa(s) à equipe;  
A partir deste momento, será determinada qual ou quais tarefas a equipe escolhida ficará responsável;  
Serão atualizados os valores de Quantidade Alocada, Percentual Alocado e Saldo nas visões de "Alocação de Mão de Obra" e "Alocação de Mão de Obra da Equipe".

Serão exibidas apenas alocações de insumos do tipo "Mão de obra". - Não Haverá "% Alocada" acima de 100%.

**Importante:**

* O grupo DNIT do insumo e a jornada são necessários para o cálculo da alocação; - Deve-se primeiro planejar o PERT para depois fazer a Folha Tarefa; - Alocações de insumos que não sejam do tipo "Mão de obra" não serão considerados.

**Atenção:**  
Havendo a necessidade de um replanejamento com a alteração do período do PERT, haverá a necessidade do cancelamento da folha tarefa atual e a criação de uma nova folha tarefa. Evitando assim aumentar o tempo da tarefa e alocações negativas na Visão da Alocação de Mão de Obra – Programado X Alocado (Baseado no Planejamento do PERT).  
  
Ao Realizar as alocações, algumas cores irão identificar o percentual de alocação campo "% Alocada" que demonstra uma visão panorâmica relacionado ao porcentual alocado que irá variar nas cores (Vermelha, laranja e Verde Claro e Escuro).  
Legenda de cores do campo "% Alocada";  
Vermelho  = Menos de 25% Alocação; laranja   = Maior ou igual a 25% de alocação e Menos de 50% de Alocação; Verde Claro  = Maior ou Igual a 50% de alocação e Menos de 75% de Alocação; Verde Escuro  = Maior ou Igual a 75% de alocação   Até   100% de Alocação.  
  
Exemplo:  
A tarefa 001.01.01 precisa de 1000 Homem/hora para ser executada no período de uma semana (determinado pela Folha Tarefa - Data Início e Data Fim). Ao vincular a tarefa à equipe, o sistema verifica se a tarefa possui mais de um turno e verifica se existe algum membro da equipe (insumo) apto a realizar a tarefa. Esta verificação consiste em analisar o período da folha, a quantidade a ser apontada, capacidade produtiva de cada insumo e verificar se o mesmo não está alocado em algum período semelhante ao da Folha Tarefa. Caso esteja, as horas deste membro não serão consideradas no processo. Caso negativo, as horas deste membro serão consideradas para execução da tarefa.   
Se a quantidade de horas dos membros da equipe não for suficiente, O percentual será exibido; Exemplificando se o percentual for de 51% de uma determinada alocação,o campo "% Alocado" estará com a barra de Status em 51% e na cor "Verde Claro", indicando que a alocação é Maior ou Igual a 50% e Menor que 75%.  
Na Necessidade de se alterar as informações exibidas, Ex:. Selecionar quantas equipes forem necessários para cumprimento de 100% da tarefa, o mesmo poderá retornar ao Menu | Cadastro | Mobilidade | Folha Tarefa =| ANEXOS | ALOCAÇÃO DE MÃO DE OBRA e realizar as devidas alterações.

A Visualização dessas informações poderão ser visualizadas através da Visão da Alocação de Mão de Obra – Programado X Alocado Menu | Cadastro | Mobilidade | Folha Tarefa =| Anexos | Programado x Alocado.  
Exemplo para o Calculo de Alocação: Tarefa 001.01.01 = 110 Unidades Insumo Servente: 3 Horas Insumo Pedreiro: 2 Horas Período 01/01/13 à 31/01/13  
Os Insumos Servente e Pedreiro correspondem a 1 unidade tarefa sendo Servente 3 Horas e Pedreiro 2 Horas, ou seja, para cumprimento de toda a tarefa, será necessário a  multiplicação dos mesmos, que nesse caso será por 100 Unidade/Hora; então ficaremos com 300 horas de Servente e 200 Horas de Pedreiro.  
  
Esse valor deverá ser Alocado no Período 01/01/13 à 31/01/13, onde não estamos Considerando os finais de semana, ou seja, será considerado apenas os 5 dias Semanais e o período produtivo de 5 dias para cada.  
Até o momento Ficamos assim:  
  
330/5 = 66 Unidades/Hora de Servente (5 Dias/Semana) 220/5 = 44 Unidades/Hora de Pedreiro (5 Dias/Semana)  
Para o cumprimento total dessa Tarefa, a Equipe necessita de 550 Horas, sendo 330 horas de Servente e 220 horas de Pedreiro ou por Semana 66 Unidades de Servente e 44 Unidades de Pedreiro.   
  
Se a Jornada de trabalho for de 8 horas produtivas para Servente é Sugerido pelo menos 2 membros para o cumprimento da Tarefa.  
Se a Jornada de trabalho for de 6 horas produtivas para Pedreiro é Sugerido pelo menos 2 membros para o cumprimento da Tarefa. Então para a alocação poderíamos ter 1 Equipe com 4 Membros ou 2 Equipes alocadas sendo uma com 2 Membros Cada.  
  
**Alocação da Folha Tarefa sem controle de Capacidade**  
  
Devido à necessidade de um determinado projeto ter somente uma equipe de mobilidade com todos os funcionários, onde o funcionário possa atuar em mais de uma obra ao mesmo tempo, ou seja, pode estar em duas equipes diferentes ao mesmo tempo, desde que as equipes sejam de projetos diferentes, é possível que se parametrize o projeto para que tal comportamento seja permitido, porém, no momento da Alocação de Mão de Obra na Folha Tarefa, o controle de capacidade produtiva que é calculada considerando a necessidade da tarefa baseada em seus insumos e os insumos nos quais os membros da equipe estão associados deixa de ser realizado.  
  
**Parâmetro "Controlar capacidade da equipe na alocação de mão de obra"**  
Foi inserido o parâmetro "Controlar capacidade da equipe na alocação de mão de obra" em "Parâmetros do Projeto (F6) | Mobilidade | Mão de Obra " que por padrão é marcado. Este parâmetro pode ser desmarcado a qualquer momento do projeto, porém, para marcá-lo novamente, é necessário que não exista equipe ou membro que foram ativados após a desmarcação.  
  
A utilização do parâmetro proporciona alguns comportamentos no sistema:  
  
**Parâmetro marcado:**

* Todas as regras de alocação de mão de obra na folha tarefa serão consideradas;
* Ao validar se um membro ativo faz parte de outra equipe, somente serão consultados projetos que possuem o parâmetro marcado.  
    
  **Parâmetro desmarcado:**
* Permite desativar o funcionário sem fazer nenhuma consistência; - Permitir exclusão do membro da equipe sem consistir alocação; - Para ativar o funcionário ele não pode estar ativo em outra equipe do mesmo projeto; - Na inclusão deve respeitar as mesmas regras de ativar e desativar, conforme o status do funcionário que está sendo incluído; - Os Anexos "Alocação de Mão de Obra" na Folha Tarefa e "Alocação de Mão de Obra da Equipe" na Equipe de Mobilidade, não estarão disponíveis; - O processo de "Alocar Mão de Obra na Folha Tarefa deve apenas vincular a equipe à folha, sem fazer nenhum cálculo.  
    
  **Processo "Alocar Mão de Obra na Folha Tarefa"**
* Este processo estará disponível apenas se o [parâmetro de projetos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=421385196) estiver definido para que a planilha de apontamentos seja a 'Planilha de Atividades.

Permite realizar a alocação de equipes na folha tarefa, assim como é realizado pelo Drag and Drop atualmente. O comportamento desse processo depende da utilização do parâmetro "Controlar capacidade da equipe na alocação de mão de obra", onde os cálculos de alocação, podem ser necessários ou não.

Informações Complementares

---

[Alocação de mão de obra da equipe](http://tdn.totvs.com/pages/viewpage.action?pageId=421385139)
