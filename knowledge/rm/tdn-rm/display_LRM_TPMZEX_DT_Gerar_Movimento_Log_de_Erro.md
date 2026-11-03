---
content_hash: b757559e67b0eeef3b5318a72aa756d68d71d4aa7b6ba9af30090dbe7a541912
fetched_at: '2026-06-29T00:08:14.238648+00:00'
page_id: '244444205'
product: rm
source: tdn-rm
title: TPMZEX_DT_Gerar_Movimento_Log_de_Erro
type: documentation
url: https://tdn.totvs.com/display/LRM/TPMZEX_DT_Gerar_Movimento_Log_de_Erro
version: 115
---

# GERAR MOVIMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Gerar Movimento* |
| **Situação/Requisito:** | Ao Gerar Movimento, quando ocorre uma mensagem de erro, não conseguimos identificar o boleto ou aluno. |
| **Solução/Implementação:** | Ao Gerar Movimento, quando ocorrer uma mensagem de erro, será acrescentada a referência do Boleto, para melhor rastreamento do Movimento.  OBS.: Não será possível informar RA e Contrato no log de erros, pois afetaria incorretamente os boletos que utilizam agrupamento. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TVKMZR |
| **Requisito (ISSUE):** | *N/A* |

divs
