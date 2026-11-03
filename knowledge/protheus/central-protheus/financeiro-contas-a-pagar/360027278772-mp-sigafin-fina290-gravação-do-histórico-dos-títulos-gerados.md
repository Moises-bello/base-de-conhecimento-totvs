---
article_id: 360027278772
category: Financeiro - Contas a Pagar
content_hash: 492ebe97751f3ce1d91d6673853b30db507b175e0bff9b375b8fec71f80c039b
fetched_at: '2026-06-28T22:38:09.894315+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - FINA290 – Gravação do histórico dos títulos gerados
type: support-article
updated_at: '2021-04-28T15:18:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027278772-MP-SIGAFIN-FINA290-Grava%C3%A7%C3%A3o-do-hist%C3%B3rico-dos-t%C3%ADtulos-gerados
---

**Dúvida**Por que alguns títulos gerados por **Faturas a Pagar (FINA290)** não gravam o campo **E2\_HIST** (histórico)?  
   
 **Ambiente**Microsiga Protheus - Financeiro - A partir da versão 12  
  
**Solução**Ao emitir fatura de um título para N títulos, neste caso irá levar o conteúdo do histórico do título pai para os títulos filhos (títulos gerados por fatura).  
Ao emitir fatura de N títulos para um título (ou de N títulos para N títulos), não irá levar o conteúdo do histórico. Pois a rotina não irá saber qual dos históricos referente aos títulos que irá levar para o(s) título(s) filho(s).
