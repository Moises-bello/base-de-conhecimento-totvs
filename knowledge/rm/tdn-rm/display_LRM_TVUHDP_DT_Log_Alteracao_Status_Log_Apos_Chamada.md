---
content_hash: eb3ee4400f620814afbe9f5df5741c68db14fd4c4f472a6a56699d6dc4b41c47
fetched_at: '2026-06-29T00:08:18.911188+00:00'
page_id: '266976670'
product: rm
source: tdn-rm
title: TVUHDP_DT_Log_Alteracao_Status_Log_Apos_Chamada
type: documentation
url: https://tdn.totvs.com/display/LRM/TVUHDP_DT_Log_Alteracao_Status_Log_Apos_Chamada
version: 111
---

# LOG DE ALTERAÇÃO DE STATUS DE CLASSIFICAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Log de de alteração de status de classificação* |
| **Situação/Requisito:** | *Ao utilizar a classificação manual de candidatos para um processo seletivo que esteja configurado para gerar log de alteração de status de classificação, é gerado um item de log para cada candidato todas as vezes que o processo é executado, independente se o candidato não teve alguma alteração no seu status (Status, classificação ou pontuação), assim, por exemplo um candidato já matriculado no educacional após a chamada de aprovados, ao executar o processo de classificação, é gerado um novo item no log de status para este candidato, sendo que o mesmo não teve nenhuma alteração e não deve ter por já estar matriculado.* |
| **Solução/Implementação:** | *Foi feito uma alteração no processo de geração de log para que só gere itens de log quando o candidato tiver alguma alteração no seu status de classificação (status, classificação ou pontuação), assim, o processo poderá ser executado várias vezes, gerando itens de log somente para os candidatos que de fato tiveram o status alterado.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | **N/A** |
| **Requisito (ISSUE):** | *N/A* |

divs
