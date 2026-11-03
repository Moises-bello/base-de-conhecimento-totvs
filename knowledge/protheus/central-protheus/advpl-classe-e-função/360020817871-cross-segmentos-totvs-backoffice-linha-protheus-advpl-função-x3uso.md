---
article_id: 360020817871
category: ADVPL - Classe e Função
content_hash: 348df50a7ead7d5172b93a8c3503f4237ab63727a563dc3403e089bb33d9a6eb
fetched_at: '2026-06-28T22:40:19.469398+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Função X3USO
type: support-article
updated_at: '2023-09-21T14:02:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020817871-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-X3USO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min****Dúvida**A função X3\_USO não está trazendo a informação correta: **x3USO(X3\_USADO)**  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**É necessário também parâmetro para indicar o modulo, conforme documentação.

```
x3USO(X3_USADO, NMODULO)
```

**Saiba mais [X3Uso - Avaliação de campo em uso](http://tdn.totvs.com/pages/releaseview.action?pageId=6815021)**
