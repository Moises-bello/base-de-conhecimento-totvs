---
content_hash: 0a7bc8b5fa8a32bdf8b68478887569800b0695bb1b30e35d1df89611b2777115
fetched_at: '2026-06-29T00:06:21.672515+00:00'
page_id: '223175914'
product: rm
source: tdn-rm
title: TTWNCE_DT_Estorno_Previdencia_Privada_CC203_DIRF
type: documentation
url: https://tdn.totvs.com/display/LRM/TTWNCE_DT_Estorno_Previdencia_Privada_CC203_DIRF
version: 122
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | Ao gerar a Dirf em arquivo, Informe de rendimentos e Dirf para conferência no caso de funcionário com evento de Estorno de Previdência Privada (CC203), sistema está gerando com valores negativos quando não há evento de Previdência Privada ou o valor do desconto é menor que o valor de estorno. |
| **Solução/Implementação:** | *Alterado o cálculo da previdência privada para zerar o valor caso seja negativo. O valor vai continuar negativo apenas na geração da DIRF para Conferência.* |
| **Chamados relacionados:** | *TTWNCE* |
| **Versões/Release:** | *11.82.43* |

divs
