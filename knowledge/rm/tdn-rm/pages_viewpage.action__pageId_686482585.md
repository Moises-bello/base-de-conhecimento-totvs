---
content_hash: 58321530f902ceaac31187f888e0251f0c1cb93603607b67aad8fc9a1048c96d
fetched_at: '2026-06-29T00:11:20.530477+00:00'
page_id: '686482585'
product: rm
source: tdn-rm
title: FISCAL01-18054 - DT - Alteração na regra de preenchimento do campo "codpais"
  da NFS-e para preencher também para Joinville
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=686482585
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFS-e Envio |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18054 |

## **02. SITUAÇÃO/REQUISITO**

A regra de preenchimento do campo "codpais" na geração de NFS-e estava restringindo o preenchimento somente para os municípios de Vila Velha e Itajaí. É necessário gerar também para o município de Joinville.

## **03. SOLUÇÃO**

Alteração feita na regra para que o campo também seja preenchido para notas do município de Joinville.

Disponível a partir da versão 12.1.34
