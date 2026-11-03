---
content_hash: aba4155e5ac50f21b4c41e3558616f7f482a1ee025883c60dbf617663446e458
fetched_at: '2026-06-29T00:08:14.153847+00:00'
page_id: '244442030'
product: rm
source: tdn-rm
title: ENADE
type: documentation
url: https://tdn.totvs.com/display/LRM/ENADE
version: 56
---

Sumário

## 1. Introdução

O Exame Nacional de Desempenho dos Estudantes (Enade) avalia o rendimento dos concluintes dos cursos de graduação em relação aos conteúdos programáticos previstos nas diretrizes curriculares dos cursos, o desenvolvimento de competências e habilidades necessárias ao aprofundamento da formação geral e profissional, e o nível de atualização dos estudantes com relação à realidade brasileira e mundial. Mais informações no site do Inep: [Portal Enade](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enade).

O Exame foi reformulado para aprimorar o enfoque nos cursos que formam professores. Além das provas teóricas, estágio supervisionado também será avaliado. Portanto, o Enade terá dois tipos de avaliação (teórica e prática), com um cronograma específico para cada uma delas. Os procedimentos relativos à Avaliação da Prática estão divididos em dois períodos. O planejamento contempla desde atividades operacionais, como a realização de cadastros no Sistema Enade, até a avaliação propriamente dita, registrada nos instrumentos avaliativos.

### **1.1 Avaliação Teórica (AT)**

Explicação rápida

O processo no sistema consiste na geração de um arquivo com informações solicitadas pelo MEC no contexto do Ensino Superior, e segue os seguintes passos:

 I . O início do processo de Enade começa com a Instituição de Ensino Superior (IES) selecionando os alunos para fazerem a prova;

 II . São selecionados os alunos de um determinado Período Letivo de cada um dos cursos existentes;

 III. No final, o sistema envia os dados para o MEC de acordo com um layout predefinido. 

A partir das versões 12.1.2310.236, 12.1.2402.177, 12.1.2406.111 e 12.1.2410 no menu Atividades Acadêmicas | Assistentes, passa a ter um item de menu que dá acesso a esta documentação.

Requisitos

Para realizar o processo de configuração o usuário deverá ter o perfil de acesso:

* Educacional | Atividades Acadêmicas | Assistentes | **Geração de arquivo ENADE**.

* Matricula e Avaliação | Matrículas | **Atualização de Campos do ENADE**.

Após a liberação das permissões, Acesse:

Atividades Acadêmicas | Assistentes | Geração de arquivo ENADE

 Matrícula no Período Letivo | Processos | Atualização de campos do ENADE

### **1.1 Avaliação da Prática (AP)**

Requisitos

Para realizar o processo de configuração o usuário deverá ter o perfil de acesso:

* Educacional | Atividades Acadêmicas | Assistentes | **Geração de arquivo ENADE - Avaliação Prática**.

Após a liberação das permissões, Acesse:

Atividades Acadêmicas | Assistentes | Geração de arquivo ENADE - Avaliação Prática

## 2. Configurações gerais

Informe os dados corretamente!

Caso algum campo dos cadastros a seguir não estiver devidamente configurado o sistema emitirá a mensagem de aviso apenas no final do processo, não permitindo que o mesmo seja finalizado.

### **2.1 Cadastro do Aluno**

**Acesse: Currículo e Oferta | Aluno e Professor | Aluno [Guias: Documentos | Diversos]**

É solicitado o preenchimento do campo de CPF do aluno no cadastro de informações pessoais.

Necessário também informar o ano em que o aluno finalizou o Ensino Médio.

No cadastro do anexo Curso/Habilitação do aluno deve-se preencher o campo “Data de ingresso no curso” para alunos concluintes.

### **2.2 Cadastro de Curso/Habilitação**

**Acesse: Atividades acadêmicas | Acadêmico | Censo | Parâmetros do Censo**

Deve ser definido como será cadastrada a Instituição do MEC que poderá ser usada por Filial ou por Nível de Ensino de acordo com os Parâmetros de Secretaria do Educacional.

**Acesse: Módulo Gestão Fiscal | Cadastros | Globais | Filiais | Anexo | Dados Educacionais | Anexo | Instituição do MEC**

**ou: Configurações | Níveis de ensino | Anexo | Instituição do MEC**

Deve ser cadastrado a Instituição do MEC para a filial ou nível de ensino

