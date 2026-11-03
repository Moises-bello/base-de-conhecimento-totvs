---
article_id: 360047939453
category: NFe - Nota Fiscal Eletrônica
content_hash: efd98d8b5e2cc46fa3bd949df3f61d5286880680b302bb6b13015006883b8b42
fetched_at: '2026-06-28T22:40:03.717674+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de
  schema na Tag <pICMSInter>'
type: support-article
updated_at: '2025-06-16T16:58:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047939453-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-pICMSInter
---

**Dúvida**Como solucionar a falha de Schema referente a TAG pICMSInter?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**1 - Ao gerar falha de Schema referente ao **pICMSInter** verifique se o seu XML gerou conforme o exemplo abaixo com uma alíquota fora do previsto:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069002634)

2- Conforme o XML acima não foi preenchido a **pICMSInter** comalíquota que deve ser de **4, 7 ou 12 por cento**que são as alíquotas permitidas para a TAG.

* Conforme o link **abaixo no qual consta a nota técnica** página 10:

[Nota Técnica 2015.003 - v 1.94](Nota%20T%C3%A9cnica%202015.003%20-%20v%201.94)

![](https://mail.google.com/mail/u/0?ui=2&ik=b781bb0fef&attid=0.1&permmsgid=msg-a:r131691388626596814&th=16efb74f16f860fc&view=fimg&sz=s0-l75-ft&attbid=ANGjdJ8WhuIf94VNDscjU9IrnVDqTDKnpfrRY5X2P3CaEg8cxHtKlCSHLth9Ki0g6tU_G4t-9kpCMI_g100bIhJdtGkq9XCPJBbHTebn3v7BqHrkX_Sy4Q6T_vVzHAU&disp=emb&realattid=ii_k432w26n0)

3. **O conteúdo das TAGS serão retirados dos campos:**

* Grupo ICMSUFDEST x Campos CD2 da linha **CD2\_IMP = CMP:**

Tag **vBCUFDest** -> **CD2\_BC**

Tag **pFCPUFDest** -> **CD2\_PFCP**

Tag **pICMSUFDest** -> **CD2\_ALIQ**

Tag **pICMSInter** -> **CD2\_ADIF**

Tag **pICMSInterPart** -> **CD2\_PDDES**

Tag **vFCPUFDest** -> **CD2\_VFCP**

Tag **vICMSUFDest** -> **CD2\_VDDES**

Tag **vICMSUFRemet** -> **CD2\_VLTRIB**
