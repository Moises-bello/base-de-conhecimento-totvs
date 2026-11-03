---
content_hash: cc2f368db43349ab6fceb05fcf6e115bcca1c9ff7f864fb175c0a01a59a83506
fetched_at: '2026-06-29T00:09:07.610884+00:00'
page_id: '384581271'
product: rm
source: tdn-rm
title: 3325641 DEDUINTEGRACOES-2920 Inclusao Bolsa Retroativa
type: documentation
url: https://tdn.totvs.com/display/LRM/3325641+DEDUINTEGRACOES-2920+Inclusao+Bolsa+Retroativa
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
| **Solução/Implementação:** | No processo de inclusão de bolsa retroativa, para lançamentos baixados parcialmente ou totalmente baixados, ao calcular o valor liquido não era inforamado a data de vencimento, ocasionanto erro ao buscar o dia útil do vencimento. Foi realizado ajuste para que a data de vencimento informada seja a do lançamento original. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
