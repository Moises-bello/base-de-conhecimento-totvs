---
article_id: 360022832591
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d77e57b81a078809942fe59a6a400972d3049126cfc36d490d55781cd2d11ae1
fetched_at: '2026-06-28T22:38:41.186022+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos- TOTVS Backoffice (Linha Protheus)-SIGAFAT- Ajuste de parâmetro
  para gerar pedido de venda na oportunidade x proposta comercial
type: support-article
updated_at: '2022-07-26T17:33:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022832591-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ajuste-de-par%C3%A2metro-para-gerar-pedido-de-venda-na-oportunidade-x-proposta-comercial
---

**Dúvida**Como ajustar o parâmetro para gerar pedido de venda quando utilizar oportunidade de venda com proposta comercial?  
  
**Ambiente**

Cross Segmentos- TOTVS Backoffice (Linha Protheus)-SIGAFAT - a partir da versão 12  
  
**Solução**

Acesse o Configurador(**SIGACFG**) e vai em Ambiente, Cadastros, Parâmetros e faça o ajuste:  
**MV\_OPORXPV = T**

Obs: - Caso o parâmetro **MV\_OPORXPV** estiver preenchido com o valor .F., não será possível a efetivação posterior do pedido de venda , assim como o prospect não será transformado em cliente, uma vez que oportunidade estiver encerrada.

Saiba detalhes [Criação de Oportunidade de Vendas com Proposta Comercial](https://tdn.totvs.com/x/XjEaDg)
