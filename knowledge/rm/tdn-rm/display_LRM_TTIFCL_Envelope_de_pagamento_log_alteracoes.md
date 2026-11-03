---
content_hash: 9047b6eff70091e2c02787b0ffd66ad37b2d1ece1c8ae206145e1aea1f13fa3c
fetched_at: '2026-06-29T00:06:10.540600+00:00'
page_id: '203764202'
product: rm
source: tdn-rm
title: TTIFCL_Envelope_de_pagamento_log_alteracoes
type: documentation
url: https://tdn.totvs.com/display/LRM/TTIFCL_Envelope_de_pagamento_log_alteracoes
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
| **Chamados relacionados:** | *TTIFCL.* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8.* |
