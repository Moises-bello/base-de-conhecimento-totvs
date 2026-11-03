---
content_hash: 57767e9fee26b5f09e05c1e79ac49cd8f38630fa7ec1b8c9cf72ee489ecef639
fetched_at: '2026-06-29T00:11:22.132414+00:00'
page_id: '699797014'
product: rm
source: tdn-rm
title: DT FISCAL01-18317 - Sped fiscal notas fiscais canceladas estão sendo consideradas
  como ativas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=699797014
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Sped Fiscal |
| País: | Brasil |
| Ticket: | [Ticket #14569605](https://totvssuporte.zendesk.com/agent/tickets/14569605 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18317 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a rotina Sped Fiscal os registros D695/D696 estão sendo gerados considerando as notas canceladas como ativas (com valores).  
O cliente solicita que no arquivo Sped Fiscal sejam consideradas as notas canceladas (registro D695 campos 4 Número de ordem inicial e 5 Número de ordem final) e por estarem canceladas não sejam levados os valores das mesmas (registro D696 campo 5 Valor da operação),como já ocorre com o Convênio 115/2003.

## **03. SOLUÇÃO.**

Ajuste no Sped Fiscal para não considerar Lançamentos Cancelados no Registro D696.

Disponível a partir da versão 12.1.34.