**Acesse: Módulo Gestão Fiscal | Cadastros | Globais | Filiais | Anexo | Dados Educacionais | Anexo | Instituição do MEC | Anexo | Curso do MEC**

**ou: Configurações | Níveis de ensino | Anexo | Instituição do MEC | Anexo | Curso do MEC**

Deve ser cadastrado os cursos do MEC para a instituição.

**Acesse: Currículo e Oferta | Matrizes curriculares | Anexo | Matriz Aplicada**

O curso do MEC deve ser associado à Matriz Aplicada

### **2.3 Cadastro da Situação de Matrícula**

**Acesse: Currículo e Oferta | Acadêmico | Situação de Matrícula [Guia: Status no Curso]**

A Situação de Matrícula do Aluno no curso/habilitação deverá conter o parâmetro ‘No curso’ habilitado.

### **2.4 Cadastro de Matriz Curricular**

**Acesse: Currículo e Oferta | Estrutura Curricular | Matrizes Curriculares**

Na matriz curricular dos alunos, é importante conter as seguintes informações: **carga horária**, **máximo de créditos** e **total de créditos**.

Esses dados são essenciais para o cálculo do ano e semestre de formatura dos alunos concluintes, baseado em carga horária. Esse cálculo considera o limite máximo de créditos em que o aluno pode se matricular por período.

A partir da relação entre o total de créditos do curso e a carga horária total, juntamente com a carga horária das disciplinas ainda não cursadas, é possível estimar em qual ano e semestre o aluno poderá concluir o curso.

### **2.5 Cadastro de Campus/Polo**

**Acesse: Currículo e Oferta | Matrizes curriculares | Anexo | Matriz Aplicada**

**Acesse: Matrícula e Avaliação | Matrículas | Matrículas no curso**

O município do polo é obrigatório para cursos EaD. Para que essa informação seja enviada, o Campus/Polo deve ser cadastrado no anexo da matriz aplicada com registro de município.

Após realizarmos o cadastro do Campus/Polo o mesmo deve ser informado no Curso/Habilitação do aluno.

O sistema validará se o curso é presencial ou à distancia.

Curso à distancia: O mesmo deverá possuir um Campus/Polo informado no Curso/Habilitação do aluno. Caso não possua, o processo do ENADE não finalizará com sucesso.

Curso Presencial: Não possui necessidade de informar um Campus/Polo. O sistema encerrará o processo com sucesso mesmo que não possua Campus/Polo.

## 3. Geração do Arquivo AT

**Acesse: Atividades Acadêmicas | Assistentes | Geração de Arquivo ENADE - Avaliação Teórica**

### **3.1 Geração do Arquivo - Ingressantes**

Ingressantes

Estudantes Ingressantes são aqueles que tenham iniciado o respectivo curso no ano da edição do Enade, que estejam devidamente matriculados e que tenham de 0% (zero por cento) a 25% (vinte e cinco por cento) da carga horária mínima do currículo do curso integralizada até o último dia do período de retificação de inscrições.

#### **3.1.1 Parâmetros adicionais**

O **Indicador do Aluno** é o tipo de arquivo que será gerado para o MEC, conforme a **parametrização informada no passo anterior**.

Na **tela inicial do processo**, deve-se marcar a opção **"Ingressantes"** e informar a **faixa para cálculo**. Por padrão, a **Faixa Inicial** vem preenchida com **0 (zero)** e a **Faixa Final** com **25**. Esses valores podem ser alterados pela Instituição, permitindo que ela defina faixas personalizadas para que apenas os alunos **dentro dessa faixa** sejam incluídos no **arquivo do Enade**. Alunos **fora da faixa informada** **não serão considerados** no arquivo.

Outras duas informações importantes estão disponíveis no lado direito da tela, nos itens do **Sistema Inep**, chamados **"Código do Projeto"** e **"Sequencial"**:

* O **Código do Projeto** é composto pelos **dois últimos dígitos do ano** seguidos do número fixo **"11101"**.  
  Exemplo: **"2411101"** para o ano de 2024.
* O **Sequencial do Arquivo** é o número que aparecerá no final do **arquivo gerado**.

Fique atento para o cálculo de ano/semestre da formatura dos alunos baseado em:
> ⚠️ **Atenção – Carga Horária**:  
> O cálculo é feito com base nas **disciplinas já cumpridas** pelo aluno (obrigatórias, optativas, eletivas e componentes curriculares), além da **carga horária da matriz curricular** correspondente.

