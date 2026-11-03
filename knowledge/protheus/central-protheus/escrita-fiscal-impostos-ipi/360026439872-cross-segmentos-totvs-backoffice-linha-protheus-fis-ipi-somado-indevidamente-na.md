---
article_id: 360026439872
category: Escrita Fiscal - Impostos - IPI
content_hash: fd3125084f480f6a70e8da6c6fd861ee20b044e8809c2fa39ca9a34ab3edd716
fetched_at: '2026-06-28T22:39:29.017343+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - IPI somado indevidamente
  na base do PIS/COFINS/CSLL '
type: support-article
updated_at: '2021-07-28T13:53:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026439872-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-IPI-somado-indevidamente-na-base-do-PIS-COFINS-CSLL
---

**Dúvida**

Como eu faço para que o IPI não seja destacado na base do PCC (PIS/COFINS/CSLL)?  
  
**Ambiente**

Protheus - Compras e/ou Financeiro - a partir da versão 11.80  
  
**Solução**

Para que o IPI não seja considerado na base do PCC, é necessário ajustar o seguinte campo na tabela SF4 (TES):

**IPI na BC** ( **F4\_IPIPC** ) para **NÃO**.

Com isso o IPI não será considerado na base do imposto federal.
