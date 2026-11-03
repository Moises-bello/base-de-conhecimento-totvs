---
article_id: 360049467213
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: ccbb6752385808bc0b8bd6c34aca4391a9f5bc513dfeb974d63c4b79dfa493b6
fetched_at: '2026-06-28T22:39:20.489032+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - ICMS Efetivo para
  Não Atacadista '
type: support-article
updated_at: '2021-07-13T18:09:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049467213-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-ICMS-Efetivo-para-N%C3%A3o-Atacadista
---

**Dúvida**Como configurar o icms efetivo para Não Atacadista ?

**Ambiente**Protheus - Fiscal - A partir da versão 11.80  
  
**Solução**

O icms efetivo vai ser calculado para o comercio não atacadista, quando:

Venda a consumidor Final

CST = 60

TES

atualiza estoque = sim

Calcula icms = não

L. fiscal icms = isento ou outras

CST = 60

Na TES de saídas serão amarrados dois códigos de reflexo:

RS001920 - debito do icms efetivo

RS021922 - credito presumido para o comercio não atacadista

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072508454/mceclip0.png)

RS001920

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073687473/mceclip1.png)

RS021922

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072509514/mceclip2.png)

O credito presumido referente as entradas será calculado na rotina fisa196, os valores serão calculados através das notas fiscais de entradas

os campos preenchidos:

ICMS ST Destacado (campos **D1\_ICMSRET, D1\_BRICMS e D1\_ALIQSOL)**

ICMS ST Recolhido Anteriormente (digitado manualmente no item da nota de entrada por meio dos campos **D1\_ICMNDES, D1\_BASNDES e D1\_ALQNDES)**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072511454/mceclip3.png)**
