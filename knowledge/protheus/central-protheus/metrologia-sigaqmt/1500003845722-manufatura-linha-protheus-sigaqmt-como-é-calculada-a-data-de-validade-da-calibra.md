---
article_id: 1500003845722
category: Metrologia (SIGAQMT)
content_hash: 06bd4fbd7ce5a2999db3eb336d7c9c3b74559b53654e8e32aaaa58211cc6a865
fetched_at: '2026-06-28T22:42:24.774373+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Como é calculada a data de validade
  da calibração do instrumento
type: support-article
updated_at: '2024-07-29T20:24:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003845722-Manufatura-Linha-Protheus-SIGAQMT-Como-%C3%A9-calculada-a-data-de-validade-da-calibra%C3%A7%C3%A3o-do-instrumento
---

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**Como é calculada a **Data de validade** da calibração do **Instrumento**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Solução**A data de validade de calibração do campo **Val. Calibr.** da rotina **QMTA010 - Instrumentos** é calculada levando em consideração a data em que a calibração deste instrumento foi realizada pela rotina **QMTA140 - Medições**, somando a quantidade de dias definido no campo **Freq.Calib.** do cadastro deste instrumento na rotina **QMTA010**.
