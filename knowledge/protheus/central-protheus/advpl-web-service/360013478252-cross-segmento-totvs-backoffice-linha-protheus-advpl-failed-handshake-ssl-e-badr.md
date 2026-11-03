---
article_id: 360013478252
category: ADVPL - Web Service
content_hash: 7ed18bd3dedba31f7fccf4ab8665c7208abe4ffdcd9d83fa92af6be4eb956cfe
fetched_at: '2026-06-28T22:40:10.466869+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Failed Handshake
  SSL e BadRequest
type: support-article
updated_at: '2023-10-13T22:51:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013478252-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Failed-Handshake-SSL-e-BadRequest
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**Utilizando um Webservice fazendo uma requisição https ocorre o erro [ERROR][SSL] Failed Handshake SSL. e BadRequest  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão P12.1.17  
  
**Causa**BadRequest.  
  
**Solução**

Para solucionar o problema utilize as chave na sessão SSLConfigure conforme exemplo a seguir:

```
[SSLConfigure]  
Verbose = 1  
SSL2 = 0  
SSL3 = 0  
TLS1_0 = 0  
TLS1_1 = 1  
TLS1_2 = 1  
STATE = 0  
HSM = 0  
  
Para erro de BadRequest retire a acentuação da string JSon  
  
Exemplo:  
cJson:='{'   
cJson+=' "Name":"Antônio"'   
cJson+='},'
```

**Saiba mais:**  
**[Webservice\_Error\_SSL\_Failed\_Handshake\_SSL](https://tdn.totvs.com/display/public/PROT/ADV0004_Webservice_ERROR_SSL_Failed_Handshake_SSL)**
