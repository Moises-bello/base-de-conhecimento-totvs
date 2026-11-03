---
content_hash: cf0fa44c043952f5750705c2dde11ff960425b947dd627b15ae4fdbd326e7721
fetched_at: '2026-07-02T19:24:18.870937+00:00'
page_id: '221551852'
product: protheus
source: tdn-tec
title: Label e Checkbox de alguns campos não são exibidos na versão 3.0.10 do SmartClient
  HTML (P12)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=221551852
version: 2
---

|  |  |
| --- | --- |
| Situação | Label e Checkbox de alguns campos não são exibidos na versão 3.0.10 do SmartClient HTML (P12) |
| Ocorrência | * Campos do tipo password nao estavam criando label * Css do Framework apagava o indicator do TCheckBox em SmartClient HTML |
| Correção | * Correcao na criacao de Label para TGet do tipo Password * Correcao no CSS de Label sobre componentes com alinhamento de texto central. * Alteracao do indicator do TCheckBox para nao conflitar com css do framework |
| Informações adicionais | * Referente ao chamado: TTVARI * Referente à ocorrência: SSIM-239 * Disponível em builds superiores a 7.00.131227A - 3.0.11 |
