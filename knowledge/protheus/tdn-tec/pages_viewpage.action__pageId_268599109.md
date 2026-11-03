---
content_hash: 2ed28ea311366acd93019e4b2f96eafce2734f18821e637214fb0c5e9a70cc18
fetched_at: '2026-07-02T19:24:21.588198+00:00'
page_id: '268599109'
product: protheus
source: tdn-tec
title: Correção - FreeChildren não limpa label automático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268599109
version: 1
---

Ao executar um FreeChildren em um container que tem componentes como TGet ou TComboBox que geram seus labels automaticamente por parâmetro, os labels também são limpos.

|  |  |
| --- | --- |
| Situação | FreeChildren não limpa label automático |
| Ocorrência | Quando se tem um TGet que tem seu label gerado automaticamente por parâmetro, dentro de algum container como um TPanel, e é utilizada a função FreeChildren nesse container, o label não é limpo assim como o componente. |
| Correção | Foi adicionado um tratamento para que na destruição destes componentes para que se eles possuírem o label automático, ele seja destruído também. |
| Informações adicionais | * Referente ao chamado: TWEXZ8 * Referente à ocorrência: SSIM-1259 * Disponível em builds superiores a 7.00.131227A 2.3.0 |
