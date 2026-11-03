---
content_hash: 34ef1df82d3965d6f6bb3630a3d91ba2de65c94473c2fe644f7d68686c057ca5
fetched_at: '2026-06-29T00:06:27.872499+00:00'
page_id: '233736884'
product: rm
source: tdn-rm
title: TTYUWM_DT_Liberacao_Competencia_Valida_Ferias_FuncTransferido
type: documentation
url: https://tdn.totvs.com/display/LRM/TTYUWM_DT_Liberacao_Competencia_Valida_Ferias_FuncTransferido
version: 3
---

# LIBERAÇÃO DA COMPETÊNCIA ESTÁ VALIDANDO FÉRIAS DE FUNCIONÁRIO TRANSFERIDO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Liberação da Competência* |
| **Situação/Requisito:** | *Não está sendo permitido liberar a competência quando existe funcionário transferido, que teve férias no mês, mas não levou a movimentação atual para a nova chapa.*  *Está acusando erro de que "Existem ferias cadastradas que não estão lançadas/finalizadas dentro da competencia" para a nova chapa, que será ativada somente na competência seguinte.* |
| **Solução/Implementação:** | *Ajuste no processo de Liberação da Competência para não considerar a nova chapa transferida, na validação de férias não lançadas/finalizadas no mês.* |
| **Chamados   relacionados:** | *TTYUWM, TUJW58* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
