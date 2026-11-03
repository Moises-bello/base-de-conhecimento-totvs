---
content_hash: db3dedc14613cd4a3843ec9ddcc35eedbf0de5e89ef8cb7aada6519cce16a8be
fetched_at: '2026-06-29T00:10:10.063008+00:00'
page_id: '452719813'
product: rm
source: tdn-rm
title: Lançamentos Multicoligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719813
version: 8
---

O assistente de Lançamento Multicoligadas permite que grupos de eventos, férias, líquido de rescisão e finalização das férias sejam lançados para todas as coligadas em uma única execução.  
   
Lançar movimento próximo mês  
Quando marcado irá lançar o movimento para o próximo mês.   
**Atenção**  
Caso o parâmetro 'Lança movimento próximo mês' esteja marcado, os processos: Lançar Férias, Finalizar Férias e Lançar Líquido de Rescisão e lançamento do grupo de eventos, considerarão a competência seguinte. Nesse caso serão apresentadas todas as coligadas e poderá ser informado um período único para o lançamento.  
Lança Líquido de Rescisão  
Com este parâmetro marcado será processado o lançamento dos eventos de liquido rescisão, caso os eventos estejam informados no parametrizador,  para os funcionário selecionados no grupo de eventos selecionado e coligadas.  
Também é possível lançar o líquido da Rescisão complementar. Quando marcado o parâmetro, é habilitado o período para lançamento.  
   
Lança Férias  
Com este parâmetro marcado será processado o lançamento de férias para os funcionários selecionados no grupo de eventos selecionado e coligadas.  
   
Finaliza Férias  
Com este parâmetro marcado será finalizadas as férias para os funcionários selecionados no grupo de eventos selecionado e coligadas. Para que as férias sejam finalizadas é necessário que as mesmas estejam lançadas para o funcionário e que a data final das férias seja dentro da competência atual da coligada. Caso não seja selecionado o grupo de eventos, as férias não serão finalizadas.

Observação:

Caso o estagiário tenha recesso iniciando e finalizando no mesmo mês não será feita finalização ao mesmo tempo que lança o recesso pelo módulo Multicoligada, porque a atualização do funcionário para situação G - Recesso Remunerado de Estágio será feita no lançamento e como o estagiário ainda não está nessa situação não tem como finalizar ao mesmo tempo que lança.

Caso ocorra a situação de inicio e fim no mesmo mês faça a finalização pelo módulo Finaliza em Férias ou se ainda necessitar lançar Multicoligada, execute novamente o processo para finalização.

**Observação**  
Para esses lançamentos, serão respeitadas as seleções de funcionários previamente informadas nos grupos de eventos que farão parte da seleção, por esse motivo, é obrigatório a informação do grupo de eventos desejado nos parâmetros específicos de cada coligada.  
   
**Atenção:**  
O período é apresentando na tela de seleção de coligadas somente quando o lançamento é para o mês atual. Assim serão informadas apenas as coligadas com mesma competência de apuração.  
Ao finalizar férias para o próximo mês, a situação de férias do funcionário ficará 'X-Finalizadas Próximo Mês' e na liberação de competência a situação passará para 'F-Finalizadas'.  
   
**Observação:** É possível habilitar o Fracionamento de Jobs na execução desse processo caso o cliente utilize ambiente N camadas. Assim poderá dividir o processamento de suas coligadas na quantidade de processos desejados conforme a parametrização do seu ambiente.
