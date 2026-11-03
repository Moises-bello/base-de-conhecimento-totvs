---
article_id: 360028849611
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: b1ca982aaf1410b5dba970e1758d33547f851521826dde593a0b50d5c1a1daef
fetched_at: '2026-06-28T22:42:47.274104+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Mensagem Não foi possível alocar a operação xx dentro do período
  definido para a Carga Máquina
type: support-article
updated_at: '2019-12-27T11:33:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028849611-MP-SIGAPCP-Mensagem-N%C3%A3o-foi-poss%C3%ADvel-alocar-a-opera%C3%A7%C3%A3o-xx-dentro-do-per%C3%ADodo-definido-para-a-Carga-M%C3%A1quina
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Na rotina **MATA690 - Carga Máquina** ao tentar alocar as operações é apresentada a mensagem **Não foi possível alocar a operação xx dentro do período definido para a Carga Máquina**.  
   
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
   
 **Causa**Essa mensagem é apresentanda quando o **MATA690** não consegue alocar todas as operações.  
   
**Solução**Para solucionar essa ocorrência, realize as seguintes verificações:  
 1. Avalie se a alocação está **Pelo Fim**, pois tem por objetivo respeitar a data de entrega. Com isso o Sistema faz a alocação do recurso de traz para frente, ou seja, da última operação necessária para fabricar o produto, fixando esta na data de entrega negociada, até a primeira, obtendo assim a informação de quando a produção deve ser iniciada;  
2. Se a alocação está **Pelo Inicio** avalie se no filtro **Período (dias)?** informado, o Sistema consegue alocar a operação completa das **OPs - Ordens de Produção** que estão sendo processadas;  
3. Se for o caso realize o ajuste do período de alocação que não está suficiente.
