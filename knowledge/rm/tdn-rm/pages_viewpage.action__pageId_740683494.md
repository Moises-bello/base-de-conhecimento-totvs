---
content_hash: 05835c1d451cfc88a8656a8f347d448c287729e8f375a9243a03a6976858e04f
fetched_at: '2026-06-29T00:11:31.537967+00:00'
page_id: '740683494'
product: rm
source: tdn-rm
title: FISCAL01-19267 DT - Alteração da regra de geração do Registro 1601
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=740683494
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Lançamento Fiscal |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue: | FISCAL01-19267 |

## **02. SITUAÇÃO/REQUISITO**

Alterar a regra de geração do registro 1601 para ser gerado sempre que os dados da instituição financeira estiverem preenchidos. Atual ele gera somente quando o tipo do pagamento é cartão.

## **03. SOLUÇÃO**

Foi alterada a geração do registro 1601 do SPED Fiscal para considerar todos os tipos de pagamentos, exceto  
dinheiro e cheque.
