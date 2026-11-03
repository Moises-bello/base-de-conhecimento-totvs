---
content_hash: 5ad5ca58bb709157b5830901b3dafcb7887c531ff1d4ea224ed2577c17b37a29
fetched_at: '2026-06-29T00:08:20.652984+00:00'
page_id: '268582547'
product: rm
source: tdn-rm
title: TWARGZ_DT_Agendamento_Recurso_Consumindo_Todos_Mesmo_Horario
type: documentation
url: https://tdn.totvs.com/display/LRM/TWARGZ_DT_Agendamento_Recurso_Consumindo_Todos_Mesmo_Horario
version: 117
---

# PROCESSO SELETIVO - INSCRIÇÃO DE CANDIDATOS - AGENDAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Processo seletivo - inscrição de candidatos - agendamento* |
| **Situação/Requisito:** | *Ao definir uma "atividade agendada" no momento da inclusão de um candidato em um processo seletivo que tenha mais de um recurso por horário o sistema estava agendado o mesmo candidato para todo os recursos do respectivo horário.* |
| **Solução/Implementação:** | *Foi alterado o método que aloca os recursos disponíveis para aquele horário para que agende somente para o primeiro recurso disponível, mantendo os demais recursos ainda disponíveis.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
