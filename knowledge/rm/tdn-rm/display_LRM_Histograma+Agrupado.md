---
content_hash: e8f0b7f4a094d3a630900a507830de8706f7df92bd01e7ada38cc657de4b97d9
fetched_at: '2026-06-29T00:09:16.164284+00:00'
page_id: '421385473'
product: rm
source: tdn-rm
title: Histograma Agrupado
type: documentation
url: https://tdn.totvs.com/display/LRM/Histograma+Agrupado
version: 2
---

O Histograma Agrupado é uma visão anexa à funcionalidade "Geração de Pedidos em Suprimento/Faturamento" onde é possível visualizar todos os itens do pedido selecionado.   
 Para cada item são exibidas duas linhas distintas na listagem da funcionalidade: acatado e sugerido. A linha "Acatado" do item, mostrada em cor vermelha, traz os valores conforme foram pedidos. A linha "Sugerido", mostrada em cor verde, traz os valores da sugestão automática do sistema de como o pedido deveria ser feito e entregue, tomando por base os dados do planejamento de execução do projeto feito no cronograma.  
 Os períodos do projeto são exibidos e neles são marcados a quantidade de cada insumo que será entregue naquele período. Através do processo "Agrupar" é possível rearranjar as quantidades de entrega dos itens entre os períodos, conforme desejado. Para tal, selecione um insumo, acesso o menu Processos > Agrupar ou clique no botão "Agrupar" na barra de tarefas. Na tela que se abre, selecione à esquerda os insumos e, à direita, selecione os períodos dos quais deseja-se agrupar as entregas. Abaixo, no campo "Data de Destino", selecione a data na qual deseja-se que a entrega seja feita. Esta data deve ser menor que todos os períodos selecionados anteriormente. Após feito, execute o processo e as datas de entrega serão agrupadas conforme selecionado.  
 Por exemplo, se deseja agrupar as entregas de Areia que seriam feitas entre janeiro e junho para que o total seja entregue em janeiro, selecione o insumo, selecione os períodos que compreendem o período, indique a data de destino e execute o processo.  
 O histograma agrupado só permite alterar o agrupamento da data de entrega, nos itens do pedido.  
 As alterações que o histograma agrupado possibilita só podem ser utilizadas em pedidos que ainda não geraram movimento. Pedidos já movimentados não poderão sofrer alterações.

**Observações:**  
A ordem de pesquisa de centros de custo e departamento segue a seguinte lógica: Primeiro busca o centro de custo e departamento do serviço, se não encontrou busca o centro de custo e departamento da tarefa pai e assim sucessivamente até chegar à obra. Caso não encontre, então busca do projeto. Se não existir nenhum centro de custo e departamento, o movimento é gerado sem rateio. Se estiver enviando o centro de custo e departamento do projeto, o mesmo será 100% Ao enviar uma requisição, por obra, para o Gestão de Estoque Compras e Faturamento, são realizadas as seguintes etapas: \* Agrupamento dos insumos pertencentes a serviços diversos tais que estes pertençam a um mesmo período. O agrupamento por obra somente acontece durante o envio para o Gestão de Estoque Compras e Faturamento. \* Caso os serviços A e B, tenham o mesmo insumo necessário na mesma data e tais serviços sejam de obras diferentes, eles não podem ser agrupados. \* Depois de enviado o pedido ao Gestão de Estoque Compras e Faturamento o Histograma Discriminado conterá somente a(s) Obra(s) que correspondem aos serviços originalmente gerados na requisição. No Gestão de Estoque Compras e Faturamento, cada movimento, conterá uma única ocorrência de um dado insumo.  
Movimentação de Produtos no Gestão de Estoque Compras e Faturamento Na edição de um movimento, na pasta "Integrações / Projeto. " Informar, no campo "Identificador do Projeto, o projeto que deu origem ao movimento.  
No cadastro do item do movimento no Gestão de Estoque Compras e Faturamento Na edição de um item de movimento, na pasta "Integrações / Projeto informar, no campo "Identificador de Tarefa ", a tarefa que deu origem ao item do movimento. Estes campos serão obrigatórios de acordo com a parametrização feita no Gestão de Estoque Compras e Faturamento. Quando estes campos forem preenchidos o Totvs Obras e Projetos passará a disponibilizar informações referentes a estas movimentações em seus relatórios. Caso o Projeto não esteja informado não será possível informar a Tarefa. Caso a Tarefa esteja preenchida não será possível alterar o Projeto. Para os movimentos gerados pelo Totvs Obras e Projetos no Gestão de Estoque Compras e Faturamento o campo "Data da Entrega" conterá a data que os produtos relacionados naquele movimento deverão estar disponíveis na obra (local de estoque).
