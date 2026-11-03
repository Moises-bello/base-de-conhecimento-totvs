---
content_hash: dff23b4c2acdbc0ef1011ea17a2bd985253b92c2e05c3f0d09f15a0c7a6676fa
fetched_at: '2026-06-29T00:11:26.106002+00:00'
page_id: '715817169'
product: rm
source: tdn-rm
title: FISCAL01-18715 - DT Campo VL_TOT_DEBITOS - E110
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-18715+-+DT+Campo+VL_TOT_DEBITOS+-+E110
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18715 |

## **02. SITUAÇÃO/REQUISITO**

Correção do campo 2 do Registro E110, onde não está sendo considerado débitos de ICMS originados do registro D696.

## **03. SOLUÇÃO**

Alterado o registro SPED.D696 para que, caso exista valor de ICMS, o campo 02 do registro E110 seja alimentado com o valor total do ICMS dos registros D696.

Disponível a partir da biblioteca 12.1.34
