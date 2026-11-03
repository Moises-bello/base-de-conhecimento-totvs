---
content_hash: f4ba03cdce7d5c854c433d6f5499b1e12695b488bb4fabfcd7cefe9f0754c7d1
fetched_at: '2026-07-02T19:24:21.487462+00:00'
page_id: '267803683'
product: protheus
source: tdn-tec
title: Correção - cGetFile diretórios com letra maiúscula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267803683
version: 1
---

A interface cGetFile agora lista corretamente os arquivos de diretórios que possuem alguma letra maiúscula.

|  |  |
| --- | --- |
| Situação | Diretórios com letra maiúscula no cGetFile não exibem seus arquivos. |
| Ocorrência | Não havia um tratamento no SmartClient para respeitar o case sensitive de ambientes Unix. |
| Correção | Foi adicionado o tratamento para case sensitive. |
| Informações adicionais | * Referente ao chamado: TVS520 * Referente à ocorrência: TEC-7491 SSIM-1229 * Disponível em builds superiores a 131227A 2.2.1 |
