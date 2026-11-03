---
content_hash: c15b5e2c3f496e661363fd8607c1884afcefcd86085ddb4a2822f43f6faf8650
fetched_at: '2026-07-02T19:24:18.613478+00:00'
page_id: '219120940'
product: protheus
source: tdn-tec
title: TFont:nHeight
type: documentation
url: https://tdn.totvs.com/display/tec/TFont%3AnHeight
version: 2
---

TFont:nHeight

Indica o tamanho da fonte.

A unidade é pixels.

Se o valor passado for maior que zero, passará por um ajuste de \*0.8.   
Se for menor que zero, o valor utilizado será o seu inverso aditivo.

| Tipo | Valor Padrão | Somente Leitura |
| --- | --- | --- |
| numérico | N/A | N |

## Exemplos

cppEclipseExemplo 1true resulta em um tamanho real de 12,8px
oTFont:nHeight := -16 // 16 \* -1 --> resulta em um tamanho real de 16px
]]>
