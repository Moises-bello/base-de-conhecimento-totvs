---
content_hash: cd7a9cc4f7dd8a5431d3dcba6143b9c22ee9316f2a1087bffcccda3c3ba08866
fetched_at: '2026-06-29T00:10:42.723313+00:00'
page_id: '547256010'
product: rm
source: tdn-rm
title: 8271240 FISCAL01-12699 DT Escrituração Transferências Canceladas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547256010
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Processo de Escrituração Fiscal |
| Ticket: | 8271240 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12699 |

## **02. SITUAÇÃO/REQUISITO**

A Escrituração dos Movimentos de Transferências de Entrada, é feito a partir da Seleção dos Movimentos de Transferências de Saída.  
Quando tem movimentos de Saída cancelado no processo de escrituração do Lote de Entrada ocorre erro:  
"Movimento de Entrada de Transferência cujo movimento de saída esteja Cancelado."

## **03. SOLUÇÃO**

Inclusão de condição no Processo de Escrituração Fiscal para não selecionar transferências Canceladas em lotes de Entrada.
