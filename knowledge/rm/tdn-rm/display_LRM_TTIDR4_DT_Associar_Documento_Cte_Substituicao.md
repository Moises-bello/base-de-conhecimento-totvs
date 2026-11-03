---
content_hash: c9bc4807e0cd5728cdf1e06ed716f4e5c2a04dea8f442f6a20d7ddc2639cc70b
fetched_at: '2026-06-29T00:06:11.394632+00:00'
page_id: '203768703'
product: rm
source: tdn-rm
title: TTIDR4_DT_Associar_Documento_Cte_Substituicao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIDR4_DT_Associar_Documento_Cte_Substituicao
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
| **Versões/Release:** | *12.1.8* |
