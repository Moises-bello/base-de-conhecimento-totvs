---
content_hash: a3ceda6066a631c423d768c89c932ecedd5a3d23043be4bda0411cba75de331d
fetched_at: '2026-06-29T00:09:31.853625+00:00'
page_id: '425458751'
product: rm
source: tdn-rm
title: Disciplinas da Matriz Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/Disciplinas+da+Matriz+Curricular
version: 12
---

Esta janela permite cadastrar as disciplinas da matriz curricular, informando as informações de número de créditos, número mínimo de disciplinas entre outras informações que complementam estas disciplinas.  
   
Foi criada a fórmula , para retornar a quantidade de disciplinas, de crédito ou carga horária em curso, de um determinado período ou de/até um período determinado e que valide disciplinas que estão sendo matriculadas e, também, as que estão em curso. Ela é configurada no campo formula de correquisito do cadastro de disciplinas da matriz.

Campo Número de Aulas Semanais

A partir das versões **12.1.2410.261, 12.1.2502.164, 12.1.2506.108**, **12.1.2510** o sistema passou a contar com o campo **Nº de Aulas Semanais**. Esse campo informa quantas aulas da disciplina ocorrem por semana e é essencial para o planejamento do quadro de horários e para o cálculo da carga horária total no Planejamento de Oferta.

Por exemplo: uma disciplina com 2 aulas semanais de 50 minutos, oferecida durante um semestre, terá sua carga horária total calculada automaticamente a partir dessa frequência.

Ao cadastrar uma nova disciplina na matriz curricular, o campo Nº de aulas semanais da disciplina da grade será preenchido de forma automática com o valor definido previamente no cadastro da disciplina.

Para atender às novas diretrizes do Marco Regulatório da Educação a Distância e às exigências do Decreto nº 12.456, de 19 de maio de 2025, foi instituído o controle de carga horária nas disciplinas do Ensino Superior, tanto na modalidade presencial quanto a distância.

**Modalidades de Ensino**

De acordo com o **Decreto nº 12.456/2025**, os cursos de Ensino Superior no Brasil poderão ser ofertados em três modalidades:

1. **Curso presencial**
2. **Curso semipresencial**
3. **Curso a distância**

**Definições Importantes**

* **Educação a distância (EAD)**: Processo de ensino e aprendizagem realizado por meio do uso de tecnologias de informação e comunicação, onde o estudante e o docente estão em locais e horários diversos.
* **Atividade presencial**: Atividade de ensino realizada com a presença física do estudante e do docente, em tempo e local coincidentes.
* **Atividade síncrona**: Atividade mediada por tecnologia, onde o estudante e o docente participam simultaneamente, mas em locais diferentes.
* **Atividade síncrona mediada**: Atividade síncrona em grupos de no máximo 70 estudantes, com controle de frequência.
* **Atividade assíncrona**: Atividade em que o estudante e o docente realizam as atividades em horários diferentes.

**Cadastro de Disciplina na Matriz Curricular:**

Campos adicionados:

* **Presencial**: Carga horária total de atividades presenciais.
* **À distância**: Carga horária total de atividades a distância.
* **Síncrona**: Carga horária de atividades síncronas (com áudio e vídeo).
* **Síncrona mediada**: Carga horária de atividades síncronas mediadas com controle de frequência (máximo 70 alunos por docente).
* **Assíncrona**: Carga horária de atividades assíncronas.

Regras para os campos de carga horária:

* Ao criar uma disciplina na matriz, os campos de carga horária devem ser automaticamente preenchidos com os valores provenientes do cadastro da disciplina.
* A soma dos valores de Presencial e á distância não pode ultrapassar o valor do campo Total.
* A soma dos campos Síncrona, Síncrona mediada e Assíncrona não pode ultrapassar o valor do campo á distância.

Disponível a partir das versões: **12.1.2502.233, 12.1.2506.182 e 12.1.2510.116**.

Informações Complementares

---

[Disciplinas Filha](http://tdn.totvs.com/x/PvxbGQ)  
[Requisitos (Ensino Superior)](http://tdn.totvs.com/x/mvpbGQ)  
  
[Função de fórmula DiscEmCurso](http://tdn.totvs.com/x/M1H3Gg)
