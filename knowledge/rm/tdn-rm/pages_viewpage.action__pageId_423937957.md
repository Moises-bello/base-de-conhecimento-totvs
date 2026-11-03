---
content_hash: 2b6f5e7d4780bb690d1b1c0f3de533be71526bf39eb84bbdbfd455441980ed72
fetched_at: '2026-06-29T00:09:24.543871+00:00'
page_id: '423937957'
product: rm
source: tdn-rm
title: Informações do Estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937957
version: 4
---

A opção Informações de Estoque são cadastradas as informações relacionadas ao ressuprimento, como estoque máximo, estoque mínimo, ponto de reposição, lote de econômico de compra, etc.  
'Esta pasta é opcional e será parametrizada em Opções|Parâmetros Gerais|Tabelas|Produto, onde é determinada se devemos "cadastrar níveis de estoque" no produto.  
 Os seguintes campos serão expostos para preenchimento:  
 Estoque Mínimo: Existem 3 faixas para o estoque mínimo do produto. Informe o valor para cada uma delas.  
 Estoque Máximo: Informe o estoque máximo do produto, informe o valor para cada uma das 3 faixas existentes.  
 Ponto de Pedido: Informe o valor para cada uma das 3 faixas de ponto de pedido do produto.  
 ***Observações**:*

* O preenchimento dos três valores para os níveis de estoque acima são opcionais.
* No momento do cadastro do local de estoque em Cadastro/Local de Estoque, indica-se para cada local, em qual das faixas de estoque ele se encaixa. Será verificado a faixa indicada no mesmo para as consistências dos níveis de estoque no momento da inclusão e alteração de um movimento, em parâmetros gerais-Tabelas, pasta produto, subpasta saldo, você determinará se o sistema deve ou não conferir o estoque mínimo, máximo e ponto de pedido, caso informe que o sistema deve conferir avisando ou barrando a inclusão do item no movimento, o sistema verificará no local de estoque qual das três faixas o local pertence e quais dos 3 (três) estoques deverá ser conferido.
