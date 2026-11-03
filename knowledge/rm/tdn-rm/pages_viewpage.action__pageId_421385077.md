---
content_hash: 84e1d20cd524352d32e4c97393c3b2aa3b76d13a3064059d959abb55bcf96566
fetched_at: '2026-06-29T00:09:13.645580+00:00'
page_id: '421385077'
product: rm
source: tdn-rm
title: Associação de Itens ao Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385077
version: 6
---

Os itens da Planilha de Atividades ou da Planilha de Serviço do Projeto podem ser associados ao contrato de duas maneiras: associando todos os itens que estão apresentados na tela de Associação de Itens do projeto ao contrato selecionado; ou associando item a item ao contrato selecionado.

Caso escolha a primeira opção, através do botão "Associar quantidade total dos Itens selecionados ao contrato" serão associados todos os itens selecionados do projeto com a quantidade contratada igual à quantidade orçada.  
Os valores a serem associados poderão ser "Valor Unitário", "Custo Unitário" ou "Nenhum" Ao associar o item com a opção "Valor unitário" selecionado, o valor associado da tarefa será com o BDI diferenciado. Ao associar o item com a opção "Custo Unitário" selecionado, o valor associado será sem o BDI diferenciado. E ao associar o item com a opção "Nenhum" selecionado, não será associado nenhum valor e o valor associado anteriormente não sofrerá alterações. Esta opção é útil quando se deseja preservar o valor associado que tenha sido digitado manualmente ou via realinhamento.

Caso escolha associar pela segunda opção, será possível preencher as Quantidades e Valores Contratados diretamente na grade de Associação Item por Item. Outra forma de associar cada item é clicar no botão "Associação percentual dos itens selecionados" onde é possível informar o percentual a ser contratado daquele item.

Antes do processamento das associações ou remoção de associações serão validadas as solicitações e apresentadas as restrições ao usuário. As tarefas que não estiverem com um CHECK na primeira coluna não farão parte do processo de associação mesmo que tenham recebido valores nas colunas de quantidade, ou através da digitação ou pelos mecanismos de associação total e parcial.  
Em nenhuma dessas opções é permitido contratar uma tarefa que esteja desativada.

Não é possível associar um item com valor menor ou igual a 0 (zero).  
Itens com quantidades zeradas podem ser associados ao contrato, desde que o parâmetro "Permitir associar ao Contrato itens com quantidade zero (Prest.Serviço, Parc.Fixas e Marco Cont.)" esteja devidamente configurado.  
Para maiores detalhes, verifique o help de parâmetros em: 

Caso alguma associação seja excluída, na existência de Adiantamentos de Contrato liberados, ao executar o processo, o total contratado dos itens será validado em relação a soma dos saldos dos adiantamentos, onde o total dos itens não poderá ser menos que os saldos disponíveis.

A associação de itens ao contrato pode ser realizada a qualquer momento, mas para este item ser medido e liberado devem existir períodos ainda a serem liberados.  
Itens associados posteriormente a liberação de algum período, não serão exibidos neste período.

Existem dois períodos vinculados ao contrato.  
Num primeiro momento, foram associados 2 itens ao contrato, A e B. Para o primeiro período os itens A e B foram medidos com percentual de 80% para cada item e foram liberados.  
Em determinado momento resolve-se associar ao contrato um terceiro item. Item C. Se observado, no primeiro período o item C não será apresentado, pois o primeiro período ja foi liberado. Porém no segundo periodo serão apresentados os itens A e B ainda com o restante a ser medido de 20%, e 100% a ser medido do item C, associado posteriormente a liberação do primeiro período.

**Associação para Item do Contrato ou para Aditivo do Contrato**  
  
Clicando em Associação de itens ao contrato será exibida mensagem sugerindo a realização do calculo do projeto. Em seguida apresentará a janela "Itens do Contrato" com as informações:   
Código, Código Auxiliar da Tarefa, Nome, Descrição, Unidade, Quantidade e Valor Unitário do item preenchidos de acordo com as tarefas.

**Quantidade Contratada, Valor Contratado** – Para associar itens do contrato.

Clique no ícone "Associar Total" ou "Associar Parcial". A associação total faz a quantidade contratada igual a quantidade total e com o valor contratado igual ao valor unitário, mas somente para o item selecionado. Quando a associação for parcial informe a quantidade e o valor contratado se o mesmo for efetuado por item. Nesse caso, será considerada a quantidade de obras. Se a associação parcial for efetuada por etapa ou por obra basta informar o percentual. Neste caso, será calculado o percentual informado para cada serviço da etapa ou obra, de acordo com o item selecionado (etapa ou obra). A associação de itens ao contrato pode ser feita tarefa a tarefa, por etapa ou por obra. Para a associação por etapa ou por obra, é solicitado o percentual a ser associado e é feita a associação, automaticamente, de todos os itens da etapa ou da obra.  
Ao marcar a opção 'Não associar tarefa a contrato em mais de 100%' através do menu Opções | Parâmetros | Totvs Obras e Projetos | Projetos, pasta Diversos, subpasta Contrato, é verificado todas as possibilidades que podem ocorrer na associação sendo portando definido um padrão de cores para simbolizar o status de uma tarefa perante a associação.

