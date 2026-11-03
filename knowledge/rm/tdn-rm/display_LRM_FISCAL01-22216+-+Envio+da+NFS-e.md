---
content_hash: e209e552041f63f1cd2aabc1620aadc828bc1327ab78c99abae21370a6cd3ecc
fetched_at: '2026-06-29T00:11:49.349446+00:00'
page_id: '830957885'
product: rm
source: tdn-rm
title: FISCAL01-22216 - Envio da NFS-e
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-22216+-+Envio+da+NFS-e
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFSe |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-21287 |

## **02. SITUAÇÃO/REQUISITO**

Alterar o processo de envio da NFS-e para considerar o código de serviço informado no campo criado por Município, caso o campo esteja em branco deverá ser mantido o comportamento atual.

## **03. SOLUÇÃO**

Comportamento alterado. Campo "codigo" da nota fiscal de serviço passa a gerar com o valor do campo criado, caso ele possua valor.

Disponível à partir da biblioteca 12.1.2306
