---
article_id: 360028907272
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: de922b82e78b4ba51a25ba94ca39663e1f4a9ee50c0f4bab86ad22bdc04c14b0
fetched_at: '2026-06-28T22:42:45.789579+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Qual o objetivo do parâmetro MV_A650GEF
type: support-article
updated_at: '2021-05-26T11:38:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028907272-Manufatura-Linha-Protheus-SIGAPCP-Qual-o-objetivo-do-par%C3%A2metro-MV-A650GEF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:30 min****Dúvida**Qual o objetivo do parâmetro **MV\_A650GEF - Gera empenho considerando todas as filiais**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O objetivo do parâmetro **MV\_A650GEF** é gerar empenhos, ordens de produção intermediárias e/ou solicitações de compra para todas as pendências do Sistema, independente da filial, quando o conteúdo igual a **S-Sim**. Caso contrário, gerará somente para a filial logada.  
Por *default*,o parâmetro assume o conteúdo **N-Não**.
