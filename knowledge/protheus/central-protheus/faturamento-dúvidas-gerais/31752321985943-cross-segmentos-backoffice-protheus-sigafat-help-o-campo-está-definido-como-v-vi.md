---
article_id: 31752321985943
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 97bb96ace00555f0f0dd617f1e83186564133a8757795e1b016cc23574144f19
fetched_at: '2026-06-28T22:38:29.818200+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help "O campo está definido
  como V-Virtual na coluna X3_CONTEXT"
type: support-article
updated_at: '2025-04-30T17:34:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31752321985943-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-O-campo-est%C3%A1-definido-como-V-Virtual-na-coluna-X3-CONTEXT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31752321955863) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como resolver o Help "O campo está definido como V-Virtual na coluna X3\_CONTEXT" ao atualizar o UPDDISTR?

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**O erro ocorre, pois o campo está marcado no dicionário do Protheus (tabela SX3) como virtual (X3\_CONTEXT = 'V - Virtual') mas existe no banco, sendo inconsistente, pois se existir no banco ele não é virtual.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31752342989079)

Deve ser contatado um DBA ou Analista In Loco para realizar a retirada do banco de dados o campo físico da tabela, pois ele deve ser virtual, ou, alterar o contexto do campo (X3\_CONTEXT) no configurador e tratar os impactos desta alteração.
