---
content_hash: f3bb84172feae631e9225dd5ce0d56da2cdd1c6434acaa7a147d54a49c5f9a4c
fetched_at: '2026-06-29T00:11:31.939706+00:00'
page_id: '741327053'
product: rm
source: tdn-rm
title: FISCAL01-19406 DT - Melhoria para mensagem de erro no processo de calculo de
  diferimento do imposto PIS/Cofins
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=741327053
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Lançamento Fiscal |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-19406 |

## **02. SITUAÇÃO/REQUISITO**

A mensagem de erro exibida pelo processo de cálculo de diferimento Pis/Confins, em caso de ausência do valor do campo TIPOCREDITO, não deixa claro para o usuário caso o erro seja causado por lançamentos específicos em um período.

## **03. SOLUÇÃO**

A mensagem foi modificada para incluir uma lista com os Ids dos lançamentos que estejam sem o campo TIPOCREDITO preenchido no Item da Situação Tributária.

Mensagem Anterior:

Nova mensagem:
