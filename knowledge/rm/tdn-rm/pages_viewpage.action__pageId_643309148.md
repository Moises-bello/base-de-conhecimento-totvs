---
content_hash: e3a9665a21378d5b290945407152aaba5e6a80c0e17fe767bb0229e843d689de
fetched_at: '2026-06-29T00:11:10.293934+00:00'
page_id: '643309148'
product: rm
source: tdn-rm
title: DT - FISCAL01-16724 - Convênio ICMS 115/2003 - Erro sequencial item
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=643309148
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotina Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16606 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a rotina Convênio ICMS 115/2003, a coluna 49, que se refere ao sequencial do item da nota, não está gerando corretamente.

Em uma nota com mais de um item, ao invés do sistema gerar o sequencial 1, 2, 3,..., o sistema está gerando como 1, 1, 1,...

O problema passou a acontecer após alterar a máscara da NF de 9 dígitos, para 15.

## **03. SOLUÇÃO.**

Ajuste na geração do número sequencial do item, passa a ser verificado a sequência do campo NUMITEM da tabela DITEM.
