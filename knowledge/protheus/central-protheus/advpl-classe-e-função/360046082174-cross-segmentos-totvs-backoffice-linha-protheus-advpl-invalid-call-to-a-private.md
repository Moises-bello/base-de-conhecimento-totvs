---
article_id: 360046082174
category: ADVPL - Classe e Função
content_hash: c700336e20dd381e45cbe1a595eedf920915291652fe5722bfd3d69569aebf6d
fetched_at: '2026-06-28T22:40:20.479321+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Invalid call to a PRIVATE data named  DESCRIPTION
type: support-article
updated_at: '2022-01-11T21:48:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046082174-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Invalid-call-to-a-PRIVATE-data-named-DESCRIPTION
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**

```
Descrição de erro: [Invalid call to a PRIVATE data named  DESCRIPTION__}Pilha de Erro: [  
THREAD ERROR ([71864], HTTP_WT_P1225_HTTPREST_HTTPURI@99þ01|FALSE, THIS)   13/04/2020 16:06:48  
Invalid call to a PRIVATE data named  DESCRIPTION__ on H_FWRESTSRV(FWRESTSRV.APH) 05/03/2020 22:36:09 line : 21  
  
[TOTVS build: 7.00.170117A-20200102]  
Called from FWAPILIST(FWRESTSRV.PRW) 05/03/2020 22:36:09 line : 544  
Called from REST_CONNECT(FWRESTSRV.PRW) 05/03/2020 22:36:09 line : 437  
Called from HTTP_WT(FWHTTPSRV.PRX) 05/03/2020 22:36:09 line : 883
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL  – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois a classe **WSRESTFUL** não pode ser em TLPP.  
  
**Solução**Para solucionar essa ocorrência, compile a classe em  .PRW ou .PRW.
