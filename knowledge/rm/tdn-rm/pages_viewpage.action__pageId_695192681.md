---
content_hash: 686d50e1879a73bf0127f5b67fb7f30ec7a06e9309abf1609f65ab4c71be6e0e
fetched_at: '2026-06-29T00:11:21.396776+00:00'
page_id: '695192681'
product: rm
source: tdn-rm
title: FISCAL01-1945 - DT Considerar Lançamentos com a opção Consumidor Final marcada
  no Cálculo do FECP RJ
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=695192681
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cálculo do FECP RJ |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-1945 |

## **02. SITUAÇÃO/REQUISITO**

Ao calcular o FECP RJ o sistema não está considerando Lançamentos para não contribuinte de ICMS com o flag Consumidor Final marcado.

## **03. SOLUÇÃO**

Alterada a consulta usada no cálculo para não filtrar lançamentos que tenham a flag marcada.

Disponível a partir da biblioteca 12.1.33
