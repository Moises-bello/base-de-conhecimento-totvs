---
content_hash: 56c8eb9861aee4ff4094df5482d624753c7f88d602186d281318b1fc1950f5fe
fetched_at: '2026-06-29T00:11:44.720124+00:00'
page_id: '815567681'
product: rm
source: tdn-rm
title: FISCAL01-21566 - DT - Rateio de centro de custo nas guias
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-21566+-+DT+-+Rateio+de+centro+de+custo+nas+guias
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Geração de Guias |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-21566 |

## **02. SITUAÇÃO/REQUISITO**

Na geração da guia de ISS,  ao gerar o "Lançamento financeiro da guia", o sistema retorna com inconsistências referentes ao rateio, (segue abaixo), porém os valores de rateio estão corretos, mas não aparecem na visão da guia, sendo demonstrando apenas o valor 0,00; quando o valor correto é 0,0003.

Inconsistência: *Favor ajustar o rateio do Centro de Custo 4.00002.004, Natureza Orçamentária 1.09.0001, referente ao lançamento Ref. 0, pois possui valor igual a zero.*

## **03. SOLUÇÃO**

Realizado ajuste no preenchimento do rateio de centro de custo das guias para que seja considerado apenas valores maiores que zero, considerando duas casas decimais.

Disponível a partir da biblioteca 12.1.2302
