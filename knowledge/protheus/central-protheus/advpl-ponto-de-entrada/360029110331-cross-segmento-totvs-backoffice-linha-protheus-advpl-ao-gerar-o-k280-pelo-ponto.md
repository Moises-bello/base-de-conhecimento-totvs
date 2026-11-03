---
article_id: 360029110331
category: ADVPL - Ponto de Entrada
content_hash: 2f23579431b091ab7a4457ddebb480f40ca9422ee5dceb1d5e079a0c465b07ce
fetched_at: '2026-06-28T22:40:11.633473+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ao gerar o K280
  pelo ponto de entrada SPDFISBLCK não gera o registro 0200
type: support-article
updated_at: '2022-06-21T18:01:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029110331-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ao-gerar-o-K280-pelo-ponto-de-entrada-SPDFISBLCK-n%C3%A3o-gera-o-registro-0200
---

**Dúvida**Ao gerar o K280 pelo ponto de entrada SPDFISBLCK não gera o registro 0200.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**O Registro K280  tem o objetivo de escriturar a correção de apontamento de estoque, escriturado de período de apuração anterior, no Registro K200, ou seja, por conceito eu não posso ter um K280 desvinculado de um K200.   
Por este motivo não é gerado o 0200 com base no código informado no K280 e sim com base no K200. Ou seja, se o seu PE SPDFISBLCK desenvolvido gera o registro de um item para o K280, e não haja uma referência K200 deste registro, não será emitido o registro 0200.
