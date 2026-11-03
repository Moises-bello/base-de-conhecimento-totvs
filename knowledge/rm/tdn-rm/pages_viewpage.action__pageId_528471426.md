---
content_hash: 8ab1f5e663bbb1f3f9a3bbf3988a00ecd190675a0ea7359d443b54fe25b7d879
fetched_at: '2026-06-29T00:10:33.323869+00:00'
page_id: '528471426'
product: rm
source: tdn-rm
title: 2529419 FISCAL01-4131 DT EFD Contribuições - CST 49
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=528471426
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD Contribuições |
| Ticket: | 2529419 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-4131 |

## **02. SITUAÇÃO/REQUISITO**

Retirar o CST 49 da lista de CSTs utilizados na opção "Gerar Operações sem direito a crédito" pois o mesmo deve ser utilizado em operações de saída.

## **03. SOLUÇÃO**

Dado que existem lançamentos fiscais que possua CST 49 em um dos tributos: PIS / COFINS  
Ao Gerar a rotina da EFD Contribuições para o período destes lançamentos   
Devem ser exibidos os C100/C170 referentes a estes lançamentos.
