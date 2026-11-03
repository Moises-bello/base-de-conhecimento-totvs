---
content_hash: 0ba50d303fc27cd02a47a04973fdb44ce0ea52f41a79411ed8fd4550e81014b3
fetched_at: '2026-06-29T00:06:21.675756+00:00'
page_id: '223176082'
product: rm
source: tdn-rm
title: DT_TTWXG8_Estorno_Previdencia_Privada_CC203_DIRF
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_TTWXG8_Estorno_Previdencia_Privada_CC203_DIRF
version: 1
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
| **Chamados relacionados:** | *TTWXG8* |
| **Versões/Release:** | *12.1.9* |

divs