> 📅 **Períodos**:  
> O sistema verifica em **qual período o aluno está matriculado** e **quantos períodos ainda faltam ser cursados**.

Por fim, informe a **faixa de cálculo correta** e clique no botão **"Avançar"**.

#### **3.1.2 Seleção de alunos**

Selecione os **alunos que farão a prova do Enade** utilizando os **filtros disponíveis para os cursos selecionados no ano** vigente.

Após selecionar os alunos, clique no botão **"Avançar"** e, em seguida, no botão **"Executar"**.

Ao finalizar o processo, um **arquivo será gerado automaticamente**, com o nome no seguinte formato:

`ENADE[CO_PROJETO]_N92_BR_[DATA_GERAÇÃO]_[CO_CURSO]_[ORIGEM][SEQ_GERAL].TXT`

Onde:

* **[CO\_PROJETO]**: código do projeto informado no arquivo
* **[DATA\_GERAÇÃO]**: data da geração do arquivo no formato **"AAAAMMDD"**
* **[CO\_CURSO]**: código do **primeiro curso da lista de alunos** selecionados
* **[ORIGEM]**: tipo de origem enviado no arquivo
* **[SEQ\_GERAL]**: número sequencial definido na **rotina de geração do arquivo**

O **usuário do RM** terá a opção de **salvar o arquivo**. Conforme o layout solicitado pelo MEC, os **dados no arquivo serão separados por ponto e vírgula (;).**

Após a execução de todos os passos, **verifique os alunos nos arquivos .TXT** e realize a **exportação no Portal Enade**. O arquivo gerado poderá ser enviado ao **Inep**, que será responsável por **inscrever os alunos na prova**.

No cadastro da Matrícula do Período Letivo dos alunos gerados será atualizado a opção **I*****ngressante**.*

### **3.2 Geração do Arquivo - Concluinte**

### 🎓 Estudantes Concluintes

**Estudantes Concluintes dos Cursos de Bacharelado**:  
Aqueles que tenham **expectativa de conclusão até julho do ano corrente** ou que tenham cumprido **80% (oitenta por cento)** ou mais da **carga horária mínima** do currículo do curso da IES **e não tenham colado grau** até o último dia do período de **retificação de inscrições do Enade anterior**.

**Estudantes Concluintes dos Cursos Superiores de Tecnologia**:  
Aqueles que tenham **expectativa de conclusão até dezembro do ano corrente** ou que tenham integralizado **75% (setenta e cinco por cento)** ou mais da carga horária mínima do currículo do curso definido pela IES **e não tenham colado grau** até o fim do período de **retificação do Enade anterior**.

#### **3.2.1 Parâmetros adicionais**

### 🖥️ Tela Inicial do Processo

Na **tela inicial do processo**, selecione a opção **"Concluintes"**, informe a **Faixa para Cálculo** e defina se deseja calcular o **ano/semestre da formatura** dos alunos com base nos **Períodos Letivos** ou na **Carga Horária Cumprida**.

* **Carga Horária**: O cálculo será feito com base nas **disciplinas cumpridas** (obrigatórias, optativas, eletivas e componentes curriculares) e na **carga horária da matriz curricular** do aluno.
* **Períodos**: O sistema verifica o **período atual da matrícula** do aluno e **quantos períodos ainda faltam**.

> ⚠️ **Importante**: Para que o sistema calcule corretamente a carga horária concluída, é necessário que o campo **"Carga Horária"** na **Matriz Curricular** esteja devidamente **preenchido**.

A carga horária cumprida é obtida somando-se:

* A **CH das disciplinas obrigatórias, optativas e eletivas**

  + a **CH das atividades curriculares**

---

### 📊 Faixa para Cálculo

Por padrão, a **faixa inicial** vem preenchida com o valor **80** (oitenta). A geração do arquivo do ENADE considera:

* **Soma das cargas horárias das disciplinas**

  + **Soma das cargas horárias das atividades curriculares**

Se for definida uma **faixa de 80%**, os alunos com carga horária igual ou superior a esse valor **serão incluídos no arquivo**, mesmo que **não tenham completado todas as atividades curriculares**. Alunos com percentual inferior **não serão incluídos**.

