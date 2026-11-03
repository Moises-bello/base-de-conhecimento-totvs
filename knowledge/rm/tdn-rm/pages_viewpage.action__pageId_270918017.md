---
content_hash: a8cc37b7b93f17a3432c4f65cb10400bdee90eeab2886a6646aee0071183d383
fetched_at: '2026-06-29T00:08:25.545327+00:00'
page_id: '270918017'
product: rm
source: tdn-rm
title: MEDU-1881 DT Simulação de Parcela Matricula Online Disciplina Equivalente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270918017
version: 110
---

# Simulação de Parcela - Matricula Online

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Simulação de Parcela |
| **Situação/Requisito:** | Quando marcamos o parâmetro ‘Usar valor do crédito financeiro da matriz curricular do aluno’,  o sistema está sempre considerando o valor do crédito da disciplina equivalente, porem na simulação do portal o sistema esta considerando o valor da matriz aplicada do curso do aluno.  Identificamos que este cenário ocorre somente quando temos uma disciplina isolada cadastrada na "turma disciplina" sem matriz aplicada e depois cadastramos esta disciplina como equivalente de uma disciplina da grade do aluno. |
| **Solução/Implementação:** | Ajuste no recurso de simulação de parcela disponível no portal através da matricula online com objetivo de padronizar o comportamento com a geração de lançamento financeiro, pois no cálculo deve considerar o valor do crédito definido na turma/disciplina da disciplina equivalente quando a mesma não tem nenhuma matriz aplicada e não faz parte da matriz aplicada do curso do aluno |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | MEDU-1881 |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
