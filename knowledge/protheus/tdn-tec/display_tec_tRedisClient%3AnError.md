---
content_hash: 5b19f63bb30bbf7b5c3b8bd19e6c34408a51192b1bb2197e6b7fab94ac12696c
fetched_at: '2026-07-02T19:24:24.005531+00:00'
page_id: '454834577'
product: protheus
source: tdn-tec
title: tRedisClient:nError
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3AnError
version: 9
---

Contém o erro da última operação, codificado como um número inteiro.  É zero se não houve erro.

| Tipo | Valor Padrão | Somente Leitura |
| --- | --- | --- |
| inteiro | N/A | S |

## Sintaxe

cpp

## Observações

A propriedade `::nError` espelha sempre o estado da propriedade `::cError`. A primeira contém um inteiro descrevendo o possível erro da operação mais recente; a segunda contém um texto exatamente com o mesmo significado. A propriedade `::lOk` também é associada a situações de erro: será falsa (ou `.F.`) quando houver um erro.

Todos os métodos podem alterar o valor de `::nError`, exceto os métodos que apenas consultam propriedades como `::Ok()` e `::IsConnected()`.

## Veja também

* tRedisClient:New



* tRedisClient:GetReply