Os padrões são os seguintes:  
Azul Caso a tarefa esteja associada ao contrato  
Vermelho Caso a tarefa esteja associada ao mesmo ou a outro contrato e esteja com 100% ou mais associada ao contrato.  
Oliva Caso a tarefa esteja associada a outro contrato e esteja com menos de 100% associada ao contrato.

O sistema permite alterar a quantidade das tarefas, mesmo que estas já estejam associadas a contratos. Caso ela não esteja associada 100% a um outro contrato e esteja marcado no parâmetro que não se pode associar mais que 100% é mostrado um aviso informando ao usuário que alteração nas quantidades ou preços unitários afetará os contratos gerados, caso confirme é inserida a diferença, se a mesma for para maior.  
É possível efetuar um realinhamento dos valores unitários contratados para cada serviço associado ao contrato ou aos aditivos de contrato. Para isso, basta posicionar o mouse no campo "Val. Unit. Contratado" e informar o valor desejado.  
As alterações dos valores unitários contratado dos serviços associados ao contrato, refletem nos aditivos contratuais e vice-versa.

Ao associar um item ao contrato ou a um aditivo, serão apresentados os itens do projeto de acordo com o tipo de planilha definido no momento do cadastro do contrato: Planilha de Atividades ou Planilhas de Serviços.   
Se o contrato possuir algum aditivo e este possuir itens com quantidades associadas, tais quantidades serão somadas com as quantidades dos itens do contrato, caso exista.  
Se removermos uma associação dos itens do aditivo, apenas será removido a quantidade relacionada com os aditivos e vice versa.  
Caso o projeto esteja com a parametrização Integração ECM –WF ativa, no momento da associação dos itens do projeto ao contrato, o sistema dispara um Workflow para o ECM solicitando a criação de um atendimento.     
Os itens do projeto só serão associados ao contrato depois que o atendimento for concluído como aprovado. Caso o atendimento seja concluído como reprovado, identifique quais mudanças devem ser efetuadas no projeto e acione processo 'Associar Itens ao Contrato' novamente para que um novo atendimento seja gerado para nova aprovação.   
Para atendimentos abertos com essa finalidade, não é possível Aprovação pelo TOP, ou seja, o atendimento deverá ser acessado pelo ECM.   
Em caso de remoção dos itens associados ao contrato, será gerado um novo atendimento para o ECM. O atendimento deverá ser concluído com aprovação para que os itens associados sejam excluídos.

Se um item é associado ao contrato com a quantidade 100 e depois é associado um item ao aditivo de contrato com a quantidade 50, aparecerá na visão dos itens do contrato a quantidade 150 e no item do aditivo a quantidade 50. Ao remover a associação do item do contrato, o registro não sumirá por completo, aparecerá a quantidade 50 do aditivo de contrato. Por sua vez, se remover a associação do item do aditivo, o registro sumirá e nos itens do contrato aparecerá a quantidade 100.

Aviso

Apenas as obras podem ser associadas a contratos totalizadores.  
Não é possível fazer associação parcial para contrato a "Receber". A associação pode ser feita com uma quantidade maior que a planejada (orçada). O percentual de associação da etapa ou obra deve ser superior a 0 e inferior a 101. Caso a quantidade da obra seja alterada após a associação das tarefas ao contrato o sistema NÃO ajusta,. automaticamente, as quantidades associadas. Isso deverá ser feito manualmente.  
Para excluir um aditivo de contrato que possua itens associados, é necessário remover as associações, para só então excluir o aditivo de contrato.

**Rateio Default de Produtos**  
O rateio default deve ser incluído para dividir entre produtos do RM Nucleus a medição executada em um item de contrato. O percentual de 100% deve ser distribuído entre os produtos inseridos. Não é permitido que a soma dos percentuais dos produtos ultrapasse ou seja menor que 100%. A validação será feita ao clicar em OK na tela de visão do rateio default

Quando existe um rateio default cadastrado para o contrato, após Salvar a medição o rateio por produto é lançado automaticamente.  
Depois disso, caso a medição seja alterada, o rateio deverá ser alterado também pelo usuário. Caso isso não seja feito o sistema irá exibir uma mensagem informando "rateio não fecha em 100%".
