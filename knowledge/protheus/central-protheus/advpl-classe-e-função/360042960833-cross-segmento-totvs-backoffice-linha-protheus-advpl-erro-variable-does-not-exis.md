---
article_id: 360042960833
category: ADVPL - Classe e Função
content_hash: 75cd9900b9fb367a5998d2c1b6d7c7842f1c03d2ce1222ba0a87b00402eaae91
fetched_at: '2026-06-28T22:40:15.839258+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro variable does
  not exist CFILANT
type: support-article
updated_at: '2021-10-11T12:16:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042960833-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-variable-does-not-exist-CFILANT
---

**Ocorrência**Ao executar uma rotina via JOB ocorre o erro

"variable does not exist CFILANT on SUPERGETMV(MATXFUNA.PRX)"

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057616633/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Ambiente não está preparado esta sendo utilizado alguma função do repositório.  
  
**Solução**Qualquer função que esteja no repositório precisa ser executada após preparar o ambiente quando executada via Job, Schedule e WebService.
