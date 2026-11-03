---
article_id: 360007550951
category: Gestão de Transportes (TMS)
content_hash: 2eb4f9d47a6555ce2f14acc57d1add0111bac11778e5c3927bf16567d08a377a
fetched_at: '2026-06-28T22:45:27.718212+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Error TMSA240VLD
type: support-article
updated_at: '2023-02-28T14:07:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007550951-Log%C3%ADstica-Linha-Protheus-TMS-Error-TMSA240VLD
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:25 min****Dúvida**Por que é apresentado erro **TMSA240VLD**, no processo de emissão de **CT-e** na viagem *express*, durante a tentativa de transmissão do documento junto a **SEFAZ**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**Efetuado ajuste na rotina de Complemento de Viagem **TMSA240,** referente ao erro na inclusão de uma viagem *express*.  
Os procedimentos a serem realizados:

* Verificar se o parâmetro **MV\_TMSCVIAG** consta como 0

Caso afirmativo, alterar este parâmetro para 1 e realizar um novo teste.
