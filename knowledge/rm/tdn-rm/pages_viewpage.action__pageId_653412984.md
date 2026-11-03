---
content_hash: cf5781ae4d8942b85c19b3c36f00cb16b533135c4668287a061ba754ba7eefbd
fetched_at: '2026-06-29T00:11:12.456135+00:00'
page_id: '653412984'
product: rm
source: tdn-rm
title: DT FISCAL01-17024 - Agrupar Registro 1900 para lançamentos com mesma CFOP e
  CST
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=653412984
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Gerador de saída |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17024 |

## **02. SITUAÇÃO/REQUISITO**

Conforme os testes feitos na issue [FISCAL01-16772](https://jiraproducao.totvs.com.br/browse/FISCAL01-16772), foi identificado que em um lançamento com várias naturezas de mesma raiz (ex.: 6.1.XXX) o registro 1900 não foi agrupado ao gerar EFD contribuições.

## **03. SOLUÇÃO**

Foi realizada alteração no layout da rotina EFD PIS COFINS para que o registro seja agrupado conforme requisito da tarefa.
