---
article_id: 360058922853
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8f9668093a842add7d3dda3c29c40e9c201f03aa109e88d9fbbcf8371b410d72
fetched_at: '2026-06-28T22:42:44.514939+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem MATA680
type: support-article
updated_at: '2022-04-01T12:39:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058922853-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-MATA680
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:40 min  
  
Ocorrência**No apontamento de produção através da rotina **MATA681 - Produção PCP Mod2** é apresentada a mensagem **MATA680**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096836334/mceclip0.png)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**O Sistema possui uma validação impedindo o apontamento através do **MATA681** quando encontra registros de apontamento via **MATA250 - Produção Simples**, a validação ocorre através dos campos **D3\_IDENT - Identificador da OP pai** e **H6\_IDENT - Identificação da OP pai**.  
  
**Solução**  
Para apontar a produção através da rotina **MATA681**, é necessário realizar o estorno dos movimentos de produção da **OP - Ordem de Produção** na rotina **MATA250**.
