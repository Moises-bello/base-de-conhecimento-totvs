---
content_hash: 65fcbf4d6f6568c30dae997993001912935974df9daccc3badb056852d1888e8
fetched_at: '2026-06-29T00:11:43.436749+00:00'
page_id: '806773755'
product: rm
source: tdn-rm
title: FISCAL01-21327 - DT - GTINs iguais
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-21327+-+DT+-+GTINs+iguais
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD ICMS IPI - SPED Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-21270 |

## **02. SITUAÇÃO/REQUISITO**

GTINs eram gerados iguais para o fator de conversão (registro 0220, campo 04: COD\_BARRA). 

## **03. SOLUÇÃO**

Correção no cache do produto para atualizar o código de barras conforme a unidade informada no item do lançamento.  
Além disso, passa a ser necessário informar o tipo do código de barras no cadastro do produto como "GTIN" para que ele seja gerado no arquivo.

Disponível a partir da biblioteca 12.1.2302
