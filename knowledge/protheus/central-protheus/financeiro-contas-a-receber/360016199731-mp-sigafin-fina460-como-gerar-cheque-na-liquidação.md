---
article_id: 360016199731
category: Financeiro - Contas a Receber
content_hash: f6711ee92fbd7aa62e64bd1d82ce154f3a4ebf482995c465b377b25ad72b9ad1
fetched_at: '2026-06-28T22:38:14.245275+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'MP - SIGAFIN  - FINA460 - Como gerar cheque na liquidação '
type: support-article
updated_at: '2021-04-28T15:17:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016199731-MP-SIGAFIN-FINA460-Como-gerar-cheque-na-liquida%C3%A7%C3%A3o
---

**Dúvida**Como gerar cheque na liquidação?  
   
 **Ambiente**Microsiga Protheus - Contas a Receber - Liquidação (FINA460)   
   
**Solução**

Na rotina de **liquidação (FINA460)**, utilize o tipo de título **CH**.  
  
Com o parâmetro **MV\_GRSEFLQ = .T.(True)**: será gerado um cheque automaticamente na tabela**SEF Cadastro de cheques.**Caso contrário o parâmetro **MV\_GRSEFLQ = .F.****(False)**: não será gerado um cheque automaticamente na tabela**SEF Cadastro de cheques.**
