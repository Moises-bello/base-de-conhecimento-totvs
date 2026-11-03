---
content_hash: f53807638a7e321537e8ca6004d2c1341a48a269e9bb63565aec853626169c90
fetched_at: '2026-06-29T00:10:43.759480+00:00'
page_id: '550332141'
product: rm
source: tdn-rm
title: Retorno de Matrícula - Mesmo Curso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550332141
version: 14
---

O processo se aplica às situações em que um aluno retorna à instituição para realizar ***um mesmo Curso, ofertado em um mesmo Período Letivo, Matriz Curricular e Turno.***

Premissa:

A instituição para a qual este cenário se aplica, (geralmente em cursos lineares) deverá configurar previamente o Parâmetro: Permitir matricular o aluno em outra disciplina já aprovada, disponível em: Totvs Educacional l Ambiente l Parâmetros l Educacional l 15.03 - Matrícula l Movimento 1/4.

Considerando a realização/conclusão da primeira oferta de curso, o aluno deverá ter os seguintes resultados associados:

* **Turmas/Disciplinas:** Aprovado ou Reprovado;
* **Matrícula no Período Letivo:** Aprovado ou Reprovado;
* **Curso/Habilitação:** Concluinte ou Reprovado.

## **Processos Iniciais - Curso/Habilitação e Matrícula no Período Letivo**

Ao Curso/Habilitação, aplique as alterações:

* **Situação de Matrícula:** 2 - Matriculado.
* **Motivo da Alteração:** Conforme definido pela instituição de ensino.

Após, clique em: Salvar.

À Matrícula no Período Letivo, mantenha:

* **Status:** 2 - Matriculado
* **Resultado:** Conforme Apuração de Resultados executada.

Considerando a execução/verificaão dos Processos Iniciais, o aluno deverá então ser matriculado nas Turmas/Disciplinas da nova oferta de curso, a partir da Matrícula no Período Letivo da oferta de curso anterior/inicial.

## **Matrícula no Período Letivo - Processo**

A partir da Matrícula no Período Letivo da oferta de curso anterior/inicial, o aluno deve ser matriculado novamente apenas nas Turmas/Disciplinas da nova oferta de curso.

Assim, selecionada a Matrícula no Período Letivo, em: Processos, selecione o item: Matricular Aluno nas Disciplinas.

Clique em: Avançar.

Vincule a Nova Turma na qual o aluno irá cursar a nova oferta de curso. Após, clique em: Avançar.

Selecione as disciplinas que compõem a Nova Turma, nas quais o aluno deverá ser matriculado e, em seguida, clique em: Avançar até a execução do processo.

Finalizado o processo de matrícula, temos:

* **Matrícula no Período Letivo:** Alterado o vínculo da turma para a Nova Turma de Oferta de Curso.
* **Matrícula em Disciplinas:** Mantidas as matrículas em disciplinas cursadas na oferta anterior/inicial de curso e adicionadas as matrículas nas disciplinas associadas a nova turma, correspondente à nova oferta de curso a ser realizada pelo aluno.

Observações:

O Totvs Educacional (SGE) mantém o registro de movimentação do aluno no período letivo, disponível em: Totvs Educacional l Currículo e Oferta l Alunos l Lig de Movimentação.

Após finalizar a nova oferta de curso, a equipe de secretaria escolar deverá executar novo processo de Apuração de Resultados, que será considera apenas o registro da nova matrícula para leitura dos registros (nota/frequência - conforme a oferta de curso) e aplicação de resultado.
