---
content_hash: 1d0685375bb7c6a61bc96bd98fd313933676d04aac97684ff4b7c6040317667e
fetched_at: '2026-06-29T00:06:00.512705+00:00'
page_id: '196809712'
product: rm
source: tdn-rm
title: TSTUP5_DT_ERRO_NA_GERACAO_DE_CONTABILIZACAO
type: documentation
url: https://tdn.totvs.com/display/LRM/TSTUP5_DT_ERRO_NA_GERACAO_DE_CONTABILIZACAO
version: 7
---

# SIMULAÇÃO DE PARCELAS POR CRÉDITO FINANCEIRO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Simulação de parcelas* |
| **Situação/Requisito:** | *Ao ser consumido o serviço de simulação de parcelas, caso todas as parcelas estejam geradas com todo o valor de créditos financeiros utilizados, o sistema levanta uma exceção, devido o log não estar inicializado. Com isso os processos que consomem esse serviço são impedidos de serem executados.* |
| **Solução/Implementação:** | *Foi realizada otimização do processo de simulação de lançamentos financeiros, de forma que o sistema não consista a existência de parcelas a serem geradas por crédito, caso todos os créditos disponíveis já tenham sido utilizados em parcelas anteriores do mesmo contrato.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A.* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.40* |
