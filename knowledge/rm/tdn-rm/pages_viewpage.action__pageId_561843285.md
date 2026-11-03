---
content_hash: 1341318226c0a79d6f9261b55f7dc26a27815b292e4c391064d35cd610799cc4
fetched_at: '2026-06-29T00:10:48.382612+00:00'
page_id: '561843285'
product: rm
source: tdn-rm
title: Disponibilidade do Itinerário Formativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=561843285
version: 22
---

Nessa tela é possível cadastrar o período que o itinerário formativo ficará ofertado na matriz aplicada selecionada. Após finalizado o período de oferta, o itinerário formativo ofertado na matriz aplicada não ficará disponível na tela de [matrícula](https://tdn.totvs.com/x/4vtbGQ) para ser selecionado.

Se **não** houver cadastro de disponibilidade o itinerário formativo, o mesmo ficará sempre disponível. Para restringir é necessário criar um registro e informar uma data e hora do período de matrícula.

Para que seja possível enturmar o aluno no itinerário formativo na matrícula do portal do aluno é necessário informar uma turma neste cadastro, sem esta turma não é possível enturmar o aluno. Somente será exibido nesta seleção turmas que possuem no mínimo uma disciplina do itinerário correspondente.

A partir da versão **12.1.2205** seguem algumas mudanças de comportamento

Se dar por obrigatório para exibição das disciplinas marcar o parâmetro **Exibir disciplinas do itinerário formativo durante a matrícula no portal do aluno** e ter este registro criado no anexo da .

Para que o **itinerário formativo** seja **exibido** no portal do aluno no momento da matrícula é **obrigatório** criar o registro neste anexo para cada itinerário, caso o mesmo não exista, o itinerário passa a não ser exibido na matrícula no portal do aluno e no RM.exe.

Caso o aluno esteja matriculado em algum itinerário que não possua cadastro na disponibilidade não será possível prosseguir na matrícula do portal e nem no RM.exe, ou seja, é **obrigatório**ter o registro da disponibilidade de cada itinerário. Se for necessário deixar um itinerário indisponível utilize a data inicial e final do período de disponibilidade. Entretanto vale ressaltar que se o aluno estiver matriculado em itinerário que o mesmo esteja indisponível (pelas datas informadas) o mesmo será visível, porque o aluno está matriculado nele, caso contrário se não possuir matrícula o itinerário não será visível.

A partir da **12.1.2306** segue uma mudança de comportamento

Este cadastro passa a conter o campo **obrigatório**, que define se um itinerário formativo é obrigatório ou não durante a matrícula.

A partir da versão **12.1.2306.133** seguem algumas mudanças de comportamento

Ao marcar a opção, "Exibir disciplinas do itinerário formativo durante a matrícula no portal do aluno",ocampo Turma do Itinerário Formativo torna-se obrigatório.

Para verificar a disponibilidade das disciplinas de Itinerário Formativo no portal, o sistema ira validar se a [turma disciplina](https://tdn.totvs.com/display/LRM/Turma+Disciplina) referente a turma parametrizada em questão, está com a data inicial e final da matricula válida, ou em branco. E se a [turma disciplina](https://tdn.totvs.com/display/LRM/Turma+Disciplina) está ativa. Após essas validações as disciplinas são exibidas no portal.

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
* [Matricular Aluno](https://tdn.totvs.com/x/4vtbGQ)
* [Registro de avaliação por habilidades](https://tdn.totvs.com/x/Ygp9IQ)
