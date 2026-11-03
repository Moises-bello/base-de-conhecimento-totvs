---
article_id: 360025941751
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 4aa991c33158134b3e6b6464300c59a4932d4159e1c046bb28f4e02bb68d5160
fetched_at: '2026-06-28T22:42:45.792004+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Quando é realizado o registro na tabela
  SDC '
type: support-article
updated_at: '2021-11-23T14:44:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025941751-Manufatura-Linha-Protheus-SIGAPCP-Quando-%C3%A9-realizado-o-registro-na-tabela-SDC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**  Tempo aproximado para leitura: **00:00:57 min****Dúvida**Por que ao empenhar o material, não ocorre registro do empenho na tabela **SDC - Composição do Empenho**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
 **Solução**O registro na tabela **SDC** ocorre quando o produto em questão possui controle de endereçamento e o parâmetro da opção **F12** da rotina **MATA650 - Ordem de Produção**, **Sugere Lote/End a Empenhar?** está marcado como **Sim** e possui saldo disponível nos endereços.   
Outro momento no qual ocorre o registro na tabela **SDC** é no apontamento da **OP - Ordem de Produção**, quando não foi indicado o endereço do produto para reserva, neste caso, o Sistema realiza um registro e exclui o mesmo.
