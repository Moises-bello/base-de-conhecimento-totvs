---
content_hash: 337367631a83e60c692f1bca48db62b659e2d4ac256b60e42f0e760a5a2fb240
fetched_at: '2026-06-29T00:08:05.107385+00:00'
page_id: '235583778'
product: rm
source: tdn-rm
title: TU6901_DT_Rematricula
type: documentation
url: https://tdn.totvs.com/display/LRM/TU6901_DT_Rematricula
version: 116
---

# REMATRÍCULA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Rematrícula* | *Rematrícula* | |
| **Cadastros Iniciais:** | *1) Aluno cadastrado;*  *2) Aluno matriculado em dois cursos para um mesmo período letivo;*  *3) Consulta SQL para seleção de alunos (opcional).* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows 7* |

## Descrição

Ajuste na grid de alunos que é exibida ao adicionar os alunos para rematrícula, para que inclusão das colunas Código do Curso, Nome do Curso, Nome da Habilitação e Turno..

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(12.1.11)* deste chamado.

## Procedimento para Utilização

Para a rotina Rematrícula:

1. Acessar o TOTVS Educacional;
2. Acessar Matrícula e Avaliação | Rematrícula | Escolher uma forma de seleção de alunos\* | Adicionar alunos;
3. Após selecionar os alunos a grid de seleção de alunos contém as colunas: Código do curso, Curso, Habilitação (para ensino superior) / Série (para ensino básico) e Turno; conforme abaixo:

\* Caso seja selecionado por consulta SQL é necessário possuir as tabelas SCURSO, SHABILITACAO, STURNO e inserir o campos SCURSO.CODCURSO (sem alias), SCURSO.NOME (deverá ter o alias CURSO), SHABILITACAO.NOME (deverá ter o alias HABILITACAO) e STURNO.NOME (deverá ter alias TURNO), caso não seja feito desta forma, as novas colunas da grid exibirão o seu conteúdo vazio.

 

divs
