---
article_id: 360021351991
category: ADVPL - Ponto de Entrada
content_hash: ce1ded55f653e6409b2adbe0a31a1bd3a434f50bcc1fced5fefa74ee829cfcd3
fetched_at: '2026-06-28T22:40:11.837506+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  M410PVNF
type: support-article
updated_at: '2021-12-29T19:42:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021351991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-M410PVNF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Qual ponto de entrada posso utilizar na opção de Prep. Doc saída no pedido de venda?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Ponto de entrada para validação, executado antes da rotina de geração de NF's

```
User function M410PVNF()  
  
Local lRet  
//Validações do Usuário  
lRet := ApMsgYesNo('Continua ?')  
  
Return lRet
```

**Saiba mais  
[M410PVNF - Geração de notas fiscais](http://tdn.totvs.com/pages/releaseview.action?pageId=6784152)**
