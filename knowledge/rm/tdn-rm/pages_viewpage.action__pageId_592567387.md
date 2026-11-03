---
content_hash: bb3852464c475d31528753087d5d262bf266b26bcacdcaf9542682c8a7b04d79
fetched_at: '2026-06-29T00:10:56.701708+00:00'
page_id: '592567387'
product: rm
source: tdn-rm
title: FISCAL01-14478 - DT Gerar o EFD Contribuições com NF-e de Devolução por Recusa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592567387
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14478 |

## **02. SITUAÇÃO/REQUISITO**

Gerar a EFD com NF-e de Devolução por Recusa sem os dados do cliente.

## **03. SOLUÇÃO**

Na geração do registro 0150 e C100 da EFD Fiscal será considerado o Emitente/Destinatário Filial quando a CFOP (Aba - Outros Dados - Tipo Natureza (Rotinas Legais) → Devolução Por Recusa ) presente na situação tributária do lançamento.
