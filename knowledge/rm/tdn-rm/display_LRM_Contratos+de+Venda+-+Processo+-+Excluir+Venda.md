---
content_hash: 0e2f067c45b0b68b171a4d0502296519bf24059217daed77041c9b16f9c3e8c3
fetched_at: '2026-06-29T00:09:46.549133+00:00'
page_id: '435104831'
product: rm
source: tdn-rm
title: Contratos de Venda - Processo - Excluir Venda
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Processo+-+Excluir+Venda
version: 6
---

Esse processo permite excluir a venda que esteja nas seguintes Situações:

* Em Preparação
* Cancelada

Ao executar esse processo, será excluído todos os cadastros vinculados a venda.

Para excluir uma venda devemos verificar algumas pendências.

* Não pode ter lançamentos financeiros baixados.
* Não pode ter aditivos em aberto.
* Não pode ter movimentos gerados na venda, seja de entrega de chaves ou comissão, para isso deve cancelar a venda para deixar a rastreabilidade.

Caso houver coberturas referentes a solicitação de atendimento, essas serão excluídas automaticamente junto com a venda.

Importante

As vendas com situação **'Em Proposta' ou 'Cancelada'** **no Portal de Imóveis** têm origem no próprio portal e só podem ser excluídas por meio dele
