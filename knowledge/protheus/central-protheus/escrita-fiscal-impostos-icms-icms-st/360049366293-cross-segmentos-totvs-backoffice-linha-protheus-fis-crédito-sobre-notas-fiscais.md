---
article_id: 360049366293
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 379f5442db0c8261d67be3c7086afbb65f422063790030a8163d849dd8be1b33
fetched_at: '2026-06-28T22:39:20.471630+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Crédito sobre notas
  fiscais de entradas - regra 02
type: support-article
updated_at: '2021-07-13T17:29:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049366293-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Cr%C3%A9dito-sobre-notas-fiscais-de-entradas-regra-02
---

**Dúvida**Como configurar - credito sobre notas fiscais de entradas para regra 02?   
  
**Ambiente**  
Protheus - Fiscal -  A partir da versão 11.80  
  
**Solução**  
O credito para contribuintes Atacadistas será realizado por meio da nota fiscal de entradas por código de reflexo, podendo ser através de duas formas:  
  
1) ICMS ST destacado em campo próprio na nota fiscal

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072136774/mceclip0.png)

Dessa forma serão populados os campos

ICMS ST Destacado (campos **D1\_ICMSRET, D1\_BRICMS e D1\_ALIQSOL)**

**TES**

**![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073367173/mceclip9.png)**

Criar um código de reflexo

**Base p/ Calc (CE0\_NFBASE):**

4 - base sol

**Alíquota (CE0\_NFALIQ)****:**

3 - aliq sol

**Valor (CE0\_NFVALO):**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072137314/mceclip1.png)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073366413/mceclip2.png)**

2)ICMS ST destacado em observações

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073366533/mceclip3.png)

Dessa forma serão populados os campos

ICMS ST Recolhido Anteriormente (digitado manualmente no item da nota de entrada por meio dos campos **D1\_ICMNDES, D1\_BASNDES e D1\_ALQNDES)**

**TES**

**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072138034/mceclip10.png)**

Criar um código de reflexo

**Base p/ Calc (CE0\_NFBASE):**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072137694/mceclip4.png)

**Alíquota (CE0\_NFALIQ)****:**

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073366813/mceclip5.png)**

**Valor (CE0\_NFVALO):**

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073366893/mceclip6.png)**

**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072137914/mceclip7.png)**

Em ambas as opções o valor do credito será demonstrado na aba - lançamento da apuração

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073366973/mceclip8.png)

gerando a tabela CDA
