---
content_hash: d14c897c7ed809fcd9da26ebe424387f55642df80c2f6b279e35ecef8e7e3020
fetched_at: '2026-07-02T19:24:21.280281+00:00'
page_id: '266970624'
product: protheus
source: tdn-tec
title: Encerramento do AppServer quando não tem permissão de criar arquivo na própria
  pasta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266970624
version: 4
---

Encerramento do AppServer quando não tem permissão de criar arquivo na própria pasta

|  |  |
| --- | --- |
| Situação | Encerramento do AppServer quando não tem permissão de criar arquivo na própria pasta |
| Ocorrência | Ao utilizar o método ParseURL da classe WSDLManager, o AppServer tenta criar arquivos na própria pasta com o objetivo de otimização, quando não há a permissão para criar esse arquivo o AppServer era encerrado. |
| Melhoria | Uma mensagem é exibida e o método ParseURL retorna erro. |
| Informações adicionais | * Referente ao chamado: SSIM-1141 * Referente à ocorrência: Não há ocorrência associada * Disponível em builds superiores a 7.00.131227A - 2.0.3 |
