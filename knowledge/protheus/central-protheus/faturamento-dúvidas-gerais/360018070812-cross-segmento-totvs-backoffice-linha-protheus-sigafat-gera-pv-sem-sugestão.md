---
article_id: 360018070812
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 600f4d0bce988727ed1d30a929717f8b9caaea22024bab1507731fe58b1d2c41
fetched_at: '2026-06-28T22:38:28.575414+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Gera pv sem
  sugestão
type: support-article
updated_at: '2023-08-15T15:01:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018070812-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Gera-pv-sem-sugest%C3%A3o
---

**Dúvida**

Não gera pedido de venda com a pergunta do menu F12  da aprovação de orçamento (**mata416)** - "**Gera PV s/sugestão**" igual a não.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

A pergunta "Gera PV s/sugestão" do menu F12 da aprovação de orçamento(**mata416)** setado como Não, somente irá gerar pedido de venda se o Orçamento possuir uma configuração de Sugestão de Orçamento.

Se o Orçamento vier de uma proposta comercial, de uma oportunidade de venda ou for gerado via orçamento (**mata415)** e não possuir itens com Sugestão de Orçamento, o sistema não irá gerar pedido de venda mesmo, é conceito de sistema.

Para que o pedido seja gerado em todas as situações citadas, inclusive no Orçamento com Sugestão de Orçamento, deixe a pergunta "Gera PV s/sugestão" como Sim, caso contrário, o pedido só será gerado para orçamentos com produtos de sugestão de orçamento.
