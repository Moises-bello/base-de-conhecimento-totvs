---
content_hash: f2ddc49df15be77bf0bb0c610eedf6b7143a1ae1c54deac9d18c3ef1001b87d9
fetched_at: '2026-06-29T00:06:00.562043+00:00'
page_id: '196811544'
product: rm
source: tdn-rm
title: TSVWXH_DT_ERRO_NA_GERACAO_DE_CONTABILIZACAO
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVWXH_DT_ERRO_NA_GERACAO_DE_CONTABILIZACAO
version: 2
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
| **Versões/Release:** | *12.1.7* |
