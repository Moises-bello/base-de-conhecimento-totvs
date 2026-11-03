---
content_hash: 4f71251822fabbbd752d23d5d8854cf1c8aa3343c60b09a629eaafcb3e269db6
fetched_at: '2026-06-29T00:08:25.080436+00:00'
page_id: '270912036'
product: rm
source: tdn-rm
title: MRH-3507_DT_Pensao_PLR_Informada_Base_IRRF
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-3507_DT_Pensao_PLR_Informada_Base_IRRF
version: 110
---

# PENSÃO ALIMENTÍCIA DE PLR INFORMADA NÃO DEDUZ DA BASE DE IRRF PLR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Pensão Alimentícia* |
| **Situação/Requisito:** | *Quando o funcionário tem o desconto de Pensão de PLR informada (CC 321), o valor não é deduzido da Base de IRRF PL (CC 127), mas está sendo deduzido na Base do IRRF folha (CC 04).* |
| **Solução/Implementação:** | *Como não existe parâmetro específico para a incidência de IRRF PL, tratar pelo código de cálculo 321 para que, caso o evento esteja marcado com a incidência de IRRF Folha, o considere na Base de IRRF PL.*  *Assim como já é feito com o CC 121.* |
| **Chamados relacionados:** | MRH-3507 |
| **Requisito (ISSUE):** | MRH-3507 |

divs
