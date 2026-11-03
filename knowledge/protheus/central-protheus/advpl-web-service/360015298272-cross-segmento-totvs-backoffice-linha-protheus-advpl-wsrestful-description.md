---
article_id: 360015298272
category: ADVPL - Web Service
content_hash: 10ade02d8b87b237750e17f5d412660cb07724f0a5da51ac0bcabc4f8e3d8f95
fetched_at: '2026-06-28T22:40:10.521509+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - WsRestful Description
type: support-article
updated_at: '2021-12-29T14:01:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015298272-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-WsRestful-Description
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Ao Criar um serviço REST, como posso editar ou criar uma página para a opção "*For more details*"?

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010477652/mceclip3.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80   
  
  
**Solução**

No caso do serviço padrão FWMODEL é utilizado define ou seja constantes no formato HTML

```
#DEFINE STR001  "<p>TESTE</p>"    
#DEFINE STR002  "<ul><li>Teste2</li></ul>"  
WSRESTFUL m140_tst DESCRIPTION STR001+STR002
```

**Saiba mais:**  
**[Wsmethod / Rest](http://tdn.totvs.com/pages/viewpage.action?pageId=75269436)**
