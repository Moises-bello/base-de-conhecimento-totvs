---
content_hash: 4157ebf0c450364ea4a74ec79cc91472088f441ce9d6f2615a28bc290a6c12fd
fetched_at: '2026-06-29T00:08:18.566080+00:00'
page_id: '264340891'
product: rm
source: tdn-rm
title: TVPPQF_DT_Cadastrar_Ocorrencias_Para_Alunos
type: documentation
url: https://tdn.totvs.com/display/LRM/TVPPQF_DT_Cadastrar_Ocorrencias_Para_Alunos
version: 113
---

# CADASTRAR OCORRÊNCIAS PARA OS ALUNOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastrar *Ocorrências* para os Alunos* | *Cadastrar Ocorrências para os Alunos* | |
| **Cadastros Iniciais:** | *1) Situações de matrícula cadastrados uma com parâmetro "Conta como aluno matriculado na turma" para o ensino básico e "É uma disciplina em curso" para o ensino superior;*  *2) Turmas A e B com disciplinas vinculadas;*  *3) Aluno que efetuou mudança de turma da A para a B, possuindo situações de matrícula diferentes que foram cadastradas.* |
| **Parâmetro(s):** | * *Ensino básico* *Educacional | Atividades Acadêmicas | Cadastrar ocorrências para os alunos | Somente aluno(s) com status "Conta como aluno matriculado na turma";* * *Ensino superior* *Educacional | Atividades Acadêmicas | Cadastrar ocorrências para os alunos | Somente aluno(s) com status "É uma disciplina em curso".* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows 7* |

## Descrição

Ajuste no processo de Cadastrar ocorrências para os alunos, para que seja possível filtrar os alunos de acordo com o parâmetro na situação de matrícula, sendo "Conta como aluno matriculado na turma", no ensino básico, "É uma disciplina em curso", no ensino superior.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(12.1.14)* deste chamado.

## Procedimento para Utilização

Para a rotina Cadastrar ocorrências para os alunos:

1. Acessar o Educacional | Atividades Acadêmicas | Assistentes | Cadastrar ocorrências para os alunos;
2. Informar os dados básicos para execução do processo e ir até o passo de seleção de alunos;
3. No passo de seleção dos alunos foi incluído um parâmetro para filtrar de acordo com o seguinte critério:  
     
   3.1**Ensino básico:**
   1. O parâmetro terá o seguinte nome: ***Somente aluno(s) com status "Conta como aluno matriculado na turma"***;
   2. **Parâmetro selecionado:** somente virá alunos com a situação de matrícula que possuir o item "Conta como aluno matriculado na turma" marcado;
   3. **Parâmetro não selecionado:** virá todos alunos como funciona hoje;3.2 **Ensino superior:**
   1. O parâmetro terá o seguinte nome: ***Somente aluno(s) com status "É uma disciplina em curso"***;
   2. **Parâmetro selecionado:** somente virá alunos com a situação de matrícula que possuir o item "É uma disciplina em curso" marcado;
   3. **Parâmetro não selecionado:** virá todos alunos como funciona hoje.

divs
