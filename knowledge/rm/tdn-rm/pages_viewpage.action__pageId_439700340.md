---
content_hash: 128df6ea8b209f2b25187373673f255b463dad866fe4cd1672d077948a87b92a
fetched_at: '2026-06-29T00:09:52.913193+00:00'
page_id: '439700340'
product: rm
source: tdn-rm
title: Associação de Itens ao Aditivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439700340
version: 8
---

A partir da versão 12.1.25, o cadastro de aditivo de contrato no TOTVS Construção Obras e Projetos, passou por uma revitalização; e a associação de itens ao aditivo que antes era feita através de um processo, agora é feita diretamente na tela de edição do aditivo:

Através dos botões de Novo item  e Alteração de item contratado , podemos especificar qual o tipo de alteração será feita no contrato.

Na inclusão de novo item, é apresentada tela contendo todas as tarefas da planilha para que possa informar qual será incluída através do aditivo:

A associação poderá ser feita através da seleção das tarefas e um percentual informado, clicando em aplicar:

Ou diretamente nos campos das grandezas na linha da respectiva tarefa:

Da mesma forma, a remoção de associação ocorre quando se seleciona os itens que estiverem na cor azul.

O sistema permite definir como o valor poderá ser associado: Valor unitário, Custo Unitário ou Nenhum.

Na alteração de item contratado, são apresentadas as tarefas já associadas ao contrato para que possa proceder com a alteração desejada:

Os itens do aditivo serão apresentados de acordo com o tipo de associação:

Importante

Ao marcar a opção 'Não associar tarefa a contrato em mais de 100%' através do menu Opções | Parâmetros | Totvs Obras e Projetos | Projetos, pasta Diversos, subpasta Contrato, é verificado todas as possibilidades que podem ocorrer na associação.  
   
O sistema permite alterar a quantidade das tarefas, mesmo que estas já estejam associadas a contratos. Caso ela não esteja associada 100% a um outro contrato e esteja marcado no parâmetro que não se pode associar mais que 100% é mostrado um aviso informando ao usuário que alteração nas quantidades ou preços unitários afetará os contratos gerados, caso confirme é inserida a diferença, se a mesma for para maior. É possível zerar a quantidade de um item para manter o histórico de alteração sem necessariamente remover o item .

Observações:

Ao associar um item ao contrato ou a um aditivo, serão apresentados os itens do projeto de acordo com o tipo de planilha definido no momento do cadastro do contrato: Planilha de Atividades ou Planilhas de Serviços.   
Se o contrato possuir algum aditivo e este possuir itens com quantidades associadas, tais quantidades serão somadas com as quantidades dos itens do contrato, caso exista.  
Se removermos uma associação dos itens do aditivo, apenas será removido a quantidade relacionada com os aditivos e vice versa.  
Caso o projeto esteja com a parametrização [Integração ECM –WF](http://tdn.totvs.com/pages/viewpage.action?pageId=421385430)  ativa, no momento da associação dos itens do projeto ao contrato, o sistema dispara um Worflow para o ECM solicitando a criação de um atendimento.     
Os itens do projeto só serão associados ao contrato para medição depois que o atendimento for concluído como aprovado. Caso o atendimento seja concluído como reprovado, identifique quais mudanças devem ser efetuadas no projeto e acione processo 'Associar Itens ao Contrato' novamente para que um novo atendimento seja gerado para nova aprovação.   
Para atendimentos abertos com essa finalidade, não é possível Aprovação pelo TOP, ou seja, o atendimento deverá ser acessado pelo ECM.   
Em caso de remoção dos itens associados ao contrato, será gerado um novo atendimento para o ECM. O atendimento deverá ser concluído com aprovação para que os itens associados sejam excluídos.    
Por sua vez, se remover a associação do item do aditivo, o registro sumirá e nos itens do contrato aparecerá a quantidade 100.  
  
Não é possível fazer associação parcial para contrato a "Receber". A associação pode ser feita com uma quantidade maior que a planejada (orçada). O percentual de associação da etapa ou obra deve ser superior a 0 e inferior a 101. Caso a quantidade da obra seja alterada após a associação das tarefas ao contrato o sistema NÃO ajusta,. automaticamente, as quantidades associadas. Isso deverá ser feito manualmente.  
Para excluir um aditivo de contrato que possua itens associados, é necessário remover as associações, para só então excluir o aditivo de contrato.

**Rateio Default de Produtos**  
O rateio default pode ser incluído para dividir entre produtos do RM Nucleus a medição executada em um item de contrato. O percentual de 100% deve ser distribuído entre os produtos inseridos. Não é permitido que a soma dos percentuais dos produtos ultrapasse ou seja menor que 100%. A validação será feita ao clicar em OK na tela de visão do rateio default

Quando existe um rateio default cadastrado para o contrato, após Salvar a medição o rateio por produto é lançado automaticamente.  
Depois disso, caso a medição seja alterada, o rateio deverá ser alterado também pelo usuário. Caso isso não seja feito o sistema irá exibir uma mensagem informando "rateio não fecha em 100%".
