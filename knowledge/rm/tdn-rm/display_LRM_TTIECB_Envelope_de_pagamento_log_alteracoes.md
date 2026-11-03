---
content_hash: 074f1521db249b8edf87c2e738003eef5691fe310c6d6ca0b2f34aa6913d232c
fetched_at: '2026-06-29T00:06:10.476002+00:00'
page_id: '203763374'
product: rm
source: tdn-rm
title: TTIECB_Envelope_de_pagamento_log_alteracoes
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIECB_Envelope_de_pagamento_log_alteracoes
version: 1
---

# ENVELOPE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *Folha de Pagamento.* |
| **Função:** | *Envelope.* |
| **Situação/Requisito:** | *Ao carregar o envelope de pagamento do funcionário em base oracle, apresentava um erro de sentença SQL.* |
| **Solução/Implementação:** | *A sentença SQL que apresentava o erro devido a um tratamento que a LIB realiza quando se tem a função CASE no SELECT foi alterada para não causar erro.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTIECB.* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41.* |
