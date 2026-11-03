---
content_hash: 02e15127e4eeea9b7c0b5ac3391cb9c4b614c6f7d760e637f7ed5fb61a50ba6b
fetched_at: '2026-06-29T00:11:39.871963+00:00'
page_id: '790644867'
product: rm
source: tdn-rm
title: FISCAL01-19031 - DT - TOTVS Backoffice > Linha RM > Compras - Alterar Job Serviço
  de Consulta de Arquivos XML
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=790644867
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Consulta de arquivos xml |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-19031 |

## **02. SITUAÇÃO/REQUISITO**

Ao executar o processo "Serviço de Consulta de Arquivos XML", sem arquivos na pasta usada pelo processo, é exibida uma mensagem de erro no log.

## **03. SOLUÇÃO**

Alterado o log para não ser mostrado como erro, mas como sucesso.

Disponível a partir da biblioteca 12.1.2310
