---
content_hash: 61c77864bb4cfef33ab14b8e35b185ba2258b0718d7200c26441998dba1a4ffa
fetched_at: '2026-06-29T00:06:09.323605+00:00'
page_id: '203752912'
product: rm
source: tdn-rm
title: TTGSBN_DT_Fechar_Avaliacao_Desempenho
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGSBN_DT_Fechar_Avaliacao_Desempenho
version: 1
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
| **Chamados relacionados:** | *TTGSBN* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
