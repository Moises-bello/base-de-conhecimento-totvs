---
article_id: 360021555432
category: ADVPL - Ponto de Entrada
content_hash: c15059134513d8fe53f2fb4eae8a7fcccd345ccd162846f3e8d7c3ddc09498f2
fetched_at: '2026-06-28T22:40:11.863082+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de Entrada
  MAEXCEFISC não está sendo chamado no Documento de Entrada.
type: support-article
updated_at: '2021-12-29T20:52:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021555432-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-Entrada-MAEXCEFISC-n%C3%A3o-est%C3%A1-sendo-chamado-no-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao utilizar o PE MAEXCEFISC  o mesmo não está sendo chamado no Documento de Entrada?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**O ponto de entrada MAEXCEFISC  só será chamado se ao preencher o campo Tipo de Operação (D1\_OPER) ele encontrar a TES inteligente e alterar os campos da TES ( D1\_TES)

**Exemplo**

```
#include 'protheus.ch'  
#include 'parmtype.ch'  
  
user function MAEXCEFISC()  
  
Local aRet := PARAMIXB  
  
msginfo("MAEXCEFISC")  
   
return aRet
```

**Saiba mais****[MAEXCEFISC](http://tdn.totvs.com/pages/releaseview.action?pageId=253985194)**
