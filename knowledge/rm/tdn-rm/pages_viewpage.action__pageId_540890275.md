---
content_hash: f68547b70fbb01408a3235e6e134e08ba8fbbfdf0ad84cfe2dfdbd7bda044aea
fetched_at: '2026-06-29T00:10:37.800050+00:00'
page_id: '540890275'
product: rm
source: tdn-rm
title: FISCAL01-12530 DT Ajustar geração do SPED para não selecionar lançamentos de
  sub-apuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=540890275
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12530 |

## **02. SITUAÇÃO/REQUISITO**

Ajustar a geração do SPED Fiscal para NÃO selecionar lançamentos de Outros Débitos/Créditos que possuam sub-apuração informada, na geração dos registros referente apuração do ICMS.

## **03. SOLUÇÃO**

Durante a geração do bloco E do SPED Fiscal não serão considerados os Lançamentos de Outros Débitos/Créditos  cujo campo "Sub-Apuração do Período" esteja preenchido.
