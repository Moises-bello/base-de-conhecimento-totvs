---
article_id: 360055297514
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: cc8a8cde926ff91516e41e024ac8f233ed7e9d93eec1d9f44f5689078089622d
fetched_at: '2026-06-28T22:42:44.491556+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem MA240NEGLT no apontamento
  de produção a maior
type: support-article
updated_at: '2026-02-19T18:48:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055297514-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-MA240NEGLT-no-apontamento-de-produ%C3%A7%C3%A3o-a-maior
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38507472762903)*** Tempo aproximado para leitura: **00:00:45 min**  
  
**Ocorrência**  
Ao realizar um apontamento de produção e identificar o excedente como produção a maior é apresentada a mensagem **MA240NEGLT**.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**  
A mensagem **MA240NEGLT** ocorre quando o Sistema não encontra saldo em todos os lotes empenhados.  
  
**Solução**  
Quando o excedente é identificado como produção a maior, o Sistema calcula a proporção de todos os lotes empenhados, sendo necessária a existência de saldo em todos. Para o caso de não existir mais saldo disponível de um lote, mas existir saldo disponível de outro, sugerimos que faça as requisições para esta **OP - Ordem de Produção** de forma manual por meio da rotina de estoque **MATA241 - Movimentação Múltipla** e faça o apontamento de produção considerando como ganho de produção.
