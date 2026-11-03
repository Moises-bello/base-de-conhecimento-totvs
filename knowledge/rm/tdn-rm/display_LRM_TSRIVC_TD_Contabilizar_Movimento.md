---
content_hash: eed54d10c8916945becdbc5e3d9e8ed51df0c47cabe0164203be8c5f893052da
fetched_at: '2026-06-29T00:06:01.043327+00:00'
page_id: '198935184'
product: rm
source: tdn-rm
title: TSRIVC_TD_Contabilizar_Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TSRIVC_TD_Contabilizar_Movimento
version: 2
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
| **Versões/Release:** | *11.82.40* |
