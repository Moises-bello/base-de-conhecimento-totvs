---
article_id: 4420633928727
category: Inspeção de Entradas (SIGAQIE)
content_hash: aabcb29587306d00cee0a032a80cd802c6c55dc9b5615fc2572230d9a7ae2d2e
fetched_at: '2026-06-28T22:42:26.951329+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAQIE - Error log QE6010: SetOrder - Index
  not found. on A215DEPR'
type: support-article
updated_at: '2022-01-28T18:05:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420633928727-Manufatura-Linha-Protheus-SIGAQIE-Error-log-QE6010-SetOrder-Index-not-found-on-A215DEPR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:35 min****Ocorrência**Na rotina **QIEA215 - Resultados** ocorre o **error.log** **QE6010: SetOrder - Index not found. on A215DEPR(QIEA215.PRW)**.

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**O **error.log QE6010: SetOrder - Index not found. on A215DEPR(QIEA215.PRW)** ocorre quando não existe o índice **3** da tabela **QE6 - Especificações** na tabela **SIX -****Índices**, conforme exemplificado abaixo:

![_ndice_QE6.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4420633792023/_ndice_QE6.jpg)

**Solução**  
Para solucionar essa ocorrência, ajuste o índice **3** da tabela **QE6** na tabela **SIX**, conforme tabela **SIX** anexada neste artigo.
