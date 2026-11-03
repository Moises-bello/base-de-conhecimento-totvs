---
article_id: 16777567415319
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: f2308bd93f895c35eb785a58a369d419a64719a72c66154ab9d18c14c8d53dc3
fetched_at: '2026-06-28T22:42:45.882194+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Requisições de empenhos com lote na
  produção a maior
type: support-article
updated_at: '2023-08-15T21:23:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16777567415319-Manufatura-Linha-Protheus-SIGAPCP-Requisi%C3%A7%C3%B5es-de-empenhos-com-lote-na-produ%C3%A7%C3%A3o-a-maior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16777572070935) Tempo aproximado para leitura: **00:02:06 min** **Dúvida**Quando ocorre **produção a maior**, como ocorre a requisição do material empenhado com lote?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Quando o material está empenhado com lote é necessário que exista mais saldo do lote empenhado para que desse lote ocorra a requisição na proporção da **produção a maior**. Se mais de um lote estiver empenhado, de todos os lotes serão realizadas as requisições proporcionalmente.  
Não será feita a requisição de outro lote que não esteja empenhado.  
  
**Exemplo**Para uma **OP - Ordem de produção** de 10, que tem de um determinado produto a quantidade 10 empenhado com lote, ao apontar 15 dessa **OP**, será necessário que tenha 15 do lote.  
Se ao invés de um lote, tiver dois empenhos, cada um de 5, será necessário que de cada lote tenha 7,5 em estoque para que ocorra a requisição.