> ✅ A faixa inicial é configurável pela **Instituição**. O valor padrão é **80**, mas pode ser ajustado conforme necessidade.

### 🔢 Código do Projeto e Sequencial

À direita da tela, localizam-se os campos do **Sistema Inep**:

* **Código do Projeto**: formado pelos **dois últimos dígitos do ano** + o número fixo **"11101"**  
  Exemplo: **"2411101"**
* **Sequencial do Arquivo**: é o valor que irá compor a TAG **[SEQ\_GERAL]** do nome do arquivo gerado. Esse número é **escolhido durante a rotina de geração**.

Informe o **Código do Projeto** e clique no botão **"Avançar"**.

#### **3.2.2 Seleção de alunos**

Selecione os **alunos concluintes que farão a prova do Enade**, utilizando os **filtros disponíveis para os cursos selecionados no ano**.

### 📘 Fórmula para Identificação de Possíveis Formandos

Quando utilizamos a opção **"Concluintes"**, antes de finalizar o processo, será exibida uma tela que permite o uso de uma **fórmula para identificar possíveis alunos formandos**.  
Essa fórmula deverá **retornar 'S' (sim)** se o aluno for considerado um **possível formando**.

> ⚠️ **Vale ressaltar que a fórmula somente será executada caso o aluno não tenha atingido os critérios mínimos definidos anteriormente, seja por carga horária ou por período.**  
> Ou seja, se o aluno **não cumprir o percentual mínimo de carga horária** ou **não cumprir o numero de períodos definido**, o sistema utilizará a fórmula como **critério complementar de avaliação**.

Abaixo, apresentamos um exemplo simples de fórmula utilizada para esse cálculo:

#### Exemplo de fórmula:

`Atribui('RA',BuscaCampoPL('RA','S'));
DECL PERIODO, SIMNAO;
EXECSQL('ENADE_PF');
SETVAR(PERIODO, RESULTSQL('ENADE_PF','PERIODO'));
SE PERIODO = 2 ENTAO
SETVAR(SIMNAO, 'S')
FIMSE
SENAO SE PERIODO = 1 ENTAO
SETVAR(SIMNAO, 'N')
FIMSE;
SIMNAO;`

#### 🧠 Explicação da Lógica:

* A função **`Atribui('RA', BuscaCampoPL('RA', 'S'))`** armazena em memória o **RA do aluno** retornado a partir de sua matrícula no período letivo.
* A consulta **ENADE\_PF** busca o **período atual do aluno** com base no RA armazenado:

`SELECT PERIODO
FROM SMATRICPL
WHERE RA = :FRM_RA.01`

O **parâmetro da consulta** é alimentado com o valor de **`FRM_RA.01`**, que é fornecido com base no **retorno da memória do sistema**, previamente preenchida com o **RA do aluno** por meio da função **`Atribui`** na fórmula.

No parâmetro da consulta, também é informado **qual fórmula deve ser executada** por meio da função **`FRM_CódigoFórmula`**.

#### 🧾 Conteúdo da fórmula `RA.01`:

`MEMORIA('RA')`

Essa fórmula retorna o valor armazenado anteriormente na memória com a chave **'RA'**.

> ⚠️ **Importante**:  
> Se durante a execução do ENADE houver alunos com **menos de 80% de conclusão**, e o campo **Período** na matrícula for **1** para alguns e **2** para outros, o sistema **gerará o arquivo somente para os alunos com período igual a 2**, conforme retorno da fórmula.

### 📁 Geração e Estrutura do Arquivo

Finalizado o processo, será gerado um **arquivo no formato .TXT**, com o nome estruturado da seguinte forma:

`ENADE[CO_PROJETO]_N92_BR_[DATA_GERAÇÃO]_[CO_CURSO]_[ORIGEM][SEQ_GERAL].TXT`

#### Explicação dos elementos:

* **[CO\_PROJETO]**: Código do projeto informado no arquivo
* **[DATA\_GERAÇÃO]**: Data de geração do arquivo no formato **"AAAAMMDD"**
* **[CO\_CURSO]**: Código do **primeiro curso da lista de alunos** selecionada
* **[ORIGEM]**: Tipo da origem informada no arquivo
* **[SEQ\_GERAL]**: Número sequencial definido na rotina de geração

