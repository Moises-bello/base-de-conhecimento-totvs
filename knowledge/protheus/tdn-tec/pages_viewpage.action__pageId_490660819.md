---
content_hash: 2406cbdfb55955c81560e553ac0ea284914371aa38bcf220e2b2bc96ed549a1c
fetched_at: '2026-07-02T19:24:24.880111+00:00'
page_id: '490660819'
product: protheus
source: tdn-tec
title: Correção - Tamanho das abas no SIGAMDI (TWorkSpace)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=490660819
version: 2
---

|  |  |
| --- | --- |
| Situação | Carregar as abas do SIGAMDI em "background", não calcula corretamente os tamanhos disponíveis para pintura da TWorkSpace |
| Ocorrência | Ao deixar o componente em "background" a propriedade "visible" fica como falsa, o que causa problema no cálculo do tamanho do TWorkSpace. |
| Correção | Alteração feita para calcular o tamanho da TWorkSpace corretamente independentemente se a aba está visível ou não |
| Informações adicionais | * Referente ao chamado: 4998606, 3044477, 2825917 e 2922014 * Referente à ocorrência: MTEC-1929 MTEC-1930 MTEC-1931 MTEC-1932 MTEC-1933 MTEC-1934 MTEC-1935 MTEC-1936 MTEC-2356 * Disponível em builds iguais ou superiores a 7.00.131227A - 13.2.3.40 e 7.00.170117A - 17.3.0.8 |
