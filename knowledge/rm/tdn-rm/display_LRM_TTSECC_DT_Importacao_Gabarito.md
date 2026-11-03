---
content_hash: 916f72323886e19b3aea6e445df54dc79cab9d72c5f7b346370684826a5dd907
fetched_at: '2026-06-29T00:06:18.632410+00:00'
page_id: '219121865'
product: rm
source: tdn-rm
title: TTSECC_DT_Importacao_Gabarito
type: documentation
url: https://tdn.totvs.com/display/LRM/TTSECC_DT_Importacao_Gabarito
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Função:** | *Importação de Gabarito* |
| **Situação/Requisito:** | *Ao importar os gabaritos dos alunos, caso a situação de matrícula do aluno na disciplina esteja parametrizada para bloquear a alteração de notas e faltas, as notas não são atualizadas mesmo que o usuário tenha permissão para alterar notas e faltas bloqueadas por situação de matrícula.* |
| **Solução/Implementação:** | *Ajuste na Importação de Gabarito para que o processo valide as permissões de usuário. Caso o perfil do usuário esteja parametrizado para permitir a alteração de notas e faltas bloqueadas por situação de matrícula, o usuário atualizará as notas do aluno ao importar o gabarito, mesmo que a situação de matrícula na disciplina estiver parametrizada para bloquear alteração de notas e faltas.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9.* |
| **Versão Corrigida:** | *12.1.8* |
| **Versão Expedida:** | *12.1.8.100* |

divs
