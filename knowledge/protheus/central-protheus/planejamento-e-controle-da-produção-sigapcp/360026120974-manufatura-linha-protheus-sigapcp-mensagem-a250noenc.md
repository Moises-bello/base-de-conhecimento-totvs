---
article_id: 360026120974
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 89adebb82117320877e12ac583b96a7acd3d67d0534d95df0093e3c4d9f712da
fetched_at: '2026-06-28T22:42:43.585228+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem A250NOENC
type: support-article
updated_at: '2025-09-01T19:24:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026120974-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-A250NOENC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34613885115031)**Tempo aproximado para leitura: **00:01:21 min****Ocorrência**No módulo do **Planejamento e Controle da Produção** ao tentar encerrar uma **OP - Ordem de Produção** é apresentada a mensagem **A250NOENC - A ordem de produção não pode ser encerrada pois possui saldo de requisição em processo**.  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
 **Causa**Essa situação ocorre quando o registro selecionado não é o último registro de apontamento da **OP** ou quando após esse último apontamento aconteceram requisições para a **OP**.   
  
 **Solução**Avalie se foi selecionado o último apontamento, pois somente por meio dele é possível encerrar a **OP** e verifique se após esse último apontamento não foram realizados **movimentos de requisição**, deixando assim a **OP** pendente de novo apontamento.

Se ocorreu alguma movimentação para essa **OP** com data posterior ao último apontamento, essa movimentação deve ser reavaliada e caso proceda, deve ser realizado um novo apontamento com data igual ou posterior ou essa movimentação deve ser estornada e realizada novamente com data anterior ao último apontamento.
