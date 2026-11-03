---
content_hash: a031c2f43759fa33ca41a44f8c3bdcf4625ce7d7df39b564e519fde1af22d207
fetched_at: '2026-07-02T19:24:21.500791+00:00'
page_id: '267807626'
product: protheus
source: tdn-tec
title: Botão direito do mouse não funciona em TGrid
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267807626
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Ocorrência | Ao clicar com o botão direito do mouse em cima do componente TGrid, o bloco de código associado na propriedade bRClicked não é executado.  Ex: :bRClicked:= {|| MsgStop("bRClicked") } |
| Correção | Corrigido o componente TGrid para executar o bloco de código associado a propriedade bRClicked |
| Informações adicionais | * Referente ao chamado: TWAKBF * Referente à ocorrência: SSIM-1258 * Disponível a partir da build 7.00.131227A - 2.3.6 |
