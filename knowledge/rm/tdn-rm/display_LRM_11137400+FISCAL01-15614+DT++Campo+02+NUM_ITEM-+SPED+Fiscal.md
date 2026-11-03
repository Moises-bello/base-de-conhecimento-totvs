---
content_hash: 806bab64770c4de3ac95c9ac9c369374f833a118394c680c079ff3c568e274cd
fetched_at: '2026-06-29T00:11:03.384317+00:00'
page_id: '621582016'
product: rm
source: tdn-rm
title: 11137400 FISCAL01-15614 DT  Campo 02 NUM_ITEM- SPED Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/11137400+FISCAL01-15614+DT++Campo+02+NUM_ITEM-+SPED+Fiscal
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| País: | Brasil |
| Ticket: | 11137400 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15614 |

## **02. SITUAÇÃO/REQUISITO**

Atualmente geramos o Campo 02 NUM\_ITEM - Número sequencial do item no documento fiscal - do Registro C170 com sequencial IDLAF e NUMITEM. O Cliente solicita que seja gerado com o sequencial igual ao informado na NFe.

## **03. SOLUÇÃO**

Foi alterada a geração do campo 2 NUM\_ITEM do SPED Fiscal, para ser gerado pelo NUM\_ITEM da DLAF.
