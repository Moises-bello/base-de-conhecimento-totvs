---
content_hash: 72520604cb70b223a58e8b8948140eff7924f8c09841c9f06522dd248ea96f21
fetched_at: '2026-06-29T00:10:56.698358+00:00'
page_id: '592566346'
product: rm
source: tdn-rm
title: 10396006 FISCAL01-14586 DT NFS-e DSFNET - Percentual/valor de dedução para
  item que possui dedução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592566346
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | NFS-e |
| País: | Brasil |
| Ticket: | 10396006 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14586 |

## **02. SITUAÇÃO/REQUISITO**

Para todos os municípios DSFNet iremos alterar a geração do grupo de deduções para gerar de acordo com os dados do itens sem agrupar.

## **03. SOLUÇÃO**

Alteração no grupo de dedução da NFS-E. O grupo passa a ser gerado com valor do item para municípios que utilizam o layout DSFNET, desde que o percentual de dedução seja superior a 0%.
