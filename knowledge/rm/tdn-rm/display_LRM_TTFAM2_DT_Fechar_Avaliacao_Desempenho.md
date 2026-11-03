---
content_hash: 0e50506dcfe4819e911e1cdcb53588bd028cc1ce32546ee3451846dbc7a11849
fetched_at: '2026-06-29T00:06:09.296480+00:00'
page_id: '203752452'
product: rm
source: tdn-rm
title: TTFAM2_DT_Fechar_Avaliacao_Desempenho
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFAM2_DT_Fechar_Avaliacao_Desempenho
version: 2
---

# AVALIAÇÃO DE DESEMPENHO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Contrução e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Função:** | *Avaliação de Desempenho* |
| **Situação/Requisito:** | *Ao fechar a avaliação de desempenho o sistema apresenta a mensagem de erro abaixo:* *O índice estava fora dos limites da matriz.* |
| **Solução/Implementação:** | *O erro ocorria pois não havia escala cadastrada como ponto de corte. Como é necessário que haja um ponto de corte, o sistema passa a não permitir a exclusão de uma escala que seja ponto de corte. Para que essa escala seja excluída, é necessário que antes seja criada uma nova escala que seja ponto de corte.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTFAM2* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
