---
content_hash: 77f81f135581ab627b6c991f2bfba07e7d3a9dbb5428ab230dbe70806dd76730
fetched_at: '2026-06-29T00:09:15.298559+00:00'
page_id: '421385338'
product: rm
source: tdn-rm
title: Cronograma de Desembolso
type: documentation
url: https://tdn.totvs.com/display/LRM/Cronograma+de+Desembolso
version: 8
---

O Cronograma Desembolso é utilizado para exibir os gastos do projeto, discriminados por tarefa e insumo em cada período. Pode ser acessado pelo menu Planejamento | Cronograma Desembolso. O módulo respeita as permissões de acesso em Serviços Globais |Perfis e as parametrizações efetuadas nos parâmetros do Projeto para Cronograma |  e   e .

Para gerar o Cronograma Desembolso é necessário escolher qual a fonte de informação, ou seja, qual planilha será utilizada: as principais (Planilha de Atividades ou Planilha  de Serviços) ou algum dos Cenários ativos. O Cronograma Desembolso permite visualizar a receita e despesa do projeto, para que o planejador verifique o que será gasto nos períodos e se a receita para aquele período será maior ou menor que os gastos.

Na tela do Cronograma Desembolso serão listadas as datas dos períodos criados conforme a parametrização. Também é possível visualizar as tarefas de despesas e receita, que poderão ser identificadas através da coluna "Tipo Tarefa" presente na visão. Para melhor visualizar a receita e a despesa é possível agrupar a visualização por tipo, arrastando a coluna "Tipo Tarefa" acima das outras colunas e soltando.

Para obter essa previsão de gastos é utilizado como pré-requisito o cálculo do Histograma (Curva S), que pode ser feito assim que o cálculo do Cronograma de Desembolso é acionado ou diretamente pelo processo  . Existem duas formas distintas de calcular o Cronograma de Desembolso:   ou considerando também os contratos do projeto . Uma vez calculado, o Cronograma Desembolso utilizará as quantidades geradas pela Curva S para definir os desembolsos para cada insumo/tarefa/período, levando em consideração a condição de pagamento de cada insumo, gerando a previsão dos pagamentos a serem efetuados durante a execução do projeto.

O parâmetro "**Considera prazo de ressuprimento no cronograma de desembolso**", localizado em **Parâmetros do Projeto > Integração > Financeiro > Geral**, é considerado no cálculo do cronograma de desembolso que originará os lançamentos. Sendo assim, o prazo de ressuprimento de cada insumo será considerado caso o parâmetro esteja marcado, possibilitando que os insumos sejam pedidos com antecedência, para que na data de utilização já tenham sido entregues. Além disso, o cronograma desembolso utiliza a condição de pagamento do insumo.

O cálculo realizado pelo Cronograma de Desembolso é feito da seguinte forma: O custo da tarefa em cada período é a soma de todos os recursos nela contida no período vigente, o valor do recurso se obtém da quantidade do mesmo para a tarefa multiplicado pelo seu percentual no período do cronograma multiplicado pelo seu preço unitário, lembrando que este preço considera a vigência do mesmo. Os valores do Cronograma de Desembolso é o valor real do custo da tarefa.

**Exemplo 01:**Caso seja informado à requisição do material no cronograma no 2º período (Fevereiro), na condição de pagamento do insumo estiver 30 dias e o campo prazo ressuprimento não constar informação. A compra do insumo será feita em Fevereiro e o desembolso será em Março.

Cronograma de compra  
  
Jan          Fev          Mar  
               x  
  
Cronograma de desembolso  
  
Jan          Fev          Mar  
                               x

Seguindo o exemplo acima, porém constando informação de 30 dias no campo prazo ressuprimento. A compra do insumo será feita em janeiro e o desembolso será em fevereiro.  
  
Cronograma de compra  
  
Jan          Fev          Mar  
x  
  
Cronograma de desembolso  
  
Jan          Fev          Mar  
                X

**Exemplo 02:**

Observação

Importante lembrar que o cálculo leva em consideração o número de dias e parcelas da condição de pagamento.

Exemplo:

* Sem prazo de ressuprimento e com pagamento em 30 dias para cronograma no mês de **Maio**

             01/05 + 30 dias = Desembolso em 31/05 devido ao mês de Maio ter mais de 30 dias.

* Sem prazo de ressuprimento e com pagamento em 30 dias para cronograma no mês de **junho**

             01/06 + 30 dias = Desembolso em 01/07 devido ao mês de Junho ter somente 30 dias.

---

 Anexos

 

 

 Processos
