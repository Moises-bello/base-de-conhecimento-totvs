---
content_hash: ec15706a385d4bac902c43f6096d338b9c8bbae2869fe1303f40cb31cd155675
fetched_at: '2026-06-29T00:10:30.412498+00:00'
page_id: '520094809'
product: rm
source: tdn-rm
title: Mudança de Turma Mista
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520094809
version: 34
---

A mudança de Turma Mista é um processo criado para facilitar a movimentação de alunos.

Para realizarmos uma mudança, é necessário possuir pelo menos um aluno matriculado em uma Turma Mista com disponibilidade em outra Turma Mista da mesma disciplina.

Possuindo o cenário anterior, basta selecionar o aluno que deseja e arrastá-lo para a próxima Turma Mista.

Lembrando que devido a essa nova funcionalidade foram incluídos alguns parâmetros e opções extras de informação para o usuário. Sendo elas: Situação da turma/disciplina de origem e destino, Cópia de presença diária para a turma de destino, cópia de notas para a turma de destino e a possibilidade de ignorar conflitos de horários.

Situação de matrícula de turma/disciplina de origem: Deve-se informar neste campo a situação que a turma/disciplina origem irá receber após a mudança de turma mista.

Situação de matrícula de turma/disciplina de destino: Deve-se informar neste campo a situação que a turma/disciplina destino irá receber após a mudança de turma mista.

Copiar registros de presença diária para a turma de destino: Deve-se marcar o parâmetro caso queira que as faltas e frequências dos alunos sejam copiados para a turma destino.

Copiar os registros de notas para a turma de destino: Deve-se marcar o parâmetro caso queira que as notas e notas de avaliação dos alunos sejam copiados para a turma destino.

Ignorar conflito de horário: Deve-se habilitar o parâmetro caso queira ignorar choques de horários.

O parâmetro de ignorar conflito de horário estará visível somente caso o usuário possua permissão de matricular aluno com choque de horário.

Na visão de matrículas disponíveis e de turmas disponíveis, foram incluídos ícones explicativos sobre o processo.

A partir das versões 12.1.27.179, 12.1.28.113 e release 12.1.29 o Importador do TOTVS Educacional foi alterado para contemplar o novo campo (IDTURMADISCPRINCIPAL) criado na tabela SMATRICULA para o vínculo da turma mista. O layout do importador é o 12.0.0.30. Para mais informações sobre o importador, acesse: .
