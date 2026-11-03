---
article_id: 360016799371
category: ADVPL - Classe e Função
content_hash: f5f52ad26cbf7c80b24976bda7a010b003da99e3f7a9efd85ee7dfd2936d7413
fetched_at: '2026-06-28T22:40:15.728463+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Customizar o duplo
  click da classe FWChartFactory
type: support-article
updated_at: '2022-01-05T15:12:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016799371-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Customizar-o-duplo-click-da-classe-FWChartFactory
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**É possível a customização do duplo click da classe FWChartFactory?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para que possa customizar o duplo *click* da função **FWChartFactory** é necessário o preenchimento da propriedade **BSERIEACTION,** como o exemplo abaixo:

```
oFWChart:BSERIEACTION:={||ALERT("OI")}
```

**Sabia mais**[FWChartFacTory](http://tdn.totvs.com/display/public/PROT/FwChartFactory)
