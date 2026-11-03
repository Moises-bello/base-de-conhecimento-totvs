---
content_hash: 8a7bd2cc5f6c3759fe8effe7007c02636b2d3696745d0190d1499cad85612302
fetched_at: '2026-06-29T00:11:17.260545+00:00'
page_id: '678578733'
product: rm
source: tdn-rm
title: 12830280 FISCAL01-17441 - DT - Apuração Tributo CIDE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=678578733
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Escrituração |
| País: | Brasil |
| Ticket: | 12830280 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17000 |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar a escrituração de um movimento de serviço, com emissão 09/2021 e entrada 10/2021 é apresentada a inconsistência abaixo, mesmo com o período de apuração do tributo ISS 10/2021 aberto:

"Erro na Inclusão do Registro:  
Data Movimento: 02/09/2021  
Documento: 000556677  
Série: U  
Tipo: 1.2.04  
Filial: 1  
Natureza de Operação: 2.949.0003  
Motivo: Período de Apuração do(s) Tributo(s) ISS não está aberto para movimentação."

## **03. SOLUÇÃO**

Ajustada escrituração para usar o novo serviço criado no financeiro ([~~FISCAL01-17681~~](https://jiraproducao.totvs.com.br/browse/FISCAL01-17681 "Serviço para retornar a data de Vencimento")), que passará a considerar a menor data de vencimento do movimento no financeiro ao invés de olhar para a data do lançamento.
