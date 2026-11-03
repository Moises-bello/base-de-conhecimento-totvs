---
content_hash: 8c7c5c9da6966944bd008adb50dcf4200066d537fa53bcbd00eea14458198d92
fetched_at: '2026-06-29T00:09:29.265822+00:00'
page_id: '423938858'
product: rm
source: tdn-rm
title: Produtos Compostos
type: documentation
url: https://tdn.totvs.com/display/LRM/Produtos+Compostos
version: 6
---

Esta opção Produto Composto são informados os subprodutos do produto em edição.  
Esta pasta só aparecerá se nos Parâmetros Gerais | Tabelas | Produtos | Gerais marcou a opção "Produto Composto", aqui você indicará quais os produtos que compõem o produto que se está incluindo.   
Esta pasta indica quais os produtos compõem o produto que se está incluindo.  
***Observações**:*

* Vamos supor que vende copos de liquidificador e a baixa do estoque é feita por componente do copo, ou seja, um copo, uma borracha, uma tampa e uma base. Desta forma, ao invés de sempre que vender um copo tiver que incluir no movimento todos estes itens para baixar o estoque, você só incluirá no movimento o produto "Copo Completo de Liquidificador" e após informar a quantidade movimentada "desmembra os itens com produtos compostos", para isso, é necessário que se inclua no cadastro de produtos cada um dos produtos que compõem o copo completo, feito isso, incluir o produto "Copo Completo de Liquidificador" e nesta pasta produtos compostos coloque os produtos copo, borracha, tampa e base cada um com quantidade 1. Ao incluir um movimento em que vendeu 2 copos de liquidificador, inclua apenas o produto "Copo completo de liquidificador" com quantidade igual a 2, depois basta pressionar o botão "desmembra os itens com produtos compostos" que fica ao lado da grid de itens do movimento, que este único item será desmembrado em 4 diferentes itens cada um com quantidade 2 são eles: copo, borracha, tampa e base.
* Para que o botão "desmembra os itens com produtos compostos" no movimento esteja habilitado é necessário que o parâmetro "Utiliza produto composto" na pasta Itens/outros dados do tipo de movimento esteja marcado.
* Informe o produto a inserir como composto, a quantidade utilizada e pressione a seta "Adicionar como subproduto".
* O produto pode ser informado/pesquisado tanto por código ou por descrição.
* Não é permito faturar movimentos que possuam produto composto. O faturamento de movimentos só será permitido após o desmembramento do produto, antes disto o sistema irá barrar o faturamento. Esta consistência é necessária, pois garante a integridade do desdobramento.
* Apenas produtos Ativos poderão ser incluídos como composto.

Informações Adicionais
