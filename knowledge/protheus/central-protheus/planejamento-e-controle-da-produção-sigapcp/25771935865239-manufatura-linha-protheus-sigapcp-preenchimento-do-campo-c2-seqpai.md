---
article_id: 25771935865239
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 12167fa5c1f6dea29feefb545c3610e32a308aaa1a5f1e9182ece0209d74cd1c
fetched_at: '2026-06-28T22:42:45.709923+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Preenchimento do campo C2_SEQPAI
type: support-article
updated_at: '2024-08-20T16:51:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25771935865239-Manufatura-Linha-Protheus-SIGAPCP-Preenchimento-do-campo-C2-SEQPAI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25771935846935) Tempo aproximado para leitura: **00:02:48 min** **Dúvida**Como se dá o preenchimento do campo **C2\_SEQPAI**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Ao incluir uma **OP** e gerar automaticamente **OPIs**, no campo **C2\_SEQPAI** temos a informação da sequência (campo **C2\_SEQUEN**), desse conjunto de **OPs**, que tem o item em questão empenhado e que por isso demanda a abertura da **OPI** **- Ordem de Produção** intermediária avaliada.  
  
**Exemplo**Supondo que temos a estrutura abaixo:

**![Estrutura.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/25771935848087)**

Onde ao incluir a **OP** com **C2\_NUM** 000001 , **C2\_ITEM** 01 e **C2\_SEQUEN** 001 para o PA, são geradas automaticamente as **OPIs** listadas abaixo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **C2\_NUM** | **C2\_ITEM** | **C2\_SEQUEN** | **C2\_PRODUTO** | **C2\_SEQPAI** |
| 000001 | 01 | 002 | PI01 | 001 |
| 000001 | 01 | 003 | PI02 | 002 |
| 000001 | 01 | 004 | PI04 | 003 |
| 000001 | 01 | 005 | PI03 | 001 |

Ao avaliarmos o campo **C2\_SEQPAI** da **OP** com **C2\_NUM** 000001, **C2\_ITEM** 01 e **C2\_SEQUEN** 001 observamos que esse campo está em branco, isso porque essa é a **OP** pai do conjunto e neste conjunto seu produto não está empenhado para nenhuma outra **OP.**  
Já a **OP** com **C2\_NUM** 000001 **C2\_ITEM** 01 e **C2\_SEQUEN** 002 tem o campo **C2\_SEQPAI** preenchido com 001, já que o produto PI01 está empenhado para a **OP** com **C2\_NUM**  000001 **C2\_ITEM** 01 e **C2\_SEQUEN** 001.  
  
A **OP** com **C2\_NUM** 000001 **C2\_ITEM** 01  e **C2\_SEQUEN** 003 tem o campo **C2\_SEQPAI** preenchido com 002, já que  o produto PI02 está empenhado para a **OP** com **C2\_NUM** 000001 **C2\_ITEM** 01 e **C2\_SEQUEN** 002.  
  
A **OP** com **C2\_NUM** 000001 **C2\_ITEM** 01  e **C2\_SEQUEN** 004 tem o campo **C2\_SEQPAI** preenchido com 003, já que o produto PI04 está empenhado para a **OP** com **C2\_NUM** 000001 **C2\_ITEM** 01 e **C2\_SEQUEN** 003.  
  
E por fim, a **OP** com **C2\_NUM** 000001 **C2\_ITEM** 01  e **C2\_SEQUEN** 005 tem o campo **C2\_SEQPAI** preenchido com 001, já que o produto PI03 está empenhado para a OP com **C2\_NUM** 000001 **C2\_ITEM** 01 e **C2\_SEQUEN** 001  
  
**Glossário****OP** - Ordem de produção **OPs** - Ordens de produções **OPI** - Ordem de produção intermediária **OPIs** - Ordens de produções intermediárias  
**C2\_NUM** - Número ordem de produção **C2\_ITEM** - Item da ordem de produção **C2\_SEQUEN** - Sequência da ordem de produção **C2\_PRODUTO** - Código do produto  **C2\_SEQPAI** - Sequência da OP Pai
