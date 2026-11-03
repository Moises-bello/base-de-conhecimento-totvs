---
content_hash: 8c3cfd05bea700cc4798116a57b566f2f0e3b8dcc147adefb5c87bea03e8a67a
fetched_at: '2026-06-29T00:10:22.544018+00:00'
page_id: '497202895'
product: rm
source: tdn-rm
title: 1331994 FISCAL01-1457 DT EFD Contribuições - NF Canceladas A100
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=497202895
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | EFD Contribuições |
| Ticket: | 1331994 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-1457 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o EFD Contribuições verificamos que a Nota Fiscal de serviço que foi   
emitida em um mês e cancelada no mês posterior, foi levada para a   
rotina como cancelada no mês de emissão.

## **03. SOLUÇÃO**

Alterar a Rotina da EFD Contribuições para considerar Status de Lançamento Fiscal   
que estiver “Cancelado” igual a “Normal” quando o mesmo for cancelado no   
Período posterior ao da geração da Rotina.
