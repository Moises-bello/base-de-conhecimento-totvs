---
content_hash: fd675e615535bcb68a590ca68c5bad173765d3a55be07108bca350531af7649f
fetched_at: '2026-07-02T19:24:24.918698+00:00'
page_id: '490986191'
product: protheus
source: tdn-tec
title: Queda no Appserver após compilar arquivo log80101.per (4gl Logix)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490986191
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Invasão de memória ao compilar o fonte log80101.per no Server com arquitetura x64. |
| Correção | fazer o cast correto no fonte logixformparserreduce.cpp. Em dois pontos, havia o cast tLogixStackElement& stkEle = \*((tLogixStackElement\*) stackElement()). Contudo, o método stackElement() retorna um ponteiro da classe tLogixFormStackElement, portanto o cast correto é tLogixFormStackElement& stkEle = \*((tLogixFormStackElement\*) stackElement()). Isso resolve a invasão de memória que ocorre nas versões 64 do Server. |
| Informações adicionais | * Referente ao chamado: TTEC-3042 * Disponível em builds iguais ou superiores a [13.1.3.43](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.43). |
