---
content_hash: 7f721a2541bdc6549d3a80909264bbacc7393c89e18f6320f608eef7af55ff65
fetched_at: '2026-07-02T19:24:25.147729+00:00'
page_id: '499105572'
product: protheus
source: tdn-tec
title: '[NS] Erro no SUP50001 ao realizar pesquisa na descrição de item que contém
  aspas'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=499105572
version: 2
---

|  |  |
| --- | --- |
| Ocorrência | Totvstec estava traduzindo aspas duplas para aspas simples no conteúdo de um filtro de campo, contudo só os delimitadores podem fazê-lo. |
| Correção | Tratamento para que o conteúdo dentro de aspas simples não seja alterado, mesmo que haja aspas duplas. |
| Informações adicionais | * Referente ao chamado: TTEC-2401 * Disponível em builds iguais ou superiores a [13.1.3.44](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.44). |
