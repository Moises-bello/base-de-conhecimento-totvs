---
article_id: 115011993568
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 9211c5499ce838aea41b66532f37a5ff5952c21627057dfb434c5d7ceddbbd62
fetched_at: '2026-06-28T22:38:41.225666+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'MP - FAT - Erro na inclusão na abertura de pedido: array out of bounds ( 3
  of 2 )  on BROWSEDEF(MATA410.PRX) '
type: support-article
updated_at: '2021-04-28T15:51:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011993568-MP-FAT-Erro-na-inclus%C3%A3o-na-abertura-de-pedido-array-out-of-bounds-3-of-2-on-BROWSEDEF-MATA410-PRX
---

**Ocorrência**

Erro na inclusão na abertura de pedido: array out of bounds ( 3 of 2 )  on BROWSEDEF(MATA410.PRX)

**Causa**

Mudança na configuração do ponto de entrada MA410COR() para a versão 12

**Ambiente**

Microsiga Protheus - a partir da versão 12

**Solução**

1 - Descompilar o ponto de entrada MA410COR() do RPO, via Dev. Studio ou Vs\_code.

2-Altere o rdmake, conforme a documentação do artigo: **[MA410COR NA P12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115010934747-MA410COR-NA-P12)** .

3-Recompile o ponto de entrada ao RPO e reinicie o sistema para poder utilizá-lo novamente na rotina de pedido de venda.
