---
content_hash: 3a024130e594eccadf2c13277b685b5cb53728cebc25fccdaea6f19d0b908030
fetched_at: '2026-06-29T00:10:55.976609+00:00'
page_id: '590048093'
product: rm
source: tdn-rm
title: FISCAL01-14477 - DT Gerar o Sped Fiscal com NF-e de Devolução por Recusa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590048093
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14477 |

## **02. SITUAÇÃO/REQUISITO**

Geraro Sped Fiscal com NF-e de Devolução por Recusa sem os dados do cliente.

## **03. SOLUÇÃO**

Na geração do registro 0150 e C100 do SPED Fiscal será considerado o Emitente/Destinatário Filial quando a CFOP (Aba - Outros Dados - Tipo Natureza (Rotinas Legais) → Devolução Por Recusa ) presente na situação tributária do lançamento.
