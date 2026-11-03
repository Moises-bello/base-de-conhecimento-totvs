---
content_hash: 1b6525db74da659f43dddc17c2792af1184a89a0c5333fcbb0cc5b83787d1a7e
fetched_at: '2026-06-29T00:10:56.146943+00:00'
page_id: '592076962'
product: rm
source: tdn-rm
title: 10642131 FISCAL01-14688 - DT Sub Apuração - Outros Déb/Créd
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592076962
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Outros Débitos/Créditos  Subapuração |
| País: | Brasil |
| Ticket: | 10642131 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14688 |

## **02. SITUAÇÃO/REQUISITO**

Ao lançar as informações em outros Débitos e outros Créditos o campo de Sub Apuração (DLDC.IDSUPAPURAAOPERIODO) não está ficando gravado no lançamento.

## **03. SOLUÇÃO**

Realizado ajuste para que ao incluir/alterar o registro do lookup de Subapuração do Período o mesmo seja gravado no lançamento.
