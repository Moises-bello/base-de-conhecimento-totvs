---
content_hash: e539db2eadad81f69066cca3bf42205aca2fa22ad8ef1f33134b02678f4fbc16
fetched_at: '2026-06-29T00:05:48.095065+00:00'
page_id: '102268973'
product: rm
source: tdn-rm
title: Matrícula entre Filiais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=102268973
version: 2
---

| Produto | TOTVS Educacional |
| --- | --- |
| Processo | Matrícula |
| Subprocesso | Matrícula entre Filiais |
| Versão | 11.80 |

A funcionalidade busca facilitar o dia a dia das instituições de ensino que operam com diversas filiais. É comum hoje, em instituições de ensino superior, alunos cursando disciplinas no formato online ou em diversos locais físicos. É o resultado das restrições no contexto educacional quando se trata de ofertas de turmas, matrículas de alunos, otimização de campus e gestão de resultados

Basicamente, o aluno com vínculo único no curso, período letivo e contrato financeiro, poderá enturmar-se em quaisquer turmas de contextos pré-definidos, sem a necessidade de procedimentos na matrícula/transferência do mesmo entre filiais.

**Desenvolvimento/Procedimento**

1. Em um determinado contexto, matricular o aluno em um Curso/Habilitação, Período Letivo, Turma e Turma/disciplina.  
   1. Faça a matricula do aluno em um curso/habilitação. Acesse: **Currículo e Oferta | Aluno e Professor | Aluno | Curso/Habilitação.**
   2. Após vincular o aluno ao curso faça a matricula no período letivo e na turma. Acesse: **Currículo e Oferta | Aluno e Professor | Aluno | Curso/Habilitação | Matricular Aluno.**
   3. Por último matricule o aluno em uma turma/disciplina pertencente a sua filial de origem. Acesse: **Currículo e Oferta | Aluno e Professor | Aluno | Curso/Habilitação | Matricula no Período Letivo | Matricular Aluno nas Disciplinas.**
2. Parametrizar o sistema para que sejam exibidas disciplinas de outras filiais como opção durante o processo de matricula do aluno.  
     
   1. Acessar: **Configurações | Parâmetros | Matricula | Sugestão de disciplinas.**

      1. Marcar as 2 últimas opções: "De outras filiais que não sejam a do aluno (matrícula presencial)" e "De outras filiais que não sejam a do aluno (matrícula pelo portal)"
   2. Acessar o cadastro da parametrização por curso **Currículo e Oferta | Oferta | Parametrização por curso.**

      1. Marcar o parâmetro "Permite matrícula em turmas-disciplinas de filiais diferentes". OBS: Este parâmetro por padrão já fica marcado.
3. O próximo passo é realizar a relação de cadastro entre as filiais. Nessa etapa temos que cadastrar o "de-para" de período letivo e turno entre as filiais. Ou seja, é nesse passo que vamos dizer para o sistema que, por exemplo, o período 2012/2 turno Manhã (filial Belo Horizonte) é igual ao período 2012-2 turno Matutino (filial São Paulo)...  
     
   1. Acesse "**Currículo e Oferta | Acadêmico | Relação de cadastro | Entre filiais de mesma coligada**".
   2. Preencha os dados da coligada de origem e de destino: Coligada, filial e nível de ensino. Após preencher carregue os dados.
   3. Após preencher e carregar os dados de origem e destino devemos cadastrar o "de-para" de período letivo e turno entre as filiais. Ou seja, é nesse passo que vamos dizer para o sistema que por o período x (filial Belo Horizonte) é igual ao período y (filial São Paulo) ...
   4. Por último Seguindo a mesma ideia do cadastro anterior, devemos também realizar o "de-para" de turno, pois devemos informar ao sistema que o turno [x] MANHÃ (BH) é igual ao turno [y] Manhã (SP)...
4. Matricular o aluno em disciplinas de outras filiais.  
   1. Acesse: **Currículo e Oferta | Aluno e Professor | Aluno | Curso/Habilitação | Matricula no Período Letivo | Matricular Aluno nas Disciplinas.**
   2. Observe que na lista de sugestão de disciplinas estarão listadas turmas/disciplinas de outras filiais, lembrando, que serão exibidas apenas disciplinas da filial selecionada no processo de ‘Relação de Cadastro’ (item 3).
   3. Selecione uma turma/disciplina de outra filial que não seja a do aluno e conclua o processo de matricula.
