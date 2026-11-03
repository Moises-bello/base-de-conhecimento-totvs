---
content_hash: 17894a9891e4eb885e9eeaa056b580dda9d663ef84808f7cb7048e09e4d719de
fetched_at: '2026-07-02T19:24:23.209893+00:00'
page_id: '271182230'
product: protheus
source: tdn-tec
title: Erro na propriedade cTooltip
type: documentation
url: https://tdn.totvs.com/display/tec/Erro+na+propriedade+cTooltip
version: 2
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Ocorrência | Ao utilizar a propriedade cTooltip com o caracter '\r' ocorria o seguinte erro:  Error: Invalid or unexpected token  comp(6020).tsay('setHint', ....) |
| Correção | Corrigida a propriedade cTooltip para sempre converter caracteres especiais. |
| Informações adicionais | * Referente ao chamado: 117807 * Referente à ocorrência: MTEC-62 / BAS-1042 * Disponível a partir da build 7.00.131227A - 2.3.7 |
