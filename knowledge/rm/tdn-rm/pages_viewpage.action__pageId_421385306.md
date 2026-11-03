---
content_hash: 0eaff125e78bed71a59b9df0abf9cfe459f92e492e812546513bf4f28ab05496
fetched_at: '2026-06-29T00:09:14.918658+00:00'
page_id: '421385306'
product: rm
source: tdn-rm
title: Curva de Distribuição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385306
version: 7
---

O objetivo da funcionalidade é permitir a distribuição de um planejamento através de uma curva previamente cadastrada pelo usuário. As Curvas de Distribuição podem ser copiadas pelo processo de  ou podem ser cadastradas. O cadastro de Curvas de Distribuição é efetuado pelo menu Planejamento | Curva de Distribuição. O campo "Código da Curva" é obrigatório. Em cada curva, é possível cadastrar vários períodos de distribuição e em cada período é possível cadastrar vários percentuais a serem aplicados.

Uma mesma curva poderá ter apenas uma distribuição para a mesma quantidade de períodos, ou seja, caso já exista uma distribuição para 4 períodos, não será permitido uma nova distribuição para essa quantidade. O campo percentual não aceita valor nulo e o somatório dos percentuais deve fechar em 100%.  
Ao criar uma curva, ela passa a pertencer apenas ao projeto de origem, ou seja, é uma curva local. No entanto, pelo processo "Tornar Curva Global", é possível transformar uma curva local em global, com isso, a curva passará a ser visível para todos os projetos da base. Para excluir uma curva global é preciso executar o processo "Exclusão de Curva Global". A exclusão de curvas locais é efetuado pela exclusão padrão. Também é possível criar uma nova curva a partir de uma curva local ou global, pelo processo "Duplicar Curva", que permite efetuar alterações na curva criada. O processo "Criar Curvas Defaults" permite criar curvas com distribuições mais comuns como Gauss, Log, Exponencial e Triangular. Cada curva possui 100 períodos e são curvas globais, portanto não podem ser alteradas. ASSOCIAÇÃO DAS CURVAS NO PROJETO A associação de curvas ao projeto pode ser feito de 2 maneiras:  associando diretamente à atividade ou associando ao cadastro de uma composição. Mesmo que todos sejam preenchidos, é possível utilizar a curva definida no processo de aplicação. As curvas associadas serão utilizadas no momento da aplicação de acordo com uma hierarquia, que será abordado a seguir. APLICAÇÃO DE CURVAS DE DISTRIBUIÇÃO  
Para que as curvas sejam aplicadas para uma tarefa é preciso que o processo "Aplicar Curva de Distribuição" seja acionado e os campos sejam preenchidos. Deve ser informado no campo "Data" os períodos que deverão ser planejados. Caso o parâmetro    estiver marcado, serão utilizadas as datas do PERT e o campo não ficará habilitado para edição. Defina a Curva de Distribuição a ser aplicada ou marque a opção "Utilizar Curva Default". Caso a última opção seja marcada, a curva será aplicada de acordo com a seguinte hierarquia: será aplicada a curva associada à atividade, caso contrário, será aplicada a curva associada à composição, caso não exista curva associada à composição, será aplicada a curva associada ao projeto.

**Atenção:** Caso a opção "Utilizar Curva Default" tenha sido marcada e o usuário tenha definido uma curva no processo, se o sistema identificar uma curva na hierarquia, está será aplicada à tarefa, caso contrário, será aplicada a curva informada pelo usuário na tela do processo.  
Caso existam várias curvas e nenhuma delas contenha o mesmo número de períodos do projeto, será aplicada a curva que contém o número mais próximo.

**Exemplo:** A tabela a seguir representa o número de distribuições de uma curva com seus respectivos períodos:

| **Períodos** | **Distribuição** |
| --- | --- |
| 2 | 30% / 70% |
| 3 |  |
| 4 | 20% / 15% / 40%/ 25% |
| 5 |  |
| 6 |  |
| 7 | 10% / 10% / 30% / 5% / 20% / 15% / 10% |

                              
Caso o planejamento da tarefa seja de: 6 períodos: será utilizada a distribuição de 7 períodos. 5 períodos: será utilizada a distribuição de  4 períodos. 3 períodos: será utilizada a distribuição de 4 períodos.

**Observação:** Caso existam duas distribuições com a mesma diferença de períodos, será aplicada a distribuição com o maior número de períodos. No caso do exemplo acima, para um projeto com 3 períodos existe a possibilidade de aplicar as distribuições 2 e 4, porém será aplicada a 4 que é maior. 

