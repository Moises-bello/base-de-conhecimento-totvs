---
article_id: 360028023392
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 432301569b484fa4f0dda9877bcd82dbd91889ec42a959745a52a40cf9754463
fetched_at: '2026-06-28T22:39:56.429966+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - DadosConstrucaoCivil
  GINFES
type: support-article
updated_at: '2025-07-18T14:47:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028023392-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-DadosConstrucaoCivil-GINFES
---

**Dúvida**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Ambiente**Protheus a partir da versão 11.80  
  
**Solução**Conforme o manual ABRASF, as tags que representam a Construção Civil são **CodigoObra** e **Art**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360028290431/mceclip0.png)  
  
As duas tags devem ser enviadas no XML.  
O rdmake NFSEXMLENV usa o conteúdo dos campos **C5\_OBRA** e **C5\_ARTOBRA** para envio das tags.
