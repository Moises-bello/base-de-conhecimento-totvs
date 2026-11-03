---
content_hash: dc7581f2aba3dfa114a6f1fe73aa319573eec5188cf184c331c0bd77014bbfd4
fetched_at: '2026-07-02T19:24:23.941541+00:00'
page_id: '451267323'
product: protheus
source: tdn-tec
title: GzStrComp não retorna corretamente o tamanho do conteúdo compactado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=451267323
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Ao compactar um conteúdo no formato gzip utilizando a função GzStrComp, o tamanho do conteúdo compactado não era retornado corretamente. Problema gerava falha de comunicação no servidor rest. |
| Correção | Correção no retorno do tamanho do conteúdo compactado. |
| Informações adicionais | * Referente ao chamado: TTC-2833 * Disponível em builds iguais ou superiores a [13.1.3.41](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.41) e [13.2.3.41](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.41). |
