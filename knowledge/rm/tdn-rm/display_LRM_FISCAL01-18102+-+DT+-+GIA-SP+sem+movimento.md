---
content_hash: f4f538c6465bbb64e2f36989cb1c28f98407cc5022e33cc49d827127a2b52269
fetched_at: '2026-06-29T00:11:21.103999+00:00'
page_id: '687762694'
product: rm
source: tdn-rm
title: FISCAL01-18102 - DT - GIA-SP sem movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-18102+-+DT+-+GIA-SP+sem+movimento
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotinas Estaduais |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18056 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a Rotina GIA – ST para o estado de São Paulo, não foi gerado o arquivo para a opção “GIA Sem Movimento”

## **03. SOLUÇÃO**

Correção no Layout da GIA-ST para considerar apenas o período de apuração de ST quando gerar sem movimento.  
Há dois registros para o A0, quando gera com movimento e quando gera sem. Apenas o que gera sem foi alterado, e os valores que dependiam de lançamentos fiscais foram zerados, já que não faz sentido preenchê-los se não é para considerar lançamentos com essa opção marcada.

Disponível a partir da versão 12.1.33
