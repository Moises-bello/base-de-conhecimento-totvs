---
content_hash: 349233a82d4534160e532e91d482cdd7cf05fdaa8c92cae8dd66bb0a6a2310f5
fetched_at: '2026-06-29T00:08:28.148743+00:00'
page_id: '271662572'
product: rm
source: tdn-rm
title: 494870 MEDU-2637 DT Timeout na matrícula online
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271662572
version: 114
---

# TIMEOUT NA MATRÍCULA ONLINE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Matrícula online* |
| **Situação/Requisito:** | *Para alguns alunos o portal está dando a mensagem de "Aguarde, validando as informações do aluno..." e no final aparece a mensagem "Thread was being aborted"* |
| **Solução/Implementação:** | *Alteração na consulta de verificação de inadimplência que não estava considerando a tabela SBOLSA no JOIN fazendo com que bolsas não relacionadas ao contrato do aluno fossem retornadas causando o timeout na execução da query.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *[439194](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22439194%22 "439194")* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
