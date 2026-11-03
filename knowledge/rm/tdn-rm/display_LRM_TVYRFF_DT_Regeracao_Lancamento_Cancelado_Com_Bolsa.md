---
content_hash: b70e4cbb0cb90f7bb0c893db35b6d23e0fe01c9a7a0fc7a7576ce68e9d2f4a3c
fetched_at: '2026-06-29T00:08:20.209248+00:00'
page_id: '268571701'
product: rm
source: tdn-rm
title: TVYRFF_DT_Regeracao_Lancamento_Cancelado_Com_Bolsa
type: documentation
url: https://tdn.totvs.com/display/LRM/TVYRFF_DT_Regeracao_Lancamento_Cancelado_Com_Bolsa
version: 109
---

# Regeração de lançamento cancelado

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Regeração de lançamentos |
| **Situação/Requisito:** | Ao regerar um lançamento cancelado que possui bolsa, o sistema emite a mensagem de chave duplicada (Violação de chave primária) em SBOLSALAN |
| **Solução/Implementação:** | Ajuste na regeração de lançamento cancelado para considerar o IDLAN do lançamento que está sendo criado na tabela de bolsas do lançamento (SBOLSALAN) |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | N/A |

divs
