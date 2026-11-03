---
content_hash: fa82fcac5893c0bfb0e7f003c3e4c55784cea96ad12e74b525158bb437f07bed
fetched_at: '2026-07-02T19:24:25.003597+00:00'
page_id: '494975075'
product: protheus
source: tdn-tec
title: CodeBlock End() não são chamados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=494975075
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Ao inserir dois browsers na janela apenas o End() do primeiro estava sendo chamado |
| Correção | Corrigido iteração dos objetos de forma que todos elementos sejam percorridos |
| Informações adicionais | * Referente ao chamado: TTEC-3196 * Disponível em builds iguais ou superiores a [13.1.3.44](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.44) e [13.2.3.44](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.44). |
