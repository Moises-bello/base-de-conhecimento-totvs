---
content_hash: 83c9c84073de1e7bd0a00ec9e431323a59298f3d06426fbcc396bdcb511c368c
fetched_at: '2026-06-29T00:11:21.566016+00:00'
page_id: '697265899'
product: rm
source: tdn-rm
title: FISCAL01-18291 - DT - NFS - Geração do movimento com número da Prefeitura.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=697265899
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFS-e |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18281 |

## **02. SITUAÇÃO/REQUISITO**

[...] ao realizarmos o processo de geração do movimento com o número da Prefeitura através do Sped Municipal, o movimento não era gerado e uma mensagem de erro era apresentada, devido à data de competência estar vazia.

## **03. SOLUÇÃO**

Ajuste na data de competência, que caso seja nula ou possua seu valor mínimo, recebe o mesmo valor da data de emissão.

Disponível a partir da versão 12.1.34
