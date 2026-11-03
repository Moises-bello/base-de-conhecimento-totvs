---
content_hash: dc277b7284a41e2917595ff0d75afea851269573614741051fbd0d2456748285
fetched_at: '2026-06-29T00:08:24.736040+00:00'
page_id: '270902183'
product: rm
source: tdn-rm
title: MEDU-1797_DT_Aproveitamento_Conta_Corrente_Aluno_Resp_Financeiro_Diferente
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-1797_DT_Aproveitamento_Conta_Corrente_Aluno_Resp_Financeiro_Diferente
version: 111
---

# Aproveitar valores em conta corrente

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Processo de Aproveitamento valores em conta corrente |
| **Situação/Requisito:** | Ao executar o processo de aproveitamento de valores da conta corrente do aluno o sistema estava gerando a parcela e o valor do lançamento a pagar zerado e não estava aproveitando o valor selecionado.  Identificamos que esta situação estava ocorrendo em função do responsável financeiro do aluno, pois o mesmo estava diferente do responsável financeiro que constava no lançamento de débito da conta corrente. |
| **Solução/Implementação:** | Melhoria no processo de aproveitamento de conta corrente do aluno para que o sistema sempre considere o responsável do débito/crédito que está sendo aproveitado, independente se o responsável financeiro do aluno for diferente. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | MEDU-1797 |
| **Requisito (informe o requisito relacionado):** |  |

divs
