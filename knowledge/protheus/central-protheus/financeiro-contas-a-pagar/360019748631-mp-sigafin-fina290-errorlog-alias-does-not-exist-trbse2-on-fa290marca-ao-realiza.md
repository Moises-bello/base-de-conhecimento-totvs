---
article_id: 360019748631
category: Financeiro - Contas a Pagar
content_hash: a8cdc94d1a9c2a6b9a55be00fe78e69d34ed760d1778690b343746188eea489b
fetched_at: '2026-06-28T22:38:09.891462+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - FINA290 - Error.log "Alias does not exist TRBSE2 on FA290MARCA"
  ao realizar nova fatura a pagar
type: support-article
updated_at: '2021-04-28T15:19:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019748631-MP-SIGAFIN-FINA290-Error-log-Alias-does-not-exist-TRBSE2-on-FA290MARCA-ao-realizar-nova-fatura-a-pagar
---

**Ocorrência**Ao realizar nova fatura na rotina **FINA290** com a data de  22/08/2018 é apresentado o erro.log:  
Alias does not exist TRBSE2 on FA290MARCA(FINA290.PRW) 22/08/2018 09:55:30 line : 3288

**Ambiente**Microsiga Protheus - Financeiro - Versão 12.1.17  
   
 **Causa**Este **error.log** é apresentado no momento da montagem da tabela temporária para selecionar os títulos para gerar um nova fatura.  
   
 **Solução**Aplicar o pacote disponibilizado após a tratativa na *issue* DSERFINP-17758.  
  
Segue *link* para *download* do pacote:  
12.1.17: <https://suporte.totvs.com/portal/p/10098/download?e=711695>
