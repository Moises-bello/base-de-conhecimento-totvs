---
article_id: 360017693791
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: ddacebba90c1bfd509b2e4e200259642e3021e2e9bf56ca61ba4190d548a4d0d
fetched_at: '2026-06-28T22:38:31.119669+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP- FAT - Por que o orçamento do módulo Faturamento não reabre após a exclusão
  do pedido
type: support-article
updated_at: '2021-04-28T15:55:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017693791-MP-FAT-Por-que-o-or%C3%A7amento-do-m%C3%B3dulo-Faturamento-n%C3%A3o-reabre-ap%C3%B3s-a-exclus%C3%A3o-do-pedido
---

**Dúvida**

Por que o orçamento do módulo Faturamento não reabre após a exclusão do pedido?

**Ambiente**

Microsiga protheus - desde das versões anteriores a 11.80.  
   
**Solução**

Ao excluir um pedido que teve aprovação de orçamento, dentro do módulo faturamento, o sistema não reabre o orçamento, pois trata-se regras de negociação.

Uma vez que foi o pedido, foi negociado aquele valor com aquelas condições, se o pedido é excluído , entende-se que aquela negociação não vale mais e por isso, deve ser efetuado uma nova negociação e incluir um novo orçamento para esta venda.

Você tem a opção de copiar um orçamento, esteja ele em aberto ou encerrado, caso queira manter as mesmas características.

Este conceito precede de versões anteriores a versão 11.
