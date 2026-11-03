---
content_hash: c59932305a8c328f527bffac8ab43892ced5ea1ac1036bed2030302d5213e1f5
fetched_at: '2026-06-29T00:09:54.411653+00:00'
page_id: '444617432'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-3988 Ajuste cálculo número de crédito buscando da matriz com
  disciplina equivalente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=444617432
version: 1
---

# Geração de Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de lançamento |
| **Situação/Requisito:** | Ao executar o processo de geração de lançamento em lote (vários lançamentos simultâneos), o cálculo por crédito de um determinado lançamento estava apresentando uma não conformidade, e se executasse a geração de lançamento individualmente o cálculo ficava correto.    A não conformidade é apresentada somente se o sistema estiver paramatrizado "Usar número de créditos financeiro da matriz currilar do aluno", para disciplinas equivalentes quando a mesma disciplina é cursada por vários alunos de matriz curricula distinta. |
| **Solução/Implementação:** | Ajustamos a não conformidade para que o número de crédito considerado seja conforme a matriz curricular do aluno ao indentificar a disciplina equivalente. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
| **Documento de Referência:** |  |
| **Pacote:** |  |
