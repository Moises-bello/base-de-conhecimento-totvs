---
content_hash: 85dedc93b4d90f336d49a197707fd6c069970cade0dbdd13daa7776453fe6b39
fetched_at: '2026-06-29T00:12:10.624572+00:00'
page_id: '953002985'
product: rm
source: tdn-rm
title: Grupo P - Imposto de Importação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953002985
version: 1
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo P - Imposto de Importação** | | | | | | | | | | | | |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocorrência | Tamanho | Observação | **Campo de Origem** | **Campo na Aplicação** | Mais Informações |
| 262 | P01 | II | Grupo Imposto de Importação | CG | M01 |  | 0-1 |  | Informar apenas quando o item for sujeito ao II |  |  |  |
| 263 | P02 | vBC | Valor BC do Imposto de Importação | E | P01 | N | 1-1 | 13v2 |  | TTRBMOV.BASEDECALCULO | Base de Cálculo |  |
| 264 | P03 | vDespAdu | Valor despesas aduaneiras | E | P01 | N | 1-1 | 13v2 |  | TITMMOVFISCAL.VALORDESPADU | Valor das Despesas Aduaneiras |  |
| 265 | P04 | vII | Valor Imposto de Importação | E | P01 | N | 1-1 | 13v2 |  | TTRBMOV.VALOR | Valor |  |
| 266 | P05 | vIOF | Valor Imposto sobre Operações Financeiras | E | P01 | N | 1-1 | 13v2 |  |  |  | Fixo 0 |
