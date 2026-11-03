---
content_hash: 39d07b4834fabf4697d25c6ac672b223a4bd3657173c4eac339e35ab0e99380f
fetched_at: '2026-06-29T00:09:28.741762+00:00'
page_id: '423938777'
product: rm
source: tdn-rm
title: Unidade de Medida do Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/Unidade+de+Medida+do+Produto
version: 9
---

A opção Unidades de Medidas são cadastradas as unidades que poderão ser utilizadas nas movimentações do produto.   
O cadastro de unidades do produto permite cadastrar várias unidades pelas quais o produto poderá ser comprado ou vendido.   
O cadastro de unidades mantêm um histórico de todas as unidades informadas no Cadastro de Produtos|Controle Estoque.

***Observação*:**Há uma restrição no sistema que obriga que todas as unidades sejam conversíveis para a unidade de controle de estoque. Quando a unidade de controle de estoque é modificada, o sistema exige que as unidades de compra e venda defaults sejam ajustadas em conformidade com a nova unidade de controle de estoque. O mesmo acontece com as unidades de medida do produto.Se for feita uma referência em uma unidade de compra ou venda default que ainda não esteja na lista de unidades de medida do produto, estas serão copiadas automaticamente para a Pasta Unidades de Medida.

IMPORTANTE

Ao cadastrar um produto global, as informações do anexo de unidades de medida do produto só serão exibidas na coligada em que foi inserido, pois as unidades de medida são por coligada, portanto, caso necessário deverá ser feita a cópia de produto entre coligadas. Para mais detalhes veja a documentação de [Produto Global](https://tdn.totvs.com/display/public/LRM/Produto+Global). 

* **Unidade Tributável**

Foi disponibilizado o campos "Tributável" e " Cod. unidade Tributável" para informação do usuário.  
Este cadastro tem como objetivo possibilitar que o TOTVS Gestão de Estoque, Compras e Faturamento atenda à Nota Técnica 2016/001 que adéqua a NF-e ao Projeto do Portal Único do Comércio Exterior, padronizando a Tabela de Unidades de Medidas Tributáveis no Comércio Exterior, conforme o código NCM (Nomenclatura Comum do Mercosul) da mercadoria a que se refere, com base nas unidades recomendadas pela Organização Mundial de Aduanas (OMA).   
***Importante*:**Caso o campo Tributável esteja marcado, o campo Cod. unidade Tributável tem seu preenchimento obrigatório.  
Os cálculos da unidade tributável funcionam conforme parametrização dos campos  "Unidade Tributável/Unidade Tributável Exterior" e "Fator de Conversão Tributável/Fator de Conversão Tributável Exterior" disponíveis na aba "Controle de Estoque" do cadastro de Produto. Para consultar mais detalhes sobre os cálculos possíveis acesse [Unidade Tributável no Comércio Exterior](http://tdn.totvs.com/pages/viewpage.action?pageId=270900577) e [Unidade Tributável no Comércio Interno](http://tdn.totvs.com/pages/viewpage.action?pageId=361452375).
