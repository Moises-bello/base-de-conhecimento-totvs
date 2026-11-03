---
article_id: 360027902712
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 4b50c4f5f584b753775d42a089292afa8681c0945cc75a72df07d2de9f9797c9
fetched_at: '2026-06-28T22:39:44.361474+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - FA050DELPA
type: support-article
updated_at: '2021-12-27T13:07:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027902712-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-FA050DELPA
---

**Ocorrência**No módulo SIGAEIC, ao tentar realizar o estorno da compensação de um PA é apresentada mensagem **FA050DELPA** O cheque referente a este título já foi impresso.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Causa**Este ocorre pois o parâmetro MV\_EIC0001 esta com conteúdo, gerando assim uma numeração de cheque para o Financeiro (SIGAFIN).  
  
**Solução**Apagar o conteúdo do parâmetro MV\_EIC0001.  
Para os processo que estão apresentando a mensagem deve-se realizar através do SIGAFIN exclusão da geração do cheque, sendo assim será necessário excluir primeiramente o cheque na rotina FINA190 e após isso excluir o PA.
