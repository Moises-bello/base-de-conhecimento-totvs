---
content_hash: 73af640f9203db15c7841db7cd44abe18499d57ff6417ad571ef15f1fd560aeb
fetched_at: '2026-06-29T00:09:16.176360+00:00'
page_id: '421385481'
product: rm
source: tdn-rm
title: Histograma Resumo
type: documentation
url: https://tdn.totvs.com/display/LRM/Histograma+Resumo
version: 3
---

O Histograma Resumo é uma visão anexa à funcionalidade "Geração de Pedidos em Suprimento/Faturamento" onde é possível visualizar todos os itens do pedido selecionado.   
Na visão de histograma resumo serão listados todos os itens do pedido agrupados por insumo e produtos, e suas quantidades na requisição corrente, quantidade necessária, quantidade pendente, quantidade pedida e quantidade pedida extra.  
A quantidade requisitada do insumo poderá ser alterada através da visão de histograma resumo. Ao alterar a quantidade pedida, todos os itens que possuem o mesmo produto terão suas quantidades pedidas alteradas. Essa alteração será efetuada de maneira que os valores da quantidade pedida dos itens somadas deem o valor desejado, ou seja, o valor para o qual a quantidade foi alterada dentro histograma resumo.  
Será permitida alteração da data de entrega do item através do histograma resumo. Ao alterar a data de entrega de um produto, todos os itens pertencentes ao pedido do mesmo produto terão sua data de entrega alterada.  
As alterações que o histograma resumo possibilita só podem ser utilizadas em pedidos que ainda não geraram movimento. Pedidos já movimentados não poderão sofrer alterações.

**Observação sobre a edição de quantidades:** Ao utilizar o Histograma Resumo, note que a alteração da quantidade de um insumo só é permitida de forma nativa se o pedido possuir apenas um período vinculado. Quando o insumo estiver distribuído em mais de um período, o sistema fará a alteração da quantidade.
