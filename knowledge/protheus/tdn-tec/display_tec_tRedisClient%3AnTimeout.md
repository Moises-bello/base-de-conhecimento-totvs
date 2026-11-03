---
content_hash: 92d4be198366541d900623fe56d1bc29ab0432ba2f18081464ab572f96112279
fetched_at: '2026-07-02T19:24:24.152458+00:00'
page_id: '458774374'
product: protheus
source: tdn-tec
title: tRedisClient:nTimeout
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3AnTimeout
version: 8
---

Contém o tempo máximo de espera (*timeout*) em segundos pela resposta de um comando no servidor Redis.

| Tipo | Valor Padrão | Somente Leitura |
| --- | --- | --- |
| numérico | 5 | Sim |

## Sintaxe

## Observações

* A propriedade `::nTimeout()` é alterada pelo método `::SetRecvTimeout()`, que recebe como parâmetro seu novo valor em segundos.  
    
  Ver na página de [tRedisClient:SetRecvTimeout](http://tdn.totvs.com.br/display/tec/tRedisClient%3ASetRecvTimeout) uma discussão mais detalhada sobre a operação e implicações do ajuste do valor de *timeout*.
* É considerado um erro, caso o servidor Redis demore mais tempo para responder do que aquele especificado em `::nTimeout`.  
    
  Neste caso, o valor da propriedade `::lOk` será tornado `.F.`, indicando que falhou o comando mais recente.

## Veja também
