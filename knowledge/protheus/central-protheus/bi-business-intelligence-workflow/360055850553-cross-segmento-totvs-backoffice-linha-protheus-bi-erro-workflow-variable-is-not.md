---
article_id: 360055850553
category: BI - Business- Intelligence - Workflow
content_hash: 840f3d6a38e54fc00e2478de2841755c5cef3679d4ef6d4c23d1f7cc978bb7b6
fetched_at: '2026-06-28T22:37:03.036280+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Erro Workflow "Variable
  is not array - Tipe [U]"
type: support-article
updated_at: '2025-02-18T19:18:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055850553-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Erro-Workflow-Variable-is-not-array-Tipe-U
---

**Ocorrência**Ao disparar um novo Workflow, o sistema retorna o seguinte erro:  
  
**variable is not array - Type [U]**  
**Called from: SENDMAIL - Line: 729**  
**Called from: SEND - Line: 477**  
**Called from: SEND - Line: 227**  
**Called from: WFJOBSNDMAIL - Line: 345**  
**Called from: WFLAUNCHER - Line: 489****Ambiente**MP – BI – A partir da versão 11.80  
  
**Causa**Este erro ocorre devido a uma inconsistência em um dos arquivos **.wfm** gerados pelo Workflow, que eventualmente ainda está preso dentro da pasta **"Outbox"** do processo.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360090933334/mceclip0.png)  
  
**Solução**Neste caso, sugerimos que faça inicialmente um Backup da pasta **Outbox** e em seguida exclua todos os arquivos **.wfm** da mesma. Desta forma, o próximo disparo do Workflow criará um novo arquivo e enviará o e-mail corretamente.
