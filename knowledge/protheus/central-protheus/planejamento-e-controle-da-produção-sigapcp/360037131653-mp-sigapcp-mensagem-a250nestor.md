---
article_id: 360037131653
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 983c118e9759ec1d4e18728e136b719aea57585bc27787599a9eb5b85779d5c8
fetched_at: '2026-06-28T22:42:47.239437+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Mensagem A250NESTOR
type: support-article
updated_at: '2020-09-08T13:47:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037131653-MP-SIGAPCP-Mensagem-A250NESTOR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:45 min**  
 **Ocorrência**Ao tentar estornar o apontamento de produção por meio da rotina **MATA250 - Produção Simples**, o usuário recebe a mensagem **A250ESTORN - Este apontamento de produção não poderá ser estornado**.  
   
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
   
 **Causa**Esta mensagem surge quando o apontamento de produção foi realizado através da rotina **MATA680 - Produção PCP Mod 1** ou **MATA681 - Produção PCP Mod 2**.  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:  
 1. Acesse a rotina utilizada para o apontamento, **MATA680** ou **MATA681**;  
 2. Estorne o apontamento por meio desta rotina.
