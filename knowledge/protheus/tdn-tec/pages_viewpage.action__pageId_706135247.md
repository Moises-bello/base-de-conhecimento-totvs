---
content_hash: 7970337533eba918785b2396f6dc4ab30832331db4c205640e8f481dc549ddfd
fetched_at: '2026-07-02T19:24:28.008975+00:00'
page_id: '706135247'
product: protheus
source: tdn-tec
title: Correção - TWebEngine não imprime com método window.print() - v20.3.1.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=706135247
version: 1
---

Correção - TWebEngine não imprime com método window.print()

|  |  |
| --- | --- |
| Situação | A página carregada através do componente TWebEngine não executa a impressão ao invocar o método window.print(). |
| Ocorrência | O componente TWebEngine não imprime com window.print() |
| Correção | Uma correção foi aplicada no componente TWebEngine para que a página consiga disparar o processo de impressão após um window.print(). |
| Informações adicionais | * A impressão será sempre da página inteira do WebEngine mesmo quando o método window.print() for invocado de dentro de um iframe. * Referente à ocorrência: DTCLIENT01-3586 * Disponível em builds iguais ou superiores a 20.3.0.5 e 20.3.1.0 |
