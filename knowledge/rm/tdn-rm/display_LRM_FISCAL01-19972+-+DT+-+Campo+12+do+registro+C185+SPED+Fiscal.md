---
content_hash: 061f34dc82e7e92a8bfb8a5a9f9a897b6d374c4965a0bc81edb83fe42dceea9a
fetched_at: '2026-06-29T00:11:35.881662+00:00'
page_id: '766954315'
product: rm
source: tdn-rm
title: FISCAL01-19972 - DT - Campo 12 do registro C185 SPED Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-19972+-+DT+-+Campo+12+do+registro+C185+SPED+Fiscal
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD ICMS IPI | SPED Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-19972 |

## **02. SITUAÇÃO/REQUISITO**

O campo 12 (VL\_UNIT\_ICMS\_OP\_ESTOQUE\_CONV) do registro C185 – SPED Fiscal não é gerado com o valor do Campo 2 do registro H030.

## **03. SOLUÇÃO**

Realizado ajuste nos campos 12,13 e 14 do registro C185 do SPED Fiscal para considerar o valor médio unitário do ICMS, ICMS ST e FCP ST respectivamente. 

Disponível à partir da biblioteca 12.1.2209
