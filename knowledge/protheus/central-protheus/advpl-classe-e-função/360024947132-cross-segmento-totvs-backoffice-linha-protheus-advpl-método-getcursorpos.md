---
article_id: 360024947132
category: ADVPL - Classe e Função
content_hash: f0656a77819a62746dbe3251971cbeae4c6b2300662b99e05f548c72b76f7962
fetched_at: '2026-06-28T22:40:14.199545+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Método GetCursorPos()
type: support-article
updated_at: '2021-05-06T19:29:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024947132-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-M%C3%A9todo-GetCursorPos
---

**Dúvida**Ao utilizar o método **GetCursorPos**() gera error.log o que o método não existe.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.23  
  
**Solução**

O método esta disponível a partir da Versão 12.1.23 - Build 17.3.0.8 - LOBO GUARA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023723831/mceclip0.png)  
O Método GetCursorPos() pertence a classe TGRID, no exemplo do TDN a classe MyGrid utiliza a TGRID, para que o método funcione deve utilizar desta forma

```
aCurPos := oGrid:oGrid:GetCursorPos()   
ConOut("Cursor posicionado na linha " + allTrim(str(aCurPos[1])) + " e coluna " + allTrim(str(aCurPos[2])))
```

**Saiba mais**

[TGrid](http://tdn.totvs.com/display/tec/TGrid)
