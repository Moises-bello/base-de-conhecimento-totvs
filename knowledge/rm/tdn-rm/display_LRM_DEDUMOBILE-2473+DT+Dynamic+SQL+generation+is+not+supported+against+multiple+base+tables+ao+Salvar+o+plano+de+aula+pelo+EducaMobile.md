---
content_hash: daac8a7aea0d1fcb99734a92bed013a6b0f7cb59f78b7f9f54d13051b08465ca
fetched_at: '2026-06-29T00:10:30.404018+00:00'
page_id: '520093998'
product: rm
source: tdn-rm
title: DEDUMOBILE-2473 DT Dynamic SQL generation is not supported against multiple
  base tables ao Salvar o plano de aula pelo EducaMobile
type: documentation
url: https://tdn.totvs.com/display/LRM/DEDUMOBILE-2473+DT+Dynamic+SQL+generation+is+not+supported+against+multiple+base+tables+ao+Salvar+o+plano+de+aula+pelo+EducaMobile
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | TOTVS Educacional |
| Módulo: | TOTVS Educa Mobile |
| Função: | Aulas (Plano de Aulas) |
| Ticket: | [7081910](https://totvssuporte.zendesk.com/agent/tickets/7081910 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUMOBILE-2473](https://jiraproducao.totvs.com.br/browse/DEDUMOBILE-2473) |

## **02. SITUAÇÃO/REQUISITO**

         Ao tentar editar conteúdo efetivo ou lição de casa pelo aplicativo eduCONNECT é exibido o erro: *Dynamic SQL generation is not supported against multiple base tables.*

## **03. SOLUÇÃO**

Otimizado a rotina de plano de aula do TOTVS Educa Mobile, pois o sistema estava apresentando erro ao salvar alguma informação no plano de aula quando este possuía algum arquivo associado a aula.
