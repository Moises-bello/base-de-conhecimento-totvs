---
content_hash: 48e3fa4213fab9b7019aebcec18017f3ed5370b1027cc7412178a7614c67da77
fetched_at: '2026-07-02T19:24:19.540597+00:00'
page_id: '223172338'
product: protheus
source: tdn-tec
title: TMSGraphic:DelSerie
type: documentation
url: https://tdn.totvs.com/display/tec/TMSGraphic%3ADelSerie
version: 3
---

DelSerie

Exclui uma série do gráfico.

## Sintaxe

 ] )]]>

## Parâmetros

| Nome | Tipo | Descrição | Obrigatório |
| --- | --- | --- | --- |
| nSerie | Numérico | Indica a série que será excluída. | x |

## Retorno

| Retorno | Tipo | Descrição |
| --- | --- | --- |
| lRet | Lógico | Retorna se a série foi excluída com sucesso.  (.T.) - Se a série foi excluída com sucesso. (.F.) - Se a série não foi excluída. |

## Observação

A TMSGraphic não permite a deleção e re-inserção de séries. Para isso é necessário re-criar o objeto.  
No exemplo abaixo consta a forma correta para esta operação.

## Exemplo

1
