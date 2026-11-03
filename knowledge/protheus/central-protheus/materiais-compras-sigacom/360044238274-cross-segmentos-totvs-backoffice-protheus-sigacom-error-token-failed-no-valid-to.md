---
article_id: 360044238274
category: Materiais - Compras (SIGACOM)
content_hash: ea6de586ad20589d4f6bef47923fbf2adf64030241a6b800e1f4459a7b1a1dfd
fetched_at: '2026-06-28T22:41:17.654667+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Error token failed,
  no valid token):({|a,b,c| FWInitCpo(a,b,c),lRet:=(..F),FWCloseCpo(a,b,c,lRet,.T.),lRet
  })
type: support-article
updated_at: '2022-05-18T20:45:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044238274-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Error-token-failed-no-valid-token-a-b-c-FWInitCpo-a-b-c-lRet-F-FWCloseCpo-a-b-c-lRet-T-lRet
---

**Ocorrência**

*invalid macro source (SSYacc0105e: Error token failed, no valid token):({|a,b,c| FWInitCpo(a,b,c),lRet:=(..F),FWCloseCpo(a,b,c,lRet,.T.),lRet }) on FWBUILDFEATURE(PROTHEUSFUNCTIONMVC.PRX)*  
  
**Ambiente**Protheus – Compras – A partir da versão 12.1.25  
  
**Causa**Esse incidente ocorre devido uma não conformidade na validação **X3\_WHEN** (Modo Edição no **SIGACFG**) do campo **DS\_NOMEFOR.**

**Solução**Ajuste o conteúdo do campo:

**De:** ..F  
**Para:** .F.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060094014/mceclip0.png)
