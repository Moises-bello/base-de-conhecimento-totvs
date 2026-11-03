---
article_id: 1500004242762
category: LEGAIS - BLOCO H/MATR460
content_hash: 235840220cde46a535ca3b9e222d274d60df65d6d44788eaa80cb5c5b3c947c7
fetched_at: '2026-06-28T22:42:15.137015+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Montagem
  da seção "Material de Consumo"
type: support-article
updated_at: '2021-06-14T14:32:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004242762-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Montagem-da-se%C3%A7%C3%A3o-Material-de-Consumo
---

**Dúvida**Como é gerada a seção "Material de Consumo" no relatório Inventário Modelo 7 (P7)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para esta seção ser gerada no Relatório P7, as condições são:

- Existência de produtos com B1\_TIPO = MC (Material de Consumo)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005212401/mceclip0.png)

- O produto do tipo MC possuir Saldo (seja em estoque próprio, DE ou EM terceiros):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005212521/mceclip1.png)

Com isso, no relatório P7 ele aparece na seção "Material de Consumo':

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005212621/mceclip2.png)

**Observação**: Produtos de Material de Consumo, na tabela H\_ (espelho do Bloco H do EFD), enquadram-se na Situação 01 (Em Estoque).

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005104362/mceclip3.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre o relatório MATR460(P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)*
