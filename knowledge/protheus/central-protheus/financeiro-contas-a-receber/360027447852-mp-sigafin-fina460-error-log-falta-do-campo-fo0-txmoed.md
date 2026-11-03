---
article_id: 360027447852
category: Financeiro - Contas a Receber
content_hash: c12d5257f9ffe5ee78cd385f46a4bc535490ffae1fea2f0e2d428e6cecfde710
fetched_at: '2026-06-28T22:38:15.065432+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - FINA460 - Error log falta do campo FO0_TXMOED
type: support-article
updated_at: '2021-04-28T15:17:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027447852-MP-SIGAFIN-FINA460-Error-log-falta-do-campo-FO0-TXMOED
---

**Ocorrência**Ao realizar o processo de **liquidação** na rotina **FINA460** é apresentado o errorlog "erro no parâmetroFWFormViewStruct: O erro no método SETPROPERTY: Campo **FO0\_TXMOED** não encontrado. on FWFORMVIEWSTRUCT:SETPROPERTY(FWFORMVIEWSTRUCT.PRW)"

**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.1.17  
   
 **Causa**Falta do campo **FO0\_TXMOED.**  
   
 **Solução**  
Aplicar o pacote do dicionário diferencial onde consta o campo **FO0\_TXMOED.**

Segue *link* para *download* do pacote:<https://suporte.totvs.com/portal/p/10098/download#detail/706376>  
  
Print dos campos padrões da **tabela FO0**:  
  
![](https://totvssuporte.zendesk.com/attachments/token/6mhx3KauWgUkc0a9uiZQGc9uU/?name=inline-1860654944.png)
