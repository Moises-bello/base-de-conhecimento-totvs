---
content_hash: 2ecd7a646ab36a320cf56f3efe3a8f5c52c34e7f2ceaf2a23c13aacfde808b94
fetched_at: '2026-06-29T00:06:10.431339+00:00'
page_id: '203763066'
product: rm
source: tdn-rm
title: TTEIJE_DT_Associar_Documento_Cte_Substituicao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEIJE_DT_Associar_Documento_Cte_Substituicao
version: 1
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento.* |
| **Função:** | *Associação* *de documento para CTE de substituição.* |
| **Situação/Requisito:** | Ao realizar a associação de um documento à um CTE de substituição a chave de acesso não estava sendo preenchida. |
| **Solução/Implementação:** | * Para movimentos de CT-e Substituição e Cliente contribuinte ICMS a chave de acesso do movimento de anulação será o campo TMOV.CHAVEACESSONFE. * Para Cliente não contribuintes ICMS a chave de acesso será TCTE.CHAVEACESSO. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.41* |
