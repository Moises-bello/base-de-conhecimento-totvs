---
article_id: 360021258491
category: Escrita Fiscal - Impostos - ICMS
content_hash: 2c21376635ad7efde50a6710ed00eebd44570fcb495fc13100e31200c6d9c159
fetched_at: '2026-06-28T22:39:26.037845+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: MP - FIS - Cálculo Difal - Venda para Não Contribuinte - Para Ano 2019
type: support-article
updated_at: '2021-06-15T11:33:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021258491-MP-FIS-C%C3%A1lculo-Difal-Venda-para-N%C3%A3o-Contribuinte-Para-Ano-2019
---

**Dúvida**Como configurar o sistema para cálculo do Difal - Venda para Não Contribuinte para ano 2019 com Percentual do Cliente Destino = 100%?  
   
 **Ambiente**A Partir Versão 11.8  
  
**Solução**Será necessário configurar o Parâmetro:

MV\_PPDIFAL = {{2016,40,60},{2017,60,40},{2018,80,20},{2019,100,0}}
