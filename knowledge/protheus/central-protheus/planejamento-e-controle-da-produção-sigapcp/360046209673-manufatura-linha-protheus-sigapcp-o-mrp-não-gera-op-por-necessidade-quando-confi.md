---
article_id: 360046209673
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: ae58474423567c141945943bb0efee4e7c7c8359379295143c619529db1e97da
fetched_at: '2026-06-28T22:42:44.639704+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - O MRP não gera OP por necessidade quando
  configurado o campo B5_FORMMRP
type: support-article
updated_at: '2021-07-30T11:45:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046209673-Manufatura-Linha-Protheus-SIGAPCP-O-MRP-n%C3%A3o-gera-OP-por-necessidade-quando-configurado-o-campo-B5-FORMMRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:35 min**  
**Dúvida**Por que o **MRP - Material Requirement Planning** não gera **OP - Ordem de Produção** por necessidade para o produto configurado no campo **B5\_FORMMRP - Form. MRP**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Ao marcar no produto o campo **B5\_FORMMRP** **Por Necessidade**, o **MRP** não gerará as **OPs** dele por necessidade.  
Serão geradas por necessidade as **OPs intermediárias**, ou seja, dos componentes intermediários que fazem parte da estrutura daquele produto.
