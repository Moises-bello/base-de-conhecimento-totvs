---
article_id: 4402530170135
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 6787f846aeaf59063fb6f8142d36accc8b812f398a6b82a1c5e1bdcabba235b8
fetched_at: '2026-06-28T22:38:38.597374+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - O que faz a
  função A410vend
type: support-article
updated_at: '2021-06-11T21:31:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402530170135-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-O-que-faz-a-fun%C3%A7%C3%A3o-A410vend
---

**Dúvida**O que faz a função A410Vend do pedido de vendas?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

A função **A410Vend**() encontra-se na rotina do pedido de venda (**matv410**) efetua a validação do código do vendedor , verificando se este código realmente existe no cadastros de vendedores(**MATA040**) para uso do pedido e geração de comissão. Também valida o código para não permitir duplicidade da informação no pedido.
