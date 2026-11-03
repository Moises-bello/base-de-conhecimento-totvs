---
content_hash: 66e1ec61563c35a04726ff3c7945aa5465e2b77dedad542717414fdb41a562aa
fetched_at: '2026-06-29T00:10:32.693609+00:00'
page_id: '527835901'
product: rm
source: tdn-rm
title: Atividades educacionais para fórmulas visuais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527835901
version: 5
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Definições**

## **01. VISÃO GERAL**

O TOTVS Educacional disponibiliza algumas atividades específicas que podem ser utilizadas em fórmulas visuais.

Fórmulas visuais

Para mais informações sobre fórmulas visuais acesse o a documentação: 

* EduMudancaStatusCursoActivity
  + Altera a situação de matrícula do aluno no curso.
* EduMudancaStatusMatricPLActivity
  + Altera a situação de matrícula do aluno no período letivo.
* EduMudancaStatusDisciplinaActivity
  + Altera a situação de matrícula do aluno na disciplina.
* EduFrequenciaActivity
  + Grava uma frequência para o aluno

## **02. Definições**

As atividades disponibilizadas possuem os mesmos campos/parâmetros utilizados pelos respectivos processos no TOTVS Educacional, porém existem alguns campos mínimos a serem preenchidos.

Abaixo segue a lista de campos por atividade:

EduMudancaStatusCursoActivity

| Campo | Tipo | Obrigatório? | Observação |
| --- | --- | --- | --- |
| Cód. Coligada | inteiro | Não |  |
| Cód. Filial | inteiro | Sim |  |
| Cód. Motivo de alteração | inteiro | Sim |  |
| Cód. Nova situação de matrícula | inteiro | Sim |  |
| Cód. Tipo Curso | inteiro | Sim |  |
| Id. Matriz aplicada | inteiro | Sim |  |
| R.A. | texto | Sim |  |

EduMudancaStatusMatricPLActivity

| Campo | Tipo | Obrigatório? | Observação |
| --- | --- | --- | --- |
| Cód. Coligada | inteiro | Não |  |
| Cód. Filial | inteiro | Sim |  |
| Cód. Motivo de alteração | inteiro | Sim |  |
| Cód. Nova situação de matrícula | inteiro | Sim |  |
| Cód. Tipo Curso | inteiro | Sim |  |
| Id. Matriz aplicada | inteiro | Sim |  |
| Id. Período Letivo | inteiro | Sim |  |
| R.A. | texto | Sim |  |

EduMudancaStatusDisciplinaActivity

| Campo | Tipo | Obrigatório? | Observação |
| --- | --- | --- | --- |
| Cód. Coligada | inteiro | Não |  |
| Cód. Filial | inteiro | Sim |  |
| Cód. Motivo de alteração | inteiro | Sim |  |
| Cód. Nova situação de matrícula | inteiro | Sim |  |
| Cód. Tipo Curso | inteiro | Sim |  |
| Id. Matriz aplicada | inteiro | Sim |  |
| Id. Período Letivo | inteiro | Sim |  |
| Id. Turma/Disciplina | inteiro | Sim |  |
| R.A. | texto | Sim |  |

EduFrequenciaActivity

| Campo | Tipo | Obrigatório? | Observação |
| --- | --- | --- | --- |
| CodColigada | inteiro | Não |  |
| Data | data | Sim |  |
| IdHorarioTurma | inteiro | Sim |  |
| IdTurmaDisc | inteiro | Sim |  |
| RegistroAcademico | texto | Sim |  |
| TipoFrequencia | texto | Sim | A - Ausência | P - Presença |
| AulasDatas | inteiro | Sim |  |
| CodEtapa | inteiro | Sim |  |
| IdJustificativa | inteiro | Sim |  |
| Justificada | inteiro | Sim |  |
