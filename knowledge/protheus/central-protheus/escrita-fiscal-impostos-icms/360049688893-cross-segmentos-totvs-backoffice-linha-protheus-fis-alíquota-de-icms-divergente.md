---
article_id: 360049688893
category: Escrita Fiscal - Impostos - ICMS
content_hash: bc55820d0e245b4e19f2a61b2cb59d8615e8953a0670fd6fdf9df0f79b0a9f4d
fetched_at: '2026-06-28T22:39:24.130738+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Alíquota de ICMS
  divergente em operações com retorno de beneficiamento para o estado de São Paulo
type: support-article
updated_at: '2021-07-28T02:56:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049688893-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Al%C3%ADquota-de-ICMS-divergente-em-opera%C3%A7%C3%B5es-com-retorno-de-beneficiamento-para-o-estado-de-S%C3%A3o-Paulo
---

Alíquota de ICMS divergente em operações com retorno de beneficiamento para o estado de São Paulo.  
**Dúvida**

Em operação de beneficiamento foi efetuado o cálculo com 12% na alíquota do ICMS, porém ao realizar o retorno dessa nota o sistema está considerando a alíquota de 18%.

**Ambiente**Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**Para o estado de SP ao lançar uma nota de retorno de beneficiamento deverá ser considerada a alíquota da nota de origem (nesse caso 12%) desde que esse retorno ocorra dentro do período de 180 dias.  
Passado esse prazo a operação será tratada como retorno de beneficiamento com suspensão fora do prazo, onde nesse caso deverá ser aplicada a alíquota interna do estado de SP (18%).

Esse procedimento está de acordo com o art. 402 do RICMS-SP/2000 e na portaria CAT nº 22/2007.
