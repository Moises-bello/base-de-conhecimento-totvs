---
article_id: 360018125112
category: ADVPL - Ponto de Entrada
content_hash: c53c8fe3ba89b0f0b152410473cfca03b86ecefb4715698c7525bc3d3015ca3c
fetched_at: '2026-06-28T22:40:11.765284+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - MT140TOK - Valida
  todos os itens do Pré-Documento
type: support-article
updated_at: '2021-12-29T13:40:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018125112-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-MT140TOK-Valida-todos-os-itens-do-Pr%C3%A9-Documento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Qual ponto de entrada posso utilizar para validar todos os itens no  pré-documento de entrada?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Responsável por validar todos os itens do pré-documento

Este ponto é executado após verificar se existem itens a serem gravados e tem como objetivo validar todos os itens do pré-documento

```
User Function MT140TOK  
  
Local lRetorno := PARAMIXB[1]  
  
Local lRet:=.T.  
  
//..Customização do cliente  
  
Return lRet
```

**Saiba Mais**

[MT140TOK - Valida todos os ítens do Pré-Documento](http://tdn.totvs.com/pages/releaseview.action?pageId=6085513)
