---
content_hash: eb3c548d7ad2b106ac0f77c06b0074b59eac62ade774bd82319e79318deefb12
fetched_at: '2026-07-02T19:24:18.623328+00:00'
page_id: '219121358'
product: protheus
source: tdn-tec
title: Construtor TSocketClient:New
type: documentation
url: https://tdn.totvs.com/display/tec/Construtor+TSocketClient%3ANew
version: 2
---

Construtor TSocketClient:New

# Construtor TSocketClient:New

Cria o objeto TSocketClient sem conexão ativa.

## Sintaxe

false

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório | Referência |
| --- | --- | --- | --- | --- |
| lClient | lógico | Indica se o client de socket será criado do lado do Client (.T.) ou do lado do AppServer (.F.). O padrão é (.F.) AppServer. |  |  |

## Retorno

| Nome | Tipo | Descrição |
| --- | --- | --- |
| oObj | objeto | Nova instância da classe TSocketClient |

trueObservações

* O client de socket do lado do **Client** (SmartClient Desktop e Webapp com WebAgent) está disponível somente em builds **superiores a 20.3.1.x**. Portanto em versões não suportadas, o parâmetro **lClient** existe somente por compatibilidade (passar Nil nesse caso).
