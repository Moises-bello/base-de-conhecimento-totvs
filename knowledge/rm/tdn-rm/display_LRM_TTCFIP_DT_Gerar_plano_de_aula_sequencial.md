---
content_hash: 89219a2a8815c83535c2d7f50b3cd5d44bbe9d35709b67b85eace4f6cd5c6223
fetched_at: '2026-06-29T00:06:05.454860+00:00'
page_id: '201722378'
product: rm
source: tdn-rm
title: TTCFIP_DT_Gerar_plano_de_aula_sequencial
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCFIP_DT_Gerar_plano_de_aula_sequencial
version: 1
---

# GERAR PLANO DE AULA SEQUENCIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Gerar plano de aula sequencial* |
| **Situação/Requisito:** | *Ao gerar planos de aula sequenciais para as disciplinas de uma respectiva turma X, utilizando a rotina Gerar plano de aula sequencial, localizada em Processos > Gerar plano de aula sequencial, ela cadastra os planos de aula, porém a data inicial e final das disciplinas fica incorreta, e também não são gerados todos os planos de aula. (A duração de cada aula é 50 minutos). Existem também datas de início posterior à data de fim, na turma e nos horários da turma..* |
| **Solução/Implementação:** | *Ajuste no contador de dias úteis, o mesmo estava sendo zerado toda vez que o processo passava por uma disciplina no qual seria gerado o plano de aula sequencial.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.7* |
