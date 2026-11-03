---
content_hash: 899de4d38c7caa9f71fcb6d207c4db97c9c53f99204c68e777a216d9830fc410
fetched_at: '2026-06-29T00:09:26.501030+00:00'
page_id: '423938305'
product: rm
source: tdn-rm
title: 'Exemplo 4:'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938305
version: 2
---

Uma vez que um item da nota foi distribuído para um patrimônio, o somatório do valor deste item nos patrimônios deve ser igual ao valor de aquisição original / valor base de depreciação original, levando em consideração a quantidade.

Exemplo:

Itens da Nota:

01 Mouse       | Qtd: 2 | Valor Aquisição:10,00 | Valor Base depreciação: 9,00

02 CPU          | Qtd: 2 | Valor Aquisição:900,00 | Valor Base depreciação: 850,00

03 Teclado     | Qtd: 2 | Valor Aquisição:30,00 | Valor Base depreciação: 25,00

Patrimônios Formados:

01 -  COMPUTADO 01 – Valor Aquisição:940,00| Valor Base depreciação: 884,00

01 Mouse       | Qtd:1 | Valor Aquisição:10,00 | Valor Base depreciação: 9,00

02 CPU          | Qtd: 1 | Valor Aquisição:900,00 | Valor Base depreciação: 850,00

03 Teclado     | Qtd: 1 | Valor Aquisição:30,00 | Valor Base depreciação: 25,00

02 -  COMPUTADO 02 – Valor Aquisição:910,00| Valor Base depreciação: 859,00

01 Mouse       | Qtd: 1 | Valor Aquisição:10,00 | Valor Base depreciação: 9,00

02 CPU          | Qtd: 1 | Valor Aquisição:900,00 | Valor Base depreciação: 850,00

Observe que no Computador 02 esta faltando o item teclado, neste caso o sistema irá apresentar erro.
