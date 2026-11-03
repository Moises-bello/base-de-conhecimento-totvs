---
content_hash: bd421ec2288c56989e68e77cc8f97864d78204b20ae6af2e5e773f059dbc974a
fetched_at: '2026-06-29T00:06:00.580383+00:00'
page_id: '196811758'
product: rm
source: tdn-rm
title: TSVT58_DT_ERRO_NA_GERACAO_LANCAMENTOS_EM_LOTE
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVT58_DT_ERRO_NA_GERACAO_LANCAMENTOS_EM_LOTE
version: 1
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Assistente de geração de lançamentos* |
| **Situação/Requisito:** | *O processamento de lançamentos foi criado para que fossem processados 500 lançamentos por vez, porém em casos de agrupamento de lançamentos por boleto, pode ocorrer de um novo ciclo iniciar com uma transação em aberto, causando falha na execução do processo e o não processamento dos lançamentos subseqüentes.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de geração de lançamentos em lote de forma a evitar que o processo seja abortado para quando é feito uso de agrupamento de lançamentos financeiros por boleto.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *12.1.7* |
