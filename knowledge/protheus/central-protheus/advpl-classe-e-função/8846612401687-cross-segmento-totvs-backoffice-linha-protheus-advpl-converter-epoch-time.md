---
article_id: 8846612401687
category: ADVPL - Classe e Função
content_hash: 10546b69120c60384b745039060bacf652d17b57d12457b9de60f5b039d94565
fetched_at: '2026-06-28T22:40:15.689536+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Converter Epoch
  Time
type: support-article
updated_at: '2023-05-22T21:28:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8846612401687-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Converter-Epoch-Time
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**  
Como converter para Data e Time?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Todas as versões  
  
**Solução**Atualmente não possuímos função para esta finalidade, no entanto pode desenvolver sua própria função para esta, desde que saiba qual a base do seu **EPOCH**, digamos que seja 1970.  
  
**Exemplo:**

```
Data Epoch =1596060836  
  
nSec:=1596060836  
  
dData :=  CToD("01/01/1970") +  Int(nSec/86400) // Retorna a data  
  
nAdicionais :=  Int(nSec%86400) // segundos adicionais da data
```
