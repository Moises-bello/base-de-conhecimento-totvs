---
article_id: 4404259504151
category: RH - Rescisão
content_hash: 63a4b017dd9a5d0509b02c1c9e6dd2daf181a0f11152021629f1fc24601449c9
fetched_at: '2026-06-28T22:43:53.521011+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Por que cálculo de rescisão calcula FGTS 2% para
  funcionário categoria  Sefip 01
type: support-article
updated_at: '2025-05-09T19:18:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404259504151-RH-Linha-Protheus-GPE-Por-que-c%C3%A1lculo-de-rescis%C3%A3o-calcula-FGTS-2-para-funcion%C3%A1rio-categoria-Sefip-01
---

**Dúvida**Por que calculo de rescisão calcula FGTS 2% para funcionário categoria Sefip 01?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O cálculo apresentou 2% de FGTS categoria Sefip 01 pois o funcionário está cadastrado com tipo de contrato determinado. Para calcular FGTS 8% contrato determinado categoria Sefip 01, deve ser cadastrado em tabela S037, linha com tipo de contrato determinado 2 e FGTS 8%.

**Exemplo:**

**Tabela S037.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404259404183)

**Cadastro funcionário.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18728030222359)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18728021268503)**

**Cálculo rescisão.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18728030240279)**

**140,00 \* 8% = 11.20.**
