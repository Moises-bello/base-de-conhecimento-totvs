---
article_id: 360022209492
category: TAF - REINF
content_hash: 663c698074df8d210d1d787a31f903ad07b88013a96d41ba5a8e69508ea873fc
fetched_at: '2026-06-28T22:41:34.799372+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - R-1000- Rejeição MS0030
  e erro de schema na transmissão do R-1000
type: support-article
updated_at: '2023-04-04T12:14:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022209492-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-R-1000-Rejei%C3%A7%C3%A3o-MS0030-e-erro-de-schema-na-transmiss%C3%A3o-do-R-1000
---

**Dúvida**Como corrigir a rejeição MS0030 e erro de Schema na transmissão do R-1000

**Ambiente**TAF- REINF – A partir da versão 12.01.33  
  
**Solução**

1- Verificar qual a versão valida da REINF e preencher no parâmetro MV\_TAFVLRE.

Hoje a versão está na 1\_05\_01

Exemplo de preenchimento do parâmetro:

MV\_TAFVLRE = 1\_05\_01

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019441292/mceclip0.png)

No print abaixo o parâmetro está com o preenchimento errado, causando a rejeição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019312331/mceclip1.png)

Valide também se existe o schema na versão 1\_05\_01 no TSS.

![SCHEMAS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13606740541207)
