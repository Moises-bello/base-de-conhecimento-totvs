---
content_hash: 98c1bd77b0b816bad81fd253e335ffd996b1a3d2573c51f30526e0a8f6a67070
fetched_at: '2026-06-29T00:09:24.681297+00:00'
page_id: '423937994'
product: rm
source: tdn-rm
title: Lote de Produto
type: documentation
url: https://tdn.totvs.com/display/LRM/Lote+de+Produto
version: 6
---

A opção Lote do Produto são cadastrados os lotes que serão amarrados aos produtos.

As datas no cadastro do lote devem seguir a seguinte consistência:

* A data de entrada não pode ser menor que a data de fabricação e nem a data de validade menor que a data de fabricação.
* Se o lote já tiver sido movimentado, os seguintes campos não poderão ser modificados: Número do lote, Produto, Fornecedor, Filial, Local de Estoque e Data de Entrada.
* Na interface de inclusão/edição de lote, foi atribuída a verificação de filtro por usuário. Assim o usuário que não possui permissão sobre determinado produto, não poderá atribuí-lo a lote e nem consultar o lote do produto.

Nos movimentos parametrizados para usar lote, ao realizar a seleção do lote a ser movimentado, caso o lote esteja vencido será apresentado ao usuário uma mensagem solicitando a confirmação da utilização do lote vencido.
