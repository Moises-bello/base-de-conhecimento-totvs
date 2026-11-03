---
content_hash: 34ad264d181dad12ec2bd7bf559d8521543e05b36d1fc8ba089983a3ec1cbfbf
fetched_at: '2026-07-02T19:24:24.148579+00:00'
page_id: '458760013'
product: protheus
source: tdn-tec
title: tRedisClient:Ok
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3AOk
version: 14
---

## **DEPRECADO**

O método `::Ok()` não deve ser usado, pois foi substituído pela propriedade `::lOk.`

---

O método `::Ok()` retorna Verdadeiro (`.T.`) caso a operação mais recente tenha sido bem sucedida, ou `.F.` em caso contrário.

## Sintaxe

`lResult := oRedisClient::Ok()`

## Parâmetros

O método `::Ok()` não usa nenhum parâmetro.

## Retorno

| Nome | Tipo | Descrição | Observações |
| --- | --- | --- | --- |
| `lResult` | `lógico` | Verdadeiro (`.T.`) a última operação do objeto `tRedisClient` tenha sido verdadeira; `.F.` em caso contrário. |  |

## Observações

* O método `::Ok()` não deve ser usado, pois foi substituído pela propriedade `::lOk`.
* O método `::Ok()` será eliminado em futuras versões da classe `tRedisConnect`.

## Exemplos

### Exemplo 1 – Impressão do resultado de `::Ok()` depois de tentativa de conexão true

cpptrue

Este programa mostra o uso do método `::Ok()` para avaliar a correção de diversas chamadas a métodos de um objeto `tRedisClient`.

## Veja também
