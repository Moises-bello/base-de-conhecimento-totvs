---
article_id: 360017472492
category: ADVPL - Rotina Automática
content_hash: 804c1f02ae1429bd352924993e6d69568d5b13e45b1c75caac4a3642cec7e43d
fetched_at: '2026-06-28T22:40:24.178650+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Rotina automática da Mata103
  realiza o rateio por centro de custo
type: support-article
updated_at: '2021-12-29T19:07:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017472492-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Rotina-autom%C3%A1tica-da-Mata103-realiza-o-rateio-por-centro-de-custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**A rotina automática da Mata103 realiza o rateio por centro de custo?  
  
**Ambiente**Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**Para que seja realizado o rateio por centro de custo, o campo D1\_RATEIO tem que estar preenchido com '1' no *Array* da ExecAuto.

```
aadd(aLinha,{"D1_RATEIO" ,'1' , Nil})
```

**Saiba Mais  
[ExecAuto Mata103](http://tdn.totvs.com/pages/viewpage.action?pageId=235592777)**
