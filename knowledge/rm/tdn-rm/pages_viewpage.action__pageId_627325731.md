---
content_hash: b545c3c57f66d267ede8f075d4cd1061b8ab43488a00275b852b1a9c768ffc91
fetched_at: '2026-06-29T00:11:04.472141+00:00'
page_id: '627325731'
product: rm
source: tdn-rm
title: FISCAL01-15588- DT Parâmetros de Processos - Processo FCI - Ficha de Conteúdo
  de Importação - MDI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=627325731
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cadastro Parâmetros de Processos |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FISCAL01-15588](https://jiraproducao.totvs.com.br/browse/FISCAL01-15588) |

## **02. SITUAÇÃO/REQUISITO**

Considerar o novo cadastro .Net verificando o parâmetro HABILITANOVOCADPARAMPROCESSO da tabela DPARAMETROS para o cálculo de ficha de conteúdo de importação e considerar o parâmetro de processo pela coligada de contexto.

***SubGrupo do Processo:***

Seleção de Produtos para geração da FCI

## **03. SOLUÇÃO**

A geração de Cálculo de FCI passa a considerar também os processos da MDI com base no parâmetro ***HABILITANOVOCADPARAMPROCESSO.**.*
