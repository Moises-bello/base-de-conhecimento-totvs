---
article_id: 25529054315927
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 2ac5e2a74321f0dbb370752da4135c38e32d0e22988f0310e2b357064f2fde18
fetched_at: '2026-06-28T22:42:45.747095+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Processamento do MRP bloqueado para
  este ambiente
type: support-article
updated_at: '2025-05-26T17:49:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25529054315927-Manufatura-Linha-Protheus-SIGAPCP-Processamento-do-MRP-bloqueado-para-este-ambiente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25529016185751) Tempo aproximado para leitura: **00:00:44 min****Ocorrência**Ao tentar executar a rotina **PCPA712 - MRP Memória** é apresentada a mensagem **Processamento do MRP bloqueado para este ambiente**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Esse incidente ocorre, pois a chave **MRPBlock** no arquivo **appserver.ini** na sessão **General** do ambiente do **Protheus** está com o conteúdo **1**.   
  
**Solução**Para solucionar essa ocorrência, altere o conteúdo da chave **MRPBlock** para **0** no arquivo **appserver.ini** na sessão **General** do ambiente do Protheus, como na imagem abaixo, ou retire a chave:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25529016187799)
