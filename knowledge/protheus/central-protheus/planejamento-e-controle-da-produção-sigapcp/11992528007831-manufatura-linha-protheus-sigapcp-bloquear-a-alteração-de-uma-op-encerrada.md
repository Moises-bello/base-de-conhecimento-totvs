---
article_id: 11992528007831
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: b542ac617667b837757324870881940a4f63aaecae6463f038872a0801bbd8d5
fetched_at: '2026-06-28T22:42:40.903506+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Bloquear a alteração de uma OP encerrada
type: support-article
updated_at: '2024-05-06T20:21:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11992528007831-Manufatura-Linha-Protheus-SIGAPCP-Bloquear-a-altera%C3%A7%C3%A3o-de-uma-OP-encerrada
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:36 min  
  
Dúvida**É possível bloquear o alteração de uma **OP - Ordem de Produção** encerrada?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Sim, para que o Sistema não permita realizar a alteração de uma **OP** encerrada através da rotina **MATA650 - Ordem de Produção**, o parâmetro **MV\_ATOPFEC - Permite alterar OP encerrada para campos do usuário**, deve ter seu conteúdo igual a **1**.
