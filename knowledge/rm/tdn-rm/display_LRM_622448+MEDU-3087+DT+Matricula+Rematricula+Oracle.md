---
content_hash: d3bbfc38034a993bafaf6727fdbff3f00ce7648079d80956a4b09d1eefbe4212
fetched_at: '2026-06-29T00:08:29.762909+00:00'
page_id: '272164242'
product: rm
source: tdn-rm
title: 622448 MEDU-3087 DT Matricula Rematricula Oracle
type: documentation
url: https://tdn.totvs.com/display/LRM/622448+MEDU-3087+DT+Matricula+Rematricula+Oracle
version: 118
---

# MATRÍCULA / REMATRÍCULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Matrícula / Rematrícula* |
| **Situação/Requisito:** | *Foi identificado que ao efetuar uma matrícula ou rematrícula o sistema retorna um erro informando que a consulta oracle não foi fechada corretamente.* |
| **Solução/Implementação:** | *Foi identificado que o erro era causado por uma espaço entre o 'parênteses' "(" com espaço no termo "NOLOCK" da consulta "( NOLOCK)", foi feito o ajuste e o erro não ocorreu novamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
