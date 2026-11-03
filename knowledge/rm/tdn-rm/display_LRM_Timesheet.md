---
content_hash: 4a600a2cf624f43c2a0fdb60939dc4ee0227cafc95e56e870c68621660fdcd23
fetched_at: '2026-06-29T00:09:16.902263+00:00'
page_id: '421385604'
product: rm
source: tdn-rm
title: Timesheet
type: documentation
url: https://tdn.totvs.com/display/LRM/Timesheet
version: 13
---

---

Esta funcionalidade permite um acompanhamento do projeto através dos índices de prazo (IDP), custo (IDC) e dedicação (IDD), que poderão ser analisados por tarefa e/ou por recurso. Estes números serão alimentados através de um novo controle de apontamentos de tarefas, que será utilizado para registrar o tempo consumido, os recursos utilizados e o percentual de completude das tarefas.  
    
 **IDP - Índice de Desempenho de Prazos**

Com o Índice de Desempenho de Prazos é possível identificar se o a velocidade em que o projeto gera valor agregado está acima ou abaixo da prevista originalmente.  Com este índice é possível identificar se está havendo atrasos ou se todo o trabalho executado está dentro do esperado, ou ainda, acima do previsto. Portanto, o IDP mostra a relação do Valor Agregado pelo Valor Previsto.

* IDP = Valor Agregado/Valor Previsto.
* IDP < 1: Atraso em relação ao Previsto;
* IDP = 1: Em dia em relação ao Previsto;
* IDP > 1: Adiantado em relação ao Previsto.

**IDC - Índice de Desempenho e Custos**

Com o Índice de Desempenho de Custos, é possível identificar se o custo utilizado no projeto está de acordo com o valor agregado.  Com este índice podemos identificar, se está havendo desperdícios/retrabalhos, ou se todo o custo gasto está entrando como valor agregado. Portanto, o IDC mostra a relação do Valor Agregado pelo Valor Realizado.

* IDC = Valor Agregado/Valor Realizado.

A análise do IDC é semelhante ao do IDP onde:

* IDC < 1: Custo maior que o Previsto;
* IDC = 1: Custos iguais ao Previsto;
* IDC > 1: Custo menor que o Previsto.

**IDD - Índice de Desempenho de Dedicação**

Com o Índice de Desempenho de Dedicação é possível identificar, se a dedicação ao projeto está de acordo com o Valor Realizado. Com este índice, podemos identificar se está havendo empenho por parte dos recursos, em relação às tarefas. Portanto, o IDD mostra a relação do Valor Realizado pelo Valor Previsto.

* IDD = Valor Realizado/Valor Previsto.

A análise do IDD é semelhante ao do IDP e IDC onde:

* IDD < 1: Dedicação maior que a Prevista;
* IDD = 1: Dedicação iguais a Prevista;
* IDD > 1: Dedicação menor que a Prevista.

**Cálculo dos indicadores de desempenho ICD, IDP e IDD**

O cálculo dos indicadores de desempenho é baseado no andamento das tarefas, no que diz respeito à percentuais de completude e apontamentos de recursos.   
*Variáveis:*

* Valor Agregado (VA) = Valor Planejado \* Percentual Apontado;
* Valor Previsto (VP) = Valor definido para a tarefa (número de horas necessárias);
* Valor Realizado (VR) = Quantidade gasta para a execução até o momento (Quantidade de horas apontadas).

*Fórmulas para cálculo de cada indicador:*

* IDP = VA/VP;
* IDC = VA/VR;
* IDD = VR/VP.

Para cálculo dos indicadores de tarefas e projeto é considerada a funcionalidade de cálculo de índices de tarefas, presente na Análise de Valor Agregado já existente no sistema.  
No caso de o projeto estar parametrizado para não utilizar a alocação de membro nas atividades, o mesmo é calculado para que as tarefas estejam disponíveis para o cálculo de índices dos recursos, pois é o cálculo do projeto que organiza as informações da relação Tarefa-Insumo.

**Indicadores: Recursos Alocados**

Para calcular o IDC, IDP e IDD é necessário consultar todas as apropriações relacionadas com os insumos e membros de equipes alocados nas tarefas e os percentuais de completude indicados nos apontamentos de cada membro no qual originaram cada apropriação. Em relação à alocação, se o parâmetro de projeto que permite a utilização de alocação não estiver marcado, será considerado a associação Tarefa-Insumo nos cálculos.

