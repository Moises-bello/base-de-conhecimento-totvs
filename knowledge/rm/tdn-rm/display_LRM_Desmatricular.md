---
content_hash: 62833ab91a063caf3534775275108be734f992fdfd3f27f03ffa335d0c74bba0
fetched_at: '2026-06-29T00:09:31.870600+00:00'
page_id: '425458760'
product: rm
source: tdn-rm
title: Desmatricular
type: documentation
url: https://tdn.totvs.com/display/LRM/Desmatricular
version: 17
---

No processo de desmatricular o aluno através do processo seletivo é necessário que o mesmo tenha sido matriculado através do processo:  Processo Seletivo RM > Matricular.

Para listar os alunos para desmatricular, o usuário terá que informar o Período Letivo, o Processo Seletivo e a situação de matrícula.

Após informar os dados acima, o usuário irá clicar no botão Avançar, onde irá listar a relação de todos os alunos que foram matriculados através do processo em questão conforme a área ofertada informada que estão com status na opção como "Compareceu a Chamada" (Código do status 7).

Após a seleção do(s) aluno(s) , o usuário terá a possiblidade de escolher uma situação de matrícula e um motivo para os alunos, que possuírem algum tipo de impedimento, possam ter suas vagas liberadas no Processo Seletivo e no Educacional.

Versão disponível

Essa etapa do processo, somente está disponível a partir da versão 12.1.31.201 e 12.1.32.138.

São 3 possíveis cenários ao final do processo:

1. Caso o aluno não possua nenhum impedimento, o sistema irá excluir o aluno, do Educacional, e o status da opção na inscrição do Processo Seletivo será classificado como "Não compareceu à chamada" e sua vaga será liberada.
2. Caso o aluno tenha um impedimento, ele não será excluído e terá sua situação de matrícula redefinida, conforme selecionada no processo. No Processo seletivo, o seu status de opção, na sua inscrição, será definido como "Não compareceu à chamada" e sua vaga será liberada.
3. Caso o aluno tenha um impedimento e nenhuma situação de matrícula seja selecionada, ele não será excluído e sua situação não será alterada. O Processo Seletivo permanecerá inalterado e sua vaga não será liberada.

**Impedimentos:**

São considerados impedimentos:

* Contratos assinados.
* Parcelas com lançamentos gerados.
* Atendimento criado no TOTVS Gestão de Relacionamento com o Cliente.

As situações de matrícula que serão exibidas para seleção devem obedecer a seguinte regra de parametrizações:

**Ensino Básico:**

* Aba Status no período letivo, opção "No período letivo" deve estar marcada;
* Parâmetro "Altera situação de matrícula nas disciplinas para:" deve possuir alguma situação preenchida;
* Aba Status na disciplina, opção "Na disciplina" deve estar marcada;
* Parâmetro "Conta como aluno matriculado na turma" deve estar desmarcada.

**Ensino Superior**

* Aba Status no curso, opção "No Curso" deve estar marcada;
* Aba Status no período letivo, opção "No período letivo" deve estar marcada;
* Parâmetro "Altera situação de matrícula nas disciplinas para:" deve possuir alguma situação preenchida;
* Parâmetro "Altera situação de matrícula do aluno no curso para:" deve possuir alguma situação preenchida;
* Aba Status na disciplina, opção "Na disciplina" deve estar marcada;
* Parâmetro "Conta como aluno matriculado na turma" deve estar desmarcada.

Ao final do processo será possível ver o log onde será listado todos os alunos selecionados e sua situação após o processo.

Caso o aluno esteja matriculado em algum [itinerário formativo](https://tdn.totvs.com/pages/viewpage.action?pageId=547240322), o mesmo será desmatriculado. Este recurso esta disponível a partir da 12.1.27.

Caso o responsável financeiro do aluno possua vinculo com o cadastro de pessoa o processo não vai excluir o cadastro do responsável financeiro e será mostrado uma observação no log do processo (a matricula será desfeita com sucesso).

Exclusão do cadastro de pessoa 

Nos casos em que a pessoa relacionada ao aluno tiver um vínculo com outro sistema, como o TOTVS Gestão de Pessoas por exemplo, o processo de desmatricular será realizado porém a pessoa relacionada não será excluída (somente o registro do aluno será excluído).

Quando este cenário ocorrer o processo será concluído com sucesso, no entanto será mostrado no LOG conforme o exemplo abaixo a mensagem de alerta.
