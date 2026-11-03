---
content_hash: da4e83c445faa85da41cc57c827efeb6cd14b1659c62802f2b273282e7ca6504
fetched_at: '2026-06-29T00:12:14.073970+00:00'
page_id: '964585797'
product: rm
source: tdn-rm
title: FISCAL01-17507 - REINF - Evento R-2050 - Indicativo de comercialização = 9
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=964585797
version: 2
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | REINF - R2050 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-170507 |

## **02. SITUAÇÃO/REQUISITO**

Cliente solicita que o campo <indCom> do evento R-2050 seja gerado com o valor 9 para venda de exportação indireta com CFOP **5501, 5502, 6501 e 6502**.

## **03. SOLUÇÃO**

Ajuste no código para retornar o valor 9 (Indicativo de comercialização) na tag indCom para operações de Exportação Indireta (CFOP **5501, 5502, 6501 e 6502**).

Disponível à partir da biblioteca 12.1.2410
