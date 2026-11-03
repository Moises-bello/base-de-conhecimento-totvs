---
article_id: 360018061152
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: f647a0519674f44cab941b09193470a435f3f94a2232760134de0edc60a402c2
fetched_at: '2026-06-28T22:38:31.312671+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Notas de Contabilização para Emenda Const 087
type: support-article
updated_at: '2021-12-08T19:12:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018061152-MP-FAT-Notas-de-Contabiliza%C3%A7%C3%A3o-para-Emenda-Const-087
---

**Dúvida**

Emenda Const. 087, como contabilizar o ICMS partido em vendas a cliente final, não contribuinte, onde os valores vem nas informações complementares (XML) Documento de Saída?

**Ambiente**

Microsiga Protheus -  a partir da versão 11.  
  
**Solução**

A premissa de contabilização do documento de saída estão baseadas em buscar as informações nas tabelas da nota fiscal de saída, que são SF2 - Cabeçalho da nota - e SD2 - itens da nota, a rotina de contabilização não tem como buscar informações direta do xml.

No geral, mensagens no xml relacionada a ICMS vem da tabela fiscal CD2, desta forma, é importante avaliar se esses valores são passíveis de contabilização via Livros Fiscais ou mesmo se a tabela CD2 possui os valores relacionados ao ICMS partido, via nota de saída, não há como efetuar esse processo, a menos que a informação esteja nos campos pertencentes as tabelas SF2 e SD2.
