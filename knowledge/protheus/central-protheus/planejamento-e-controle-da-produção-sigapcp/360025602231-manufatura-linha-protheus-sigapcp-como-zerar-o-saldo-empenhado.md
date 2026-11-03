---
article_id: 360025602231
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d349b24de7ec01506fa6086517ecd2d513fe57d6ea33360f98e0cf6271037ed3
fetched_at: '2026-06-28T22:42:42.063263+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Como zerar o saldo empenhado
type: support-article
updated_at: '2025-07-04T20:00:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025602231-Manufatura-Linha-Protheus-SIGAPCP-Como-zerar-o-saldo-empenhado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33259038173847)***Tempo aproximado para leitura: **00:01:05 min****Dúvida**Como zerar o saldo empenhado?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Quando já houve o apontamento de alguma quantidade, o campo **D4\_QTDEORI - Quantidade Empenho** deve possuir a quantidade que foi empenhado e o campo **D4\_QUANT - Saldo Empenho** o valor **0**, assim o Sistema identifica que daquele componente não há mais quantidade a ser requisitada.  
  
Essa alteração pode ser realizada:

* Selecionar o registro desejado > **Alterar** > **Outras Ações** > **Zera Emp.** nas rotinas **MATA380 - Empenho Simples** ou **MATA381 - Empenho Múltiplo**;
* Zerando automaticamente quando realizar o apontamento total da **OP - Ordem de Produção**.

Se a **OP - Ordem de****Produção** estiver encerrada e mesmo assim tiver saldo empenhado é necessário:

* Acessar o **MATA381** > **Selecione a OP encerrada** > **Visualizar** > **Outras ações** > **Zerar empenho**> **Será apresentada a mensagem perguntando se deseja zerar o empenho** > Clicar em **Sim** > **Confirmar**.  
  Desta forma o saldo do empenho é zerado.
