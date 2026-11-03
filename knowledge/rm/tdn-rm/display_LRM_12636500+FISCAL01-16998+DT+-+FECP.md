---
content_hash: 7526a76d9ba7ffa9d22fbf17a23a52d039ae4758813908e466d5d3bd908d1fdf
fetched_at: '2026-06-29T00:11:12.462668+00:00'
page_id: '653420481'
product: rm
source: tdn-rm
title: 12636500 FISCAL01-16998 DT - FECP
type: documentation
url: https://tdn.totvs.com/display/LRM/12636500+FISCAL01-16998+DT+-+FECP
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | REINF |
| Ticket: | 12636500 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16998 |

## **02. SITUAÇÃO/REQUISITO**

Ao escriturar uma nota de saída o campo valor ICMS FECP e valor ST localizado no:  
Lançamento fiscal | situação tributária | Substituição tributária, está calculando valores incorretos.

## **03. SOLUÇÃO**

Realizada alteração para que ao calcular o ICMS por dentro ele siga o seguinte comportamento:

1 - (AliqStMajorada) / 100)

Antes da alteração era feito da seguinte forma:

1 - (AliqStMajorada + AliqFECP) / 100)

A partir desta implementação não é mais somado a alíquota do FECP, pois a alíquota. do ST já vem majorada no NUCLEUS

Disponível a partir da 12.1.31
