---
content_hash: a1d5b550ce8f6538d38f22e8559d04299f1fc15da27ec2d0f2793f63f0169854
fetched_at: '2026-06-29T00:09:36.099579+00:00'
page_id: '425459467'
product: rm
source: tdn-rm
title: Turma Disciplina
type: documentation
url: https://tdn.totvs.com/display/LRM/Turma+Disciplina
version: 53
---

As turmas/disciplinas são as disciplinas de uma matriz curricular, que são vinculadas as turmas e então, disponibilizadas para que os alunos possam cursá-las.

O cadastro da turma/disciplinas pode ser executado de três formas:

1. Currículo e Oferta | Oferta | Turmas/disciplinas
2. Currículo e Oferta | Oferta | Turma | Anexo | Turma/disciplina
3. Currículo e Oferta | Oferta | Turma | Processo | [Cadastrar turmas/disciplina](http://tdn.totvs.com/x/YPtbGQ)

Observações

Com a entrada em vigor do novo ensino médio, também será possível cadastrar [turmas/disciplinas a partir de disciplinas de itinerários formativos](https://tdn.totvs.com/pages/viewpage.action?pageId=561059212) vinculados a matriz curricular do aluno.

Na tela de cadastro da turma/disciplina o usuário pode inserir prédio e sala.  Caso ocorra um choque de horários, prédio/sala entre Turma/disciplina distintas, o sistema irá exibir uma mensagem de confirmação para o usuário decidir se continua a gravação ou não.

O sistema possibilita reservar vagas para calouros limitando vagas para alunos de outro curso. Para que isso seja possível o usuário deve informar no cadastro da turma/disciplina o número de vagas para calouros e o número de vagas para alunos de outros cursos, ou seja, alunos de cursos diferentes do vinculado a turma/disciplina em questão.

No ato da matrícula do aluno em "Curso/Habilitação/Período Letivo "será verificado se o aluno é calouro, caso positivo, será analisado o número de vagas disponíveis através do campo número de vagas para calouros da Turma / Disciplina que se está matriculando, se não houver vagas o usuário será notificado sobre a impossibilidade de prosseguimento do processo. Isto também ocorrerá para matrícula de alunos de outros cursos, porém o campo da Turma/Disciplina analisado será o número de vagas para alunos de outros cursos. Lembrando sempre que o número de vagas para calouros tem caráter de RESERVA e o número de alunos de outros cursos tem caráter de LIMITE. É importante ressaltar que um aluno calouro é aquele matriculado apenas no primeiro período; possui uma única matricula no período letivo.

**Cobrança por crédito Turma Livre:** Na tela de cadastro de turma disciplina existem dois campos para preenchimento referente a cobrança por créditos: Número de créditos para cobrança e Valor do crédito para permitir a cobrança de matrículas livres (Isoladas) em turmas livres (Isoladas), lembrando que estes campos apenas vão estar habilitados se a turma disciplina não possuir matriz aplicada. Para saber mais sobre o calculo, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=590628080)

No cadastro da Turma/Disciplina, possuem dois campos: Data Inicial e Data Final, que determinam o [Período de Aula da Turma/Disciplina](http://tdn.totvs.com/x/tvpbGQ).

No cadastro da Turma/Disciplina pode informar o link para [aula online](https://tdn.totvs.com/display/LRM/Aula+Online?moved=true) pelo campo "Aula Online". O link ficará disponível nos portais Educacionais para o aluno e para o professor. O professor poderá atualizar ou informar um novo link da aula online pelo portal do Professor.

O usuário tem a opção de definir também qual o tipo da Turma/disciplina:

* P - Presencial;
* D - Distância;
* S - Semipresencial.

No processo de Matrícula em turmas disciplinas através do Portal, o aluno irá visualizar o tipo da Turma/Disciplina através das siglas com cores diferenciadas para cada Tipo. 

No Processo de Matrícula nas Turmas/disciplinas através do RM.exe, o usuário da Secretaria Acadêmica, irá visualizar o Tipo das Turmas/disciplinas através do Tipo definido sem abreviações. 

Na tela de cadastro de turma disciplina existe um parâmetro "Turma Disciplina Gerencial" que Possibilita aos usuários do sistema trabalhar com turma/disciplina gerencial, que é usada para agrupar outras turmas/disciplinas (gerenciadas) podendo ter diferentes disciplinas, filiais e contextos, porém com o mesmo modelo de etapa e avaliação.

É possível também através desse processo a criação de turmas e turmas/disciplinas em lote. Também foi implementada a geração de horários e a associação dos professores nestas novas turmas/disciplinas.

1. Acesso à Funcionalidade: a funcionalidade está disponível através do TOTVS Educacional, no menu Atividades Acadêmicas | Assistentes | Cadastro de Turma e Turma/Disciplina;
2. Após avançar pela tela de apresentação do processo, informe os campos período letivo, (matriz aplicada) curso, habilitação, matriz curricular e turno;
3. Ao avançar no passo anterior, informe os dados para a criação das turmas.  A geração em lote pode acontecer de duas formas: "Criar uma turma para cada turma/disciplina" ou conforme o campo Geração em Lote, que permite criar "n" turmas, cada uma com o conjunto de turmas/disciplinas que será selecionada em um passo mais adiante;
4. Avance e Informe dados da Turma/Disciplina;
5. Em seguida, escolhas as disciplinas;
6. Em seguida, o usuário pode associar à disciplinas escolhidas, o horário e professor;
7. Em seguida, avance e execute o processo;
8. Agora iremos testar a geração em lote criando uma turma para cada turma/disciplina, para tal, clique no checkbox "Criar uma turma para cada turma/disciplina", além de informar os dados pertinentes e comuns às turmas a serem criadas;
9. Avance e repita o 4º passo;
10. Escolha novamente as disciplinas, porém com uma diferença, iremos entrar com a quantidade de turmas a serem geradas por turma/disciplina;
11. Repita o 6º passo, veja que as disciplinas estão repetidas conforme a quantidade informada. Pode-se fazer a associação dos horários e professores da mesma forma feita no passo 6;
12. Em seguida, avance e execute o processo para finalizar.

Alguns parâmetros disponíveis na tela de cadastro de etapa são comuns para as etapas de notas e de faltas:

* Parâmetros
  + Etapa Final

Este parâmetro quando marcado identifica a etapa como final. Não permite a criação de etapas posteriores.

* + Exibe no Portal

A instituição tem a opção de exibir ou não a etapa no portal para digitação de notas e faltas pelo professor.

* + Disponível para os alunos

Este parâmetro quando marcado libera a etapa para que os alunos possam acessar os dados no portal tanto de notas quanto de faltas.

Permitir a visualização das notas e faltas da etapa somente após liberação do professor

O parâmetro que permite visualização da nota após a liberação do professor também será considerado.  
Ou seja, caso o parâmetro do Educacional**(Configurações | Parâmetros| Secretaria | Notas/Faltas |Permitir a visualização das notas e faltas da etapa somente após liberação do professor)**estiver **marcado** as notas de etapa só serão apresentadas após liberadas.

caso o parâmetro acima citado, esteja **desmarcado,** no cadastro da etapa, a flag "Disponível para os alunos" não será exibida.

Parâmetro **marcado**                                                  Parâmetro **desmarcado**

         

* + Etapa encerrada

Este parâmetro identifica que a etapa foi finalizada. A partir do momento que este parâmetro está marcado, os professores não conseguem mais fazer nenhuma alteração nas etapas referente a notas, faltas, conteúdo...    
**Observação:** Foi incluído um parâmetro no perfil de usuário para permitir alterações no plano de aula quando a etapa estiver encerrada.

* + Permite digitação diretamente na etapa

Este parâmetro quando demarcado impede a digitação de notas e faltas bloqueando o campo

* + Etapa de notas:

A coluna "Nota" não permitirá digitação, bem como a coluna "Comentário", onde não será aberto pop-up para digitação.

* + Etapa de Faltas:

A coluna "Falta" não permitirá digitação, bem como a coluna "Nº Aulas". As informações do campo "Nº de aulas dadas" não serão replicadas para a coluna "Nº Aulas".

Filtro por usuário - STURMADISC

A visão de turma/disciplina e seus lookups poderão receber o filtro por usuário no cadastro de usuário, pela tabela STURMADISC, ou seja, se um usuário receber um filtro que não poderá ver turmas/disciplinas do período letivo com o id. igual a 35, conforme imagem abaixo, ao abrir a visão de turma/disciplina não irá ser possível visualizar as turmas/disciplinas com o id. do período letivo igual a 35.

Não é exibido as turmas/disciplinas do id. período letivo igual a 35.

Informação

Os campos “Adicional” e “Adicional noturno” são apenas informativos, ou seja, não são utilizados no cálculo da folha de pagamento.

A regra de processamento do adicional noturno seguirá as parametrizações do TOTVS Gestão de Folha de Pagamento.

A partir das versões **12.1.34.164**, **12.1.2205.107** e **12.1.2209** (release) houveram alterações na tela.

Renomeado a aba "Períodos de matrícula" para "Informações adicionais".

Foram  movidos da aba Identificação para Informações adicionais os seguintes campos:

* Aula online;
* Agenda Infantil;
* Centro de custo;
* Adicional extra;
* Adicional noturno;
* Agrupamento de "Créditos para cobrança" com seus campos

Anexo - Monitor de documentos para assinatura eletrônica

Para acessar o anexo "Monitor de documentos para assinatura eletrônica", o perfil do usuário deverá ter a seguinte permissão:

* **Educacional | Currículo e Oferta | Oferta | Turmas/Disciplinas | Monitor de documentos enviados para assinatura**

Campo Número de Aulas Semanais

No cadastro da turma/disciplina, ao selecionar a disciplina, caso a turma/disciplina seja uma turma livre (não tenha uma matriz aplicada selecionada), o campo Nº de aulas semanais será preenchido com a informação de número de aulas semanais cadastrada no cadastro da disciplina. Caso a turma/disciplina seja de uma turma de matriz aplicada, este campo será preenchido com a informação de número de aulas semanais cadastrada no cadastro da disciplina da matriz curricular.

O campo é editável e caso se deseje recuperar o valor original de número de aulas semanais da disciplina (turma livre) ou da disciplina da matriz curricular (turma de matriz aplicada), basta clicar no botão ao lado do campo, que o valor do campo será atualizado com a respectiva informação.

O campo **Nº de aulas semanais** indica quantas aulas da disciplina são realizadas por semana, sendo fundamental para o planejamento do quadro de horários e o cálculo da carga horária total no Planejamento de Oferta. Por exemplo, uma disciplina com 2 aulas semanais de 50 minutos cada, ministrada durante um semestre, terá sua carga horária total derivada dessa frequência. Esse campo impacta diretamente na montagem do horário e na distribuição da disciplina ao longo do período letivo.

**OBS: A informação do campo Nº de aulas semanais não tem relação com a geração do plano de aulas, servindo somente para fins do Planejamento de Oferta.**

Informações Complementares

---

[Professores](http://tdn.totvs.com/x/X-tbGQ)

Horário da Turma/Disciplina

Etapa/Fórmulas

[Avaliações da Turma/Disciplina](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425458766)

[Sub-Turmas da Turma/Disciplina](http://tdn.totvs.com/x/qfpbGQ)

[Plano de Aula da Turma/Disciplina](http://tdn.totvs.com/x/bJ7eHQ)

[Processo Atualizar Período de Matrícula da Turma/Disciplina](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425458767&moved=true)

[Turma Disciplina Gerenciada](http://tdn.totvs.com/x/g-1bGQ)

[Turma Disciplina do Itinerário Formativo](https://tdn.totvs.com/pages/viewpage.action?pageId=561059212)

Processo Alteração Global de Professores da Turma Disciplina

Parâmetro "Ativa" no cadastro da Turma/Disciplina

Processo: Atualizar Etapas das Turmas/Disciplinas

Processo Associar Professores aos Horários da Turma/Disciplina

Como Fazer

---

Geração de horário  
[Gerar plano de aula](http://tdn.totvs.com/x/IfxbGQ)Associar Provas do RM Testis às avaliações

 

Veja Também

---

[Boletim Técnico - Exibir Tipo da Turma/Disciplina na Matrícula](http://tdn.totvs.com/pages/viewpage.action?pageId=160105035)
