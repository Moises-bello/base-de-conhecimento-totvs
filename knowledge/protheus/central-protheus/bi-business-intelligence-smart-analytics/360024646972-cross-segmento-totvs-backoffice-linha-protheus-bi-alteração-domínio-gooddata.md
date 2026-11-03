---
article_id: 360024646972
category: BI - Business Intelligence - Smart analytics
content_hash: 0392adb40d42ec370efdbe3619deddf0039d83a94305b0746100a12fa4e8f946
fetched_at: '2026-06-28T22:37:04.079594+00:00'
product: protheus
section_id: 1500001539741
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Alteração domínio GoodData
type: support-article
updated_at: '2022-07-27T18:17:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024646972-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Altera%C3%A7%C3%A3o-dom%C3%ADnio-GoodData
---

**Ocorrência**Durante a execução do Agent 3.2.1 do Smart Analytics, o log retorna com o seguinte erro referente ao GoodData: "hostname in certificate didn't match:"  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - GoodData – A partir da versão 3.2.1  
  
**Causa**Esse incidente ocorre devido a alteração do domínio do GoodData para o Agent 3.2.1.  
  
**Solução**Para solucionar essa ocorrência, realize o seguinte passo:  
Dentro do arquivo **my.properties, altere** o endereço do **gdc.etl.process** para **<https://analytics.totvs.com.br>**

**de**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023306972/mceclip0.png)

**para**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023346451/mceclip2.png)
