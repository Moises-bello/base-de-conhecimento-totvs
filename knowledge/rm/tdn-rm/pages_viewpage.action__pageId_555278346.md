---
content_hash: 6ff034ca89566519d9ceb841507ea527b3ffffc3ab359830676364e0a197bcb9
fetched_at: '2026-06-29T00:10:46.662524+00:00'
page_id: '555278346'
product: rm
source: tdn-rm
title: Pedido e Pedido Extra Utilizando a Integração Orçamentária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555278346
version: 10
---

O Pedido e Pedido Extra utilizará as parametrizações de integração orçamentária dos parâmetros do Projeto F6. Na geração de Movimento para os Pedidos/Pedidos Extras, a Natureza Orçamentária será discriminada no Item do Movimento e o Grupo Orçamentário será discriminado no Rateio do Item do Movimento. A parametrização pode seguir os seguintes cenários:

* Utilizando Natureza Orçamentária no Projeto e Não Utilizando Grupo Orçamentário
* + Os **Itens** dos Movimentos gerados terão a mesma **Natureza Orçamentária** informada no **Projeto**

* Utilizando Natureza Orçamentária na Tarefa e Não Utilizando Grupo Orçamentário
* + Os **Itens** dos Movimentos gerados terão a mesma **Natureza Orçamentária da Tarefa selecionada no Pedido/Pedido Extra**. Os Itens terão a Natureza Orçamentária **discriminada por Tarefa**.
  + Caso um **Item** do Pedido/Pedido Extra possua o **mesmo Produto em mais de uma Tarefa** mas as Tarefas possuem **Naturezas Orçamentárias diferentes**, o Movimento terá **um Item para cada Natureza Orçamentária** de sua respectiva Tarefa.
  + Caso um **Item** do Pedido/Pedido Extra possua o **mesmo Produto em mais de uma Tarefa** e as Tarefas possuem **Naturezas Orçamentárias iguais**, o Movimento terá **um Item para todas as Naturezas Orçamentárias das Tarefas**.

* Utilizando Natureza Orçamentária no Insumo/Grupo de Custo e Não Utilizando Grupo Orçamentário
* + Os Itens dos Movimentos gerados terão as Naturezas Orçamentárias respectivas ao Insumo ou ao grupo de custo que está associado no Pedido/Pedido Extra.
  + Caso o Pedido/Pedido Extra possua **Insumos/Grupos de Custo com Naturezas Orçamentárias diferentes** mas que o **Produto associado** é **igual**, o Movimento terá **um Item para cada Natureza Orçamentária** e o **Rateio do Item** discriminado **por Grupo de Custo/Insumo**.
  + Caso o Pedido/Pedido Extra possua **Insumos/Grupos de Custo com Naturezas Orçamentárias iguais** e o **Produto associado** é **igual**, o Movimento terá **um Item agrupado pela Natureza Orçamentária** e o **Rateio do Item** será discriminado **por Grupo de Custo/Insumo da Tarefa**.

* Utilizando Natureza Orçamentária por Projeto e Grupo Orçamentário por Tarefa
* + Ao gerar o Movimento, a Natureza Orçamentária dos Itens será a mesma informada no Projeto e o Grupo Orçamentário será definido pela Tarefa selecionada no Pedido/Pedido Extra.
  + Caso o Pedido/Pedido Extra possua **Tarefas que solicitem o mesmo Produto do nucleus** e as Tarefas estejam com **Grupos Orçamentários diferentes**, o **Movimento** será gerado com **um Item** e no **Rateio do Item** será visualizado o valor e a quantidade **separado por Grupo Orçamentário e Tarefa**.
  + Caso o Pedido/Pedido Extra possua **Tarefas que solicitem o mesmo Produto do nucleus** e as Tarefas estejam com **Grupos Orçamentários iguais**, o **Movimento** será gerado com **um Item** e no **Rateio do Item** a quantidade será **separada por Tarefa**.

* Utilizando Natureza Orçamentária por Projeto e Grupo Orçamentário por Grupo de Custo/Insumo
* + Ao gerar o Movimento a Natureza Orçamentária dos Itens será a mesma informada no Projeto e o Grupo Orçamentário será definido pelo Insumo associado ao Pedido/Pedido Extra
  + Caso o Pedido/Pedido Extra possua **Tarefas que solicitem o mesmo Produto do nucleus** e o **Grupo Orçamentário informado no Insumo/grupo de custo** seja **diferente**, o **Movimento** será gerado com **um Item** e no **Rateio do Item** será visualizado o valor e a quantidade **separado por Grupo Orçamentário e Tarefa**.
  + Caso o Pedido/Pedido Extra possua **Tarefas que solicitem o mesmo Produto do nucleus** e o **Grupo Orçamentário informado nos Insumos/grupos de custos** forem **iguais**, o **Movimento** será gerado com **um Item** e no **Rateio do Item** a quantidade será **separada por Tarefa**.

* Utilizando Natureza Orçamentária por Tarefa e Grupo Orçamentário por Grupo de Custo/Insumo
* + Ao gerar o Movimento a Natureza Orçamentária do Item será definida pela Tarefa respectiva selecionada no Pedido/Pedido Extra e o Grupo Orçamentário será definido pelo Insumo associado ao Pedido.
  + Caso o Pedido/Pedido Extra possua **Tarefas com Naturezas Orçamentárias diferentes**, os **Insumos selecionados no Pedido possuam Produtos associados iguais** e os **Grupos Orçamentários dos Insumos solicitados sejam iguais**, ao gerar o **Movimento**, serão gerados **um Item para cada natureza** e o **Rateio de cada Item irá conter o Grupo Orçamentário por Insumo**.
  + Caso o Pedido/Pedido Extra possua **Tarefas com Naturezas Orçamentárias diferentes**, os **Insumos selecionados no Pedido possuam Produtos associados iguais** e os **Grupos Orçamentários dos Insumos solicitados sejam diferentes,** ao gerar o **Movimento**, serão gerados **um Item para cada natureza** e o **Rateio de cada Item irá conter o Grupo Orçamentário por Insumo.**
  + Caso o Pedido/Pedido Extra possua **Tarefas com Naturezas Orçamentárias iguais**, os **Insumos selecionados no Pedido possuam Produtos associados iguais** e os **Grupos Orçamentários dos Insumos solicitados sejam diferentes**, ao gerar o **Movimento**, os **Itens serão agrupados por natureza** e o **Rateio de cada Item irá conter o Grupo Orçamentário por Insumo**.
  + Caso o Pedido/Pedido Extra possua **Tarefas com Naturezas Orçamentárias diferentes**, os **Insumos selecionados no Pedido possuam Produtos associados diferentes**, ao gerar o **Movimento**, serão gerados **um Item para cada natureza** e o **Rateio de cada Item irá conter o Grupo Orçamentário do seu respectivo Insumo**.
