---
content_hash: 5e186fb8960a7909071f026182b5dd6336ee74aa9c8566ee08e06c4d535dc1d4
fetched_at: '2026-07-02T19:24:23.194572+00:00'
page_id: '271171385'
product: protheus
source: tdn-tec
title: Pedido de Vendas apresenta erro ao digitar a quantidade e pressionar a tecla
  enter do teclado.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271171385
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Ocorrência | É necessário possuir um produto configurado com grade para reproduzir o problema.  - Acessar o pedido de venda, Incluir, Informar os campos de cabeçalho.  - Informar o produto de ref de grade.  - Informa a quantidade e pressionar enter, então é gerado errorlog:  Error: Invalid or unexpected token |
| Correção | Correção no componente TGetdados |
| Informações adicionais | * Referente ao chamado: 96108 * Referente à ocorrência: SSIM-1314 * Disponível a partir da build 7.00.131227A - 2.3.7 do SmartClient HMTL |
