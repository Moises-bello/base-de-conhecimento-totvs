---
content_hash: 5333c40f206a447d1094c603fcbdf8538ea5913175a6e0445a0e83a33ef23a2b
fetched_at: '2026-07-02T19:24:24.981718+00:00'
page_id: '493634860'
product: protheus
source: tdn-tec
title: Implementação - TMultiGet passa a alterar cores de fundo e texto via SetColor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493634860
version: 1
---

Implementação - TMultiGet passa a alterar cores de fundo e texto via SetColor

|  |  |
| --- | --- |
| Situação | O método SetColor() não surtia efeito quando utilizado no componente TMultiGet. |
| Ocorrência | O componente TMultiGet ignorava os valores passados através do método SetColor(). |
| Implementação | O método SetColor() foi implementado para que seja possível especificar uma cor de fundo (background) e uma cor para o texto (foreground) no componente TMultiGet. |
| Informações adicionais | * Referente à ocorrência: MTEC-2503 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.8 |
