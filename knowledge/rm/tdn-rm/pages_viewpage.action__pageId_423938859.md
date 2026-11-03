---
content_hash: dc5a0e86f5b0bdd687930572b6b16bf45a5cec746a32b6f42baad66ad1a772e2
fetched_at: '2026-06-29T00:09:29.267661+00:00'
page_id: '423938859'
product: rm
source: tdn-rm
title: Produto Substituto/Similar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938859
version: 4
---

O processo de substituição do Produto por um Substituto ou Similar tem como objetivo permitir que o usuário substitua o item do movimento por um item substituto ou similar no momento de incluir, faturar ou até mesmo realizar a cópia de um movimento. Este processo geralmente ocorre quando não temos a necessidade em estoque.

* **Parametrização**

Para trabalhar com a funcionalidade de troca do produto atual pelo produto substituto/similar é necessário parametrizar o movimento. A parametrização é realizada acessando o assistente de parametrização menu | Ambiente| Parâmetros | TOTVS Gestão de Estoque, Compras e Faturamento | escolher o Tipo de Movimento que vai tratar produto substituto/similar | acessar a Etapa "Estoque 3/3" no item "Trata Produto Substituto/Similar" | e selecionar uma das 3 opções disponíveis: "Substituto", "Similar" ou "Ambos". Após o usuário parametrizar o movimento, o botão Produto Substituto/Similar ficará visível no item do movimento.  
 Além de parametrizar o movimento é necessário também acessar o cadastro de produtos no menu Cadastros | Produtos | Anexo - Similares e escolher quais serão os produtos substitutos similares do produto usado no movimento.

* Substituto: Selecionando esta opção, ao clicar no botão Produto Substituto/Similar só serão exibidos os produtos substitutos.
* Similar: Selecionando esta opção, ao clicar no botão Produto Substituto/Similar só serão exibidos os produtos similares.
* Ambos: Selecionando esta opção, ao clicar no botão Produto Substituto/Similar serão exibidos ambos produtos, substitutos e similares.

***Observação:***  
 Em movimentos que forem do tipo devolução não será permitido realizar a troca do produto Substituto/Similar.  
 Ao selecionar um produto substituto/similar que possua unidade de controle diferente da unidade do produto principal o sistema fará a conversão das unidades do produto similar que irá substituir o produto principal.  
 Ao substituir o produto principal pelo substituto ou pelo similar o sistema irá consistir o saldo de acordo com o que estiver parametrizado no TOTVS Gestão de Estoque, Compras e Faturamento, os parâmetros existentes para a consistência são "Avisa", "Barra" e "Não Confere".  
 Caso o movimento esteja com o status recebido, não poderá ser efetuada a troca do produto substituto/similar.  
 Em movimentos que não estão parametrizados para tratar Produto Substituto/Similar o botão "Produto Substituto/Similar" não estará visível na tela do item do movimento.
