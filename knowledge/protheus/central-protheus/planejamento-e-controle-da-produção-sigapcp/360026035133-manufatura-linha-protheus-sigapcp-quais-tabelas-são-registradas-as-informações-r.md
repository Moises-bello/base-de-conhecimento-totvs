---
article_id: 360026035133
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 328fa3c35b269f181626e8ae5c257d7adbc9cea65111744cb1a29cd63363387c
fetched_at: '2026-06-28T22:42:45.778389+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Quais tabelas são registradas as informações
  referentes ao apontamento de perda
type: support-article
updated_at: '2021-07-26T17:50:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026035133-Manufatura-Linha-Protheus-SIGAPCP-Quais-tabelas-s%C3%A3o-registradas-as-informa%C3%A7%C3%B5es-referentes-ao-apontamento-de-perda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura**: 00:00:45 min**  
**Dúvida**Quando é realizado o apontamento de perda através do **MATA685 - Apontamento de perda** ou através da tela apresentada nas rotinas de apontamento de produção, em quais tabelas essa informação é registrada?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Os dados referentes ao apontamento de perda são registrados na tabela **SBC - Perda por OP**. Além disso, se o parâmetro **Requisita Produto de Origem**da rotina **MATA685** na opção **F12** estiver igual a **Sim**, e a informação for preenchida, também haverá um registro de requisição referente a este produto na tabela **SD3 - Movimentações internas**.   
Referente ao produto de destino, haverá a entrada em estoque também através da tabela **SD3**.
