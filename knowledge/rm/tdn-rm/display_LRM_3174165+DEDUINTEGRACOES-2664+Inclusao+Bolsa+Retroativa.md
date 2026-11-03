---
content_hash: a5bb08ed5d3ba83d2a2e339944bc2f2e21040fd9c984cecb41dea9be2d7ecbdb
fetched_at: '2026-06-29T00:09:01.755662+00:00'
page_id: '378276095'
product: rm
source: tdn-rm
title: 3174165 DEDUINTEGRACOES-2664 Inclusao Bolsa Retroativa
type: documentation
url: https://tdn.totvs.com/display/LRM/3174165+DEDUINTEGRACOES-2664+Inclusao+Bolsa+Retroativa
version: 1
---

# INCLUSÃO DE BOLSA RETROATIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Incluir / Excluir bolsas retroativas. |
| **Situação/Requisito:** | Ao executar o processo de inclusão de bolsa retroativa o sistema apresenta erro de estouro de date time. |
| **Solução/Implementação:** | No processo de inclusão de bolsa retroativa, para lançamentos baixados parcialmente, ao calcular o valor liquido não era inforamado a data de vencimento, ocasionanto erro ao buscar o dia útil do vencimento. Foi realizado ajuste para que a data de vencimento informada seja a do lançamento original. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 3174165, 3117812 |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
