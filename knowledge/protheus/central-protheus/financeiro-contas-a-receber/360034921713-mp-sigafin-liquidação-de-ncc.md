---
article_id: 360034921713
category: Financeiro - Contas a Receber
content_hash: 98904d85e79795b3a28d32314f427b3fba54c19a8b134ab8f664b9ce8a1e1bab
fetched_at: '2026-06-28T22:38:15.110167+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN- Liquidação de NCC
type: support-article
updated_at: '2021-04-28T15:17:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034921713-MP-SIGAFIN-Liquida%C3%A7%C3%A3o-de-NCC
---

**Ocorrência**  
 No módulo Financeiro, ao tentar liquidar um título do tipo NCC, o registro não é localizado.  
   
 **Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 12.1.17

**Causa**   
 Esse incidente ocorre, devido a uma validação na rotina de liquidação (FINA460), que não irá apresentar os títulos de crédito(NCC), pois esta rotina tem por funcionalidade apenas a negociação/renegociação de parcelas e prazos, e estes títulos devem ser utilizados em compensações através da rotina destinada para esta finalidade, Compensação CR(FINA330).  
   
 **Solução**Utilize a rotina de compensação a receber (FINA330) para compensação deste tipo de título.
