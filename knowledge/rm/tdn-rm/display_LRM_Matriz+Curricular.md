---
content_hash: 51d24adae2143e8b9bf1e2e8be1e24ff9f637e3eda23abce709d80fbe1fe9023
fetched_at: '2026-06-29T00:09:32.733616+00:00'
page_id: '425458911'
product: rm
source: tdn-rm
title: Matriz Curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/Matriz+Curricular
version: 47
---

---

A matriz curricular é um conjunto de disciplinas que compõe o currículo acadêmico (teórico e prático) de um determinado [curso](http://tdn.totvs.com/x/Af9bGQ) e [habilitação](http://tdn.totvs.com/pages/viewpage.action?pageId=425458683). A matriz curricular está, obrigatoriamente, associada a uma coligada, curso e habilitação. Portanto, a definição de uma matriz curricular está associada ao conjunto [curso/habilitação.](http://tdn.totvs.com/pages/viewpage.action?pageId=425458938)

Os campos, anexos e processos da matriz curricular possuem comportamentos distintos nos contextos Básico e Superior.

**Ensino Básico**

A matriz curricular do ensino básico possibilita que seja informado qual o próximo curso, [série](http://tdn.totvs.com/pages/viewpage.action?pageId=425459707) e a próxima matriz curricular (se aplicável).

**Anexos:**

[Período](http://tdn.totvs.com/pages/viewpage.action?pageId=425458568)

[Matriz Aplicada](http://tdn.totvs.com/x/dPtbGQ)

[Disciplinas da Matriz Curricular](http://tdn.totvs.com/x/P-xbGQ)

[Disciplinas Optativas/Eletivas](http://tdn.totvs.com/pages/viewpage.action?pageId=425458716)

[Itinerários Formativos da Matriz Curricular](https://tdn.totvs.com/pages/viewpage.action?pageId=561059150)

[Grupo de disciplinas Optativas/Eletivas](http://tdn.totvs.com/pages/viewpage.action?pageId=425458519)

**Processos:**

[Copiar Matriz Curricular](http://tdn.totvs.com/x/Pv1bGQ)

[Ofertar Matriz Curricular](http://tdn.totvs.com/x/q-tbGQ)

 

[Associar matrizes aplicadas à Campus/Polo](http://tdn.totvs.com/pages/viewpage.action?pageId=425458507)

**Ensino Superior**

No contexto Superior, a Instituição de Ensino pode visualizar o total da carga horária das atividades complementares no 'Campo de Carga Horária de Atividades Complementares - **(C.h. de Atv.Compl.)**.

**Obs.:** Esse campo não existe no banco de dados portanto não é editável. O controle da carga horária é apenas visual. O objetivo é somar o total da carga horária das atividades complementares (componente) da matriz aplicada e exibir a soma na matriz curricular.

***Tipo de avaliação das atividades curriculares***

Pode ser por carga horária ou por créditos.

**Obs.:** Essa parametrização faz relação com a quantidade de horas ou créditos no item curricular que o aluno deverá cursar. O item curricular é acessível através do anexo Componentes - Item Curricular disponível na Matriz Curricular.

Esta parametrização obriga que os alunos que cursam essa matriz devem cursar o valor mínimo informado de carga horária ou créditos.

***Status***

A matriz curricular possui 3 status:

* **Ativa:** Indica que a matriz pode ser utilizada na realização da matrícula dos alunos.
* **Inativa:** Indica que a matriz não pode ser utilizada.
* **Atual:**Indica que a matriz é a atual ou seja na realização da matrícula dos alunos essa matriz será preenchida automaticamente. Fica a critério do usuário alterar para outra matriz ativa**.**

***Controle de vaga***

Este controle é utilizado na verificação de vagas disponíveis para matrícula em determinada turma. As opções disponíveis são:

1. Por turma
2. Por disciplina da turma

**Obs.:** Caso a matriz possua controle de vaga, o campo número máximo de alunos será obrigatório no [cadastro de turma](http://tdn.totvs.com/x/yP1bGQ) ou no [cadastro de Turma/Disciplina.](http://tdn.totvs.com/x/C-9bGQ)

***Mínimo e Máximo de Créditos***

Esses campos permitem que a Instituição informe a quantidade créditos mínimos e máximos. Esta quantidade será validada no processo de matrícula do aluno, sendo que o sistema irá verificar se a quantidade mínima de créditos foi atendida pelas disciplinas a serem matriculadas e se a quantidade máxima não foi extrapolada. A quantidade mínima somente irá ser validada se ela é menor do que a soma dos créditos das disciplinas restantes a serem cursadas.

**Exemplo:** supondo que a quantidade mínima é 10, mas para o aluno resta apenas cursar uma disciplina com crédito igual a 5, como não é possível atingir o mínimo o sistema não irá validar o mesmo. Por outro lado, se existissem três disciplinas a serem cursas e cada uma delas possuir 5 de créditos e se for tentar matricular o aluno em apenas uma disciplina, o sistema vai bloquear, pois não foi atingido o mínimo de créditos.  
Os campos 'Fórmula para cálculo da média global' e 'Fórmula do coeficiente de rendimento' são exclusivos no contexto Superior.

**Perc. CH Extensão**

Este campo foi incluído a partir das versões **12.1.2310.164** e **12.1.2402.104** para informar, em percentual, quanto da carga horária total da matriz curricular corresponde às atividades de extensão.

A partir da versão **12.1.2406**, houve uma alteração para que a informação registrada passe a ser o **número de horas**, e não mais o percentual, trazendo assim maior assertividade aos dados informados.

O valor informado será utilizado na análise curricular do aluno para calcular tanto a carga horária de atividades de extensão exigida quanto a pendente no currículo do aluno.

Também na Geração de Diploma, ao verificar a conclusão do curso, o sistema irá validar dentre outros requisitos, se o aluno cumpriu a carga horária de extensão mínima exigida baseado nesse percentual para que o aluno seja considerado apto.

> ***ATENÇÃO:***Seguindo a Resolução nº 7, de 18 de dezembro de 2018  
> Art. 4º As atividades de extensão devem compor, no mínimo, 10% (dez por cento) do total da carga horária curricular estudantil dos cursos de graduação, as quais deverão fazer parte da matriz curricular dos cursos; 

Sendo assim, ao criar uma nova Matriz Curricular, em níveis de ensino que utilizam a apresentação do contexto de "Ensino Superior" (no cadastro do Nível de ensino), o campo ***Perc. CH extensão*** será preenchido automaticamente com o valor "10,000", podendo ser alterado para um valor "vazio" ou maior que "10,000", de acordo com a necessidade da instituição.

**Observação:** Incluído o campo [Ênfase](https://tdn.totvs.com/pages/viewpage.action?pageId=993698315) no cadastro da matriz curricular.

   No anexo foi incluído a [linha de formação e pesquisa](https://tdn.totvs.com/pages/viewpage.action?pageId=993698358) com a opção de informar mais de uma.

Funcionalidade disponível a partir dos patchs 12.1.2410.308, 12.1.2502.216, 12.1.2506.165 e 12.1.2510.100.

A partir da versão **12.1.2406**, foi incluído o parâmetro **oferta ativa** na [matriz aplicada](https://tdn.totvs.com/pages/editpage.action?pageId=425458548) que permite habilitar ou desativar a matriz aplicada para a vinculação da oferta.

Para realizar a associação é necessário que o status da matriz curricular seja Ativa ou Atual. Para a matriz curricular inativa o parâmetro oferta ativa fica desabilitado, impossibilitando a utilização desta matriz aplicada.

 A partir das versões **12.1.2502.232**, **12.1.2506.181** e **12.1.2510.115**, o sistema permite o cadastro detalhado da **Composição da Carga Horária** e da **Distribuição por Modalidade** dos cursos.

**Composição da carga horária**

Neste agrupamento o usuário registra a distribuição da carga horária total entre diferentes componentes curriculares do curso.

Campos disponíveis criados:

* CH Disciplinas Obrigatórias
* CH Disciplinas Optativas/Eletivas
* CH Atividades Complementares
* CH Estágio Supervisionado
* CH Trabalho de Conclusão de Curso (TCC)
* CH Extensão *( Campo já existente no sistema)*

**Observação:**

A soma de todos os campos deste agrupamento não deve ultrapassar o valor da Carga Horária Total do curso.

Caso seja diferente, o sistema exibe um alerta informativo:

 "A soma dos componentes da carga horária deve ser igual a carga horária da matriz curricular."

A mensagem não impede o salvamento, apenas informa o usuário para conferência.

**Distribuição por Modalidade:**

Neste agrupamento, o usuário poderá definir a forma de oferta das aulas (Presencial, EaD).

Campos disponíveis criados:

* CH Presencial
* CH à Distância (EaD)
* CH Síncrona
* CH Síncrona Mediada
* CH Assíncrona

#### Soma de CH Presencial + CH à Distância (EaD):

Refere-se à Carga Horária Total do curso.

A soma não pode ultrapassar o valor total informado.

Caso seja diferente, o sistema exibe um alerta:

 "A soma dos componentes da carga horaria por modalidade deve ser igual a carga horária da matriz curricular."

#### Soma de CH Síncrona + CH Síncrona Mediada + CH Assíncrona:

Refere-se à CH à Distância (EaD).

A soma não pode ultrapassar o valor de CH à Distância (EaD) informado.

Caso seja diferente, o sistema exibe um alerta:

 "A soma dos componentes da carga horaria á distância deve ser igual a carga horária á distância (EAD). "

Informações Complementares

---

 

 

[Período](http://tdn.totvs.com/pages/viewpage.action?pageId=425458568)

[Matriz Aplicada](http://tdn.totvs.com/x/dPtbGQ)

[Disciplinas da Matriz Curricular](http://tdn.totvs.com/x/P-xbGQ)

[Disciplinas Optativas/Eletivas](http://tdn.totvs.com/pages/viewpage.action?pageId=425458716)

[Itinerários Formativos da Matriz Curricular](https://tdn.totvs.com/pages/viewpage.action?pageId=561059150)

[Grupo de disciplinas Optativas/Eletivas](http://tdn.totvs.com/pages/viewpage.action?pageId=425458519)

Como Fazer

---

[Copiar Matriz Curricular](http://tdn.totvs.com/x/Pv1bGQ)[Ofertar Matriz Curricular](http://tdn.totvs.com/x/q-tbGQ)[Atualizar número e valor de créditos das disciplinas](http://tdn.totvs.com/pages/viewpage.action?pageId=425459077)[Associar matrizes aplicadas à Campus/Polo](http://tdn.totvs.com/pages/viewpage.action?pageId=425458507)
