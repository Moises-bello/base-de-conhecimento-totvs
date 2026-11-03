---
content_hash: 9c88da2557261f22f0783db59206ec21a6675279685adc853796299a206cad73
fetched_at: '2026-07-02T19:24:23.997350+00:00'
page_id: '454834455'
product: protheus
source: tdn-tec
title: tRedisClient:New
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3ANew
version: 14
---

Cria um objeto que permitirá a conexão com um servidor Redis.

Em outras palavras, depois de `::New()` **NÃO** está disponível uma conexão com um servidor Redis. Para isso é necessário chamar o método `::Connect()` do objeto.

## Sintaxe

## Parâmetros

Nenhum

## Retorno

| Nome | Tipo | Descrição | Observações |
| --- | --- | --- | --- |
| ``` oRedisCli ``` | objeto | objeto para conexão com o servidor Redis | Sempre retorna objeto, a não ser em caso de falta total de memória. |

## Observações

## Exemplos

### Exemplo

cpptrue> " + cValToChar(oRedisClient:lConnected))
oRedisClient:Disconnect()
Return .T.]]>

## Veja também
