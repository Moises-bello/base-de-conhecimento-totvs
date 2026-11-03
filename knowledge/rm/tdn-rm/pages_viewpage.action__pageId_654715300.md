---
content_hash: 7311e9324915dae2fcca324b1c6a5bcbadf4ab5bc03f7e7d7f5fa753a5056c0c
fetched_at: '2026-06-29T00:11:12.553370+00:00'
page_id: '654715300'
product: rm
source: tdn-rm
title: DT - FISCAL01-17125 - Convênio ICMS 115/2003 - Erro sequencial item
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=654715300
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotina Fiscal - Convênio ICMS 115/2003 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17121 |

## **02. SITUAÇÃO/REQUISITO**

Campo 49 do arquivo "Sequencial do item" está sendo gerado fora de ordem.

## **03. SOLUÇÃO.**

Realizado tratamento para acertar a contagem do número de itens de cada lançamento.

Com isso o campo 49 da rotina Convênico ICMS 115 será gerado corretamente.
