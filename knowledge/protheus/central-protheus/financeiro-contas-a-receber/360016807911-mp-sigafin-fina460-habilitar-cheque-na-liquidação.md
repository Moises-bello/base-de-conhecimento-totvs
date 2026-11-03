---
article_id: 360016807911
category: Financeiro - Contas a Receber
content_hash: 6aa3e61e14d4ddaf37c455bf0bc3cd49ff6c387ef0b00b88787e620e11d74f86
fetched_at: '2026-06-28T22:38:14.247634+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'MP - SIGAFIN  - FINA460 - Habilitar cheque na liquidação '
type: support-article
updated_at: '2021-04-28T15:17:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016807911-MP-SIGAFIN-FINA460-Habilitar-cheque-na-liquida%C3%A7%C3%A3o
---

**Dúvida**Como fazer para habilitar o cheque na rotina de **Liquidação** **FINA460**?  
   
 **Ambiente**Microsiga Protheus - Financeiro - FINA460  - A partir da versão 12  
  
   
**Solução**Para habilitar o campo cheque na rotina de **Liquidação** **FINA460**, se faz necessário alterar o parâmetro **MV\_GRSEFLQ** que deve ser preenchido com **conteúdo = T** no módulo **Configurador.**

**Importante:**O parâmetro **MV\_GRSEFLQ** indica se deseja gravar cheque no cadastro de cheque **(SEF)** quando gerada uma liquidação de títulos do **tipo CH  = T**
