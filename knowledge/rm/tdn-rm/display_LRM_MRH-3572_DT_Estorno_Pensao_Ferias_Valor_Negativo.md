---
content_hash: 9c2bdc5f78b57b62a8b10f7f0581814655c343cfbebf944ff62baf310a715724
fetched_at: '2026-06-29T00:08:25.524297+00:00'
page_id: '270916884'
product: rm
source: tdn-rm
title: MRH-3572_DT_Estorno_Pensao_Ferias_Valor_Negativo
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-3572_DT_Estorno_Pensao_Ferias_Valor_Negativo
version: 109
---

# ESTORNO DE PENSÃO DE FERIAS COM VALOR NEGATIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença de Férias* |
| **Situação/Requisito:** | *No cálculo da diferença de férias, quando o funcionário tem um estorno de pensão alimentícia de férias, está lançando valor negativo no evento com CC 201.* |
| **Solução/Implementação:** | *Ajuste no cálculo do estorno de pensão alimentícia de férias para verificar se o CC 201 está cadastrado como provento ou desconto, e lançar valor negativo somente se for desconto.* |
| **Chamados relacionados:** | MRH-3572 |
| **Requisito (ISSUE):** | MRH-3572 |

divs
