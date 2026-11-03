---
content_hash: be292051a2d43168a571f0b29f19e6f96f63373b03aebcac5fa807cb5d162b70
fetched_at: '2026-06-29T00:11:12.582523+00:00'
page_id: '655438238'
product: rm
source: tdn-rm
title: 12636500 FISCAL01-16998 DT - Valor do ICMSST está divergente na escrituração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=655438238
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Escrituração |
| País: | Brasil |
| Ticket | 12636500 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16998 |

## **02. SITUAÇÃO/REQUISITO**

Ao escriturar com a flag marcada "ICMSST por dentro", o valor do ICMSST está desconsiderando o valor do FECP.

Já ao escriturar com a flag desmarcada "ICMSST por dentro", o valor do ICMSST está considerando o valor do FECP.

## **03. SOLUÇÃO.**

Foi removido trecho de código: **Item.VlrICMSSTPrd -= Item.VlrICMSItemFCPEstDest + RMSConvert.ToDecimal(Item.VlrFCPProprio.Value, 0)**do método CalcularValorFECPItem,

pois o campo Valor do ICMSST no lançamento deve conter o valor do ST + o FECPST, independente da flag ICMSST por dentro estiver marcada.
