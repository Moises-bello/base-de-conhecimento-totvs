---
article_id: 360037247133
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 5176e80c9b645f51defafe18d372cbcd6552162de598b9d6c5ddde2a0cb1fc25
fetched_at: '2026-06-28T22:42:48.115941+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Saldo de terceiros no apontamento
type: support-article
updated_at: '2019-12-27T11:46:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037247133-MP-SIGAPCP-Saldo-de-terceiros-no-apontamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:45 min**  
 **Dúvida**No processo produtivo é consumido material de terceiros, como considerar esse saldo de terceiros como disponível no estoque, de modo a não apresentar a mensagem de falta de estoque?  
   
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**Na rotina de apontamento utilizada no processo**MATA250 - Apontamento Simples**, **MATA680 - Producao PCP Mod 1** ou **MATA681 - Produção PCP Mod 2**, altere o conteúdo do parâmetro **Cons. Saldo de 3º N/Poder** para **Sim**, lembrando que o saldo de terceiros deve estar no mesmo armazém do empenho.
