---
article_id: 360058740093
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: ff841808ec879582144f5852efcd40b0b9f11534789b6dd1a20de7f2438c32a8
fetched_at: '2026-06-28T22:39:36.909671+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como é controlado
  o desconto na base de cálculo do PIS e COFINS apuração?
type: support-article
updated_at: '2021-06-29T12:39:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058740093-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-%C3%A9-controlado-o-desconto-na-base-de-c%C3%A1lculo-do-PIS-e-COFINS-apura%C3%A7%C3%A3o
---

**Dúvida**Exclusão do desconto na base de cálculo do PIS e COFINS apuração.  
  
**Ambiente**Protheus – Compras ou Faturamento – A partir da versão 11.80.  
  
**Solução**Para controlar essa questão utilize o seguinte campo no TES:

F4\_PISBRUT (PIS Bruto) e F4\_COFBRUT (COFINS Bruto)

Com base no valor da mercadoria = 1.000:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098822033/mceclip2.png)

Valor do desconto = 100,00

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098822053/mceclip3.png)

Campos configurados = **Não**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096508594/mceclip0.png)

Campo configurado = **SIM**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096508714/mceclip1.png)
