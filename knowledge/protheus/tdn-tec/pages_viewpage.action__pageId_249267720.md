---
content_hash: c2690c08864aa7c6493b4193499da9b7787ebbe608c187564bad4fa596ceb243
fetched_at: '2026-07-02T19:24:20.451909+00:00'
page_id: '249267720'
product: protheus
source: tdn-tec
title: Falha na criação do LSNumber.val
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=249267720
version: 4
---

Falha na criação do LSNumber.val

|  |  |
| --- | --- |
| Situação | Falha na criação do LSNumber.val |
| Ocorrência | Quando a máquina era reiniciada sem finalizar o AppServer o arquivo LSNumber.val não era criado. |
| Melhoria | O arquivo LSNumber.val não será mais criado, obrigando a regeração a partir de a numeração do banco de dados. |
| Informações adicionais | * Referente ao chamado: SSIM-1149 * Referente à ocorrência: não há ocorrência associada * Disponível em builds superiores a 7.00.131227A -  1.0.3 |
