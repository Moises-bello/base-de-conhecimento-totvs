---
content_hash: 48cdf78fb440984f122776c60a3f8348594aacc55d6e431ba2ed461350ff4cdb
fetched_at: '2026-06-29T00:11:18.153586+00:00'
page_id: '684008815'
product: rm
source: tdn-rm
title: FISCAL01-17616 - DT - Correção para código de estado na rotina DMS Jaboatão
  dos Guararapes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=684008815
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DMS Jaboatão dos Guararapes |
| País: | Brasil |
| Ticket: | [#13689146](https://totvssuporte.zendesk.com/agent/tickets/13689146 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17616 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o arquivo XML da rotina DMS Jaboatão dos Guararapes, o campo drLoEs fica preenchido incorretamente com a sigla do estado, este campo deveria receber o código do estado de acordo com a seguinte tabela do IBGE: <https://www.ibge.gov.br/explica/codigos-dos-municipios.php>

## **03. SOLUÇÃO**

Correção aplicada na rotina para garantir que o campo seja preenchido corretamente com o código do estado.

Disponível a partir da versão 12.1.33
