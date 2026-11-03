---
content_hash: e8dc033fafd5f420489d6d5d01732c06536c89590ed2c6a1d10907d72a28c2a9
fetched_at: '2026-06-29T00:09:32.459780+00:00'
page_id: '425458852'
product: rm
source: tdn-rm
title: Digitação de frequência diária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458852
version: 40
---

A digitação de frequência diária é uma funcionalidade que permite ao professor lançar faltas para o aluno usando como filtro os dias letivos da turma/disciplina.

Realizar frequência diária

Ao realizar a frequência diária dos alunos deve-se, obrigatoriamente, informar os seguintes campos: **Período letivo,** **Disciplina e** **Etapa**

**Não é possível** realizar o lançamento de uma frequência para uma data futura

Caso o sistema apresenta alguma **inconsistência**, **não será salva nenhuma informação**, como a frequência lançada, a liberação, o sincronismo de faltas na etapa

Situação da matrícula

O filtro ira listar os alunos com a situação de matrícula na disciplina conforme regra abaixo:

* Se o aluno **tiver** resultado final (aprovado, reprovado, etc), este filtro vai considerar a situação final do aluno;
* Se o aluno **não tiver** resultado final, este filtro vai considerar a situação do aluno na disciplina;
Bloquear alterações de notas e faltas

A fórmula da etapa selecionada será executada apenas para os alunos que estiverem com a opção "Bloquear alterações de notas e faltas" **desmarcada** na situação de matrícula na disciplina.

Permissão de acesso

Essa parametrização acima será desconsiderada se o parâmetro educacional "**Alterar notas e faltas bloqueadas por situação de matrícula**" estiver marcado para o usuário logado.

Liberar frequência após salvar

A tela conta com a funcionalidade de liberação de frequência diária. Quando a opção de liberar estiver marcada, também será marcado o campo de controle "FrequenciaDispWeb" do plano de aula (SPLANOAULA.FREQUENCIADISPWEB = 1).

Após a frequência ter sido liberada para os Alunos, o usuário **não** poderá alterar os registros de frequência para os horários do Aluno.

Para que isso, seja feito, será necessário **cancelar a liberação da frequência diária** através do processo: **[Liberar / Cancelar Frequência diária](https://tdn.totvs.com/x/1sMpJw)**.

Exibir a oção de liberar frequência diária após salvar

A opção de “Liberar frequência diária após salvar” será exibida apenas se o parâmetro “Justificar as faltas e liberar a frequência pelo coordenador definido na turma/disciplina” estiver **desmarcada** em Configurações | Parâmetros | Educacional | Secretaria | Notas/Faltas

Justificativa de falta

O sistema possui a funcionalidade de permitir o professor justificar a falta de um aluno. Essa justificativa pode abonar ou não a falta, isso é definido na tela de [Cadastro de Justificativa de Falta](http://tdn.totvs.com/x/pfpbGQ)

Para justificar basta clicar com o botão direito do Mouse e selecionar a justificativa.

Execução de fórmulas

O sistema ao realizar uma frequência, executa a fórmula cadastrada na etapa de falta selecionada automaticamente caso esteja com o parâmetro “Executar fórmulas automaticamente” **marcado** em **Configurações | Parâmetros | Secretaria | Notas/Faltas**.

A fórmula também será chamada quando o campo de número de aulas dadas for alterado, entretanto somente para os alunos que possuam este campo diferente na etapa.

Alteração de aulas dadas

Suponhamos que a frequência diária listou 60 alunos, e 30 deles possuem aulas dadas igual 10 e os demais 40. Ao informarmos o valor de 40 e salvar, a fórmula será executada apenas para os outros 30 alunos cuja aulas dadas esta igual a 10.

Liberação de frequência sem interação com grid

Para realizar a liberação da frequência sem a necessidade de interagir com a tabela de frequência é necessário:

* O parâmetro "**Justificar as faltas e liberar frequência pelo coordenador definido na Turma/disciplina**" esteja **desmarcado** em **Educacional | Secretaria | Notas/Faltas**
* A opção na tela ***"*Liberar frequência** **após salvar"** esteja **marcado**.
* Preencher o campo *"***Número de Aulas dadas"** da tela.

Sincronizar o número da faltas do aluno na etapa

O sistema possui o recurso de sincronizar o número de faltas do aluno na etapa com base na quantidade de faltas diária lançadas, caso atenda as seguintes regras:

Campo "Aulas dadas" preenchido

O sistema irá contabilizar somente se o campo **"Aulas dadas"** esteja **preenchido**.

Subturma

O sistema irá contabilizar as faltas atendendo o critério da subturma. Caso a subturma seja selecionada, o sistema irá contabilizar as faltas apenas dos alunos da subturma selecionada, caso não seja selecionada nenhuma subturma ou não exista, será contabilizado as faltas para todos os alunos da turma/disciplina.

Período da etapa 

O sistema irá considerar as etapas de faltas que atenderem os critérios, se a etapa esteja:

* Se **"Data de início"** e**"Data de término"** **não** **preenchida** (em branco);
* Se **"Data de início"** e**"Data de término" esteja** **preenchida** e a **data da falta** (data em que o aluno recebeu a **ausência**) esteja dentro deste período.

Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina

O sistema irá contabilizar somente se o parâmetro "**Justificar as faltas e liberar frequência pelo coordenador definido na turma/disciplina**" estiver **desmarcado**. Este parâmetro se encontra: **Parâmetros | Secretaria | Notas/Faltas**

Após o **coordenador realizar a liberação da frequência do dia**, o sistema irá realizar o **sincronismo automaticamente.**
