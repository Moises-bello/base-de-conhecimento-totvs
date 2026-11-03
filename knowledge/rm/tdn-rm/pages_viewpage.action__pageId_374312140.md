---
content_hash: bead5e13d118ab552076b7633121f3cddc8c196d39a6e521323ab280620c1fd8
fetched_at: '2026-06-29T00:09:01.634867+00:00'
page_id: '374312140'
product: rm
source: tdn-rm
title: 3135297 DEDUINTEGRACOES-2644 DT Geração de Lançamentos por Crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=374312140
version: 85
---

# GERAÇÃO DE LANÇAMENTOS POR CRÉDITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos financeiros |
| **Situação/Requisito:** | Processo de geração de lançamentos estava calculando valor errado quando existiam disciplinas com situação de matricula parametrizadas com a opção "Abater valor da disciplina somente para parcelas com vencimento igual ou posterior a data de alteração da situação de matricula.    O problema ocorria quando eram processados mais de um aluno com cancelamento de disciplinas e datas de cancelamentos distintas o que fazia com que os demais alunos (exceto o primeiro) considerasses a data de cancelamento da disciplina do primeiro aluno. |
| **Solução/Implementação:** | Limpeza das datas de processamento antes de processar os cancelamentos de disciplinas a fim de que o cálculo do valor da parcela para disciplinas canceladas seja processado corretamente por aluno. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
