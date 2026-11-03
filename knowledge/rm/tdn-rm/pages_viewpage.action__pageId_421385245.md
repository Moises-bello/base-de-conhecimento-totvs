---
content_hash: 2f24c1824ab99637fc33274d0e96d89f31fee6260e6b186bca672b8f2db449eb
fetched_at: '2026-06-29T00:09:14.737558+00:00'
page_id: '421385245'
product: rm
source: tdn-rm
title: Medição de Itens do Contrato no Fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385245
version: 2
---

---

A medição de contrato consiste, resumidamente, em informar a quantidade que um serviço foi executado em um determinado período de um contrato.  
 Para a funcionalidade de Medição de Contrato do TOTVS Obras e Projetos serão desenvolvidas páginas Web utilizando o Portal/ FLUIG.  
 São três páginas para a Medição de Contrato, da seguinte forma:

* Página com a listagem dos Contratos e seus respectivos Períodos com opções para realizar uma Medição por período;
* Página com os detalhes de um Contrato, com informações dos itens associados, períodos gerados e itens medidos.
* Página com um formulário para Incluir, editar e excluir medições para um período de contrato.

**Página de Listagem de Contrato e Períodos**

Na página de listagem dos Contratos serão mostradas as seguintes informações:

* Número do Contrato (será um link que ao clicar será redirecionado para a página com os detalhes do Contrato e suas medições);
* Finalidade do Contrato;
* Tipo (à pagar ou à receber)
* Cliente/Fornecedor;
* Data do Contrato;
* Data de Início do Contrato;
* Data de Término do Contrato;
* Periodicidade;
* Total do Contrato;
* Total de Medição;
* Posição Atual;
* Saldo Contratual.

Ainda na listagem dos Contratos ao clicar no link "Exibir detalhes..." serão exibidos as seguintes informações:

* Código do Período (será um link para realizar a medição para o período);
* Data Início
* Data Fim
* Data da Liberação da Medição
* Quem liberou a medição
* Total Medido no Período
* Valor Retido no Período

Para cada período terá um botão chamado "Medir" para realizar a medição para o período. Ao clicar nesse botão será redirecionado para a página de Incluir/Editar/Excluir medições para um período de Contrato. Caso o período já esteja liberado o botão irá se chamar "Visualizar" e levará para a mesma página porém nenhuma informação poderá ser editada.  
 Existe um botão 'Pesquisar' para que seja pesquisado através do número ou cliente/fornecedor do contrato. Também tem um filtro, onde lista os períodos abertos ou todos, que por default, lista os em aberto.

**A página de detalhes de um Contrato** contém os mesmos dados de contrato da página de listagem e contém três pastas abas:

* Períodos: Dados dos Períodos de Contrato com um botão chamado "Medir" ou "Visualizar para cada período que leva para a página de Incluir/Editar/Excluir Medição de Período do Contrato.
* Itens Associados ao Contrato: Uma lista com as informações dos itens que foram associados ao contrato
* Itens Medidos: Uma lista com informações de medições que já foram realizadas no Contrato

**Página de Incluir/Editar/Excluir Medição de Item de Contrato** Essa página poderá incluir/editar/excluir medições de um determinado período de Contrato. Será composta por uma lista contendo os itens (serviços) associados ao contrato que serão medidos. Haverá também um filtro para filtrar por item (serviço) chamado "Pesquisar Tarefa".  
 Para cada item haverá um formulário onde será definido qual o percentual, quantidade ou valor que deseja informar para o item, além do valor retido para o período.  
 Ao informar um percentual, a quantidade e valor já será calculado automaticamente. Ao informar a quantidade, o percentual e o valor serão calculados automaticamente. Para cada item haverá um botão salvar, editar e excluir a medição.   
 Cada item de contrato é mostrado como um item de uma lista. O Código e Nome do item é o título. Terá um link "Exibir detalhes..." que ao clicar irá mostrar mais informações do item.

* Código, Nome, Descrição e Unidade do Item (Serviço)
* Quantidade, Valor e Percentual Medido
* Valor Retido do item
* Quantidade, Valor e Percentual Medido acumulado
* Quantidade e Valor Contratado
* Saldo de Quantidade e Valor
* Valor unitário atual e Valor unitário liberado no período

Ao editar um item, na janela que será aberta serão exibidas também três abas para Rateio de Produtos, Centro de Custo e Estado/Município.  
 Para informar um Rateio haverá um campo para escolher o item de Rateio e um campo para definir o Valor do Rateio. Esse campo de Valor será correspondente ao campo medido do item.  
 Exemplo: Se o campo medido for percentual o campo irá se chamar Percentual. E assim para cada campo que pode ser medido (Percentual, Quantidade e Valor).  
 Para cada item de Rateio definido será mostrado em uma lista sua descrição e valor informado além de um botão para exclusão.
