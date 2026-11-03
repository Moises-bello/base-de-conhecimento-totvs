---
content_hash: 5edf3bdc7b94f4571b01366f69c05e7f3c5be324ce00e32b7138273ead4536fc
fetched_at: '2026-06-29T00:09:15.379810+00:00'
page_id: '421385360'
product: rm
source: tdn-rm
title: Contratos de Timesheet
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Timesheet
version: 3
---

---

Para o controle de consumo dos recursos relacionados com timesheet, isto é, tarefas e insumos, o contrato de insumos deverá ser utilizado, considerando algumas características citadas a seguir.  
    
 **Contratos de Insumo**

Na tela de criação de um novo , há um campo check (Timesheet), que caso esteja selecionado define que o contrato terá um controle por TimeSheet. Este atributo apenas aparecerá, ao criar um novo contrato e definir seu tipo como "Contrato de Insumo". Caso o usuário selecione o Contrato de Insumos, uma vez salvo o contrato, não será possível marcar/desmarcar o uso do Timesheet.

**Associação e Consumo de Objetos**

O processo de associação de objetos em contrato de insumos que utiliza Timesheet, tem colunas ("Nome" e "Tipo") incluídas na visão da tela, pois neste processo, são associado os membros das equipes, que estão associadas a um insumo. Sendo o contrato de timesheet, será exibido no passo de seleção de grupo de custo, apenas grupos que fazem parte do Grupo Mão de obra, e no passo de insumos serão exibidos, na associação de objetos, os membros que estiverem sendo utilizados no projeto.  
 Como o membro está associado a um insumo, o custo unitário deste membro por padrão será o custo do insumo, mas caso o usuário queira modificar este valor, é possível a edição deste custo. A utilização da associação de membros ao contrato no modulo de Timesheet pode ser usada apenas se o parâmetro de projeto "Utilizar Alocação de Membros de Equipes nas Tarefas de Timesheet" estiver selecionado. Caso este parâmetro não esteja selecionado, o comportamento da associação de objetos seguirá o mesmo padrão do contrato de insumo, o usuário irá associar ao contrato os insumos e não mais o membros.

**Importação de Insumos da Apropriação**

Para realizar o consumo de objetos pela apropriação, na visão de períodos de contrato, há o processo "Atualizar consumo pela Apropriação" e este processo é responsável por importar as informações de insumos que tiveram apropriações e juntamente com seus respectivos valores, isto é, valores e quantidades apropriadas, no período.  Se o parâmetro de projeto "Utilizar Alocação de Membros de Equipes nas Tarefas de Timesheet" estiver selecionado a consulta será feita pelo Funcionário/Terceiro da apropriação e será consumido a quantidade apropriada na tarefa, mas se este parâmetro não estiver selecionado a consulta será feita apenas pelo insumo apropriado, apropriações que não contenham Funcionários/Terceiros não serão consumidas pelo processo. Nesse processo serão recuperadas as informações de apropriação que estiverem no intervalo do período do contrato e os responsáveis pelo apontamento. Na opção de menu em processos também é possível selecionar o processo de "Consumir Objetos de contrato", quando o mesmo for selecionado será exibido apenas os insumos medidos pelo processo de "Atualizar consumo pela apropriação". Como o valor hora de cada membro associado poderá ser diferente do valor do insumo apropriado, tem-se a necessidade de na importação de apropriação, executar a revalorização da apropriação. A revalorização será feita entre o custo unitário do membro associado ao contrato multiplicado pela quantidade de horas apropriadas. Caso seja preciso excluir o consumo da apropriação, no anexo de ''atualizar consumo pela apropriação é possível excluir.

**Vínculo entre Contratos**

Para contrato de insumos do tipo Timesheet há a opção de vínculo entre contratos, que é feita através do anexo "vínculo de Contratos". Esse vínculo entre contratos apenas poderá ocorrer, se o vínculo for entre um contrato "A Pagar" vinculado a um "A Receber".  O vínculo entre contratos apenas poderá ocorrer, se os dois contratos obtiverem o mesmo número de períodos, caso contrário o vínculo não será feito. Este processo, apenas será considerado na liberação de períodos, onde o contrato que contém o vínculo só terá o seu período liberado, se o período correspondente do contrato vinculado já estiver liberado. O contrato de insumo só irá considerar que é a receber se for selecionado a opção 'Timesheet', do contrário o TOP irá desabilitar a opção 'a receber' e automaticamente manter 'a pagar'.

**Liberação de Períodos de Contrato**

A liberação de períodos desse tipo de contrato ocorre normalmente, tanto através do processo de "Liberar Período" quanto do processo de "Gerar Integração com Suprimento/Faturamento". O rateio de tarefas é automático na liberação para o Suprimento/Faturamento, considerando as tarefas que tem apontamentos do membro associado ao contrato no intervalo do período a ser liberado. Ao liberar esse tipo de contrato, o vínculo entre contratos é considerado, e em caso de inconsistência a liberação é abortada. No momento da liberação, na aba de Detalhamento de Retenção do processo de Liberar Período deverá ser incluído o campo quantidade, pois a apropriação trabalha com quantidade e no caso de timesheet a quantidade de horas poderá ser deduzida.

**Cancelamento de Períodos Liberados do Contrato**

O cancelamento do período liberado, ocorre normalmente. É possível realizar o cancelamento de liberação de períodos de contratos (via Suprimentos/Faturamento ou Financeiro) bastando apenas acionar o processo "Cancelamento de liberação" que o mesmo será cancelado. Porém caso o movimento gerado através da liberação já tenha sido alterado, o cancelamento não pode ser realizado. Quando o "Cancelamento de Liberação" é realizado o movimento no BackOffice é excluído e no Totvs Obras e Projetos o período volta para o estado consumido.

**Anexo de Objeto de contrato**

O anexo de objeto de contrato que exibe as informações de quantidade contratada, valor contratado e consumo é modificado para exibir o nome da pessoa associada ao contrato.

 Informações Complementares

---

[Alocação de Recurso](http://tdn.totvs.com/pages/viewpage.action?pageId=421385140)

   
   Como Fazer

---
