---
article_id: 360057226774
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d29e238db5af035d90c9b687191826df861ae5b5255840538efde4d889b16004
fetched_at: '2026-06-28T22:42:47.176940+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Conceito do parâmetro Saldo Rejeitado pelo CQ no MRP
type: support-article
updated_at: '2020-12-07T20:42:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057226774-MP-SIGAPCP-Conceito-do-par%C3%A2metro-Saldo-Rejeitado-pelo-CQ-no-MRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**De que forma o **MRP - Material Requirements Planning** avalia o estoque quando o parâmetro **Saldo Rejeitado pelo CQ** possui o **Subtrai Rejeit**?  
  
**Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**Quando o parâmetro **Saldo Rejeitado pelo CQ** possui o conteúdo **Subrai Rejeit**, o **MRP** verifica em cada armazém incluído no cálculo se há quantidade rejeitada e para a qual ainda não foi emitida nota fiscal de devolução ao fornecedor. Nesse processo, ele valida as tabelas **SD7 - Movimentações de CQ** e **SD2 - Itens de Venda da NF.**Em alguns casos, quando o cliente não emite nota fiscal de devolução ou a rejeição é proveniente de item produzido, a sugestão é, ao rejeitar o material através da rotina **MATA175 - Baixas de CQ**, remeter esse material rejeitado a um armazém de descarte, e não incluí-lo no cálculo do **MRP**.
