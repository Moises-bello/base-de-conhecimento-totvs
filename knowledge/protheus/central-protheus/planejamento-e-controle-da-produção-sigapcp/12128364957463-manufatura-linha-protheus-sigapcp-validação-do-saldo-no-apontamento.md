---
article_id: 12128364957463
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 73ed012dd1907a5977b6c1dc4044cf941b7cd256689be79125592ef180e91cb9
fetched_at: '2026-06-28T22:42:47.116974+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Validação do saldo no apontamento
type: support-article
updated_at: '2023-02-03T13:48:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12128364957463-Manufatura-Linha-Protheus-SIGAPCP-Valida%C3%A7%C3%A3o-do-saldo-no-apontamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:18 min** **Dúvida**Se mais de uma **OP - Ordem de produção** for aberta, e a quantidade em estoque do material empenhado para essas **OPs** não atender todas as produções, no momento do apontamento, o Sistema consegue impedir o apontamento daquelas que foram abertas quando, apesar de ainda existir material em estoque, toda a sua totalidade já encontra-se empenhada para as **OPs** abertas anteriormente?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**É possível ter esse controle, desde que o o produto seja controlado por **lote e/ou endereço** e o **lote e/ou endereço** tenha sido reservado no momento do empenho, caso contrário no momento do apontamento o Sistema verifica a quantidade em estoque do material empenhado e a quantidade necessária desse material para a produção que se deseja apontar, se existir estoque disponível, permite o apontamento, mesmo que essa OP seja a última aberta.  
  
**Exemplo**  
Se existir em estoque 1 unidade de uma determinada matéria prima, e existirem duas **OPs**, cada uma consumindo uma unidade desse produto, no momento do apontamento é possível apontar a primeira ou a segunda **OP**.
