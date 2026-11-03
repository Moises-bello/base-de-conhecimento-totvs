---
article_id: 360035724253
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b0e1fd46371ae7a62d0a4eefae3afbdaa44dd27ca0e1ff9530cf10c2bf2049e3
fetched_at: '2026-06-28T22:38:30.000865+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nota sobre
  Ctbanfs utilizado via Schedule
type: support-article
updated_at: '2021-12-17T14:58:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035724253-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-Ctbanfs-utilizado-via-Schedule
---

**Dúvida**

Ao agendar via schedule do configurador do Protheus, a rotina **CTBANFS**, o processo não é executada.  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus)- SIGAFAT - todas as versões.  
  
**Solução**

A rotina de contabilização via faturamento, **CTBANFS**, só funciona via schedule, caso ela não esteja configurada para utilizar múltiplas threads.

Para identificar se o processo de contabilização está configurado para múltiplas threads, verifique o parâmetro **MV\_CNFSTHR** se está utilizando mais que 1 única thread.

Mais informações sobre contabilização:

**<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051395953-MP-FAT-CTBANFS-via-Schedule>**

**[FAT0161\_Como melhorar a performance da contabilização Off-Line (CTBANFS)](https://tdn.totvs.com/x/cPUFE)**

**[Integração Faturamento X SigaCtb (SIGAFAT)](https://tdn.totvs.com/x/W2nXIQ)**
