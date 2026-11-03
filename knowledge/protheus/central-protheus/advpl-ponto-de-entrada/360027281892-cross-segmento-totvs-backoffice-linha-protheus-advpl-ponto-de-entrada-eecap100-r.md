---
article_id: 360027281892
category: ADVPL - Ponto de Entrada
content_hash: 592ee0aedb7cf7266432aef34f8651d4c339ff3fc3ac04aeb8de2f2a125dc0ff
fetched_at: '2026-06-28T22:40:11.797907+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de Entrada
  EECAP100: ROD_CAPA_PED'
type: support-article
updated_at: '2021-12-29T15:07:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027281892-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-Entrada-EECAP100-ROD-CAPA-PED
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**É possível adicionar campos no rodapé da rotina EECAP100?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**

Sim, utilizando a função [MSGET](http://tdn.totvs.com/pages/viewpage.action?pageId=24346994), no ponto de entrada **ROD\_CAPA\_PED** da EECAP100 pois a rotina permite acesso aos Objetos **oItens** e **oPanel2**

Exemplo

```
If cParam == "ROD_CAPA_PED"  
cNum:= 1  
   @ 34,10 MSGET oItens   VAR cNum   SIZE 58,16 RIGHT PIXEL OF oPanel2   
EndIf
```

**Saiba Mais****[SAY](http://tdn.totvs.com/pages/viewpage.action?pageId=24347069)**
