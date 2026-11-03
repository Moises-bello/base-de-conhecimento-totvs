---
article_id: 5118721909655
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: b2a6098e2726398edaee19e32658382ce4c39838ca5e137a64ab3a2b1178a14f
fetched_at: '2026-06-28T22:39:41.149504+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Erro parâmetro
  MV_EIC0008
type: support-article
updated_at: '2022-04-01T15:05:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5118721909655-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Erro-par%C3%A2metro-MV-EIC0008
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao tentar estornar uma Purchase Order (**EICPO400**) é apresentada a seguinte mensagem: **"Este pedido foi gerado com o parâmetro MV\_EIC0008 desligado. Para realizar o estorno e alteração, o mesmo deve estar desligado."** Como podemos estornar o processo uma vez que mesmo com o parâmetro desligando não é possível efetuar o estorno?

![MV_EIC0008_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5118465059863/MV_EIC0008_.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Foi efetuada a correção da validação, para que o sistema permita o estorno do Purchase Order, independente de ter sido incluído com o parâmetro **MV\_EIC008** habilitado ou não, pois o parâmetro em questão foi descontinuado.   
  
Segue abaixo os patches para correção:  
12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1062179> 12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1062180>  
  
**Saiba mais**[DTRADE-7369 DT Estorno do Purchase Order valida o parâmetro MV\_EIC0008](https://tdn.totvs.com/pages/releaseview.action?pageId=672102784)
