---
article_id: 1500005612382
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 0f6b012c4c53a4b2b27b7097fdc202bbc3d17a84e9af1c3cc0f2de857fd864f9
fetched_at: '2026-06-28T22:38:41.223378+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP - FAT - Desconto inserido no campo "Indenização" (C5_DESCONT) não considera
  o valor do Frete
type: support-article
updated_at: '2021-04-28T15:49:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005612382-MP-FAT-Desconto-inserido-no-campo-Indeniza%C3%A7%C3%A3o-C5-DESCONT-n%C3%A3o-considera-o-valor-do-Frete
---

**Ocorrência**Na rotina de Pedidos de venda (MATA410), caso insira um desconto no campo "Indenização" (C5\_DESCONT), o sistema considera apenas os valores dos produtos, ignorando o valor das despesas como Frete, Seguro e Despesa.  
**Ambiente**Microsiga Protheus - Faturamento - A partir da versão 12  
  
**Causa**Todos os descontos no pedido de vendas, entre eles o "Indenização" (C5\_DESCONT), consideram apenas os valores dos produtos, por regra o desconto é concedido sobre o "Preço de Lista" (C6\_PRCLIST), este preço não considera as despesas acessórias.  
  
**Solução**Indique um valor de desconto que seja inferior à somatória dos preços dos itens.

**Saiba mais**: [**https://tdn.totvs.com/x/KE1tDQ**](https://tdn.totvs.com/x/KE1tDQ)
