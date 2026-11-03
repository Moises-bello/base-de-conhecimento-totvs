---
content_hash: 156b9315d35ed7b277a9a8e13ba647fd45b919e0270368d9fe02f1a13316b572
fetched_at: '2026-07-02T19:24:24.258124+00:00'
page_id: '473104559'
product: protheus
source: tdn-tec
title: Variáveis Privates são alteradas no uso da função __Hrs2Min
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=473104559
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Variáveis do tipo Private eram alterados quando passados via parâmetro na função \_\_Hrs2Min. |
| Correção | Correção da função \_\_Hrs2Min para não alterar o valor do parâmetro informado. |
| Informações adicionais | * Referente ao chamado: TTEC-2998 * Disponível em builds iguais ou superiores a [13.1.3.42](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.42) e [13.2.3.42](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.42). |
