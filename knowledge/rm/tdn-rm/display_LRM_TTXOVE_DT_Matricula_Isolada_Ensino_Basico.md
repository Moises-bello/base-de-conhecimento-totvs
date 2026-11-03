---
content_hash: 0be13f24ae9565f30d52295a061af07cbd2cbc69aba69f0c8e9abbe4c712543e
fetched_at: '2026-06-29T00:06:22.300781+00:00'
page_id: '223913762'
product: rm
source: tdn-rm
title: TTXOVE_DT_Matricula_Isolada_Ensino_Basico
type: documentation
url: https://tdn.totvs.com/display/LRM/TTXOVE_DT_Matricula_Isolada_Ensino_Basico
version: 130
---

# MATRÍCULA ISOLADA NO ENSINO BÁSICO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Matrícula Isolada no Ensino Básico* | *Matrícula Isolada no Ensino Básico* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Digitação de Notas e Faltas Por Aluno** | ***Digitação de Notas e Faltas Por Aluno*** | | **Digitação de Notas de Avaliação Por Aluno** | **Digitação de Notas de Avaliação Por Aluno** | | **Digitação de Notas e Faltas da Etapa** | **Digitação de Notas e Faltas da Etapa** | | **Digitação de Notas de Avaliação** | **Digitação de Notas de Avaliação** | | **Notas de Avaliação **(Portal)**** | **Notas de Avaliação **(Portal)**** | | **Notas/Faltas Etapas (Portal)** | **Notas/Faltas Etapas (Portal)** | | **Quadro de Aviso - Aviso de Frequência **(Portal)**** | **Quadro de Aviso - Aviso de Frequência **(Portal)**** | |
| **Cadastros Iniciais:** | *1) Aluno cadastrado no Ensino Básico;*  *2) Período letivo cadastrado;*  *3) Turma/Disciplina cadastrada sem matriz aplicada;*  *4) Etapa de Nota (com e sem o grupo conceito preenchido) e Falta cadastrada na turma/disciplina;*  **5) Avaliação cadastrada para a etapa de nota da turma/disciplina.**  ****6) Professor responsável pela disciplina, para digitação de notas e faltas no portal.**** |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TUAVTX* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *SMATRICULA, STURMADISC, SDISCIPLINA, SETAPAS* |
| **Sistema(s) Operacional(is):** | *Windows 7* |
| **Versões/Release:** | *11.82.43*  *12.1.10* |
| **Versão Corrigida:** | *11.82.42.112*  *11.82.43*  *12.1.10* |
| **Versão Expedida:** | *11.82.42.112*  *11.82.43*   *12.1.10* |

## Descrição

A implementação de melhoria consiste em permitir a matrícula isolada para alunos do ensino básico, bem como permitir a digitação de notas e faltas por aluno, quando matriculado em turma/disciplina isolada.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(11.82.42.112)* deste chamado.

## Procedimento para Utilização

Para a rotina Matrícula Isolada no Ensino Básico:

1. Logar no TOTVS Educacional;
2. Acessar Currículo e Oferta | Alunos e selecionar um aluno para efetuar a matrícula isolada | Anexos | Matrícula Isolada;
3. Criar um novo registro no anexo Matrícula Isolada, preencher os campos pertinentes a tela e salvar;

Para a rotina Digitação de Notas e Faltas Por Aluno:

1. Acessar Matrícula e Avaliação | Grupo Notas e Fatas | Mais | Digitação por aluno | Notas e faltas de etapas, selecionar aluno, período letivo e marcar check "Somente matrícula em disciplinas isoladas".
2. Selecionar a disciplina que deseja lançar notas. Após selecionar, será aberto as etapas, com isso informe os valores das notas e clique em salvar.

Para a rotina Digitação de Notas de Avaliação Por Aluno:

1. Acessar Matrícula e Avaliação | Grupo Notas e Fatas | Mais | Digitação por aluno | Notas de avaliação, selecionar aluno, período letivo e marcar check "Somente matrícula em disciplinas isoladas".
2. Selecionar a disciplina que deseja lançar notas. Após selecionar, será aberto as etapas de notas e suas respectivas avaliações, com isso informe os valores das notas de avaliações e clique em salvar.

Para a rotina Digitação de Notas e Faltas da Etapa:

1. Acessar Matrícula e Avaliação | Grupo Notas e Fatas | Notas e faltas de etapas, selecionar período letivo, turma da matrícula isolada, a disciplina e etapa de notas e/ou faltas.
2. Selecionar o aluno que deseja lançar notas e/ou faltas e lançar os valores e clique em salvar.

Para a rotina Digitação de Notas de Avaliação:

1. Acessar Matrícula e Avaliação | Grupo Notas e Fatas | Notas de avaliação, selecionar período letivo, turma da matrícula isolada, a disciplina, etapa de nota e a prova correspondente.
2. Selecionar o aluno que deseja lançar nota de avaliação e lançar os valores e clique em salvar.

Para a rotina Notas de Avaliação (Portal) - Contexto Aluno:

1. Acessar menu Acadêmico | Notas de avaliação, será exibido as notas das avaliações do aluno.

Para a rotina Notas de Avaliação (Portal) - Contexto Professor:

1. Acessar menu Professor | Notas de avaliação, selecionar a turma/disciplina da matrícula isolada.
2. Efetuar o filtro e clicar em Selecionar.
3. Informar/alterar a(s) nota(s) do(s) aluno(s) e salvar.

Para a rotina Notas/Faltas Etapas (Portal) - Contexto Aluno:

1. Acessar menu Acadêmico | Notas/Faltas Etapas, será exibido as notas e faltas do aluno.

Para a rotina Notas/Faltas Etapas (Portal) - Contexto Professor:

1. Acessar menu Professor | Notas/Faltas Etapas, selecionar a turma/disciplina da matrícula isolada.
2. Efetuar o filtro e clicar em Selecionar.
3. Informar/alterar a(s) nota(s) e/ou falta(s) do(s) aluno(s) e salvar.

Para a rotina Quadro de Aviso - Aviso de Frequência (Portal):

1. Acessar menu Acadêmico | Quadro de Aviso, será exibido as frequências das disciplinas do aluno, entretanto para turmas/disciplinas que pertencem a matrícula isolada, o percentual de faltas será sempre zero, pois, a carga horária da disciplina no ensino básico é informada no anexo da matriz curricular (disciplinas da matriz curricular). Como a turma/disciplina da matrícula isolada não possui matriz aplicada, não será possível informar a carga horária da disciplina.

**Observação:**Para rotinas que envolvem o portal, somente será exibido as turmas/disciplinas da matrícula isolada, somente se o aluno possuir uma matrícula válida em um período letivo, caso contrário, não será possível carregar o contexto, com isso não terá possibilidade de visualizar nenhum dado das turmas/disciplinas de matrícula isolada.

divs
