---
article_id: 4403023006615
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: be70697a64efaa996ad1d7bb435e1c6c13df8f8afcc74f47fa785df7ce39f824
fetched_at: '2026-06-28T22:42:43.606759+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A650DATPRF
type: support-article
updated_at: '2021-06-22T11:31:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403023006615-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A650DATPRF
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min**  
**Ocorrência**Ao incluir uma **OP - Ordem de Produção** através do **MATA650 - Ordens de Produção** e preencher o campo **C2\_DATPRF - Data prevista de entrega** o Sistema apresenta a mensagem **A650DATPRF - Não é permitido o cadastramento de uma ordem de produção com data de entrega anterior a data base.**  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**A data informada no campo **C2\_DATPRF** é menor do que a **database** com a qual o usuário está logado no Protheus.  
  
**Solução**Para solucionar essa ocorrência, verifique a **database**com a qual está logado no Sistema, o conteúdo do campo **C2\_DATPRF** deve ser maior ou igual a este valor.
