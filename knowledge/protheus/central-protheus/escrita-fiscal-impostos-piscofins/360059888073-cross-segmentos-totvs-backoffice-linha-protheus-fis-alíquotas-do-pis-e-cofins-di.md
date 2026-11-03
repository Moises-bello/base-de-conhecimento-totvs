---
article_id: 360059888073
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 5b0b617af99fb0ee69723ccc406e04469356c1b09659c0cb1a64ae5ccf8f3314
fetched_at: '2026-06-28T22:39:36.853053+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Alíquotas do PIS
  e COFINS diferenciadas por conta e ordem de terceiros
type: support-article
updated_at: '2021-06-24T13:32:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059888073-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Al%C3%ADquotas-do-PIS-e-COFINS-diferenciadas-por-conta-e-ordem-de-terceiros
---

**Dúvida**  
Cliente lança nota de mercadoria e despesa de serviço com o mesmo fornecedor e produto, como destacar somente as alíquotas diferenciadas no documento de entrada?  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80.  
  
**Solução:**

Para utilizar alíquotas diferenciadas de PIS e COFINS somente na nota origem, é necessário utilizar uma situação tributária diferente entre as TES envolvidas, exemplo:

**TES de mercadoria = Sit Trib ICM = 00 (F4\_SITTRIB)**

**TES de serviço = Sit Trib ICM = 90 (F4\_SITTRIB)**

Na exceção fiscal (tabela SF7), amarre a situação tributária da nota de mercadoria:

**Campo: F7\_SITTRIB = 00**

Com isso, assim que utilizar a rotina MATA119 com o mesmo produto (SB1) e mesmo fornecedor (SA2), mas com o TES de serviço, o sistema não vai reconhecer as alíquotas diferenciadas de importação.
