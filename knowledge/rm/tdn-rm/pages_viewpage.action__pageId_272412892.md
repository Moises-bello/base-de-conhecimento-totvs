---
content_hash: 4beafd3f30125953f4720119c5aeec60c1749759cfcfd9dc0b987b1496d47f2b
fetched_at: '2026-06-29T00:08:30.228626+00:00'
page_id: '272412892'
product: rm
source: tdn-rm
title: 648695 MEDU-3204 DT Geração de Plano de Aula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272412892
version: 111
---

# GERAÇÃO DE PLANO DE AULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Geração de Plano de Aula* |
| **Situação/Requisito:** | *Erro na geração do plano de aula devido a quantidade de caracteres do campo ‘locacao’. Na tabela SHORARIOTURMA o campo possui 60 caracteres e na SPLANOAULA possui 50.* |
| **Solução/Implementação:** | *Aumento dos campos LOCACAO de 50 para 60 da tabela SPLANOAULA, LOCACAOATUAL de 50 para 60 da tabela SLOGPLANOAULA e LOCACAOANTERIOR de 50 para 60 da tabela SLOGPLANOAULA.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
