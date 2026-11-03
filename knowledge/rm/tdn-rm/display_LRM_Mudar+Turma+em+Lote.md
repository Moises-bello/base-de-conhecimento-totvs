---
content_hash: 49ed97fa48b3ddc1bdff39cee0f20ad5d06aeb0967664696dd58d306552e202d
fetched_at: '2026-06-29T00:10:20.021336+00:00'
page_id: '485425596'
product: rm
source: tdn-rm
title: Mudar Turma em Lote
type: documentation
url: https://tdn.totvs.com/display/LRM/Mudar+Turma+em+Lote
version: 23
---

Atenção ao Nível de Ensino.

Este processo está disponível apenas para o Nível de Ensino Básico.

O processo realiza a mudança de turma e/ou turno para um ou mais de um aluno, levando em consideração a matriz aplicada, o período letivo, turma origem e destino. É possível por meio deste processo mudar a turma e/ou turno de alunos de um mesmo curso e série, não sendo necessário serem da mesma matriz curricular, turno e/ou turma.

Durante o processo, através da matriz aplicada e do período letivo é possível selecionar os alunos que terão suas turmas alteradas pelo processo.

Atenção a seleção do mesmo aluno mais de uma vez

Caso o aluno seja selecionado mais de uma vez, o processo não irá executar nenhuma mudança de turma e/ou turno para este aluno, sendo que este problema será informado no log ao final do processo.

Após a seleção dos alunos deve-se selecionar os dados de destino e todos os parâmetros necessário para efetuar a mudança de turma para os alunos selecionados na tela anterior.

# Observações Importantes

* A situação de matrícula no período letivo de origem somente irá aparecer para ser preenchida, quando for uma troca de turno, caso contrário este campo não ficará visível.
* O campo turno de destino somente irá aparecer para ser preenchido, quando o aluno não possuir turma de origem, caso contrário não ficará visível.

Parâmetros e Validações

***Atente-se*** aos parâmetros e validações para que o sistema realize o processo de acordo com sua necessidade.

**Parâmetros:**

* **Copiar os registros de presença diária para a turma de destino**: realiza a copia das faltas e presenças das etapas e alunos presentes na turma.
* **Copiar os registros de notas para a turma de destin**o: realiza a copia de notas das etapas e alunos existentes na turma.
* **Aproveitar contrato na mudança de turma**: realiza o aproveitamento de contrato quando se troca o turno do aluno. Este parâmetro **somente** será **habilitado**, se houver uma **troca** de **turno**.
  + Quando **desmarcado** será **exibido** um grupo referente a data de **cancelamento do contrato**.

* **Copiar descontos por antecipação para novo contrato**: realiza a copia dos descontos por antecipação dos alunos para o contrato que será criado ao trocar de turno. Este parâmetro somente será habilitado, se houver uma troca de turno e se o parâmetro que faz o aproveitamento de contrato estiver desmarcado.
* **Apagar o número do diário da origem**: realiza a remoção das numerações presentes na turma origem.

**Validações:**

* **Ignorar turma cheia**: dá permissão ao processo para que ignore o número máximo de alunos.
* **Ignorar conflito de horário**: dá permissão ao processo para que ignore conflitos de horário caso haja algum.

Este processo não sofreu alteração, ou seja, ela apenas manipula as turmas/disciplinas normais do aluno. Tudo que for de **itinerário formativo** (apenas **ensino básico - novo ensino médio**) será ignorado. Este processo ainda passará por evolução.

A partir das versões **12.1.2205.252, 12.1.2209.204 e 12.1.2302.129,** este processo passou por uma reestruturação de layout e incremento de funcionalidade referente ao **itinerário formativo** (ensino básico), para mais informações sobre as regras .

No passo 1 foram criados três lookups conforme abaixo.

* Turma: serão selecionados apenas alunos cuja a turma seja a mesma preenchida na matrícula do período letivo do aluno.
* Itinerário formativo: serão selecionados apenas alunos que possuem matrícula em disciplinas do itinerário selecionado.
* Turma do itinerário formativo: serão selecionados apenas alunos que possuem matrícula em disciplinas de turmas do itinerário selecionado.

No passo 2, foi criado uma grid para fazer o de-para de origem e destino das turmas de itinerário formativo dos alunos selecionados, adicionado o parâmetro para mudança parcial das turmas do itinerário formativo e o parâmetro para não realizar a mudança de turmas de itinerário.

Vale ressaltar que as turmas de itinerário de origem apresentadas na grid é um agrupamento de todas as turmas em que os alunos selecionados estão matriculados.
