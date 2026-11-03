---
content_hash: 86bb0448aee4f2c0deefdba631a97857b987b33168089bb661ac58ba59868a4a
fetched_at: '2026-06-29T00:09:34.129737+00:00'
page_id: '425459150'
product: rm
source: tdn-rm
title: Matrícula na disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459150
version: 14
---

Esta tela contém as informações da matricula do Aluno na(s) disciplinas.

Para que o Aluno possa efetuar a matrícula nas Turmas/ Disciplinas, a Secretaria Acadêmica realiza a configuração de controle de vagas\*.

Ao iniciar o processo de Matrícula do Aluno na Turma/disciplina, o usuário consegue identificar se as turmas/disciplinas possui vagas disponíveis através da sugestão de disciplinas. Caso não existam vagas, o usuário não conseguirá selecionar a turma/disciplina, a mesma ficará disponível apenas para visualização (Apenas para ensino superior).

Se o aluno realizar a matrícula no Portal, a Turma/disciplina terá o mesmo comportamento, o aluno não conseguirá selecionar, apenas visualizar o cadastro.

O controle de vagas utilizará a configuração informada na [Matriz Curricular](https://tdn.totvs.com/x/3-xbGQ), sendo elas:

* Controle por Turma
* Controle por Turma/Disciplina da Turma

Na aba de dados adicionais na edição da matrícula na disciplina o parâmetro "Considerar no cálculo de cobrança somente para parcelas com vencimento igual ou posterior a data da matrícula", quando este estiver marcado em uma disciplina o sistema irá calcular o valor desta disciplina levando em consideração a data de matrícula.   
Para mais informações sobre o comportamento desse parâmetro acesso o documento [Aumento e Cancelamento de disciplinas - Cobrança por crédito](https://tdn.totvs.com/pages/viewpage.action?pageId=546264605).

**Matricula em disciplina para alunos inadimplentes:**

Foi criado o parâmetro de Tesouraria "Mostrar valor original total na validação de inadimplência" que fará com que o valor final mostrado para o usuário na mensagem de validação de inadimplência seja o valor total original dos lançamentos vencidos.

Na marcação desse parâmetro, como o sistema não precisará mostrar o valor total líquido na mensagem de validação, será calculado o valor líquido de cada lançamento e somado nos cálculos anteriores. Caso esse valor seja maior do que o valor do parâmetro "Valor máximo de tolerância para inadimplência", o sistema não processará o valor líquido do restante da lista de lançamentos.

Portanto, ao marcar o parâmetro, o tempo de repostas do processo tende a ser menor.

 Informações Complementares

---

[Sugestão de Disciplinas](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425458566)

 Veja Também

---

[Boletim Técnico - Desabilitar Disciplinas Sem Vagas na Matrícula](http://tdn.totvs.com/pages/viewpage.action?pageId=160105037)
