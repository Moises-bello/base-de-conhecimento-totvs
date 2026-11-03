---
content_hash: f126d94713a453f23ad61b2c9db444d51cfe8229f1099e31d46b26ab6c811226
fetched_at: '2026-07-02T19:24:24.070202+00:00'
page_id: '454835809'
product: protheus
source: tdn-tec
title: tRedisClient:lOk
type: documentation
url: https://tdn.totvs.com/display/tec/tRedisClient%3AlOk
version: 20
---

Contém Verdadeiro (`.T.`) caso a operação mais recente tenha sido bem sucedida, ou `.F.` em caso contrário.

| Tipo | Valor Padrão | Somente Leitura |
| --- | --- | --- |
| lógico | N/A | Sim |

## Sintaxe

## Observações

A propriedade `::lOk` pode ser entendida como resumindo todas as situações de erro da operação mais recente: ao passo que as propriedades associadas `::cError` e `::nError` dão informações sobre **qual** foi o erro, `::lOk` apenas informa **se** houve erro na operação mais recente.  
  
Todos os métodos podem alterar o valor de `::lOk`, exceto os métodos que apenas consultam propriedades como `::Ok()` e `::IsConnected()`.

## Veja também
