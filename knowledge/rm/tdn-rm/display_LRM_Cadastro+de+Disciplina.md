---
content_hash: a16db802f48608cda04e5493654876588e84cc5ccb14ae84aebd5dad70bc332b
fetched_at: '2026-06-29T00:09:33.891327+00:00'
page_id: '425459074'
product: rm
source: tdn-rm
title: Cadastro de Disciplina
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Disciplina
version: 11
---

Esta janela permite **cadastrar** e **consultar** as disciplinas que serão utilizadas pela instituição de ensino. Essas informações são fundamentais, pois as disciplinas registradas aqui **farão parte da matriz curricular dos cursos** futuramente.

Embora o cadastro seja simples, ele é essencial para o funcionamento de diversos processos acadêmicos e administrativos. Por isso, é importante compreender bem o **significado e a finalidade de cada campo** disponível na tela antes de preenchê-los. Um cadastro correto e completo garante mais agilidade e precisão na montagem de horários, no cálculo de carga horária, no lançamento de notas e na organização do curso como um todo.

### Cadastro de Disciplina

No campo **Disciplina**, você poderá definir o código da disciplina. Este código pode ser alfanumérico e deve ajudar na identificação rápida da disciplina, de forma resumida. Embora não exista um padrão obrigatório, é recomendado que este código se relacione com o nome da disciplina. Por exemplo:

* **Disciplina**: `CALC.1`
* **Nome**: `Cálculo 1`
* **Segundo Nome**: `Cálculo Matemático I`

Cada instituição pode adotar diferentes padrões para o preenchimento desses campos, conforme sua própria organização interna. O importante é garantir que as informações estejam completas e façam sentido dentro do contexto acadêmico da instituição.

Além disso, o campo **Nome Reduzido** permite definir uma versão abreviada da disciplina, que será utilizada na exibição do quadro de horários, facilitando a visualização pelos alunos.

### Grupo de Complemento

O campo **Grupo de Complemento** é aplicável apenas ao **ensino superior** e possibilita associar conteúdos complementares à disciplina, como:

* Ementa
* Bibliografia
* Plano de Ensino

Esses itens ajudam a compor o conteúdo acadêmico da disciplina. Para o **ensino básico**, os complementos são definidos diretamente no cadastro de disciplinas da grade.  
Mais detalhes podem ser encontrados na documentação de [Complemento da Disciplina](http://tdn.totvs.com/x/XPxbGQ).

### Tipo de Nota e Casas Decimais

* **Tipo de Nota**: define se as notas serão **numéricas** ou **conceituais**.

  > Atenção: ao escolher "conceitual", será necessário vincular um grupo de conceitos na etapa de avaliação. Não é possível utilizar os dois tipos simultaneamente.
* **Número de Casas Decimais**: define quantas casas decimais poderão ser utilizadas na digitação das notas.

  > Este campo é exibido apenas para o **ensino superior**.

### Carga Horária

O campo **Carga Horária** define a carga total da disciplina e é essencial para o controle de frequência e cumprimento dos requisitos mínimos para aprovação do aluno.

Também estão disponíveis os campos informativos para:

* **Carga Teórica**
* **Carga Prática**
* **Carga de Laboratório**
* **Carga de Estágio**

Esses campos são utilizados principalmente em relatórios e estão visíveis apenas para o **ensino superior**.

---

### Tipo de Aula e Tipo no Provão

* **Tipo de Aula**: define se a disciplina é **Teórica**, **Prática** ou **Mista**.
* **Tipo de Disciplina no Provão**: define se a disciplina é **Básica** ou **Profissional**.

---

### Créditos e Exclusividade

* **Número de Créditos**: define a quantidade de créditos da disciplina, com até quatro casas decimais.
* **Disciplina Exclusiva de Curso Livre**: marque essa opção se a disciplina for ofertada apenas em cursos livres.

---

### Número de Aulas Semanais

A partir das versões **12.1.2410.261, 12.1.2502.164, 12.1.2506.108**, **12.1.2510** o sistema passou a contar com o campo **Nº de Aulas Semanais** (somente para o Ensino Superior). Esse campo indica quantas aulas da disciplina são realizadas por semana, sendo fundamental para o planejamento do quadro de horários e o cálculo da carga horária total no Planejamento de Oferta. Por exemplo, uma disciplina com 2 aulas semanais de 50 minutos cada, ministrada durante um semestre, terá sua carga horária total derivada dessa frequência. Esse campo impacta diretamente na montagem do horário e na distribuição da disciplina ao longo do período letivo.

---

Para atender às novas diretrizes do Marco Regulatório da Educação a Distância e às exigências do Decreto nº 12.456, de 19 de maio de 2025, foi instituído o controle de carga horária nas disciplinas do Ensino Superior, tanto na modalidade presencial quanto a distância.

**Modalidades de Ensino**

De acordo com o **Decreto nº 12.456/2025**, os cursos de Ensino Superior no Brasil poderão ser ofertados em três modalidades:

1. **Curso presencial**
2. **Curso semipresencial**
3. **Curso a distância**

**Definições Importantes**

* **Educação a distância (EAD)**: Processo de ensino e aprendizagem realizado por meio do uso de tecnologias de informação e comunicação, onde o estudante e o docente estão em locais e horários diversos.
* **Atividade presencial**: Atividade de ensino realizada com a presença física do estudante e do docente, em tempo e local coincidentes.
* **Atividade síncrona**: Atividade mediada por tecnologia, onde o estudante e o docente participam simultaneamente, mas em locais diferentes.
* **Atividade síncrona mediada**: Atividade síncrona em grupos de no máximo 70 estudantes, com controle de frequência.
* **Atividade assíncrona**: Atividade em que o estudante e o docente realizam as atividades em horários diferentes.

**Cadastro de Disciplina:**

Campos adicionados:

* **Presencial**: Carga horária total de atividades presenciais.
* **À distância**: Carga horária total de atividades a distância.
* **Síncrona**: Carga horária de atividades síncronas (com áudio e vídeo).
* **Síncrona mediada**: Carga horária de atividades síncronas mediadas com controle de frequência (máximo 70 alunos por docente).
* **Assíncrona**: Carga horária de atividades assíncronas.

Regras para os campos de carga horária:

* A soma dos valores de Presencial e À distância não pode ultrapassar o valor do campo Total.
* A soma dos campos Síncrona, Síncrona mediada e Assíncrona não pode ultrapassar o valor do campo À distância.

Disponível a partir das versões: **12.1.2502.233, 12.1.2506.182 e 12.1.2510.116**.
