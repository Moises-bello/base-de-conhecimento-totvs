---
article_id: 35630426395927
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: afd865a2d76448f7ddde2d535c9f5f518ec27feaa95789676beec83194b02a0d
fetched_at: '2026-06-28T22:42:40.986547+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Campo Armazém - C2_LOCAL bloqueado
  na alteração da Ordem de Produção
type: support-article
updated_at: '2025-10-14T20:02:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35630426395927-Manufatura-Linha-Protheus-SIGAPCP-Campo-Armaz%C3%A9m-C2-LOCAL-bloqueado-na-altera%C3%A7%C3%A3o-da-Ordem-de-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35630426385559) Tempo aproximado para leitura: **00:00:40 min**  
  
**Dúvida**  
Por que o campo **Armazém - C2\_LOCAL** fica bloqueado na alteração de uma **Ordem de produção - MATA650**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
O campo **C2\_LOCAL**fica bloqueado na alteração de uma **OP - Ordem de produção** porque a quantidade pendente de produção da **OP** está registrada na tabela **SB2 - Saldos Físico e Financeiro**, no campo **B2\_SALPEDI - Qtd Prevista**para o armazém informado da **OP**.   
  
Para alterar o **Armazém**, **exclua**ou **encerre** a **OP** atual e inclua uma nova ordem de produção para o novo **Armazém**.
