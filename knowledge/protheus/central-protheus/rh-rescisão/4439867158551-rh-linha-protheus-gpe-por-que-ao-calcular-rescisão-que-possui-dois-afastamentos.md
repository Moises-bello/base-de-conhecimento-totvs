---
article_id: 4439867158551
category: RH - Rescisão
content_hash: 02a6a89773e50f380bf423d4092f97d4ffb2f8731d2d95de47d1bf7889bd1cdb
fetched_at: '2026-06-28T22:43:49.845563+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que ao calcular rescisão que possui dois afastamentos
  no mês da demissão, a verba de dia afastamento é apresentada duas vezes
type: support-article
updated_at: '2025-04-16T14:20:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4439867158551-RH-Linha-Protheus-GPE-Por-que-ao-calcular-rescis%C3%A3o-que-possui-dois-afastamentos-no-m%C3%AAs-da-demiss%C3%A3o-a-verba-de-dia-afastamento-%C3%A9-apresentada-duas-vezes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26681487086999) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Por que ao calcular rescisão que possui dois afastamentos no mês da demissão, a verba de dia afastamento é apresentada duas vezes?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O cálculo da rescisão apresenta a verba de dia afastamento em dois lançamentos, devido a configuração do campo da verba Lcto Diário. Com o campo Lcto Diário com Sim o cálculo apresenta em dois lançamentos e com Não soma os dias de afastamento em um único lançamento.

**Exemplo:**

**Lançamento ausência**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4439841493527)

**Lcto Diário com Sim**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4439843814295)**

**Rescisão****![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4439845013143)**

**Lcto Diário com Não****![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4439848680983)**

**Rescisão****![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4439856198679)**

**Somou os afastamentos: 9 + 3 = 12**

**Saiba mais**[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
