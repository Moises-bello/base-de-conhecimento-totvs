---
article_id: 360051303893
category: ADVPL - Ponto de Entrada
content_hash: e3cf5c3ce5de14bcc114064bbd49115b37f2d47060116bb19264c97a7710ad99
fetched_at: '2026-06-28T22:40:11.810303+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  F811MAILTO
type: support-article
updated_at: '2021-12-29T14:58:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051303893-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-F811MAILTO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**Como enviar mais de um e-mail na rotina **FINA811** utilizando o ponto de entrada **F811MAILTO**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões.   
  
**Solução**Para enviar mais de um e-mail deve ser retornado em uma unica string conforme o exemplo abaixo:

```
#Include 'Protheus.ch'  
  
user function F811MAILTO()  
  
local cEmail := "teste1@totvs.com;teste2@totvs.com;teste3@totvs.com"  
local cRet := ''  
  
if !empty(cEmail)  
      cRet := cEmail  
else  
      cRet := SA1->A1_EMAIL  
endIf  
  
return cRet
```

**Saiba mais**  
[Carta de Cobrança - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=492706741)
