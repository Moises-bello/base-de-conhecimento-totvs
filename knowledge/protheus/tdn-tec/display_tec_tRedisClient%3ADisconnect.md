---
content_hash: 1cd42570ab17b4de41085e163f8418d3c2c53f878e5b13e5e94325821a719515
fetched_at: '2026-07-02T19:24:24.042091+00:00'
page_id: '454835069'
product: protheus
source: tdn-tec
title: tRedisClient:Disconnect
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3ADisconnect
version: 17
---

Desconecta o cliente do servidor Redis

## Sintaxe

## Parâmetros

Nenhum parâmetro.

## Retorno

| Nome | Tipo | Descrição | Observações |
| --- | --- | --- | --- |
| ``` oRedisAfter ``` | objeto `tRedisClient` | Cópia do objeto sobre o qual foi feita a chamada de `::Connect`, já afetado pela tentativa de conexão.\* |  |

`*`Isto permite acoplar outros métodos e propriedades à chamada de `::Disconnect()`  
   Por exemplo,   
`oRedisClient:Disconnect():lConnected`

   testará se a conexão foi bem sucedida, sem a necessidade de uma consulta à parte a `::lConnected` sobre o objeto `oRedisClient`.

## Observações

* O método `::Disconnect()` permite que um cliente interrompa sua conexão com um servidor Redis. Isto permite que sejam liberados recursos alocados para conexão tanto no servidor quanto no cliente.  
    
  Deste modo, o servidor Redis pode atender a outros clientes.  
    
  Naturalmente, uma desconexão só faz sentido caso o cliente tenha de fato conseguido se conectar.

## Exemplos

### Exemplo 1 – Chamada simples a ::Disconnect()

true

### Exemplo 2 – Consulta a `::lConnected` associada a uma chamada de `::Disconnect`

cpptrue

## Veja também
