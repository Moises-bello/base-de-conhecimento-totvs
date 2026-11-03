---
article_id: 360044225173
category: NFe - Nota Fiscal Eletrônica
content_hash: d14975e23d31441aead050574e8c8a8612c88865d017a9b1e12757355944f873
fetched_at: '2026-06-28T22:40:01.747430+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar as
  TAGS vBCFCPSTRet, pFCPSTRet e vFCPSTRet para o grupo do ICMS60 ?'
type: support-article
updated_at: '2021-10-11T18:57:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044225173--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-as-TAGS-vBCFCPSTRet-pFCPSTRet-e-vFCPSTRet-para-o-grupo-do-ICMS60
---

**Dúvida**MP - NFE - Como gerar as TAGS vBCFCPSTRet, pFCPSTRet e vFCPSTRet para o grupo do ICMS60 ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**1-** Essas TAGs os campos são **preenchidas Manualmente no Documento de entrada:**  
  
  
Valor FCP anterior = **D1\_VFCPANT**  
  
Alíquota FCP anterior = **D1\_AFCPANT**  
  
Base FCP anterior = **D1\_BFCPANT**  
  
  
**![](https://totvssuporte.zendesk.com/attachments/token/Or8phOWcf6gyvyd6oW4EhdCHX/?name=inline-2028062605.png)​**  
  
  
**![](https://totvssuporte.zendesk.com/attachments/token/RV1xw6oDJb6iYdNiiRglMuDmg/?name=inline-1798823766.png)​**

**2-** Configurar na**TES de Saída:**

Calcula ICMS **(F4\_ICM)** = **Não**  
  
Sit Trib ICMS **(F4\_SITTRIB)** **= 60**  
  
Inf ST Ant **(F4\_ART274)** **= 1**  
  
LF ICMS-ST **(F4\_LFICMST)** **= Não**  
  
L. Fisc. ICMS **(F4\_LFICM)****= Outros ou ISENTO**

**3-** Ao gerar a nota de saída referente ao produto os campos na **SFT abaixo serão preenchidos:**

Base FCP anterior = **FT\_BFCANTS**

Alíquota FCP anterior = **FT\_PFCANTS**

Valor FCP anterior = **FT\_VFCANTS**
