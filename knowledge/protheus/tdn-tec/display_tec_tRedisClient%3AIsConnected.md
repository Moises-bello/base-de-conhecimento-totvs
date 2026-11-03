---
content_hash: 659bd429c215a15eb236f519bbe742f4d683f2f28ea80d70c30dd59f3915141a
fetched_at: '2026-07-02T19:24:24.141525+00:00'
page_id: '458759502'
product: protheus
source: tdn-tec
title: tRedisClient:IsConnected
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3AIsConnected
version: 17
---

## **DEPRECADO**

O método `::IsConnected()` não deve ser usado, pois foi substituído pela propriedade `::lConnected`.

---

O método `::IsConnected()` retorna Verdadeiro (`.T.`) se o cliente está conectado a um servidor Redis, ou `.F.` caso contrário.

## Sintaxe

`lResult := oRedisClient::IsConnected()`

## Parâmetros

O método `::IsConnect()` não usa nenhum parâmetro.

## Retorno

| Nome | Tipo | Descrição | Observações |
| --- | --- | --- | --- |
| `lResult` | `lógico` | Verdadeiro (`.T.`) caso o objeto `tRedisClient` esteja conectado a um servidor Redis; `.F.` em caso contrário. |  |

## Observações

* O método `::IsConnected()` não deve ser usado, pois foi substituído pela propriedade `::lConnected`.
* O método `::IsConnected()` será eliminado em futuras versões da classe `tRedisConnect`.

## Exemplos

### Exemplo 1 – Uso do método `::IsConnected()` para testar se uma conexão foi efetuadatrue

cpptrue

## Veja também
