---
content_hash: 5f6bd97d63823f08a41ccbd19d9fa2c05056c530212f7947f4bce8dc84143e0e
fetched_at: '2026-07-02T19:24:20.492717+00:00'
page_id: '252510305'
product: protheus
source: tdn-tec
title: Problema com cTooltip em notebook com touch (2.3.5)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=252510305
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

Problema com cTooltip em notebook com touch

|  |  |
| --- | --- |
| Ocorrência | Ao acessar o SmartClient HTML através de notebook com touch, ao posicionar o mouse em cima de um campo que possuía a propriedade cTooltip o texto era apresentado, porém tirando o mouse de cima deste campo, o texto continuava aparecendo. |
| Correção | Corrigida a propriedade cTooltip para quando o mouse sair de cima do campo o texto não ser apresentado. |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: SCHTML-462 * Disponível em builds superiores a 7.00.131227A - 2.3.5 |
