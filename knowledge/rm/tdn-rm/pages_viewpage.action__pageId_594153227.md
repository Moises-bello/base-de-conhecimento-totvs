---
content_hash: a33c90bbe28609e6a2915472e811bba670fda0762ee028c320ab337f7518282c
fetched_at: '2026-06-29T00:10:57.088100+00:00'
page_id: '594153227'
product: rm
source: tdn-rm
title: 10340846 FISCAL01-14548 - DT Cruzamento Sped Fiscal x EFD Contribuições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=594153227
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | EFD Contribuições |
| País: | Brasil |
| Ticket: | 10340846 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14548 |

## **02. SITUAÇÃO/REQUISITO**

Cliente informa que, ao gerar o SPED Fiscal e SPED Contribuições, a estrutura dos arquivos, Registro C170, geram de maneiras diferentes, causando inconsistência dentro do TIF.

## **03. SOLUÇÃO**

Foram realizadas alterações no Layout do Gerador de Saídas da EFD-Contribuições, afim de padronizar o comportamento do registro C170, deixando-o igual a rotina EFD ICMS/IPI.
