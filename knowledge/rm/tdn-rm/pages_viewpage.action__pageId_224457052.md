---
content_hash: 08b454502cf546b808dec71daa2aac1a06db026065d97eb9fba0e7ed7f1d9114
fetched_at: '2026-06-29T00:06:26.266686+00:00'
page_id: '224457052'
product: rm
source: tdn-rm
title: DT_Não_permitir_matricular_em_lista_de_espera_quando_existir_correquisito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224457052
version: 120
---

# Bloquear matrícula disciplina com correquisito

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Matrícula em Disciplinas* | *Matrícula em Disciplinas* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Matricula On-line* | *Matricula On-line* | | Matrícula Processo Seletivo | Matrícula Processo Seletivo | |
| **Cadastros Iniciais:** | *Parametrização do sistema, Disciplinas, Requisitos, Equivalências* |
| **Parâmetro(s):** | Bloquear matrícula em lista de espera de disciplinas com correquisitos |
| **Requisito (ISSUE):** | [PCREQ-9359](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9359 "PCREQ-4727") |
| **País(es):** | *Brasil* |
| **Tabelas Utilizadas:** | *SREQUISITOS, SDISCIPLINAS, SMATRICULA* |

## Descrição

Detalhar o comportamento do sistema TOTVS Educacional de acordo com o novo parâmetro “Bloquear matrícula em lista de espera de disciplinas com correquisitos”.

## Procedimento para Utilização

 

O TOTVS Educacional foi alterado para bloquear a matricula de alunos em lista de espera caso a disciplina possua correquisito.

 

Este bloqueio é possível somente se for selecionado o novo parâmetro “Bloquear matricula em lista de espera de disciplina com correquisito”, disponível no parametrizador do sistema, grupo de matrículas. O novo parâmetro supracitado estará disponível apenas se a lista de espera estiver ativa.

 

**Validação do parâmetro** 

 

A regra de matrícula foi alterada para validar este bloqueio durante a verificação de vaga na turma. Se o sistema estiver parametrizado para considerar a matriz do aluno para requisitos, iremos verificar se a disciplina vinculada a turma/disciplina selecionada durante o processo de matricula possui requisitos e que a mesma seja do tipo correquisito.

 

É verificado também se a disciplina em questão possuí requisitos no currículo individual do aluno do tipo correquisito.

 

Se a turma/disciplina selecionada não pertencer a matriz do aluno, será verificado se possuí uma equivalência, caso possua, o sistema irá verificar os requisitos da disciplina equivalente da matriz do aluno, e caso tenha um requisito do tipo correquisito a matricula será bloqueada.

 

Se o sistema não estiver parametrizado para considerar a matriz do aluno, será considerada a parametrização dos requisitos de acordo com a grade da matriz vinculada a turma/disciplina.

 

Em qualquer dos cenários citados, a disciplina possuindo requisito do tipo correquisito a matricula será bloqueada e apresentada a mensagem de “Não há vagas na turma informada. Disciplina com correquisito”.

 

**Parâmetros Educacionais por perfil de usuário** 

 

Uma vez o sistema bloqueando a matrícula do aluno na lista de espera devido ao requisito do tipo correquisito, o sistema verificará se o usuário do sistema possuí a permissão educacional por perfil de usuário de nome “Matricular em turmas com excesso de alunos”, caso possua o sistema irá alertar, porém irá permitir a matricula.

divs
