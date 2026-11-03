---
content_hash: 880fbec78c29d67795113b074e1aa09e26a640955617c6d5c875b16ad5490c28
fetched_at: '2026-06-29T00:05:48.077191+00:00'
page_id: '1022390706'
product: rm
source: tdn-rm
title: Matricular Aluno - Ensino Básico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1022390706
version: 1
---

# **Conteúdo**

Índice

# **Ensino Básico**

O processo de matrícula no Ensino Básico está disponível em Aluno | Processos | Matricular aluno.

Esse processo é responsável por matricular o aluno na série, mas também pode ser utilizado para matricular o aluno nas disciplinas da série, para isso a situação de matrícula do período letivo (definida no primeiro passo do processo, campo Situação Atual) deve estar com a seguinte opção marcada: **Status no Período Letivo | Matricular automaticamente nas disciplinas da turma**.

Esse processo é responsável por matricular o aluno na série, mas também pode ser utilizado para:

* Matricular o aluno nas disciplinas da série, para isso a situação de matrícula do período letivo, definida no primeiro passo do processo (campo Situação Atual), deve estar com a seguinte opção marcada: **Status no Período Letivo | Matricular automaticamente nas disciplinas da turma**.
* Matricular o aluno em [itinerários formativos](https://tdn.totvs.com/x/gjmeI).
* Matricular o aluno em [disciplinas do itinerário formativo](https://tdn.totvs.com/x/gjmeI).

O processo de matrícula do aluno é composto por alguns passos obrigatórios e outros que serão visíveis no processo de acordo com a parametrização do sistema. A seguir serão apresentados todos os passos e, no caso dos passos não obrigatórios, a parametrização necessária para que o passo seja exibido no processo.

## **Passo 1 - Matrícula no período letivo**

Nessa etapa devem ser inseridas as informações básicas sobre a matrícula do aluno no período letivo: Período Letivo, Matriz Aplicada, Turma, Tipo de Matrícula, Situação de Matrícula, Data de Matrícula, Informações sobre a Carteirinha.

Ao informar o turno a ser matriculado, serão exibidos os itinerários formativos válidos para a matriz aplicada. Dessa forma, o usuário tem a opção de selecionar os itinerários que o aluno será matriculado ao final da execução do processo:

Vale frisar que é permitido dizer se um itinerário formativo é obrigatório (configurado na ) e/ou utilizar , este processo sofreu alterações para se adequar a estas novas funcionalidades.

Caso **não** utilize o  o processo ficará conforme abaixo.

Caso utilize o  o processo ficará conforme abaixo.

Interessante dizer que em ambos os casos a obrigatoriedade de itinerário formativo será validada e todos itinerários obrigatórios são marcados automaticamente no momento do processo, porém é possível desmarcar manualmente.

## **Passo 2 - Problemas na matrícula do aluno no período letivo**

Essa etapa do processo mostrará possíveis problemas encontrado para matricular o aluno no período letivo e matriz aplicada escolhidos anteriormente e só será exibida caso algum problema seja encontrado.

## **Passo 3 - Documentos solicitados conforme parametrização do curso**

Para habilitar esse passo no processo de matrícula é necessário marcar o parâmetro **Educacional Matrícula | Movimento 1/3 | Informar documentos obrigatórios entregues**. Os documentos configurados na parametrização do curso, **TOTVS Educacional | Currículo e Oferta | Oferta | Parametrização por curso | Anexos | Documentos Exigidos**, serão apresentados nessa tela onde o usuário irá marcar a quantidade entregue e a data de entrega.

Neste passo é possível informar o **status**e/ou **motivo rejeição** (caso documento seja rejeitado)**.** Para saber mais o funcionamento sobre estes campos acesse .

## **Passo 4 - Disciplinas da matrícula do aluno**

Esse passo só estará disponível no processo quando o status definido no campo Situação Atual (passo 1) estiver parametrizado para matricular automaticamente nas disciplinas (**Status do período letivo | Matricular automaticamente nas disciplinas da turma**) e for selecionado uma Turma (passo 1) que esteja associado Disciplinas.

É nesse momento que o usuário deve selecionar as disciplinas que o aluno será matriculado.

A opção "Propagar a situação de matrícula ou tipo de matrícula definidos para todas as disciplinas" permite que ao alterar uma situação de matrícula/tipo de matrícula de qualquer disciplina, ela seja propagada para todas as outras disciplinas visíveis na tela.

O quadro de horário exibe o horário de todas as disciplinas selecionadas nesse passo e que possuem turma/disciplina configuradas com horário definido.

## **Passo 5 - Disciplinas do Itinerário Formativo**

Essa tela será exibida apenas quando for escolhido pelo menos um itinerário formativo para matricular o aluno, a turma selecionada no passo 1 tiver disciplinas do itinerário formativo ofertadas e o status definido no campo Situação Atual, passo 1, estiver parametrizado para matricular automaticamente nas disciplinas (**Status do período letivo | Matricular automaticamente nas disciplinas da turma**).

Nesse passo o usuário deve selecionar as ofertas de disciplinas do itinerário formativo que o aluno será matriculado. A tela é dividida em 4 quadrantes:

* Disciplinas → exibe os [itinerário formativos associados a matriz curricular](https://tdn.totvs.com/pages/viewpage.action?pageId=561059150) escolhida no passo 1 e suas disciplinas.
* Turmas → exibe as [turmas/disciplinas do itinerário formativo](https://tdn.totvs.com/x/jBVxIQ) que for selecionada no quadrante de disciplinas.
* Informações → esse quadrante vem comprimido ao lado do quadrante Turmas. Nele são exibidas as informações básica sobre a turma/disciplina selecionada no quadrante de Turmas como nome, código, início e término das aulas, professores da turma/disciplina, horários.
* Quadro de horários → são exibidos os horários das turmas/disciplinas selecionadas no quadrante Turmas.

Observações

1) O quadrante de Disciplinas permite multi-seleção utilizando a tecla Ctrl ou Shift.

2) Ao selecionarmos uma [turma/disciplina do itinerário formativo](https://tdn.totvs.com/x/jBVxIQ) para matrícula, a disciplina do itinerário formativo aparecerá em destaque no quadrante de disciplinas e as colunas Situação de matrícula e Tipo de matrícula serão preenchidas com o valor default definido em **Parâmetros | Educacional | Matrícula | Geral | Padrões para matrícula nas disciplinas**.

### Propagação de situação de matrícula ou tipo de matrícula

A opção **Propagar a situação de matrícula ou o tipo de matrícula definidos para todas as disciplinas** permite que ao alterar uma situação de matrícula/tipo de matrícula de uma disciplina do itinerário formativo selecionada, ela seja propagada para todas as outras disciplinas que possuem turma/disciplina marcada (as disciplinas do itinerário que estão em destaque do quadrante de disciplinas).

### Selecionar disciplinas da turma

No lookup de turma do itinerário formativo irá vir com o valor default com a **turma do aluno**, ou seja, a turma que foi selecionada no primeiro passo do processo. Somente irá ser exibido turmas que possuem no mínimo uma disciplina de itinerário formativo ofertada, caso contrário a turma não será visualizada neste lookup.

Vale frisar que se a turma do aluno, não possuir no mínimo uma disciplina de itinerário ofertada, a mesma não será visualizada no lookup de turma do itinerário formativo.

O botão  poderá ser acionado a qualquer momento, a sua finalidade é de preencher o lookup de turma do itinerário com a turma do aluno. Caso a turma do aluno não possuir disciplina de itinerário ofertada, ao clicar no botão  o sistema irá ecoar uma mensagem informando que não existe oferta de disciplina de itinerário para a turma do aluno.

Ao clicar no botão **Selecionar disciplinas da turma** serão marcadas para matrícula todas as disciplinas ofertadas na turma escolhida pelo usuário.

* Caso outra turma/disciplina que não seja da turma estiver marcada e o botão for pressionado, essa turma/disciplina será desmarcada e a disciplina da turma será marcada.
* Caso o aluno tenha matrícula em alguma disciplina que não seja da turma escolhida, essa disciplina não será desmarcada ao clicar neste botão.

## **Passo 6 - Problemas na matrícula do aluno nas disciplinas**

Essa etapa do processo mostrará possíveis problemas encontrados na matricula do aluno nas disciplinas e só será exibida caso algum problema seja encontrado.

Observações

As validações referentes ao itinerário formativo serão feitas nesse momento do processo de matrícula:

* Seleção das disciplinas do itinerário que foram definidas como obrigatórias no [cadastro de disciplinas do itinerário formativo](https://tdn.totvs.com/x/gjmeI).
* Validação do número mínimo e máximo de carga horária ou número de disciplinas do itinerário formativo a serem matriculadas (configuração feita no campo **Controle de matrícula por Carga Horária/Número de Disciplinas** no [cadastro do itinerário formativo](https://tdn.totvs.com/x/gjmeI))

*As validações citadas anteriormente serão executadas apenas quando pelo menos uma das disciplinas do itinerário formativo for selecionada para realização da matrícula do aluno. Caso nenhum disciplina tenha sido selecionada, as validações não serão executadas pois nesse caso o aluno está sendo matriculado no itinerário formativo e não nas disciplinas itinerário.*

## **Passo 7 - Lançamento, contrato e boleto**

Essa etapa do processo só estará habilitada se o status definido no campo Situação Atual, do passo 1, estiver configurado para exigir contrato financeiro no período letivo (Status do período letivo | Exige contrato financeiro).

As informações utilizadas para geração do contrato, lançamentos e boletos deverão ser informadas aqui.

O plano de pagamento será carregado **automaticamente** quando na  possuir um plano de pagamento default preenchido, lembrando que este plano de pagamento deverá ser **válido**.

Os Planos de Pagamento disponíveis para seleção devem estar previamente configurados, para mais informações sobre como configurá-los, acessar: .

**Passo 8 - Competência Contábil e Fiscal**

O último passo do processo permite ao usuário informar os dados sobre contabilização contábil e/ou fiscal.

Para que seja habilitado o sistema deve estar parametrizado para utilizar contabilização por competência e/ou utilizar movimento por competência:

Contabilização por competência:

**Parâmetros | Educacional | Integração | Contabilidade | Contabilidade 1/2 | Utilizar Contabilização por Competência**

**Parâmetros | Educacional | Integração | Contabilidade | Contabilidade 2/2 | Data Contábil | Data Contábil do Contrato**

Movimento por competência:

**Parâmetros | Educacional | Integração | Fiscal | Fiscal 1/2 | Utiliza Movimento por Competência**

**Parâmetros | Educacional | Integração | Fiscal | Fiscal 1/2 | Data de Competência | Data de Competência do Contrato e Plano de Pagamento**

Além disso, o status definido no campo Situação Atual (passo 1) deve estar configurado para exigir contrato financeiro no período letivo (Status do período letivo | Exige contrato financeiro).

Informações Complementares

---

**[Novo Ensino Médio](https://tdn.totvs.com/x/C3R9IQ)**

* [Área do conhecimento](https://tdn.totvs.com/x/njaeI)
* [Itinerário Formativo](https://tdn.totvs.com/x/gjmeI)
* [Competências e habilidades](https://tdn.totvs.com/x/8RVxIQ)
* [Itinerário Formativo da Matriz Curricular](https://tdn.totvs.com/x/ThVxIQ)
* [Estrutura Curricular](https://tdn.totvs.com/x/zf1bGQ)
* [Turma/Disciplina do Itinerário Formativo](https://tdn.totvs.com/x/jBVxIQ)
* [Parametrização por Curso](https://tdn.totvs.com/x/x-xbGQ)
* [Disponibilidade do Itinerário Formativo](https://tdn.totvs.com/x/VQx9IQ)
* [Registro de avaliação por habilidades](https://tdn.totvs.com/x/Ygp9IQ)
