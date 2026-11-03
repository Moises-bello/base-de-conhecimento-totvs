---
content_hash: 0312acf6f97ab596d1adde7b0503fb297b4ce3948930b37e4e5a9d120a0407c2
fetched_at: '2026-06-29T00:09:01.800840+00:00'
page_id: '378279930'
product: rm
source: tdn-rm
title: 3128614 DEDUINTEGRACOES-2633 DT valor incorreto ao gerar lançamento com agrupamento
  de equivalências
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=378279930
version: 82
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional. |
| **Função:** | Geração de lançamentos |
| **Situação/Requisito:** | Ao gerar lançamentos financeiros, caso a equivalência fora da grade do aluno seja de duas ou mais disciplinas e o sistema esteja parametrizado para considerar o valor do crédito da grade do aluno, a disciplina da grade do aluno está sendo processada n vezes. |
| **Solução/Implementação:** | Foi realizada otimização do processo de geração de lançamentos, de forma que o sistema, durante a rotina de cálculo de créditos financeiros, quando existirem agrupamento de disciplinas equivalentes e o sistema estiver parametrizado para buscar o valor do crédito da matriz curricular do aluno, consiga retornar o valor correto do crédito. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
