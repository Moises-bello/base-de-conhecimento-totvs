---
content_hash: 5f45180db049e961083f382f06cdc2e9262066fc63889622042547a4c0e5e013
fetched_at: '2026-06-29T00:10:53.886041+00:00'
page_id: '589514603'
product: rm
source: tdn-rm
title: FISCAL01-14476 - DT Transmitir NF-e de Devolução por recusa sem os dados do
  cliente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=589514603
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NF-e |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14476 |

## **02. SITUAÇÃO/REQUISITO**

Transmitir NF-e de Devolução por Recusa sem os dados do cliente

## **03. SOLUÇÃO**

Foi criado um novo Tipo de Natureza no cadastro da CFOP, este tipo é referente a Devolução por Recusa.

Ao enviar uma NF-e de um movimento parametrizado através processo de cópia por referência em conjunto com uma Natureza do tipo Devolução em conjunto com o Tipo de Natureza igual a Devolução por Recusa, resultará em um xml da qual a tag destinatário será referente a empresa, e não ao cliente/fornecedor de origem/destino.
