---
content_hash: c165e22fb4e62794704c1b8b49bc19f17b2776a3874940964b30e65964f99b1e
fetched_at: '2026-06-29T00:08:25.665731+00:00'
page_id: '270921748'
product: rm
source: tdn-rm
title: 354390 MEDU-1953 DT Pesquisas Realizadas Gestao de Pessoa Divisao Zero
type: documentation
url: https://tdn.totvs.com/display/LRM/354390+MEDU-1953+DT+Pesquisas+Realizadas+Gestao+de+Pessoa+Divisao+Zero
version: 110
---

# PESQUISAS REALIZADAS - GESTÃO DE PESSOAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs avaliação e pesquisa / *TOTVS Gestão de Pessoas** |
| **Função:** | *Pesquisas realizadas - visão pelo TOTVS Gestão de Pessoas* |
| **Situação/Requisito:** | *Foi identificado que ao visualizar as provas do tipo pesquisa de opinião realizadas de um funcionário pelo TOTVS Gestão de Pessoas, caso uma avaliação tenha todas as questões com peso 0, o sistema retorna um erro na visão de divisão por zero e não carrega a visão.* |
| **Solução/Implementação:** | *Foi identificado que a situação ocorre pois é feito uma tentativa de divisão do total do funcionário pelo valor da avaliação para calcular o desempenho, apesar de não ser visível e ser uma avaliação de pesquisa de opinião, mns como o somatório dos pesos é zero, o sistema não permite divisão por zero, assim retornando o erro. Foi feito um ajuste na consulta sql da visão para que identifique o valor zero no divisor do rendimento do funcionário, se for zero não efetua a divisão assim evitando o erro.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | **N/A** |
| **Requisito (ISSUE):** | *N/A* |

divs