O **usuário do RM** terá a opção de **salvar o arquivo**.  
De acordo com o **layout exigido pelo MEC**, os dados serão gerados **separados por ponto e vírgula (;)**, garantindo a conformidade com o formato esperado pelo sistema do INEP.

Na Matrícula do Período Letivo dos Alunos será atualizado a opção **concluinte** na aba Enade.

Após a execução dos processos descritos:

1. **Revise os alunos** incluídos nos arquivos `.TXT`.
2. Realize a **exportação no Portal Enade**.
3. O arquivo poderá ser enviado ao **INEP**, que será responsável por **realizar a inscrição dos alunos na prova**.

### **3.3 Geração do Arquivo - Irregulares**

Irregulares

É considerado como Aluno irregular aquele que deveria ter comparecido no ENADE e não compareceu em anos anteriores.

#### **3.3.1 Parâmetros adicionais**

O indicador do Aluno é o tipo de arquivo que será gerado para o MEC, conforme a parametrização informada no passo anterior.

Informar o Código do Projeto, e clicar no botão Avançar.

**3.3.2 Seleção de alunos de outros períodos letivos**

Somente alunos que foram selecionados para o Enade e “não compareceram” à prova serão listados. A única diferença é que estes alunos não terão o cálculo da carga horária como os demais gerados. 

Caso existam estes Alunos, utilize o filtro para selecionar os mesmos.

Clique no botão Avançar caso não seja necessário selecionar alunos de outros períodos letivos.

Clique em Executar.

Após finalizado o processo, um arquivo será gerado com o seguinte nome: 

**=>** Alunosirregulares\_2013.06.27.11.25.36.txt

 

O usuário tem a opção de Salvar o arquivo ou apenas Visualizá-lo. 

 Para Salvar, o usuário irá clicar no botão Salvar Arquivo.

De acordo com o layout solicitado pelo MEC os dados do arquivo serão gerados separados em ponto e vírgula.

O arquivo será enviado para o MEC que irá se encarregar de inscrever os alunos para a prova.

## 4. Enamed – Exame Nacional de Avaliação da Formação Médica

