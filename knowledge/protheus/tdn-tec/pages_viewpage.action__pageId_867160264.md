---
content_hash: d3b5e814ecbcffae1c5eca699c989f66a6ba295aeda5693b4e78c11a30d499ff
fetched_at: '2026-07-02T19:24:29.401132+00:00'
page_id: '867160264'
product: protheus
source: tdn-tec
title: Correção - Tela de login não aceita teclas do teclado numérico no Mac
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=867160264
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | A tela de login, ou qualquer tela com TWebEngine, não aceita dígitos entrados pelo teclado numérico em Mac |
| Ocorrência | A tela de login, ou qualquer tela com TWebEngine, não aceita dígitos entrados pelo teclado numérico em Mac |
| Correção | Removido o modificador "Keypad" ao receber um evento de teclado para que o QCefView reconheça como um digito normal. Processo feito apenas para o Mac. |
| Informações adicionais | * Referente ao chamado: [#19585934](https://suporte.totvs.com/portal/p/10098/consulta-tickets?ticket=19585934) * Referente à ocorrência: DTCLIENT01-4634 * Disponível em builds superiores a 20.3.2.9 |
