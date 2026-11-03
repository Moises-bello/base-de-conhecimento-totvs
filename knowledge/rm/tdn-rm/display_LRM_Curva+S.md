---
content_hash: 14525ee3fee7d638ef9bcb95d624cd5fd4b74bf1a1da9b3c0f99e40cfc8bafaa
fetched_at: '2026-06-29T00:09:14.922959+00:00'
page_id: '421385307'
product: rm
source: tdn-rm
title: Curva S
type: documentation
url: https://tdn.totvs.com/display/LRM/Curva+S
version: 9
---

A curva S é uma ferramenta gerencial que tem como principal objetivo comparar o planejado x realizado.

Através dessa opção é possível visualizar um gráfico em 2D ou 3D de cada item da planilha, considerando pelo menos um dos grupos DNIT do período, de acordo com o cronograma Previsto, Realizado, Medido, Base e Apropriado.

Abaixo do gráfico são visualizadas os valores dos cronogramas selecionados distribuídos por tarefas e por período. Para definir qual cronograma (Base, Previsto, Realizado, Medido e Apropriado) será visualizado, basta selecionar na tela do processo.

A Curva S poderá ser visualizada nas opções Simples ou Acumulada.  
**Simples:** Ao gerar a Curva S serão listados os valores separados por períodos.

**Acumulada:** Ao gerar a curva S serão listados os valores acumulados dos períodos.  
Passo a Passo

1º) Na primeira tela do Assistente de geração da Curva S, é possível selecionar quais Grupos de Custo (DNIT) serão considerados na Curva S ou somente desmarcar a opção "Filtrar por grupo de custo" para que o filtro não considere Grupos de Custo. Deve ser selecionado o campo Origem da Informação, esta opção permite que os valores cadastrados na Planilha de Atividades, Planilha de Serviços ou em algum dos Cenários ativos sejam usados para a visualização da Curva S.

**Observação**  
O campo Origem da Informação fica habilitado caso o parâmetro de projeto (Opções - Parâmetros - Totvs Obras e Projetos - Projetos - Aba Planilha de Serviços - Utiliza Planilha de Serviços) estiver selecionado. Esta opção permite que os valores cadastrados na Planilha de Atividades, Planilha de Serviços ou algum dos Cenários ativos sejam usados para a visualização da Curva S. 

O campo Tipo Curva é responsável por separar os valores apresentados na Curva S conseguindo realizar um filtro por despesas ou por receita. Quando selecionado a curva S do tipo despesas ela trará os valores da mesma maneira que é feita hoje(tarefa no tempo), caso a opção desejada seja uma curva do tipo receita, a curva S tratá apenas os valores das tarefas do tipo receita

2º) Na segunda tela do Assistente de geração da Curva S, selecione quais Obras serão consideradas na Curva S. A forma de visualização Simples ou Acumulada e o Tipo da Curva, que poderá ser por Despesas ou Receitas.

**Base:** O cronograma tem como objetivo armazenar o planejamento inicial do projeto.

**Planejado:** É possível identificar mudanças ocorridas em caso de replanejamento e identificar se estas mudanças foram benéficas ou não e se outras ações deverão ser tomadas.

**Realizado:** Será acumulado no cronograma realizado o percentual ou quantidade apropriada da tarefa.

**Medido:** Será acumulado no cronograma medido o percentual ou quantidade apropriada da tarefa.

**Apropriado:** O Cronograma Apropriado, você pode associar cada movimentação às tarefas do programadas.

**Atenção:**  
O assistente de geração da Curva S oferece filtro por obra, porém ao visualizar a quantidade dos itens será exibida Obra, etapa e tarefa.

**Tarefa receita**  
Uma tarefa é considerada receita quando o recurso associado a ela é um insumo do tipo receita. Este insumo em seu cadastro pode ter um tipo de derivação ou não. Se o insumo derivado tiver fórmula, é necessário informar o Tipo de derivação "Derivado para tarefa x cronograma". Se o insumo receita não utiliza fórmula o tipo de derivação passa a ser "Não se aplica".  
Para que seja considerado na curva S as receitas, o tipo de curva deve ser "Receita". O filtro será: Por grupo de custo e por obras. A fórmula de visualização será: simples ou acumulada. O gráfico dispõe de duas formas de visualização: 2D ou 3D e divide por abas os cronogramas Planejado, Realizado e Medido.

**Curva S para a Planilha de Serviços e Cenários**  
A Curva S é gerada a partir da curva ABC de serviços que demonstra o total da quantidade e o valor do insumo utilizado na obra. Com estas informações a curva S aplica os percentuais cadastrados por período no cronograma da planilha de serviços.

Na Curva S serão exibidas as tarefas da Planilha de Serviços, onde as mesmas deverão ser listadas com as datas dos períodos conforme o parametrização (Opções - Parâmetros - Totvs Obras e Projetos - Projetos - Aba Cronograma - Período), o número de períodos e os tipos de períodos (Personalizado, Diário, Semanal, Semanal Corrido, Quinzenal, Quinzenal Corrido e Mensal).

**Atenção:**  
Antes de gerar a Curva S, é necessário que pelo menos o Cronograma Previsto esteja preenchido.  
O calculo realizado pela Curva S é feito da seguinte forma: O custo da tarefa em cada período é a soma de todos os recursos nela contida no período vigente, o valor do recurso se obtém da quantidade do mesmo para a tarefa multiplicado pelo seu percentual no período do cronograma multiplicado pelo seu preço unitário, lembrando que este preço considera a vigência do mesmo. O valor da Curva S é o valor real do custo da tarefa.

**Observação:**  
Esta funcionalidade não deverá estar disponível para projetos globais.
