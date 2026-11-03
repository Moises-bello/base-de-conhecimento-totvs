---
article_id: 360025667771
category: Gestão de Transportes (TMS)
content_hash: 5278f1bbb567a7878d6325a655e916817d23fc1fc38151254ef86df889661c21
fetched_at: '2026-06-28T22:45:29.148379+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Falha de SCHEMA 029, tag <ICMS>
type: support-article
updated_at: '2022-06-01T21:09:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025667771-Log%C3%ADstica-Linha-Protheus-TMS-Falha-de-SCHEMA-029-tag-ICMS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)*** Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como contornar a falha de *schema* 029 relacionada a ***tag <ICMS>***

***![falha_no_schema.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024423692/falha_no_schema.PNG)***

**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para contornar essa situação, a **TES** **- Tipos de entrada e saída** utilizada para o calculo do **CT-e - Conhecimento de Transporte eletrônico**, deve ter o campo **F4\_SITTRIB** preenchida.  
  
Realize o ajuste na **TES**, após estorne o calculo, calcule novamente e faça uma nova transmissão.
