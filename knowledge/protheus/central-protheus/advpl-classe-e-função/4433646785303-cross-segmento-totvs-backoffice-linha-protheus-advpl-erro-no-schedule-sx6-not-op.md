---
article_id: 4433646785303
category: ADVPL - Classe e Função
content_hash: c38a3119a7c13f2b82833955ad0a64d609d131588138d35628fe666af34beb59
fetched_at: '2026-06-28T22:40:15.819814+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro no Schedule:
  SX6 not open for GetMV'
type: support-article
updated_at: '2022-02-16T13:22:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4433646785303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-no-Schedule-SX6-not-open-for-GetMV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao executar uma rotina via Schedule ocorre o erro   
"SX6 not open for GetMV in file"  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões  
  
**Causa**Ambiente não está aberto esta sendo utilizado alguma função do repositório.  
  
**Solução**Isto ocorre devido ao fato do ambiente não estar preparado (`RPCSetEnv()` ou `PREPARE ENVIRONMENT`):  
Uma vez que o ambiente não está preparado, o arquivo de trabalho da SX6 não estará aberto para utilizar de `GetMV()`.  
  
**Saiba mais**[RpcSetEnv](https://tdn.totvs.com/pages/releaseview.action?pageId=6814927)
