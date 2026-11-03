---
article_id: 10464180487831
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: f16559ecc0ec2282ba7a7969faa614499c31657e3f53e1bf640091bdca90587b
fetched_at: '2026-06-28T22:42:43.258091+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Finalidade do parâmetro MV_ENCEOP
type: support-article
updated_at: '2022-11-24T17:07:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10464180487831-Manufatura-Linha-Protheus-SIGAPCP-Finalidade-do-par%C3%A2metro-MV-ENCEOP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:05 min  
  
Dúvida**Qual a finalidade do parâmetro **MV\_ENCEOP -** **Indica se encerra apenas OP Pai ou encerra a OP pai e as intermediárias**? **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O parâmetro **MV\_ENCEOP** é valido apenas para as rotinas **MATA680 - Apontamento Produção Mod1** e **MATA681 - Apontamento Produção Mod2** e tem a finalidade de encerar a **OP Intermediária** com o encerramento da **OP pai.**Com o parâmetro **MV\_ENCEOP** ativo o Sistema encerrará a **OP Intermediária** quando:- A **OP pai** possui um movimento de produção e o encerramento dessa **OP** ocorre através da opção **encerrar**, selecionando o movimento de produção e clicando em **outras ações-> encerrar**.  
  
- Para que a **OP Intermediária** encerre ao encerrar a **OP pai**, essa **OP** precisa ter registro na **tabela SD3 - Movimentações Internas** com **PR0 - Produção Manual** também. Só vai encerrar a **OP Intermediária** se ela também já deu entrada em estoque.  
  
Lembrando que com o parâmetro **MV\_ENCEOP** ativo a **OP Intermediária** será encerrada e não apontada automaticamente.
