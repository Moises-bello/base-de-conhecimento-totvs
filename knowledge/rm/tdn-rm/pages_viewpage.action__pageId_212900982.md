---
content_hash: 010b90f069dc8b7f0e2d04cc7dfc0df32f932ed4361880946380591ed3dcc367
fetched_at: '2026-06-29T00:06:16.884873+00:00'
page_id: '212900982'
product: rm
source: tdn-rm
title: DT_Informações_Mudança_Turma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=212900982
version: 3
---

# Mudança de Turma

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Assistente de mudança de turma | Mudar turma |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Turma | Cadastro de turma | | Turma/disciplina | Cadastro de turma/disciplina | | Subturma | Cadastro de subturma | | Campus | Cadastro de campus | | Curso | Cadastro de curso | | Habilitação / serie | Cadastro de habilitação / Cadastro de serie | | Matrícula de alunos | Matrícular | |
| **Cadastros Iniciais:** | Parâmetros do sistema e dependendo deste deve-se possuir turma, turma/disciplina, subturma, curso, habilitação, grade e campus associado a turma/disciplina |
| **Parâmetro(s):** | Parâmetros do sistema relacionado a matrícula |
| **Requisito (ISSUE):** | [PCREQ-8591](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-8591 "PCREQ-4727") |
| **País(es):** | Brasil |
| **Tabelas Utilizadas:** | STURMA, STURMADISC, SSUBTURMA, SCURSO, SHABILITACAO, SGRADE, SHABILITACAOFILIAL, SCAMPUS, SMATRICPL, SMATRICULA, SPERIODO, SPERIODOALUNO, SDISCGRADEALUNO, GFILIAL, SHABILITACAOALUNO, SGRADEALUNO |
| **Versões/Release:** | 12.1.9 |

## Descrição

Visando agilizar a escolha das turmas/disciplinas durante o processo de mudança de turmas, o TOTVS Educacional foi alterado na versão 12.1.9 apresentando dados complementares as turmas/disciplinas.

# Processo de mudança de turma

O processo de mudança de turma, contexto Ensino Superior, foi alterado para prover dados complementares as disciplinas, turmas/disciplinas e subturmas listadas ao usuário do sistema.

No passo de “Seleção de disciplinas”, o sistema disponibiliza uma visualização no formato de árvore, as disciplinas, turmas disciplinas e caso exista as subturmas disponíveis.

Novas colunas referente as disciplinas que serão disponibilizadas:

* + Número de Créditos (Número de Créditos – SDISCIPLINA ou SDISCGRADEALUNO);
  + Carga Horária (Carga horária – SDISCIPLINA ou SDISCGRADEALUNO);
  + Período (Código do Período – SPERIODO ou SPERIODOALUNO).

Novas colunas referente as turmas/disciplinas que serão disponibilizadas:

* + Curso (Nome do Curso – SCURSO);
  + Habilitação (Nome da Habilitação – SHABILITACAO);
  + Grade (Nome da Grade – SGRADE);
  + Turno (Nome do Turno da Turma/Disciplina – STURNO);
  + Campus (Caso exista campus vinculado a Turma Disciplina, será exibido o nome do campus – SCAMPUS).
  + Número de Vagas (calculado pelo sistema, baseado nos parâmetros da turma/disciplina);
  + Tipo da turma - presencial, a distância ou semipresencial (tipo – STURMADISC);
  + Data de início (STURMADISC);
  + Data de fim (STURMADISC);
  + Nome da filial vinculada a turma disciplina (nome – GFILIAL);
  + Nome professor (Nome – PPESSOA);
  + Horário da turma/disciplina (SHORARIOTURMA);

Novos dados referentes as subturmas que serão disponibilizadas:

* + Horário da subturma (SHORARIOTURMA);

Os novos dados serão apresentados da seguinte maneira:

**Disciplina** / Código da disciplina - Nome da Disciplina - Número de Créditos - Carga Horária - Período

**Turma Disciplina** / Código da Turma – Nome do Campus - Nome do Curso – Nome da Habilitação – Nome da Grade – Nome do Turno – Número de Vagas – Tipo – Data de Início – Data de Fim – Nome da Filial

**Professores da Turma/Disciplina** / Nome do professor

**Horário da Turma/Disciplina** / Dia da Semana – Hora de Início – Hora de Fim – Data de Início e Data de Fim

**Subturma** / Código da subturma

**Horário da Subturma** / Dia da Semana – Hora de Início – Hora de Fim – Data de Início e Data de Fim

**Horários Subturma**

Serão exibidos os horários da subturma somente se o parâmetro do TOTVS Educacional, “Utilizar turma/disciplina e subturma com horários independentes” (Secretaria > Geral 2/5) estiver selecionado.

**Turma Livre**

É importante ressaltar que Turmas Livres serão apresentadas somente com o código da turma, o nome do campus, nome do turno, número de vagas, tipo da turma, data de início, data de fim e nome da filial.

Os novos dados serão apresentados da seguinte maneira:

**Disciplina** / Código da disciplina - Nome da Disciplina - Número de Créditos - Carga Horária - Período

**Turma Disciplina** / Código da Turma – Nome do Campus - Nome do Turno – Número de Vagas – Tipo – Data de Início – Data de Fim – Nome da Filial

**Horário da Turma/Disciplina** / Dia da Semana – Hora de Início – Hora de Fim – Data de Início e Data de Fim

**Subturma** / Código da subturma

**Horário da Subturma** / Dia da Semana – Hora de Início – Hora de Fim – Data de Início e Data de Fim

**Currículo Individual**

Alunos com currículo individual, serão apresentados dados da “Disciplina”, baseado no cadastro da Disciplina da Grade do Aluno (SDISCGRADEALUNO e SPERIODOALUNO).

Os novos dados serão apresentados da seguinte maneira em destaque:

**Disciplina** / Código da disciplina - Nome da Disciplina - **Número de Créditos - Carga Horária - Período**

**Turma Disciplina** / Código da Turma – Nome do Campus - Nome do Curso – Nome da Habilitação – Nome da Grade – Nome do Turno – Número de Vagas – Tipo – Data de Início – Data de Fim – Nome da Filial

**Horário da Turma/Disciplina** / Dia da Semana – Hora de Início – Hora de Fim – Data de Início e Data de Fim

**Subturma** / Código da subturma

**Horário da Subturma** / Dia da Semana – Hora de Início – Hora de Fim – Data de Início e Data de Fim

divs
