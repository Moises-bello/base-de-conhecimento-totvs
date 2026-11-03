---
content_hash: 85ec76cc5272b7aadf4e86dbbcbe05ff3b3ec49933607a0e94a2e9f72e0f1256
fetched_at: '2026-06-29T00:08:27.856188+00:00'
page_id: '271650459'
product: rm
source: tdn-rm
title: 400534 MEDU-2139 DT Matriculas vinculadas ao TCC com disciplinas equivalentes
type: documentation
url: https://tdn.totvs.com/display/LRM/400534+MEDU-2139+DT+Matriculas+vinculadas+ao+TCC+com+disciplinas+equivalentes
version: 111
---

# TCC DO ALUNO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Atividades Acadêmicas* |
| **Função:** | *Matrículas vinculadas ao TCC* |
| **Situação/Requisito:** | Disciplinas equivalentes não eram exibidas para vinculo ao TCC do aluno. |
| **Solução/Implementação:** | Alterado o comportamento do sistema para permitir que disciplina por equivalência  seja listada no anexo  “Matrículas vinculadas ao TCC” do TCC do aluno.  Para listar disciplinas equivalentes, o status da disciplina deverá estar “Em Curso” e na matriz curricular do aluno, a disciplina que utiliza equivalência deverá estar marcado o parâmetro “Indica se a disciplina é de TCC” (vide cadastro de  “Disciplinas da Matriz Curricular”).  A disciplina matriculada deverá pertencer à uma turma/disciplina.  Esta alteração também afetará o processo de “Análise Curricular”, onde o item TCC também listará as disciplinas equivalentes que foram vinculadas ao TCC do aluno.  Informações sobre como configurar ambiente para uso do TCC encontra-se em <http://fwrm-wiki:9999/WikiHelp/EDU/EDU.tcc.aspx> |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *MEDU-2539; MEDU-257; MEDU-335* |
| **Requisito (ISSUE):** | *N/A* |

divs