O exemplo abaixo demonstra como deverá ser o cálculo dos indicadores de cada recurso:

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tarefa (01/01/2014 à 31/01/2014)** | **Duração** | **VP (Tarefa)** | **Recurso** | **VP Total (recurso)** | **VP (recurso) em 15/01/2014** | **% Apontado** | **VA** | **VR** | **IDP** | **IDC** | **IDD** |
| 001.01.01 - Configurar Ambiente Integração | 22 | 100,00 | JOSÉ DA SILVA | 60,00 | 22,70 | 38,00% | 22,80 | 25,00 | **1,00** | **0,91** | **1,10** |
|  |  |  | JOÃO DE SOUZA | 40,00 | 18,10 | 43,00% | 17,20 | 15,00 | **0,95** | **1,15** | **0,83** |
|  |  |  | MARIA APARECIDA | 10,00 | 4,50 | 50,00% | 5,00 | 5,00 | **1,11** | **1,00** | **1,11** |

Legenda: Verde: Em dia, Vermelho: Em atraso e Azul: Adiantado

* Para o valor do "% Apontado" é considerado o valor do apontamento mais recente do recurso na tarefa;
* Para o VR é considerado o total de horas apropriadas na tarefa pelo recurso;
* Para o VP é considerado como data de corte a data final do período do cronograma da tarefa.

O processo de cálculo de índices da Análise de Valor Agregado, permite o cálculo do indicadores dos recursos, e permite que os valores possam ser calculados de forma acumulada. Para o cálculo dos indicadores dos recursos, não existe a opção da utilização de fórmulas através dos parâmetros do projeto, assim como ocorre com as tarefas.

O exemplo abaixo demonstra o cálculo do VA dos recursos:

|  |  |  |
| --- | --- | --- |
| **Alocação do Recurso** |  |  |
| **Recurso** | **Tarefa** | **Quantidade** |
| R1 | 001.02.01 | 220 |
| R1 | 001.02.05 | 100 |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Apontamentos do recurso R1** |  |  |  |  |
| **Período** | **Tarefa** | **% Completude** | **VA Total** | **VA Apontamento**\* |
| 2 | 001.02.01 | 40% | 88 | 88 |
| 3 | 001.02.01 | 90% | 198 | 110 |
| 3 | 001.02.05 | 35% | 35 | 35 |
| 3 | 001.02.05 | 55% | 55 | 20 |
| 4 | 001.02.05 | 50% | 50 | -5 |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Indicadores de R1 - Não acumulados** |  |  |  | **Indicadores de R1 - Acumulados** |
| **Período** | **VA** |  | **Período** | **VA** |
| 1 | 0 |  | 1 | 0 |
| 2 | 88 |  | 2 | 88 |
| 3 | 165 |  | 3 | 253 |
| 4 | -5 |  | 4 | 248 |

\*VA Apontamento = VA Atual - VA Anterior da Tarefa

O cálculo do VA do recurso, considera apenas as tarefas alocadas para ele, e o cálculo do VR as apropriações e apontamentos, independente de alocação.

**Indicadores: Recursos Alocados**

Em relação aos cálculos dos indicadores das tarefas e do projeto, são consideradas as funcionalidades de "Análise de Valor Agregado", já existentes no sistema. Para um melhor entendimento, consulte a respeito da  .

**Acompanhamento do Projeto**

O acompanhamento dos indicadores do projeto, tarefas e recursos poderá ser feito utilizando a funcionalidade d  existente no sistema.

Em "Menu Controle|Análise de Valor Agregado|Índices Recursos", são apresentados os indicadores de cada recurso, agrupados por período do cronograma, assim como ocorre com as tarefas. Esta tela é ser composta de uma treeview, com as equipes e seus respectivos recursos, e um grid, com os respectivos indicadores, e tem a relação mestre-detalhe, assim como é apresentado na tela de "Análise de Valor Agregado: Atividades do Projeto". O cálculo dos indicadores dos recursos é realizado no processo "Calcular Índices" presente na tela de "Versões de Avaliação do Valor Agregado".  
  
**Reuniões de Acompanhamento**

Os projetos de timesheet necessitam de reuniões de acompanhamento, e para essa finalidade, há o cadastro de Reuniões presente nas funcionalidades de . Após cadastrar as reuniões, se existir a necessidade de um plano de ação, a funcionalidade de Estratégias de Risco pode ser utilizada, assim como mostra o exemplo:

Exemplo:   
Reunião 001 - Acompanhamento do projeto Roadmap 2013-2014  
Índices: IDP = 0,99, IDC = 0,98 e IDD = 1,00  
Risco: Retrabalhos em versões anteriores  
Estratégia: Dedicação integral aos retrabalhos para reduzir mais cedo possível os mesmos

O exemplo acima demonstra que na reunião de acompanhamento "001" foi identificado o risco "Retrabalhos versões anteriores" que teve como plano de ação, estratégia adota a "dedicação integral aos retrabalhos para reduzir mais cedo possível".

Informações Complementares

---

 

[Alocação de Recurso](http://tdn.totvs.com/pages/viewpage.action?pageId=421385140)

 

 

 

   
    
 Como Fazer

---