A proporção feita entre o número de períodos distribuídos da curva e o número de períodos do projeto, em caso de divergência entre ambos, é aplicada da seguinte maneira:

**Exemplo:** - Considerando uma curva com as seguintes distribuições:

| **Período** | **Percentual de Distribuição** |
| --- | --- |
| 1 | 20% |
| 2 | 30% |
| 3 | 50% |

* A atividade do projeto onde a curva será aplicada tem 60 dias trabalháveis, que estão distribuídos nos períodos do cronograma da seguinte forma:

  | **Períodos** | **1** | **2** | **3** | **4** |
  | --- | --- | --- | --- | --- |
  | **Dias Trabalháveis** ****(A)**** | 5 | 20 | 20 | 15 |
  | **Dias Úteis de acordo** **com o calendário **do projeto**** | 20 | 20 | 20 | 20 |
* Considerando que a curva a ser aplicada possui 3 períodos e o total de dias trabalháveis é de 60 dias, cada período da curva de distribuição corresponderá a 20 dias (60/3). Portanto cada percentual da curva de distribuição ficará da seguinte maneira:

  | **Período** | **Percentual de Distribuição **(B)**** | **por dia = B/(A/Quantidade total de períodos da **curva)**** |
  | --- | --- | --- |
  | 1 | 20 | 20/(60/3) = 1 |
  | 2 | 30 | 30/(60/3) = 1,5 |
  | 3 | 50 | 50/(60/3) = 2,5 |
* Depois de calcular os percentuais diários de acordo com cada período da curva, os mesmos serão distribuídos de acordo com os períodos do Projeto (da atividade):

  | **Períodos** | **Dias por período** | **Total de dias \* Percentual do período** |
  | --- | --- | --- |
  | 1 | 5 dias do período 1 | 5\*1 = 5 |
  | 2 | 15 dias do período 1 + 5 dias do período 2 | (15\*1) + (5\*1,5) = 22,5 |
  | 3 | 15 dias do período 2 + 5 dias do período 3 | (15\*1,5) + (5\*2,5) = 35 |
  | 4 | 15 dias do período 3 | 15\*2,5 = 37,5 |

  - Assim que a curva for aplicada, a atividade será distribuída da seguinte maneira:

  | Períodos | 1 | 2 | 3 | 4 |
  | --- | --- | --- | --- | --- |
  | **Percentuais** | **5** | **22,5** | **35** | **37,5** |

  Ao planejar uma atividade no Cronograma Planejado e travar alguns períodos dessa atividade nos  , caso seja aplicada uma curva de distribuição à atividade e o novo percentual previsto for diferente do planejamento dos períodos travados, a diferença é distribuída proporcionalmente entre períodos liberados. 

  > **Exemplo:**- Segue planejamento inicial de uma tarefa onde o primeiro período está travado no cronograma:
  >
  > > > > > > **Período     Percentual Planejado**  
  > > > > > >      1                           10  
  > > > > > >      2                           40  
  > > > > > >      3                           50
  >
  > - Segue a Curva de Distribuição com os respectivos períodos a serem aplicados:
  >
  > > > > > > **Período       Percentual distribuído**  
  > > > > > >      1                             20  
  > > > > > >      2                             20  
  > > > > > >      3                             60
  >
  > - A diferença entre o primeiro período planejado do projeto (travado) e o primeiro período da curva é 10%. Essa diferença resulta no percentual que será distribuído proporcionalmente entre os períodos não travados. Os períodos não travados da Curva, 20 e 60 representam 25% e 75% respectivamente do resultado total (60+20 = 80). Distribuindo a diferença de 10% do período travado sobre os percentuais acima, resultam nos seguintes valores:
  >
  > > > > > > **Períodos           Percentual Planejado**  
  > > > > > >     1                                  10  
  > > > > > >     2                    20 + 25% \* 10 = 22,5  
  > > > > > >     3                    60 + 75% \* 10 = 67,5

  Ao gerar o backup de um projeto, somente as curvas de distribuição globais que são utilizadas pelo projeto serão incluídas no backup. No momento da restauração de um backup, as curvas globais que estão no backup e que já existem na base não serão restauradas. Caso alguma curva que esteja sendo restaurada possua o mesmo código de alguma curva global da base de destino, esta terá o seu código alterado.
