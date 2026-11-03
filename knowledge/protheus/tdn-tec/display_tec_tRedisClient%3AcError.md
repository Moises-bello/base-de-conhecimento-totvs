---
content_hash: 408733b7c4bab67318659ff56dc7f73906549a57c94aa9f4bc499e1989b14641
fetched_at: '2026-07-02T19:24:24.010660+00:00'
page_id: '454834599'
product: protheus
source: tdn-tec
title: tRedisClient:cError
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3AcError
version: 8
---

Contém mensagem descrevendo o erro da operação mais recente. Caso não tenha havido erro, contém a string vazia, ou `""`.

| Tipo | Valor Padrão | Somente Leitura |
| --- | --- | --- |
| caracter | N/A | Sim |

## Sintaxe

cpp

## Observações

A propriedade `::cError` espelha sempre o estado da propriedade `::nError`. A primeira contém um texto descrevendo o possível erro da operação mais recente; a segunda contém um inteiro exatamente com o mesmo significado. A propriedade `::lOk` também é associada a situações de erro: será falsa (ou `.F.`) quando houver um erro.  
  
Todos os métodos podem alterar o valor de `::cError`, exceto os métodos que apenas consultam propriedades como `::Ok()` e `::IsConnected()`.

## Veja também

* tRedisClient:New



* tRedisClient:GetReply
