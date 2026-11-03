---
content_hash: a1a12c79bb45e167567360f47139a434408851fa69a3209350b016727594d63e
fetched_at: '2026-06-29T00:08:04.112320+00:00'
page_id: '235336112'
product: rm
source: tdn-rm
title: TU5589_DT_Geracao_Automatica_Usuario_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/TU5589_DT_Geracao_Automatica_Usuario_Aluno
version: 114
---

# Geração automática de usuários para alunos, pais e responsáveis (Acadêmico e Financeiro)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS EDUCACIONAL* |
| **Módulo:** | *Classis.NET* |
| **Função:** | *Geração de usuários* |
| **Situação/Requisito:** | *Geração automática de usuários para alunos e responsáveis ao incluir novo aluno* |
| **Solução/Implementação:** | *Foi realizado uma melhoria para atender à necessidade de geração de usuários durante a inclusão de um novo aluno, onde esta geração automática de usuários deve ser disparada em todas as situações onde é cadastrado um novo aluno, incluindo por exemplo ao incluir um novo aluno através do WebService TBC, Processo Seletivo RM e Processo Seletivo Terceirizado, além da tela de cadastro de novo aluno do RM Educacional.*  *Qualquer outro local que realizar a chamada do SaveRecord do data server EduAlunoData, poderá ser gerado um usuário automaticamente para o aluno, pais e responsáveis (Acadêmico e Financeiro) de acordo com as definições dos parâmetros do Educacional.*  *A geração automática de usuários do aluno não é disparada durante a edição de um aluno existente, e só é realizada durante a inclusão de um novo aluno.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
