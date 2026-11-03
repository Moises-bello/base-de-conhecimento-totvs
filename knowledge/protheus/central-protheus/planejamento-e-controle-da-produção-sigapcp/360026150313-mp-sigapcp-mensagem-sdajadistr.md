---
article_id: 360026150313
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 769069643a42ab6b57f9b1b32def1bdfa65e17cb61952b75ef098062bc7033c6
fetched_at: '2026-06-28T22:42:47.280857+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Mensagem SDAJADISTR
type: support-article
updated_at: '2024-03-07T19:14:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026150313-MP-SIGAPCP-Mensagem-SDAJADISTR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:40 min****Ocorrência**No módulo **SIGAPCP - Planejamento e Controle da Produção** é apresentada a mensagem **SDAJADISTR** ao tentar realizar o estorno de um apontamento através das rotinas **MATA250 - Produção Simples**,  **MATA681 - Produção PCP Mod2** ou **MATA680 - Produção PCP Mod1**.  
   
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
   
 **Causa**Essa mensagem é apresentada quando o saldo criado pela movimentação já foi distribuído, ou seja, endereçado.  
   
 **Solução**  
Para poder estornar o apontamento é necessário realizar primeiramente o estorno do endereçamento gerado por este movimento através da rotina **MATA265 - Endereçar produtos**, para depois poder estornar o apontamento através do programa em que ele foi realizado.
