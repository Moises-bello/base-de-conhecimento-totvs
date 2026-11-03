---
content_hash: e5bf5df76a878a8069eac4705a6adce1fcfe1f0919250e6686a4928790d9d5af
fetched_at: '2026-06-29T00:08:59.430410+00:00'
page_id: '362453414'
product: rm
source: tdn-rm
title: DEDUANALYTICS-249 DT Gráfico de Frequência no detalhe do aluno com disciplinas
  sem aulas cadastradas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=362453414
version: 3
---

# DETALHES DO ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Retenção de Alunos by Carol |
| **Função:** | Gráficos de notas e frequência |
| **Situação/Requisito:** | Quando a disciplina ainda não possui número de aulas dadas cadastrado, o gráfico é exibido como se o aluno tivesse 100% de faltas. Além disso, quando o nome abreviado  das disciplinas (eixo-x) eram iguais, os valores de notas e faltas eram sobrepostos nestes dois gráficos. |
| **Solução/Implementação:** | Os gráficos de notas e faltas foram ajustados para abreviarem os nomes de disciplinas que começam com os mesmos caracteres pelo meio (e não pelo final, conforme era feito).  O gráfico de frequência foi ajustado para exibir percentual de 0% para as disciplinas que ainda não possuem número de aulas dadas cadastradas. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
