---
article_id: 360013601091
category: ADVPL - Classe e Função
content_hash: aa2969f9401ccedd49bf759b7cfdb733bec723cb4674dc9d441362603adf4262
fetched_at: '2026-06-28T22:40:17.141349+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Request could not
  be empty. e BadRequest
type: support-article
updated_at: '2022-06-13T21:17:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013601091-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Request-could-not-be-empty-e-BadRequest
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: 00:01:00 min  
  
Ocorrência**Servidor SSL com a função FWRest ou HttpPost

`[184]: Request could not be empty`. e BadRequest.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da versão P12.1.17  
  
**Causa**Erro ocorre pois há acentuações no Json enviado pela classe  
  
**Solução**

```
[SSLConfigure]  
Verbose = 1  
SSL2 = 0  
SSL3 = 0  
TLS1_0 = 0  
TLS1_1 = 1  
TLS1_2 = 1  
;BUGS = 1  
STATE = 0  
DEBUG = 1  
HSM = 0
```
