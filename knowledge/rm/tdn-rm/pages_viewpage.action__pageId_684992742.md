---
content_hash: feeb397c00f91774f4073f0cf4dc078fd02813d244ce86e097095c7cf61141d9
fetched_at: '2026-06-29T00:11:18.299928+00:00'
page_id: '684992742'
product: rm
source: tdn-rm
title: FISCAL01-17962 - DT - Desativação do envio de métricas no método de seleção
  de natureza
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=684992742
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Regras de Seleção de Natureza |
| País: | Brasil |
| Ticket: | [#13626187](https://totvssuporte.zendesk.com/agent/tickets/13626187 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17962 |

## **02. SITUAÇÃO/REQUISITO**

Em situações com mais de um usuário utilizando a funcionalidade de seleção de Natureza de Operação um número alto de envio de métricas adicionais pode ser observado no log do License Server e ocasionando na indisponibilidade do serviço.

## **03. SOLUÇÃO**

Correção aplicada na rotina para garantir que os envios de métricas no método não sejam feitas, evitando a sobrecarga do License Server.

Disponível a partir da versão 12.1.33
