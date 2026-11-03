---
content_hash: cb7a555438694d6a8c24c7d5840b71ed8900a4cf2c2da3b5bef98ba63074064a
fetched_at: '2026-07-02T19:24:24.978556+00:00'
page_id: '493634842'
product: protheus
source: tdn-tec
title: Implementação - TMultiGet passa a alterar as cores de fundo e do texto via
  SetColor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493634842
version: 1
---

Implementação - TMultiGet passa a alterar as cores de fundo e do texto via SetColor

|  |  |
| --- | --- |
| Situação | O método SetColor() não surtia efeito quando utilizado no componente TMultiGet. |
| Ocorrência | O componente TMultiGet ignorava os valores passados através do método SetColor(). |
| Implementação | O método SetColor() foi implementado para que seja possível especificar uma cor de fundo (background) e uma cor para o texto (foreground) no componente TMultiGet. |
| Informações adicionais | * Referente à ocorrência: MTEC-2503 * Disponível em builds iguais ou superiores a 13.2.3.41 |
