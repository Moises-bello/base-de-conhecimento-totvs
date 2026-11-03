---
content_hash: 4dad40d1674c373870879127022476d797536a9e9c08b5a09b5955214082c1db
fetched_at: '2026-07-02T19:24:24.161622+00:00'
page_id: '461918367'
product: protheus
source: tdn-tec
title: Inconsistência permitindo acionar F3 de campo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=461918367
version: 1
---

Inconsistência após validação de campo código e loja, com retorno falso na loja, estava permitindo acionar consulta F3 do campo código.

|  |  |
| --- | --- |
| Situação | Em interfaces onde há os campos código e loja (ex.: cliente e loja), era permitido acionar a consulta F3 do campo de código, mesmo quando havia erro indicando que a combinação de código e loja não havia sido encontrada no cadastro. |
| Correção | Realizada correção para que as validações padrão não permitam acionar a consulta sem antes dos dados estarem corrigidos |
| Informações adicionais | * Referente ao chamado: Não há * Referente à ocorrência: MTEC-2381 * Disponível a partir da build 7.00.131227A - 4.2.4 |
