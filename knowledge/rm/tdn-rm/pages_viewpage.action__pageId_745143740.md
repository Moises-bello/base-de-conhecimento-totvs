---
content_hash: 8bb6c376bed345cb66df615dded9b9d5ce8930933490b8f21c6eb815413fcebb
fetched_at: '2026-06-29T00:11:32.190797+00:00'
page_id: '745143740'
product: rm
source: tdn-rm
title: Relatórios - Desempenho de Vendas por Período - Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745143740
version: 8
---

## **Introdução**

---

O relatório de **Desempenho de Vendas por Período** tem como finalidade apresentar informações sobre imóveis vendidos e distratados em um determinado período, agrupando-os por coligada e empreendimento.

É possível filtrar os dados através de parâmetros como coligada, empreendimento, data de início e data de fim.

As informações apresentadas incluem o número de imóveis vendidos e distratados, o valor total das vendas e distratos, além do percentual de distratos em relação ao total de vendas.

O relatório é útil para análise do desempenho de vendas e controle de distratos em uma empresa imobiliária.

Importante!

Para ter acesso a este relatório, é preciso que o Perfil do usuário tenha acesso à opção: *[01.01.01] - Contratos de Venda*, sem necessidade de ter acesso às demais tarefas abaixo desta.

## **Procedimentos para utilização**

---

Ao utilizar este relatório no Smart View, é possível aplicar os seguintes Parâmetros de Visualização:

* **Código da Coligada:** Neste parâmetro é possível de se filtrar as Coligadas, onde o valor padrão *-1*, processa todas as coligadas e caso o usuário queira filtrar uma ou mais coligadas específicas, pode-se realizar esta ação alterando este valor e/ou acrescentando as demais coligadas, através do botão "+" localizado em frente à descrição do mesmo;
* **Código do Empreendimento:** Neste parâmetro é possível de se filtrar o Código do Empreendimento, onde o valor padrão -1, processa todos os empreendimentos e como ocorre com o parâmetro da entidade acima, caso o usuário tenha necessidade, pode-se filtrar um ou mais empreendimentos específicos através dos botões destinados a este fim;
* **Data Início:** Este parâmetro permite ao usuário especificar a data que será utilizada para o início do período da coleta dos dados; e
* **Data Fim:** Este parâmetro permite ao usuário especificar a data que será utilizada para o fim do período da coleta dos dados.

Após definir estes parâmetros e gerar o relatório, o sistema apresentará as seguintes informações:

* Agrupador **Consolidado**: É um totalizador com um resumo das informações de todas as coligadas e empreendimentos selecionados nos parâmetros acima. São apresentadas as seguintes informações:
  + **Número de Imóveis Vendidos:** É a soma da quantidade de imóveis vendidos, em relação aos filtros aplicados;
  + **Valor Total das Vendas:** É o somatório dos valores dos contratos de vendas no período filtrado;
  + **Número de Imóveis Distratados:** É o somatório da quantidade de distratos efetivados no período selecionado;
  + **Valor Total dos Distratos:** É o somatório dos valores dos distratos efetivados neste período. Caso o campo *[Valor do Distrato](https://tdn.totvs.com/display/LRM/Distratos+de+Venda)* de algum distrato não esteja preenchido, será considerado o *Valor da Venda*;
  + **% de Distratos:** É o percentual total de distratos efetivados para os empreendimentos e períodos filtrados.
* Agrupador **Coligada**: Neste agrupador são exibidas as mesmas informações do agrupador acima, porém sumarizados por coligada.
