---
content_hash: a0287309e48422c8c6001d6c85745cc75702d0814c94753cf0788b81707f311d
fetched_at: '2026-06-29T00:11:32.024299+00:00'
page_id: '743677091'
product: rm
source: tdn-rm
title: FISCAL01-19201 DT - DEISS Indaiatuba - Apuração ISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=743677091
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Gerador Saídas |
| País: | Brasil |
| Ticket: | [#15935590](https://totvssuporte.zendesk.com/agent/tickets/15935590) |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-19201 |

## **02. SITUAÇÃO/REQUISITO**

O campo 23 está sendo gerado conforme o campo "Regime de ISS" dos Dados Fiscais da Filial do Lançamento.

Para o registro ser gerado corretamente, deve ser considerado o campo "Regime de ISS" do Cliente/Fornecedor do Lançamento.

## **03. SOLUÇÃO**

Alterado o layout da rotina DEISS para obter o campo 23 do Cliente/Fornecedor.

Adicionadas as opções Cooperativa e ME EPP na lista de opções do campo "Regime de ISS" do Cliente/Fornecedor.
