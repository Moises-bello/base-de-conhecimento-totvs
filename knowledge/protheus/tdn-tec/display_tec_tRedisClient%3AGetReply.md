---
content_hash: bc37fff5c3781964e717cfc04fbc5ffab89d6d8d3d88eb5fba54f704faaca773
fetched_at: '2026-07-02T19:24:24.048635+00:00'
page_id: '454835453'
product: protheus
source: tdn-tec
title: tRedisClient:GetReply
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3AGetReply
version: 26
---

Obtém uma resposta do servidor, eventualmente listando erros e informações de status no console do servidor Protheus.

## Sintaxe

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência | Observações |
| --- | --- | --- | --- | --- | --- |
| `outParm` | Variados | Resposta de um comando Redis anteriormente executado | X | X |  |

## Retorno

| Nome | Tipo | Descrição | Observações |
| --- | --- | --- | --- |
| ``` oRedisAfter ``` | objeto `tRedisClient` | Cópia do objeto sobre o qual foi feita a chamada a `::GetReply()`, alterado por ela.\* |  |

\* Isto permite acoplar outros métodos e propriedades à chamada de `::GetReply()`  
   Por exemplo,   
      `oRedisClient:GetReply(@outParm):lOk`

   testará se o comando foi bem sucedido, sem a necessidade de uma consulta à parte a `::lOk` sobre o objeto `oRedisClient`.

## Observações

* O método `::GetReply()` é associado ao método `::Append()`, que enfileira a execução de comandos no servidor Redis, ao passo que `::GetReply()` obtém o resultado dessa execução.

* É a parceria entre `::Append()` e `::GetReply()` que permite a execução assíncrona de comandos, em concorrência com a execução do programa: podem-se enfileirar vários comandos através de `::Append()` e posteriormente obter seus resultados através de `::GetReply()`. Pode também haver um ganho de desempenho, pois o programa cliente não precisa aguardar a execução no comando no servidor, podendo ocupar esse tempo em outras atividades, para apenas consultar o resultado quando necessário.

* Um ponto importante é que `::GetReply()` retornará valores de tipos variados, de acordo com a resposta do comando que foi enviado por `::Append()`.
* Para que o programa possa se preparar adequadamente para as respostas recebidas por `::GetReply()` – que podem ter sido geradas em ordem indefinida *a priori* --, é útil conhecer seu tipo. O que pode ser feito consultando-se a propriedade `::nReplyType` do objeto `tRedisClient`.

## Exemplos

### Exemplo 1 – Execução do comando `set` do Redis true

cpptrue

## Veja também
