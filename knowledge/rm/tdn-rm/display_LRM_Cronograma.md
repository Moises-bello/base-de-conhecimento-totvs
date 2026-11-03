---
content_hash: 4543f293e80836afd225428c2f4433648b80a7956ca273ea5b1c56c7c2aed81e
fetched_at: '2026-06-29T00:09:15.293110+00:00'
page_id: '421385337'
product: rm
source: tdn-rm
title: Cronograma
type: documentation
url: https://tdn.totvs.com/display/LRM/Cronograma
version: 7
---

No Totvs Obras e Projetos é possível utilizar o cronograma para a programação e o acompanhamento do projeto. Nele estão disponíveis os cronogramas Previsto, Base, Realizado, Medido e Apropriado.   
O **Cronograma Previsto** tem como objetivo programar a execução de uma tarefa, etapa, obra ou do projeto no tempo, ou seja, é uma previsão de quanto da tarefa/etapa/projeto será executado em um determinado período, podendo ser definido pelas grandezas: percentual, valor ou quantidade. Com base nessa previsão é possível fazer o acompanhamento do projeto período a período.   
O **Cronograma de Linha Base** tem como objetivo armazenar o planejamento inicial do projeto. Através do processo "Lançar Linha Base" o planejamento do Cronograma Previsto é copiado para o Cronograma de Linha Base. Assim, comparando-o ao cronograma Previsto é possível identificar mudanças ocorridas em caso de replanejamento e identificar se estas mudanças foram benéficas ou não e se outras ações deverão ser tomadas.   
O **Cronograma Realizado** tem como objetivo apresentar a execução real (avanço físico) de uma tarefa, etapa, obra ou projeto em cada período. Ele auxilia no acompanhamento do projeto, ou seja, se comparado ao Cronograma Previsto, é possível identificar se o que está sendo realizado está distante ou dentro do que foi programado. Como o acompanhamento pode ser feito período a período, possibilita que ações de contorno sejam tomadas o mais cedo possível, evitando atrasos e prejuízos ao projeto.  
O **Cronograma Medido** está relacionado às contratações (a pagar ou receber) do projeto. Dessa forma, o cronograma medido pode ser diferente do realizado, pois as medições podem ser superiores ou inferiores ao que realmente foi executado (avanço físico). Para controle detalhado de Contratos (adiantamentos, retenções, deduções, realinhamento, aditivos, etc.) recomendamos a utilização do módulo de Contratos.  
O **Cronograma Apropriado** tem com objetivo mostrar todas as apropriações feitas no projeto, período a período. Assim é possível visualizar todo o consumo (compra ou gasto) e o custo real na tarefa e/ou na obra. Fazendo o seu comparativo com o cronograma previsto, é possível ter uma visão física e financeira de quanto está sendo gasto no projeto e se está dentro do programado, possibilitando a tomada de decisão em relação a uma medida de contorno para evitar um prejuízo ao projeto.

É possível copiar, colar, recortar e deletar dados na visão do cronograma, podendo utilizar os atalhos:

* Ctrl + C para copiar
* Ctrl + V para colar
* Ctrl + X para recortar
* Del para deletar

Ou é possível realizar as ações pelo menu:

**Observação:** O cronograma apropriado traz as apropriações cadastradas no Totvs Obras e Projetos e as compras apropriadas pelo sistema backoffice.  
O cronograma pode ser acessado pela visão de Tarefas ou pelo Pert, ambas através do Anexo "Cronograma". E também pode ser visualizado como planilha, mas para isso, é necessário que a grandeza dos lançamentos esteja parametrizada em "Parâmetros do projeto (F6)\ Cronograma\ Lançamentos".  
Como essa funcionalidade é apresentada na visão de Tarefas, é possível incluir uma nova tarefa e lançar o seu cronograma no mesmo momento.  
Clicando no canto superior direito na letra inicial do cronograma (P, R, M, A, B), a visualização dos mesmos pode ser configurada de acordo com a necessidade do usuário. Para obter máxima performance é aconselhado desativar os cronogramas que não forem necessários, sendo que eles podem ser reativados a qualquer momento.  
Podem ser importados gráficos para a visualização dos lançamentos do cronograma do projeto e essa importação é realizada em "Anexos | Gráficos | Importar Gráfico Anexo". Nesse caso, deve-se verificar se o usuário que está efetuando a importação tem permissão para importar gráficos da Categoria que está tentando importar. O usuário pode criar seus próprios gráficos e efetuar a importação dos mesmos.

O Cronograma terá a sua interface hachurada nos períodos em que não será possível efetuar alterações, conforme definido nos parâmetros do projeto em "Opções | Parâmetros | TOTVS Obras e Projetos | Projetos | Cronograma | Gerais; - Somente para o cronograma previsto não serão permitidos lançamentos com valor acima de 100%.  
As tarefas de custo indireto são apresentadas com os seus valores, mas os mesmos não afetam o valor da etapa e da obra das quais fazem parte.

**Atenção:**Estão disponíveis os gráficos Cronograma – Análise Financeiro (Prev x Med x Real) e Cronograma – Análise Percentual (Prev x Med x Real).  
Sempre que houver alteração de tarefas no cronograma, seja ela por exportação do pert, exportação de medição de contrato, alteração manual diretamente no cronograma ou quaisquer outras alterações em tarefas, os valores das etapas e obras estarão desatualizados até que o cronograma seja calculado, ou seja, os valores das obras e etapas não são automaticamente atualizados.  
Serão consideradas no cálculo do cronograma somente tarefas, etapas e obras ativas.

**Cronograma para Cenários**  
A utilização do Cronograma para Cenários será igual à utilização para a Planilha de Atividades, assim, para cada um dos Cenários ativos será apresentado um cronograma.

**Valor da Tarefa**  
O valor de cada tarefa de serviço/atividade no cronograma é o resultado da multiplicação da quantidade da tarefa pelo valor do seu recurso associado(composição ou insumo). O valor da Composição como recurso na tarefa é o somatório do valor parcial de cada recurso associado(composição ou insumo). O valor parcial do recurso se obtém através do valor do custo unitário multiplicado pelo coeficiente do recurso da composição.

[Planilha de Atividades](http://tdn.totvs.com/display/LRM/Planilhas)

[Planilha de Serviços](http://tdn.totvs.com/display/LRM/Planilhas)
