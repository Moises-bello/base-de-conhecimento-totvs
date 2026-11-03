---
content_hash: 29069a10d1d925c95f2d9f36f68802b59ac7e566aaada06036f6764d2963704d
fetched_at: '2026-06-29T00:06:01.144732+00:00'
page_id: '198936941'
product: rm
source: tdn-rm
title: TSWVDM_DT_Contabilizar_Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TSWVDM_DT_Contabilizar_Movimento
version: 3
---

# Contabilizar Movimento

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Construção e Projetos** |
| **Módulo:** | *Gestão de Compras, estoque e faturamento* |
| **Função:** | *Contabilizar Movimento* |
| **Situação/Requisito:** | *O processo responsável por contabilizar o movimento não refaz a contabilidade caso a mesma já tenha sido feita.* |
| **Solução/Implementação:** | Ajuste realizado no processo responsável por contabilizar o movimento, os lançamentos contábeis não estavam sendo excluídos durante a execução do processo, ou seja, para  movimentos que já haviam sido contabilizados o processo não estava sendo executado. A partir de agora, caso existam lançamentos contábeis, o processo realiza a exclusão e logo  em seguida gera as partidas. |
| **Conversores e Parâmetros:** | *Não se Aplica* |
| **Chamados relacionados:** | *Não possui chamados associados* |
| **Requisito (ISSUE):** | *Não se Aplica* |
| **Versões/Release:** | *12.1.7* |
