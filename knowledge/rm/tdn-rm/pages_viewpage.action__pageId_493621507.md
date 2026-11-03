---
content_hash: 89ecc52186905f1ba02dd8b390ec7c92d7279abb24285e55d22aab1ec9c331bc
fetched_at: '2026-06-29T00:10:21.746482+00:00'
page_id: '493621507'
product: rm
source: tdn-rm
title: FISCAL01-9194 DT Funrural - Outros Tributos do Lançamento e do Item - Alteração
  da label da tela Outros Tributos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493621507
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Lançamento Fiscal |
| Ticket: | FISCAL01-9194 |
| Requisito/Story/Issue (informe o requisito relacionado) : | Lançamento Fiscal |

## **02. SITUAÇÃO/REQUISITO**

Nos Outros Tributos do Lançamento e do Item:  
  
Desabilitar a exibição do campo "Código da Receita - SENAR".  
Alterar o nome do campo "Código de Receita" para "Identificador do Código de Receita".  
Implementar a partir do Release 12.1.23.

## **03. SOLUÇÃO**

Na tela de Outros Tributos do Item do Lançamento Fiscal, foi alterado:

* O nome do campo "Código de Receita" para "Identificador do INSS/PJ".
* Ocultação do campo "Código da Receita - SENAR" em Outros Tributos no item do lançamento.
