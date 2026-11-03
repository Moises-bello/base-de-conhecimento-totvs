---
content_hash: aaf76cba1f5c9cc2f6f6b53b70a16a675b3b11794b7730847d6cb8093cd53d07
fetched_at: '2026-06-29T00:11:05.286943+00:00'
page_id: '628956255'
product: rm
source: tdn-rm
title: FISCAL01-15193 - DT - Gerar o registro F120\F130 - Processo de Inclusão de
  Patrimônios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628956255
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Inclusão de Patrimônios em Lote |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FISCAL01-15193](https://jiraproducao.totvs.com.br/browse/FISCAL01-15193) |

## **02. SITUAÇÃO/REQUISITO**

Implementar processo para facilitar a Inclusão de Patrimônios associados aos parâmetros de processos F120 e F130.

* Este processo deve ser exibido somente para os parâmetros F120 e F130.
* O processo deve permitir a seleção de 1 ou muitos patrimônios conforme filtro definido pelo usuário na tela do processo. Só carregar patrimônio de último nível conforme lookup da tela de Filtro de Patrimônio.
* Deve ocorrer as mesmas validações que o cadastro de filtro de patrimônio realiza.
* O processo deve consistir se o parâmetro de processo é F120 ou F130.

## **03. SOLUÇÃO**

Foi criado um processo para inclusão de patrimônios em lote dos grupos F120 e F130.
