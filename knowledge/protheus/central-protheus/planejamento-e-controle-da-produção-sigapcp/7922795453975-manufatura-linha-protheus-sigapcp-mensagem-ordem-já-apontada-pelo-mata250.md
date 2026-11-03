---
article_id: 7922795453975
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 42219761cc0875a0eb5ba04dcbb95512947392c1a6a3686ff2245e7bc756c049
fetched_at: '2026-06-28T22:42:44.532825+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem ordem já apontada pelo MATA250
type: support-article
updated_at: '2022-08-03T17:32:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7922795453975-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-ordem-j%C3%A1-apontada-pelo-MATA250
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:45 min****Ocorrência**Ao tentar realizar o apontamento pela rotina **MATA681 - Apontamento de Produção Modelo 2** ou **MATA680 - Apontamento de Produção Modelo 1** o usuário recebe a mensagem **Ordem já apontada pelo MATA250 (Apontamento Simples). Não é permitido realizar o apontamento.**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**A mensagem ocorre quando a **OP - Ordem de Produção** já foi apontada pelo **MATA250** e ao tentar realizar o apontamento pelo **MATA680**/**MATA681** o usuário informa uma quantidade diferente de zero.  
  
**Solução**Neste caso é possível realizar somente apontamentos de tempo pela rotinas **MATA680** ou **MATA681**.
