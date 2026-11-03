---
content_hash: f9dcf1ee3252bcef6d116e56dfb7e12ccdbdd4887551dcc245eac426274d0e98
fetched_at: '2026-06-29T00:10:36.954229+00:00'
page_id: '532666296'
product: rm
source: tdn-rm
title: Integralização de Curso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532666296
version: 25
---

## **Conteúdo**

## **01. Visão Geral**

Importante

A integralização de curso foi implementada a partir da versão 12.1.25 e para sua utilização é necessário executar os scripts de marcações CN.2020.01\_18 e CN.2020.02\_07. Entre em contato com o nosso suporte e solicite o script informado.

Conforme a legislação: **Resolução Nº 2, de 18 de junho de 2007**, do Conselho Nacional de Educação, que determina o tempo de integralização do curso do aluno. foi disponibilizado no TOTVS Educacional a funcionalidade de integralização de curso, que consiste em validar se o aluno cumpriu o tempo mínimo do curso exigidos na matriz curricular.

Para habilitar a integralização de curso é necessário acessar as Configurações | Parâmetros | Secretaria | Geral 6/6 e marcar o parâmetro **Habilitar a integralização de curso**. Ao habilitar este parâmetro, o sistema começa a validar a integralização, mas para isso é necessário acessar a matriz curricular dos cursos e informar a quantidade de mínima exigida de períodos letivos a serem cursados e se for pertinente a quantidade mínima de disciplinas optativas/eletivas a serem cursadas. 

Para que um período letivo seja válido para a contagem de períodos da integralização, o aluno deverá ter pelo menos uma disciplina cursada, sendo aprovada/reprovada (com resultado final) ou com situação de matrícula que tem como parâmetro marcado o **Conta como aluno matriculado na turma**ou **É uma disciplina em curso**, não é contado as disciplinas aprovadas por aproveitamento de estudo. Será levado em conta todas as matrículas do aluno no curso, independente da habilitação, matriz e/ou turno.

Se o aluno está matriculado em cursos diferentes, os períodos deste cursos não serão contados para outros.

Para que um determinado curso/habilitação do aluno seja excluído da integralização, um parâmetro no cadastro do curso/habilitação do aluno ficará disponível para desabilitar a integralização. Ao marcar este parâmetro, o curso deste aluno não irá passar pelas validações da integralização.

## **02. Conclusão de Curso**

No momento da conclusão do curso do aluno irá ser feita a validação se o aluno está atendendo o tempo de integralização para concluir o curso. Esta validação consiste em verificar se o aluno cursou a quantidade mínima de períodos exigidos da matriz curricular. Um curso é dado como concluído, quando a situação de matrícula possuir como parâmetro marca o **Indica conclusão do curso**.

Supondo que a quantidade mínima de períodos letivos a cursar tenha o valor igual a 8, então no momento da conclusão do curso do aluno, o sistema irá validar se o aluno cursou no mínimo os 8 períodos letivos, caso não seja atendido o mínimo, não será possível concluir o curso do aluno.

## **03. Processo de Matrícula em Disciplinas**

No processo de matrícula em disciplinas do aluno a validação também será feita com o objetivo de conduzir o aluno a sempre respeitar o tempo de integralização. A validação irá consistir em verificar se irá existir disciplinas a serem cursadas e estas disciplinas poderão ser distribuídas nos períodos letivos restantes.

Supondo o seguinte cenário descrito abaixo.

| Matriz Curricular - MTZ2019 | | | |
| --- | --- | --- | --- |
| 1º Período | 2º Período | 3º Período | Optativas/Eletivas |
| Disc1 | Disc3 | Disc6 | Opt1 |
| Disc2 | Disc4 | Disc7 | Opt2 |
| Disc3 | Disc5 | Disc8 | Ele1 |

Quantidade mínima créditos: 6.

Quantidade mínima de períodos letivos a cursar: 3.

Quantidade mínima de optativas/eletivas a cursar: 0.

Todas as disciplinas possuem 2 créditos.

**Situação 1:**

O aluno está matriculado em 2019/1 nas disciplinas: Disc1, Disc2, Disc3, Disc4 e Disc5.

Ao tentar matricular em 2019/2 nas disciplinas Disc6, Disc7 e Disc8 o sistema irá bloquear a matrícula, por que irá faltar um período letivo para cursar e não terá disciplinas para serem cursadas.

**Situação 2:**

Quantidade mínima de optativas/eletivas a cursar: 1.

O aluno está matriculado em 2019/1 nas disciplinas: Disc1, Disc2, Disc3, Disc4 e Disc5.

Ao tentar matricular em 2019/2 nas disciplinas Disc6, Disc7 e Disc8 o sistema não irá bloquear a matrícula, por que irá faltar um período letivo para cursar e terá as disciplinas optativas/eletivas a serem cursadas.

**Situação 3:**

O aluno está matriculado em 2019/1 nas disciplinas: Disc1, Disc2, Disc3, Disc4, Disc5, Disc6.

Ao tentar matricular em 2019/2 na disciplina Disc7 o sistema não irá bloquear a matrícula, por que irá faltar um período letivo para cursar e terá uma disciplina a ser cursada. O número mínimo de créditos não está sendo atendido, mas pela integralização esta regra de mínimo de créditos está sendo quebrada.

## **04. Análise Curricular**

A análise curricular do sistema foi alterada para exibir no resumo os seguintes itens:

* Quantidade mínima de períodos letivos a cursar
* Quantidade de períodos letivos cursados/em curso
* Quantidade de períodos letivos pendentes

Somente é exibido no resumo os campos citados acima, se a integralização estiver habilitada nos parâmetros do educacional e a quantidade mínima de períodos letivos a cursar estiver preenchida na matriz curricular.

Importante

Os campos citados acima serão exibidos no sistema (RM.exe) e no .

No portal e no relatório do book (EDUREL0018 - Análise Curricular) não serão exibidos.

## **05. Análise de Integralização dos Alunos**

Localizado em Matrícula e Avaliação | Matrícula | Mais, o processo de análise de integralização dos alunos é possível verificar se os alunos possuem condições de serem integralizados no curso.

Existem duas opções para filtrar os alunos no processo: Filtro Genérico e Matriz aplicada.

Pelo filtro genérico é possível montar o filtro de acordo com os campos do curso/habilitação do aluno.

Pelo filtro da matriz aplicada, estão disponíveis os campos da matriz e a situação de matrícula.

Só serão analisados os alunos do contexto logado e que não estão desabilitados para integralização, independente do filtro escolhido.

O processo pode ser executado sem informar nenhum filtro. Nesse caso todos os alunos do contexto habilitados para integralização serão analisados.

É possível escolher o que será feito após a análise dos alunos: apenas exibir os alunos que não irão cumprir a integralização ou exibir esses alunos e desabilitá-los para integralização.

Caso seja escolhida a opção de desabilitar a integralização, o campo "Desabilita a integralização do curso" no curso/habilitação do aluno será marcado para os alunos que não possuem condições de serem integralizados.

Vale lembrar que este processo somente é habilitado se o parâmetro **Habilitar a integralização de curso**em Configurações | Parâmetros | Secretaria | Geral 6/6 estiver marcado.
