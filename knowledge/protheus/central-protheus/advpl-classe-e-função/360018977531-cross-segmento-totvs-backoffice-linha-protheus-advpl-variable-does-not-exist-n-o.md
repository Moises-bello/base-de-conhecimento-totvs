---
article_id: 360018977531
category: ADVPL - Classe e Função
content_hash: 29c1776cd8bcd6f9a3a8ea89bf1643b0a134ce38033107ae35c05e98189e06f9
fetched_at: '2026-06-28T22:40:18.219174+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Variable does not
  exist N on GDFIELDGET
type: support-article
updated_at: '2022-01-06T19:36:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018977531-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Variable-does-not-exist-N-on-GDFIELDGET
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: ***00:01:00 min*** **Ocorrência**

Tenho uma customização que ja funcionava com a função GDFIELDGET mas está gerando esse erro?THREAD ERROR ([XXXX], XXXXX, XXXX) XX/XX/XXXX XX:XX:XX   
variable does not exist N on GDFIELDGET(MATXFUNC.PRX)   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.17  
  
**Causa**a função **GDFIELDGET** não é compatível com rotina em **MVC**  
  
**Solução**

Utilize a função **[FWFldGet](http://tdn.totvs.com.br/display/framework/FWFldGet)**
