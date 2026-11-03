---
content_hash: 87528257fc8883a4afc691507689aaf7cffc9806fa62d6b6ee83cf56c1e5c37f
fetched_at: '2026-06-29T00:06:28.173803+00:00'
page_id: '233750337'
product: rm
source: tdn-rm
title: TUKMV3_DT_Processo_Inclusao_Exclusao_Bolsa_Retroativa
type: documentation
url: https://tdn.totvs.com/display/LRM/TUKMV3_DT_Processo_Inclusao_Exclusao_Bolsa_Retroativa
version: 118
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Processo de inclusão/exclusão de bolsa retroativa* |
| **Situação/Requisito:** | No assistente de inclusão de bolsa retroativa, na tela de seleção de bolsas, foi incluído 3 serviços com a mesma bolsa, em seguida foi selecionado o segundo serviço mandando excluir, porem o sistema esta excluindo sempre o primeiro registro. |
| **Solução/Implementação:** | A funcionalidade de exclusão não estava levando em consideração o código do serviço selecionado, desta forma o primeiro registro contendo a bolsa selecionada era sempre o excluído. |
| **Conversores e Parâmetros:** | *NA* |
| **Chamados relacionados:** | *NA* |
| **Requisito (ISSUE):** | NA |

divs
