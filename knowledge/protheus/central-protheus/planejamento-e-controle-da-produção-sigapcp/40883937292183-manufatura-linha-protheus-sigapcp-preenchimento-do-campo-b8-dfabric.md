---
article_id: 40883937292183
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 91bd5b93ce134565225fdf6e5c03ad271636b91b8ea1340c97551742cd2a99a2
fetched_at: '2026-06-28T22:42:45.698305+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Preenchimento do campo B8_DFABRIC
type: support-article
updated_at: '2026-06-02T18:33:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40883937292183-Manufatura-Linha-Protheus-SIGAPCP-Preenchimento-do-campo-B8-DFABRIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40883937274775) Tempo aproximado para leitura: **00:00:36 min**  
  
**Dúvida**  
Ao apontar uma produção como é preenchido o campo **B8\_DFABRIC - Data de Fabricação do Lote**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
No apontamento de produção, o campo **B8\_DFABRIC** é preenchido com a *database* do sistema do primeiro apontamento que gerou o registro na base de dados. Sendo assim, nos demais apontamentos do mesmo lote, em outras *databases* o conteúdo do campo **B8\_DFABRIC** não é alterado.