Conforme o [Edital nº 49/2026](https://www.in.gov.br/web/dou/-/edital-n-49-de-24-de-abril-de-2026-701698729) do INEP, devem ser inscritos no Enamed 2026:

Estudantes do 4 ano,com previsão de matrícula no 7º ou 8º semestre do curso de Medicina em 31/08/2026.

O Inep disponibiliza layout específico para envio de inscrições em lote dos estudantes do 4º ano de Medicina.

## Principais Campos Obrigatórios

| Campo | Descrição |
| --- | --- |
| CO\_IES | Código da IES |
| CO\_CURSO | Código do curso |
| NU\_CPF | CPF do estudante |
| NU\_PERCENTUAL\_INTEGRALIZACAO | Percentual de integralização |
| NU\_ANO\_FORMATURA | Ano da formatura |
| IN\_ORIGEM\_ENAMED | Identificação da inscrição do 4º ano |

## 5. Atualização de campos do ENADE AT

**Acesse: Currículo e Oferta | Aluno | Anexo | Matrícula no Período Letivo | Processo | Atualização de campos ENADE**

Após a prova, a instituição recebe um retorno do MEC com os dados dos alunos que foram dispensados e selecionados. E ainda se eles compareceram ou não. Para isso existe um processo que permite que estes dados sejam atualizados.

A *Atualização de campos do ENADE*, presente no processo da matrícula no período letivo, permite ao usuário atualizar de forma rápida os seguintes campos: Situação para a prova do MEC, Data da Realização e Comparecimento do aluno.

Informar os dados para atualização, e clicar no botão Executar.

Para atender o novo layout 1.05 do MEC referente ao Diploma/Histórico digital, foi incluído um novo campo Ano de Referência. Além da alteração no campo Situação do Enade - Diploma Digital para Motivos de não habilitação no ENADE - Diploma digital, passando este a ser habilitado somente se o aluno foi dispensado da realização da prova. Essas alterações estão disponíveis a partir das versões: 12.1.2205.278, 12.1.2209.235, 12.1.2302.158, 12.1.2306.103.

Foi incluído também o campo Não Habilitado, na situação para a prova do MEC. A opção de justificativa , "Motivos de não habilitação no Enade - Diploma digital", passa a ser visualizada, se o campo Não habilitado, estiver preenchido. Essas alterações foram realizadas para atender o novo layout 1.05 do MEC referente ao Diploma/Histórico digital. Versões disponíveis: 12.1.2209.265,12.1.2302.198 e 12.1.2306.139.

Aluno Habilitado: Ingressante ou Concluinte que compareceu/dispensado  
Aluno Irregular: Ingressante ou Concluinte selecionado que não compareceu  
Aluno Não habilitado: Ingressante ou Concluinte não habilitado

## 5. Configurações AP

### **5.1 Cadastro do Curso**

**Acesse: Atividades acadêmicas | Acadêmico | Censo | Instituição do MEC | Anexos | Curso do MEC**

Apenas os cursos de licenciatura serão considerados na geração dos arquivos de AP.

### **5.2 Termo de compromisso de estágio**

**Acesse: Atividades acadêmicas | Acadêmico | Estágio | Termo de compromisso de estágio**

O aluno deve possuir um termo de compromisso de estágio.

O termo de compromisso deverá possuir uma empresa, um supervisor, uma turma/disciplina pertencente ao curso de licenciatura do aluno e um orientador.

#### **5.2.1 Empresa**

**Acesse: Atividades acadêmicas | Acadêmico | Empresa**

A empresa do termo de compromisso deve ser uma escola.

##### **5.2.1.1 Instituição de ensino**

**Acesse: Currículo e oferta | Acadêmico | Auxiliares | Instituições de ensino**

A instituição de ensino da empresa deve possuir o número do INEP informado.

#### **5.2.2 Etapa do plano de atividades do estágio**

**Acesse: Atividades acadêmicas | Acadêmico | Estágio | Termo de compromisso de estágio | Anexos | Plano de atividade do estágio | Anexos | Etapas do plano de atividades do estágio**

O termo de compromisso do aluno deve possuir pelo menos um plano de atividade com uma etapa de regência com data de início (ou início previsto) e término (ou final previsto) informados.

A data de início e término deverá estar de acordo com o início e término parametrizado no processo de geração do arquivo.

## 6. Geração dos Arquivos AP

**Acesse: Atividades Acadêmicas | Assistentes | Geração de Arquivo ENADE - Avaliação Prática**

### **6.1 Parâmetros adicionais**

O Código do Projeto é formado pelos dois últimos dígitos do ano mais o número fixo "11101". Exemplo:  "2411101". O Sequencial do arquivo, será o número que sairá ao final do arquivo gerado. Essas informações já veem informadas e podem ser alteradas.

A AP acontecerá em dois períodos diferentes, portanto, deve ser informado para qual período os arquivos serão gerados.

Deve ser informado qual é o período de regência que será considerado para a geração do arquivo. Esse período é definido pelo INEP e consta no edital do ENADE. Só sairão no arquivo os estudantes que possuirem etapa de regência que comece ou termine dentro desse período informado.

Após informar os parâmetros, clicar no botão Avançar.

### **6.2 Seleção de cursos**

Selecione os cursos de licenciatura que farão parte da AP, conforme edital do Enade.

Após selecionar os cursos, clicar no botão Avançar.

### **6.3 Seleção de alunos**

Selecione os alunos que farão a AP do Enade. Apenas alunos dos cursos selecionados no passo anterior serão listados.

Após selecionar os alunos, clicar no botão Avançar.

Clique em Executar.

### **6.4 Conclusão**

Finalizado o processo, serão gerados os dados dos três arquivos: Estudantes, Orientadores e Supervisores.

Clique no botão Salvar Arquivo para que seja criados os três arquivos txt.

Esses arquivos deverão ser enviados para o INEP no portal do Enade.

## 7. Vídeos

[PARTE 1 - Conceitos e permissões.](https://www.youtube.com/watch?v=zv_LP3Ssb7o)

[PARTE 2 - Cadastros.](https://youtu.be/fr8SOKO7Xh0)

[PARTE 3 - Cadastros.](https://youtu.be/4hv3LuvqbNM)

[PARTE 4 - Estudantes Ingressantes.](https://youtu.be/RwBGlJyDbXg)

[PARTE 5 - Estudantes Concluintes.](https://youtu.be/zwKNpnWam1w)

[PARTE 6 - Geração do arquivo ENADE.](https://youtu.be/0J6nafFyIsE)

[PARTE 7 - Atualização de campos do ENADE.](https://youtu.be/znYQgVNe7B0)
