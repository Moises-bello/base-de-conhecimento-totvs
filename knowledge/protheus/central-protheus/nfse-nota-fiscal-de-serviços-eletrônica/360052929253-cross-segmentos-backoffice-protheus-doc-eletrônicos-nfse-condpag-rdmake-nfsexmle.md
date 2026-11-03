---
article_id: 360052929253
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 40402abb35695c653c5ae5e6a39b7ddd7576a93c6392f94e43e9fe5d9d2ea93a
fetched_at: '2026-06-28T22:39:56.388370+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - CondPag Rdmake
  NFSEXMLENV
type: support-article
updated_at: '2025-07-14T21:23:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052929253-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-CondPag-Rdmake-NFSEXMLENV
---

**Dúvida**Qual a tratativa do rdmake NFSEXMLENV para considerar a condição de pagamento da nota fiscal?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Extraímos do campo E4\_COND (Cond.Pagto) a definição da condição de pagamento.  
E4\_COND = 00 : **À vista**  
E4\_COND = maior que 00: **Apresentação**  
E4\_COND = "," separada por virgula, **A prazo  
  
[Detalhes tipo\_pagamento para municípios IPM](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047905953-TSS-NFSE-TAG-tipo-pagamento-IPM-)**
