---
content_hash: 44c1ad58c8be9a646f79fc37bea3af02005c6359aba3ea53210966d08c017065
fetched_at: '2026-06-29T00:08:16.185312+00:00'
page_id: '244928329'
product: rm
source: tdn-rm
title: TVOWN0_DT_Recursos_Nao_Exclui
type: documentation
url: https://tdn.totvs.com/display/LRM/TVOWN0_DT_Recursos_Nao_Exclui
version: 112
---

# RECURSOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Recursos* |
| **Situação/Requisito:** | *Ao tentar excluir um recurso existente, o sistema não exclui e retorna uma mensagem não tratada.* |
| **Solução/Implementação:** | **Foi identificado que ao tentar excluir um recurso que é utilizado no processo seletivo, o sistema não permite pois existe um outro local referenciando este recurso e mostra a mensagem não tratada, foi feito o tratamento da mensagem alertando que não é possível excluir pois o registro é utilizado em outro local.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
