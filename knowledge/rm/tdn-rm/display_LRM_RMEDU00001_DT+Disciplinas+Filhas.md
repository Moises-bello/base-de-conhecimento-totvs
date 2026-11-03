---
content_hash: 009e6f468591174261a9d46a3c9c9e9ccb1cc18087e21274da356b4a56be9e42
fetched_at: '2026-06-29T00:08:40.159859+00:00'
page_id: '286211393'
product: rm
source: tdn-rm
title: RMEDU00001_DT Disciplinas Filhas
type: documentation
url: https://tdn.totvs.com/display/LRM/RMEDU00001_DT+Disciplinas+Filhas
version: 112
---

# DISCIPLINAS FILHAS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Disciplinas Filhas* | *Disciplinas Filhas* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Digitação de Notas/Faltas de Etapa** | **Digitação de Notas/Faltas de Etapa** | |
| **Cadastros Iniciais:** | * *Aluno cadastrado para que seja matriculado nas disciplinas.* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *942493* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *EDUCACIONAL01-1032* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

Disciplinas filhas é um conceito mais utilizado no nível de ensino básico, entretanto é possível cadastrar disciplinas filhas no ensino superior. Tais disciplinas são cadastras no anexo da disciplina dentro da matriz curricular, sendo possível definir a porcentagem da nota (peso) a ser considerada de uma disciplina da matriz com outra, desde que sejam diferentes. O Objetivo é que as notas das disciplinas filhas sejam "totalizadas/computadas" na disciplina "Pai", para que essa (a "Pai") possa ter sua apuração final (resultado final).

**Exemplo**: a disciplina de Português tem como disciplinas filhas a disciplina de Redação e a disciplina de Gramática. Para este caso, foram distribuídos 50% para cálculo da nota em Redação e 50% em Gramática. As notas são lançadas pelos professores através das disciplinas filhas. A soma das notas individuais de cada filha, considerando a sua proporção, será atribuída ao valor total na disciplina de Português (disciplina "Pai") por meio de fórmula na etapa.

## Procedimento para Implantação

A funcionalidade de disciplinas filhas está disponível nas versões 12 da linha RM.

## Procedimento para Utilização

*Neste procedimento iremos utilizar como disciplina "pai" Português e como disciplinas filhas Gramática e Redação.*

1. Acessar a matriz curricular que deseja cadastrar as disciplinas filhas e no anexo Período acessar o período desejado, após isso acessar o anexo Disciplinas;
2. Criar uma disciplina que será a "pai", exemplo Português;
3. Criar mais duas disciplinas, que serão as filhas, exemplo Gramática e Redação;
4. Acessar a disciplina de Português e em seu anexo Disciplinas filhas e criar as duas filhas e informar em cada uma o percentual de notas de 50%;
5. Criar então uma turma que irá conter as três disciplinas:
6. Criar etapas para as turmas/disciplinas  
     
   1. Português

      | Etapa de Nota | Etapa de Falta |
      | --- | --- |
      |  |  |
      | A fórmula informada nesta etapa, irá somar as notas das disciplinas filhas, de acordo com a porcentagem em relação à disciplina pai. O cálculo da fórmula irá somar apenas das etapas de notas com o mesmo código. Para efetuar este somatório é utilizado a função **SomaFilhas.** | A fórmula informada nesta etapa, irá somar as faltas das disciplinas filhas. Não é levado em consideração a porcentagem. O cálculo da fórmula irá somar apenas das etapas de faltas com o mesmo código. Para efetuar este somatório é utilizado a função **FaltasFilhas****.** Além disso, é possível também somar as aulas dadas das filhas e atribuir na disciplina "pai" pela função de fórmula **AulasFilhas.** |
   2. Gramática

      | Etapa de Nota | Etapa de Falta |
      | --- | --- |
      |  |  |
   3. Redação

      | Etapa de Nota | Etapa de Falta |
      | --- | --- |
      |  |  |
7. Matricular aluno(s) nas três turmas/disciplinas;
8. Digitar notas/faltas para o aluno nas disciplinas filhas para que as fórmulas sejam executadas e populem as etapas da disciplina "pai":

   | Notas/Faltas - Gramática | Notas/Faltas - Redação |
   | --- | --- |
   |  |  |
   | **Somatório de Notas Faltas e Aulas Dadas - Português** | |
   |  | |
   | É possível verificar que a **Nota Final** da disciplina de Português recebeu o valor de 20, que é o valor da nota de 50% da nota da disciplina de Gramática (valor 10 / 2 = 5) somado com o valor de 50% da nota da disciplina de Redação (valor 30 / 2 = 15) que totaliza um valor de 5 + 15 = 20.O valor 15 de faltas da disciplina de Português foi o somatório de faltas da disciplina de Gramática (10) com a de Redação (5), totalizando 15 faltas.Além disso, o valor de 120 de aulas dadas da disciplina de Português se deu pelo somatório de aulas dadas de Gramática (60) com a de Redação (60), totalizando 120 aulas dadas. | |
9. Ao gerar o histórico do aluno será possível verificar tais valores de notas e faltas da disciplina de português.

divs
