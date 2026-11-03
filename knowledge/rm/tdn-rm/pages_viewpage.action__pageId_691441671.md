---
content_hash: 33c91a7128f8dfe08b4f98487cdf60c35f349ee7e15d442aa05f478b86772546
fetched_at: '2026-06-29T00:11:21.256250+00:00'
page_id: '691441671'
product: rm
source: tdn-rm
title: Vincular/Desvincular grupo de produtos ao produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=691441671
version: 9
---

Atenção

Recurso disponível na release 12.1.2209 ou superior.

Para uma melhor compreensão deste processo sugerimos a leitura da documentação referente ao cadastro de [Grupo de produtos](https://tdn.totvs.com/display/LRM/Grupo+de+Produtos) e do anexo de [Grupo de produtos](https://tdn.totvs.com/display/LRM/Grupo+de+Produto) disponível no cadastro de [Produtos/Serviços](https://tdn.totvs.com/pages/viewpage.action?pageId=423938817).

Este processo possibilita vincular grupos de produtos aos produtos ou desvincular grupos de produtos dos produtos permitindo uma melhor organização, classificação e agrupamento dos produtos.

Também é possível criar ou remover tal relacionamento através do anexo [Grupo de produtos](https://tdn.totvs.com/display/LRM/Grupo+de+Produto) disponível no cadastro de produtos mas pelo anexo somente é possível realizar tal operação para apenas um produto e um grupo de produtos por por vez já pelo processo é possível realizar tais vinculações/desvinculações para vários produtos e vários grupos de produtos em apenas uma execução.

O passo a passo para a execução do processo se dará da seguinte forma:

* Seleção na visão de produtos dos registros de produtos que deseja vincular/desvincular dos Grupos de produtos;
* Acionamento do processo de "Vincular/Desvincular grupos de produtos";

* Selecionar a **ação** desejada entre Vincular ou Desvincular;

* + - No caso de "Vincular" então é apresentado um controle do tipo lista vazia (seleção de múltiplos registros) para que seja feita a escolha dos grupos de produtos a serem vinculados aos produtos selecionados na visão;
  + - No caso de "Desvincular" então é apresentado uma lista preenchida com todos os grupos de produtos atualmente vinculados aos produtos selecionados na visão (não só os grupos em comum e sim todos, isto é, pode constar nesta lista grupos de produtos vinculados a um produto mas que não estejam vinculados a outros produtos) para que seja feita a seleção dos grupos de produtos que serão desvinculados dos produtos selecionados na visão;
* A vinculação consiste de, caso o produto ainda não esteja vinculado ao grupo então o vincula (cria o registro de vinculação na tabela TPRDGRUPOPRODUTO), caso contrário - já se encontre vinculado - não faz nada;
* Já a desvinculação consiste de, caso o produto esteja vinculado ao grupo então o desvincula (apaga o registro de vinculação da tabela TPRDGRUPOPRODUTO), caso contrário - não está vinculado - não faz nada.
* Neste processo não está disponibilizado a opção e/ou tratamento que permita definir se tal grupo a ser relacionado com o produto será o "Grupo principal" do produto. Esta opção deverá ser realizada através do anexo [Grupo de produtos](https://tdn.totvs.com/display/LRM/Grupo+de+Produto) editando tal relacionamento e assinalando tal opção.

Ao final do processo é apresentado um LOG de status (sucesso ou falha e motivo) apenas com os registros (produtos X grupos de produtos) processados, os que não foram processados não constarão do LOG nem mesmo com a informação "Não processado" ou "Grupo de produto não se encontra vinculado ao produto então não foi desvinculado" ou "Grupo de produto já se encontra vinculado ao produto".
