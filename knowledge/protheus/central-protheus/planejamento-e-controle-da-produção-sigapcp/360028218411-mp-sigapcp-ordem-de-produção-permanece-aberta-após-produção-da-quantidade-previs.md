---
article_id: 360028218411
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5ccc4765f103cf8c236e817757b08cf50685ed6c55b8e240f43845f92592dbe8
fetched_at: '2026-06-28T22:42:48.062990+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Ordem de Produção permanece aberta após produção da quantidade
  prevista
type: support-article
updated_at: '2020-03-11T19:15:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028218411-MP-SIGAPCP-Ordem-de-Produ%C3%A7%C3%A3o-permanece-aberta-ap%C3%B3s-produ%C3%A7%C3%A3o-da-quantidade-prevista
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:00 min****Dúvida**Por que a ordem de produção continua em aberto, mesmo tendo produzido toda a quantidade prevista?  
   
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**Ao realizar o último apontamento o mesmo não foi identificado como total e por este motivo, a ordem permanece como aberta. Neste caso, deve verificar por qual rotina este apontamento foi efetuado:

* Se o apontamento foi realizado pela rotina **MATA680 - Produção PCP MOD 1** ou **MATA681 - Produção PCP MOD 2** realize o estorno e aponte novamente.
* Se o apontamento foi feito pela rotina **MATA250 - Produção Simples,** selecione o último apontamento, clique em **Outras Ações,** e em **Encerrar**.
