---
article_id: 360022458272
category: ADVPL - Ponto de Entrada
content_hash: 9d9034bf2d8ba10713a6eb0ab359504183a9a6694d43b51cec4c456060df2543
fetched_at: '2026-06-28T22:40:12.902766+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Utilização do ponto
  de entrada FA040ALT
type: support-article
updated_at: '2021-12-30T18:06:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022458272-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Utiliza%C3%A7%C3%A3o-do-ponto-de-entrada-FA040ALT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Qual a finalidade do ponto de entrada **FA040ALT**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**O ponto de entrada **FA040ALT** sera executado na validação da alteração dos dados do contas a receber.

![KCS_F040alt.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360019843892/KCS_F040alt.gif)

**Exemplo:**

```
user function FA040ALT()  
  
Local lRet := .T.  
  
//Validações do cliente  
  
lRet := MsgYesNo("Continua","Validação PE - FA040ALT")  
  
return lRet
```

**Saiba mais**[FA040ALT - Valida alteração](http://tdn.totvs.com/pages/releaseview.action?pageId=6071094)
