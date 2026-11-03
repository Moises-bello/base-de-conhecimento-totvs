---
content_hash: 3e883fbe5e8795bb2cbbda66e8931c79d559158a310e212df3b85f60cfef24fe
fetched_at: '2026-07-02T19:24:23.266879+00:00'
page_id: '301184963'
product: protheus
source: tdn-tec
title: Correção - Função SaveAsHTML da classe TMSPrinter não exporta imagens.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301184963
version: 2
---

Correção - Função SaveAsHTML da classe TMSPrinter não exporta imagens.

|  |  |
| --- | --- |
| Situação | Ao gerar um documento através da TMSPrinter e utilizar a função SaveAsHTML, caso existam imagens no documento (incluídas por meio da função TMSPrinter:SayBitmap()), elas não são exportadas para o HTML. |
| Ocorrência | Necessidade de gerar um documento HTML com imagens através da classe TMSPrinter. |
| Correção | A função TMSPrinter:SaveAsHTML recebeu um ajuste para incluir as imagens no documento HTML. Além de incluir a referência das imagens no documento, o arquivo das imagens também é copiado para o mesmo diretório do arquivo HTML. |
| Informações adicionais | * Referente à ocorrência: MTEC-370 * Disponíveis em builds iguais ou superiores a [13.1.3.21](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.21) e [13.2.3.21](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.21). |
