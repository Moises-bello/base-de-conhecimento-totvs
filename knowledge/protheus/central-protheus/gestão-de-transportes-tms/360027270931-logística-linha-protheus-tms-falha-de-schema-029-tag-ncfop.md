---
article_id: 360027270931
category: Gestão de Transportes (TMS)
content_hash: 23e6a811fe7b0ddf5382c0edd42c68093145fda193f1e60efe7a25de0388c0a7
fetched_at: '2026-06-28T22:45:29.155976+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Falha de SCHEMA 029, TAG <nCFOP>
type: support-article
updated_at: '2022-06-01T19:23:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027270931-Log%C3%ADstica-Linha-Protheus-TMS-Falha-de-SCHEMA-029-TAG-nCFOP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:20 min****Dúvida**Como contornar a falha de *SCHEMA* 029 relacionada a *TAG **<*****nCFOP*****>***?

![Capturar8.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026800671/Capturar8.PNG)

**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Essa falha é que o CFOP da NF-e - Nota fiscal eletrônica transportada não foi informado na entrada do documento, campo DTC\_CF.

![Capturar9.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026791392/Capturar9.PNG)

Após a informação do campo, calcule novamente do documento e realize uma nova tentativa de transmissão.
