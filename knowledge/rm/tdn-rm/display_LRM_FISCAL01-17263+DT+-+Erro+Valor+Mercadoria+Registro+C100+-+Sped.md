---
content_hash: a15e61ab2c33ac3573c2996df2eb31067790474a3412cd97bcdc4ee63bed6b29
fetched_at: '2026-06-29T00:11:13.202191+00:00'
page_id: '658426889'
product: rm
source: tdn-rm
title: FISCAL01-17263 DT - Erro Valor Mercadoria Registro C100 - Sped
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-17263+DT+-+Erro+Valor+Mercadoria+Registro+C100+-+Sped
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotinas Fiscais - SPED Fiscal |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17263 |

## **02. SITUAÇÃO/REQUISITO**

INTERPRETAÇÃO DE DEMANDA  
Cliente informa que ao gerar a rotina, no registro C100 está sendo somado o valor de ST ao valor das mercadorias para notas de saída e levado ao campo 16 da rotina. Cliente solicita que nesse campo seja considerado somente o valor das mercadorias, conforme nota fiscal eletrônica.

## **03. SOLUÇÃO**

Valor do campo 16 (VL\_MERC) do registro C100 do SPED Fiscal desconsidera o valor de ST para lançamentos de saída.
