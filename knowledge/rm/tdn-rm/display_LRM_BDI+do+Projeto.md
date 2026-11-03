---
content_hash: 8ee6778e14a13d9028a8be04fe1e3c752ce0832d92e7a9174423b7fea64832c6
fetched_at: '2026-06-29T00:09:15.473038+00:00'
page_id: '421385389'
product: rm
source: tdn-rm
title: BDI do Projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/BDI+do+Projeto
version: 84
---

* Se o parâmetro "Aplica BDI de forma absoluta" estiver marcado é o BDI diferenciado for igual a um, aplica apenas o BDI projeto sobre cada tarefa, se o projeto utiliza BDI projeto e o parâmetro BDI é aplicado sobre o custo unitário do serviço.
* Se o parâmetro "Aplicar BDI de forma absoluta" não estiver selecionado o cálculo será realizado como funcionava antes da criação do parâmetro "Aplicar BDI de forma absoluta".  
   Mesmo utilizando o BDI diferenciado de forma absoluta, a aplicação do BDI do grupo de custo continua sendo aplicado de forma normal.  
   Para selecionar o parâmetro "Aplicar BDI diferenciado de forma absoluta" o parâmetro Aplicar BDI sobre o projeto deverá estar definido como "Custo unitário do serviço". Não deve ser permitindo que o parâmetro "Aplicar BDI diferenciado de forma absoluta" seja selecionado se a opção de aplicar BDI sobre o projeto estiver definida sobre o "Valor total do projeto".  
   **Observações:**  
   A aplicação do BDI diferenciado de forma absoluta não irá interferir na aplicação do BDI do Grupo de custo. Ou seja, o BDI do grupo de custo continua sendo aplicado da forma atual. Quando houver vigência de preços a aplicação do BDI diferenciado de forma absoluta também deverá ser realizada. A Curva ABC deverá considerar a incidência do parâmetro "Aplicar BDI diferenciado de forma absoluta".  
   **Vigência de preço:**  
   Marque a opção Somente o Cronograma  ou Todo Projeto, se desejar utilizar a vigência de preço. Utilizando vigência de preço o cronograma pode ser recalculado considerando a vigência de preços de insumos para cada período do cronograma previsto. Os períodos que não tiverem um preço com vigência, será considerado o preço ativo.  
   **Observações:**  
   Caso o cronograma previsto não esteja 100 % programado haverá diferença entre os cronogramas com e sem vigência das etapas e obras. Não é permitido cadastrar duas ou mais vigências com o mesmo período e aplicação para um insumo.  
   **Atenção:**  
   Caso a vigência esteja sobre "Todo o projeto", nos relatórios de orçamento (por exemplo de Composição e Insumo) para o preço unitário dos recursos não será considerado o preço vigente de cada período e sim o preço ativo, pois a mesma composição pode estar sendo utilizada em diversas tarefas e as mesmas podem ter cronogramas diferentes, conseqüentemente a composição terá preços diferentes por período. Por isso não aconselhamos o uso de vigência em orçamentos que precisem demonstrar a consistência entre o preço unitário da composição com o preço unitário do serviço.  
   **Exemplo:**   
   Considere que as tarefas abaixo, possuem a mesma composição associada. Observe que os cronogramas são diferentes. Nesse caso, o preço da composição poderá ser diferente, se houver preço diferente para cada período.  
      Tarefas               Períodos  
    001.01.01          10     30        60  001.01.15          40     50        10  
   O Parâmetro "Aplicar Preços em Percentual" ficará habilitado se uma das opções "Somente o Cronograma" ou "Todo Projeto" estiverem marcadas, e segue a regra:  
   1º regra - Criação de um preço para o insumo. Este preço pode ou não esta ativo. 2º regra - Ao criar novos preços, os mesmos serão calculados de acordo com percentuais   
   Alteração no preço de menor período de vigência fará com que ao salvar, os preços dos demais períodos sejam recalculados com base no percentual aplicado.  
   **Exemplo:**  
   1º preço            2º preço                                   3º preço                               4º preço 20,00                10% do 1º preço = 22,00           15% do 2º preço = 25,30       -30% do 3º preço =  17,71    
   As validações estão descritas no help Preço de Insumo
