---
article_id: 360036507173
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 717852a700331bf8a7c26bd6852de0d36bc83dea8f5525cf5a769895eca87ecc
fetched_at: '2026-06-28T22:42:44.677026+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Objetivo do parâmetro MV_PATUEMP
type: support-article
updated_at: '2023-10-25T20:13:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036507173-Manufatura-Linha-Protheus-SIGAPCP-Objetivo-do-par%C3%A2metro-MV-PATUEMP
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:45 min**  
 **Dúvida**Qual o objetivo do parâmetro **MV\_PATUEMP - Pergunta se atualizar o empenho quando o TM não atualiza empenho (F5\_ATUEMP ="N")**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Ao encerrar uma **OP - Ordem de Produção** cujo **TM - Tipo de Movimento** utilizado para o apontamento não atualiza o empenho, campo **Atu. Empenho -****F5\_ATUEMP** igual a **N - Não**, e o parâmetro **MV\_PATUEMP** está com conteúdo igual a **S** o usuário será questionado se o empenho deve ser atualizado, zerando assim a quantidade empenhada.  
Ou seja, tendo o mesmo comportamento de quando a **TM** possui o campo **F5\_ATUEMP** igual a **S**.
