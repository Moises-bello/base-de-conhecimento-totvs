---
article_id: 360016143112
category: ADVPL - Classe e Função
content_hash: d2b4b42132c2e0ca825adee44031af0ae5e38272a7f5c83edf7200dd5516381d
fetched_at: '2026-06-28T22:40:19.571656+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - HttpCGet via Job
type: support-article
updated_at: '2022-01-11T18:23:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016143112-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-HttpCGet-via-Job
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao utilizar a rotina Httpcget via job gerou o seguinte erro

```
THREAD ERROR ([XXXX], PROTHEUS, THIS) XX/XX/XXXX XX:XX:XX  
Function HttpCGet() doesn't available in JOB.
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão P1217  
  
**Solução**Não é possível utilizar a [HttpcGet](https://tdn.totvs.com/display/tec/HTTPCGet) via job, conforme documentação a função é utilizada diretamente da máquina onde o SmartClient está sendo executado. Via Job é necessário utilizar HTTPGet ou HTTPSGet.  
  
**Saiba mais**  
[HttpGet](http://tdn.totvs.com/display/tec/HTTPGet)  
[HTTPSGet](http://tdn.totvs.com/display/tec/HTTPSGet)
