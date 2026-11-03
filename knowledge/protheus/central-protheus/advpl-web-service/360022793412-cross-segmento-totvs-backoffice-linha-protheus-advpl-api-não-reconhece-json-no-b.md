---
article_id: 360022793412
category: ADVPL - Web Service
content_hash: acbc5cbe0d56db4f039c06ca05fb685aa1eb804f5011216cb3320340805a54bf
fetched_at: '2026-06-28T22:40:10.375630+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - API não reconhece
  json no body
type: support-article
updated_at: '2022-04-06T13:19:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022793412-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-API-n%C3%A3o-reconhece-json-no-body
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar realizar a filtragem dos dados retornados pela API (método HTTP *GET*) por meio de um JSON no corpo de requisição (*body*), o conteúdo não está sendo filtrado.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.23

**Causa**As APIs TOTVS não estão preparadas para envio de informações em formato \*.JSON em requisições do tipo *GET*.  
  
**Solução**Realizar o envio dos parâmetros via *query string*.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020504692/mceclip0.png)  
  
**Saiba mais**  
[API REFERENCE - TOTVS DEVELOPERS](https://api.totvs.com.br/)  
[HTTPGet](http://tdn.totvs.com/display/tec/HTTPGet)
