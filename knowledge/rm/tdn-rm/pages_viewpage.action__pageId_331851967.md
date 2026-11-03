---
content_hash: cb3bb3f7bcdd7989619183c4889ee6d445eaf9f6f592e1dc8ba565858ce00006
fetched_at: '2026-06-29T00:08:49.622897+00:00'
page_id: '331851967'
product: rm
source: tdn-rm
title: 2049571 EDUCACIONAL01-3775 DT Geração de Plano de Aula - Sem duração da aula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331851967
version: 91
---

# GERAÇÃO DE PLANO DE AULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Geração de plano de aula* |
| **Situação/Requisito:** | *Ao realizar a geração de um plano de aula sem a informação da duração de uma aula, o sistema apresentava uma mensagem de validação no cálculo da carga horária da turma/disciplina, o qual tinha como resultado uma divisão por 0. Essa validação impedia a execução do processo e a geração do plano de aula.* |
| **Solução/Implementação:** | *Foi realizado um ajuste no sistema para que nos casos onde haja divisão por 0 (zero), o sistema considere um valor 0 (zero) para a carga horária.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
