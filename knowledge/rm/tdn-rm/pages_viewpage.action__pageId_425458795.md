---
content_hash: b43b5adf830ee238834d82e15df48e19027082c3a2a538952743c90abb11c65e
fetched_at: '2026-06-29T00:09:31.937976+00:00'
page_id: '425458795'
product: rm
source: tdn-rm
title: Apuração de resultados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458795
version: 11
---

O objetivo desta funcionalidade é realizar a apuração de resultados dos alunos através de fórmulas.

É possível realizar o cálculo de média das provas por etapa, o cálculo de médias finais por disciplina (nota/frequência), a apuração de resultados finais no período letivo, da média global do aluno, no curso, do coeficiente de rendimento (CR) e, também, o encerramento do período letivo.

Para selecionar os alunos que irão participar do processo e necessário criar uma consulta sql, assim como para apuração de resultados finais.

Para cada opção marcada no processo de apuração, pode-se informar uma fórmula. Com exceção da opção para a apuração do status do curso, todas as demais poderão utilizar a fórmula que consta nos cadastros informados abaixo, caso não sejam informadas no processo:

**Apuração de Disciplinas/Etapas**

* Cálculo de média das provas por etapa:  A fórmula executada será de acordo com o tipo de etapa: Faltas ou Notas.
  + Currículo e Oferta | Oferta | Turmas/Disciplinas | Anexos: Etapas | Fórmula de faltas
  + Currículo e Oferta | Oferta | Turmas/Disciplinas | Anexos: Etapas | Fórmula de notas

* Cálculo de médias finais por disciplina(nota/frequência):
  + Currículo e Oferta | Oferta | Turmas/Disciplinas | Fórmula para cálculo de médias/aprovação

**Apuração de Resultados Finais**

* Cálculo resultados finais no período letivo
  + Currículo e Oferta | Oferta | Turmas | Fórmula para cálculo do resultado final
* Cálculo da média global do aluno
  + Currículo e Oferta | Estrutura Curricular | Matriz Curriculares | Fórmula para cálculo da média global
* Cálculo do status no curso
  + Não possui um campo de fórmula padrão - deve ser informado no processo.
* Cálculo do coeficiente do rendimento (CR)
  + Currículo e Oferta | Estrutura Curricular | Matriz Curriculares | Fórmula do coeficiente de rendimento

Segue abaixo duas funções de fórmula para retorno de quantidade de disciplinas:

* **NSitMat**: retorna, entre as disciplinas nas quais o aluno está matriculado, quantas possuem o status de matrícula informado no parâmetro, sendo desconsiderado as turmas mistas no cálculo.
* **NSitMatRes**: retorna, entre as disciplinas nas quais o aluno está matriculado, quantas possuem o status de resultado na matrícula informado no parâmetro, sendo desconsiderado as turmas mistas no cálculo.
