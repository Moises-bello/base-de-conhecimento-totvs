---
content_hash: 7684fa637f26194921cac4da166c639eb2bad5b3425ba3abe0bc9131c8e5baec
fetched_at: '2026-07-02T19:24:24.017222+00:00'
page_id: '454834693'
product: protheus
source: tdn-tec
title: tRedisClient:nReplyType
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3AnReplyType
version: 18
---

Contém codificação do tipo de resposta do servidor.

| ``` ::nReplyType ``` | Significado |
| --- | --- |
| -1 | Nenhuma resposta |
| 0 | resposta nula |
| 1 | *string* |
| 2 | vetor, ou *array* |
| 3 | inteiro |
| 4 | ``` Nil ``` |
| 5 | status |
| 6 | erro |

| Tipo | Valor Padrão | Somente Leitura |
| --- | --- | --- |
| inteiro | N/A | S |

## Sintaxe

cpp

## Observações

* A principal utilidade de `::nReplyType`é permitir ao programa cliente que está em contato com o servidor Redis que se adeque à resposta do servidor. Por exemplo, se a resposta de uma operação colocou o valor 2, o programa pode tratar o valor retornado como um vetor.
* O valor de `::nReplyType` pode ser alterado principalmente por chamadas aos métodos `::Exec()` e `::GetReply()`, pois neste momento é que o cliente deverá processar as respostas. Em outros contextos, o valor de  `::nReplyType` pode ser -1, indicando que não está disponível nenhuma resposta do servidor.
* Caso o valor de `::nReplyType` seja 6 (indicando erro), as propriedades `::cError` e `::nError` poderão ser consultadas para detalhar o erro encontrado. E, naturalmente, espera-se que neste caso `::lOk` seja falso, ou `.F.`
* Caso `::nReplyType` seja `-1`, o servidor está avisando que não há nenhuma resposta para esse comando. Isto acontece para os métodos `::SetRecvTimeout()` e `::Append()`.
* Caso `::nReplyType` seja `0`, o servidor está avisando que a resposta contém `Nil`.

## Veja também

* tRedisClient:SetRecvTimeout
