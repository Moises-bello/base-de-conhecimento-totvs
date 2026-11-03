---
content_hash: 29e72a8690a822d7d3d0589477b1ad10763c626f0e4362b8a6d39b611500a87d
fetched_at: '2026-07-02T19:24:22.497352+00:00'
page_id: '270101688'
product: protheus
source: tdn-tec
title: Seção [RPC], chave onCall
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270101688
version: 9
---

Chave onCall

Define o nome da função em true a ser executada pelo servidor de RPC a cada tarefa (chamada de método) solicitada por um determinado cliente RPC.

## Valores válidos

Veja a seguir os valores válidos para a chave

| Valor | Descrição |
| --- | --- |
|  | Valor default da chave. Nenhuma função será executada nas chamadas realizadas por um cliente RPC. |
| <cFunctionName> | Informa o nome da função de validação que será executada pelo servidor RPC a cada solicitação. |

## Exemplo

No exemplo a seguir, a validação do client RPC é realizada através da função customizada "u\_validFun".

## Mais informações
