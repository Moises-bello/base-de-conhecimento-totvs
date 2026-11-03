---
content_hash: b52ea2f01cd47bac1d5f15b4ad771c0bc3366d4b3e7e144d4ba3e160f74e06cd
fetched_at: '2026-06-29T00:06:29.658367+00:00'
page_id: '234614931'
product: rm
source: tdn-rm
title: TUJ683_DT_Exibicao_Desconto_Multa_Incorreto
type: documentation
url: https://tdn.totvs.com/display/LRM/TUJ683_DT_Exibicao_Desconto_Multa_Incorreto
version: 116
---

# MOVIMENTAÇÕES - DEVOLUÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Movimentação - Devolução* |
| **Situação/Requisito:** | *Ao realizar uma devolução não identificada que tenha valor de multa e permita desconto da multa, ao inserir o desconto o sistema altera o valor do empréstimo como se o desconto estivesse sendo aplicado duas vezes, porém o lançamento é gerado corretamente.* |
| **Solução/Implementação:** | *Foi identificado que o sistema não estava realizando o cálculo da exibição da multa e do total do empréstimo, após ajuste os valores passaram a ser exibidos corretamente, ressaltando que esta situação só ocorre quando é uma devolução não identificada.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
