---
content_hash: 5af4d78a564de7bd92d2ed71aec37a28f0a6ab9e9ccf54e79081a727033a38df
fetched_at: '2026-06-29T00:09:10.495664+00:00'
page_id: '398754329'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-3275 DT Gráfico de Resumo Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=398754329
version: 1
---

# GRÁFICO DE RESUMO FINANCEIRO (SQL SERVER E ORACLE)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | Gráfico de Resumo Financeiro |
| **Situação/Requisito:** | Gráfico não está considerando contratos sem vínculo com matriz aplicada |
| **Solução/Implementação:** | Ajuste na query principal do contrato a fim de considerar os contratos sem matriz aplicada Anteriormente o sistema considerava os lançamentos gerados na data atual como vencidos. Ajuste feito para que a data atual fosse considerada como, a vencer. Lançamentos de bolsa de crédito estavam sendo considerados na soma dos valores do resumo Lançamentos parcialmente baixados foram tratados como lançamentos em aberto pois os mesmos não estavam sendo considerados no relatório |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
