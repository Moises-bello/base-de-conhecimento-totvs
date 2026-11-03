---
content_hash: b6e1d74bfbf5c643b442477f7859d1c6e3b57711a116f9cab75ce1cfb5e2d8b6
fetched_at: '2026-06-29T00:06:08.820726+00:00'
page_id: '201752551'
product: rm
source: tdn-rm
title: TSVXB3_DT_Disciplinas_Reprovadas_Na_Analise_Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVXB3_DT_Disciplinas_Reprovadas_Na_Analise_Curricular
version: 1
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | **Educacional*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Análise Curricular* | *Análise Curricular* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Análise Curricular* | *Análise Curricular* | |  |  | |
| **Cadastros Iniciais:** | *O aluno deve estar matriculado em uma disciplina equivalente e ter sido reprovada nesta disciplina.* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas utilizadas:** | *SMATRICULA* |
| **Sistema(s) operacional(is):** | *Windows 7/8.1* |
| **Versões/Release:** | *12.1.8* |

## Descrição

Foi implementado uma nova condição na Análise Curricular, onde se algum aluno for reprovado em disciplinas equivalentes, elas serão listadas abaixo da disciplina da Grade do aluno, conforme já eram exibidas as disciplinas equivalentes que foram aprovadas ou estão em curso.

Se o aluno cursou a disciplina da grade e foi reprovado e também for reprovado em uma disciplina equivalente, o sistemá irá mostrar a disciplina reprovada mais recente.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.8* deste chamado.

## Procedimento para Utilização

**Exemplo:**

       1.            O aluno deve ter se matriculado em uma disciplina da grade dele

       2.            Ser reprovado nesta disciplina

       3.            Será listado logo abaixo da disciplina da Grade, a disciplina equivalente com o status de Reprovado. A exibição desta disciplina equivalente só acontecia para disciplinas equivalentes Aprovadas ou Em Curso.
