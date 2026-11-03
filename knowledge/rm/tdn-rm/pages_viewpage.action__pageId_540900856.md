---
content_hash: 8c03e576df2c3830b97c43ed370b82afb4b53e78a2d2c3601e3fcae7ee901e82
fetched_at: '2026-06-29T00:10:37.834133+00:00'
page_id: '540900856'
product: rm
source: tdn-rm
title: DT Validação do tamanho do campo de pessoa do Pergamum
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=540900856
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Gestão Educacional |
| Função: | Integrações - Pergamum |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | EDUCACIONAL01-12580 |

## **02. SITUAÇÃO/REQUISITO**

Para o correto funcionamento da integração TOTVS Educacional e o Pergamum funcionar corretamente é necessário que o parâmetro do tamanho do campo código da pessoa do Pergamum seja sempre 20, assim, era necessário que nós efetuassemos esta validação no TOTVS Educacional para evitar inconsistências.

## **03. SOLUÇÃO**

A equipe do Pergamum disponibilizou um método para ser consumido através do webservice para realizar a consulta a este parâmetro, assim ao acessar a tela de de parâmetro de integração da biblioteca, os processo de exportar usuários e importação de multas no TOTVS Educacional o sistema irá validar se o campo código da pessoa definido no ambiente do Pergamum está com 20 caracteres. Se não estiver, este processos serão abortados.

Para mais informações sobre os parâmetros 

Observações

Esta alteração está disponível à partir das versões:

* 12.1.24.286
* 12.1.25.247
* 12.1.26.195
* 12.1.27.137
