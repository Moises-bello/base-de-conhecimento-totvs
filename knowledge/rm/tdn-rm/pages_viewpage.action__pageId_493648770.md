---
content_hash: b809ef0312ea279a3cc787fd019eedcef4cd13a55fb411c25a9042561adcf562
fetched_at: '2026-06-29T00:10:21.842145+00:00'
page_id: '493648770'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1327 DT Edição de registro de cadastro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493648770
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | Retenção de Alunos by Carol |
| Função: | Cadastros |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUANALYTICS-1327 |

## **02. SITUAÇÃO/REQUISITO**

Os cadastros no Retenção de Alunos by Carol estão com comportamentos diferentes no salvamento de registros que são editados mas não são modificados, alguns estão barrando essa ação e outros permitem que isso seja feito.

## **03. SOLUÇÃO**

Padronização do comportamento citado anteriormente nos cadastros do Retenção de Alunos. Será permitido que um registro editado seja salvo mesmo que nenhuma informação tenha sido alterada. Apenas na inclusão de novos registros que será validade a duplicidade.
