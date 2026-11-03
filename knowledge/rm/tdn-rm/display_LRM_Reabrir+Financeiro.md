---
content_hash: 62f943452aa5ef74a0beb651285d8c33e46989faaff67430e98b27188e9e2100
fetched_at: '2026-06-29T00:09:29.293306+00:00'
page_id: '423938865'
product: rm
source: tdn-rm
title: Reabrir Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/Reabrir+Financeiro
version: 2
---

Este processo, assim como o processo de [Gerar Financeiro](http://tdn.totvs.com/display/LRM/Gerar+Financeiro), depende que os tipos de movimentos estejam parametrizados para não faturarem na inclusão, ou seja, na inclusão do movimento, o sistema não gerar os lançamentos financeiros.   
Para que esta rotina seja executada corretamente, o movimento selecionado deverá ter lançamentos financeiros gerados e estes não podem estar baixados, descontados (Desconto de Duplicata) ou acordados (Acordo).   
Caso estas restrições não estejam presentes nos lançamentos financeiros do movimento selecionado, o sistema irá excluir os dados financeiros deste movimento, inclusive alterando o status deste movimento para 'Pendente' (movimentos de compras) ou 'A Faturar' (movimentos de vendas).
