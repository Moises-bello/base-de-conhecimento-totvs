---
content_hash: 841e6903ade6a760672dbc0a12a8bf107174472ee1daf7144814c422851aa044
fetched_at: '2026-06-29T00:06:15.411911+00:00'
page_id: '210055247'
product: rm
source: tdn-rm
title: TTJQTA_DT_Documentos_Exigidos_Tipo_Ingresso_Matricula
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJQTA_DT_Documentos_Exigidos_Tipo_Ingresso_Matricula
version: 1
---

# DOCUMENTOS EXIGIDOS DO TIPO INGRESSO NA MATRÍCULA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Exigir documentos do tipo ingresso na matrícula* |
| **Situação/Requisito:** | *Duplicidade de documentos exigidos, quando estes são do tipo ingresso. Ao inserir um curso/habilitação para o aluno, é criado um registro em documentos exigidos, ao matricular esse aluno no período letivo, esse registro fica duplicado.* |
| **Solução/Implementação:** | *Remoção da inserção dos documentos exigidos do tipo ingresso da parametrização por curso ao incluir um curso / habilitação para o aluno. Além disso, foi feito um tratamento na rotina que salva os documentos no momento da matrícula do aluno, para que não seja duplicado os documentos do tipo ingresso, quando o parâmetro "Considerar documentos do tipo ingresso mesmo que não seja a primeira matrícula" esteja marcado.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *11.82.41.104* |
| **Versão Expedida:** | *11.82.41.104* |

divs
