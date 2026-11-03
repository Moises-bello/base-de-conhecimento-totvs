---
content_hash: 30f2eb415951b29a3e7613247f5731136d9b5779e49908e4b234346452151cc6
fetched_at: '2026-06-29T00:09:24.462819+00:00'
page_id: '423937916'
product: rm
source: tdn-rm
title: Filtro por Rateio da Solicitação de Compras Integração com o TOP 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937916
version: 2
---

Inserção de uma nova etapa no assistente de inclusão de cotação, para que o usuário possa informar parâmetros de filtro por rateio de Centro de Custo.   
O filtro poderá ser feito por Centro de Custo, Projeto, tarefa e Grupo Orçamentário, e será utilizado tanto na seleção de produtos quanto na sugestão de fornecedores da cotação.   
O uso do filtro de Rateio na sugestão de compras será opcional, podendo o usuário utiliza-lo ou não através de um check-box na tela mesma tela de filtro dos campos de rateio.  
A nova etapa foi implementada antes da tela de seleção de itens de movimento e permitirá filtrar os itens da cotação pelo rateio informado no item de movimento. Por exemplo:

* O usuário deseja ver apenas as solicitações do centro de custo XX.X, ou apenas do centro de custo X para o projeto projeto Y. etc;
* O lookup de tarefas filtrará apenas as tarefas referentes ao projeto informado;
* A etapa será apresentada apenas se na etapa anterior for selecionado algum movimento que utiliza o rateio de tarefas do TOP;
* Foi criado um check box "Usar o Filtro na Sugestão de fornecedores", para verificar se o filtro de rateio será utilizado na sugestão de fornecedores;
* A sugestão de fornecedores da cotação será alterada para respeitar o filtro de rateio informado nesta etapa apenas se o check-box "Usar o Filtro na Sugestão de fornecedores" estiver marcado.
