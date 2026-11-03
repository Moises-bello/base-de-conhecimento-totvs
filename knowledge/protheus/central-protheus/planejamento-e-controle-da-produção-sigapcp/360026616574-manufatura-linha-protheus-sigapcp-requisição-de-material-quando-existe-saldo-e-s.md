---
article_id: 360026616574
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 059a0ebd00b5b04119069864d018bf608b7f95d0bf96a0fca84f4c8233316d8f
fetched_at: '2026-06-28T22:42:45.872727+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Requisição de material quando existe
  saldo e solicitação de compra
type: support-article
updated_at: '2021-10-26T16:39:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026616574-Manufatura-Linha-Protheus-SIGAPCP-Requisi%C3%A7%C3%A3o-de-material-quando-existe-saldo-e-solicita%C3%A7%C3%A3o-de-compra
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**Se existir uma **SC - Solicitação de Compra** relacionada com a **OP - Ordem de Produção**, mas que ainda não foi atendida, o Sistema identifica esse cenário e impede o apontamento da **OP**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Se existir estoque disponível ou se o parâmetro **MV\_ESTNEG - Identifica se o sistema permitirá que os saldos em estoque dos produtos fique negativo através de movimentação**, estiver com o conteúdo **S**, o Sistema permite o apontamento, mesmo que a **OP** tenha uma **SC** que não foi atendida.  
Neste momento ocorre somente a validação do saldo, não sendo considerada as pendências de **SCs**
