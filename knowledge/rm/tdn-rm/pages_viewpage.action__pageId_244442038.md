---
content_hash: 2ed245d87768ce127e128a0cfcd3d27947941ce04aa8c2bcf8bfcda31e2ae049
fetched_at: '2026-06-29T00:08:14.175962+00:00'
page_id: '244442038'
product: rm
source: tdn-rm
title: RMEDU00001_Boletim Técnico - ENADE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244442038
version: 57
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | RM Totvs Educacional |
| **Processo** | : | ENADE |
| **Subprocesso** | : | Cadastro, atualização dos campos e geração. |
| **Data da publicação** | : | 18/07/2018 |

Para entender como funciona o processo do ENADE no sistema. É necessário você entender o que é o ENADE (Exame Nacional de Desempenho de Estudantes).

O Exame Nacional de Desempenho de Estudantes (Enade) avalia o rendimento dos concluintes dos cursos de graduação, em relação aos conteúdos programáticos, habilidades e competências adquiridas em sua formação. O Enade é obrigatório e a situação de regularidade do estudante no Exame deve constar em seu histórico escolar.

Explicação rápida

O processo no sistema consistem na geração de um arquivo com informações solicitadas pelo MEC no contexto do Ensino Superior, e segue os seguintes passos:

 I . O início do processo de Enade começa com a Instituição de Ensino Superior (IES) selecionando os alunos para fazerem a prova;

 II . São selecionados os alunos de um determinado Período Letivo de cada um dos cursos existentes;

 III. No final, o sistema envia os dados para o MEC de acordo com um layout predefinido. 

Requisitos

Para realizar o processo de configuração o usuário deverá ter o perfil de acesso:

* Educacional > Atividades Acadêmicas > Assistentes > **Geração de arquivo ENADE**.
* Educacional > Matrícula.
* Matricula e Avaliação > Matrículas > Processos > **Atualização de Campos do ENADE**.
Sumário

## 1. Configurações de dados

Informe os dados corretamente!

Caso algum campo dos cadastros a seguir não estiver devidamente configurado o sistema emitirá a mensagem de aviso apenas no final do processo, não permitindo que o mesmo seja finalizado.

### **1.1 Cadastro do Aluno**

**Acesse: Currículo e Oferta | Aluno e Professor | Aluno [Guias: Documentos | Diversos]**

É solicitado o preenchimento do campo de CPF do aluno no cadastro de informações pessoais.

Necessário também informar o ano em que o aluno finalizou o Ensino Médio.

No cadastro do anexo Curso/Habilitação do aluno deve-se preencher o campo “Data de ingresso no curso” para alunos concluintes.

### **1.2 Cadastro de Curso/Habilitação**

**Acesse: Atividades acadêmicas | Acadêmico | Censo | Parâmetros do Censo**

Deve ser definido nos parâmetros do Censo como será cadastrada a Instituição do MEC.

**Acesse: Módulo Gestão Fiscal | Cadastros | Globais | Filiais | Anexo | Dados Educacionais | Anexo | Instituição do MEC**

**ou: Configurações | Níveis de ensino | Anexo | Instituição do MEC**

Deve ser cadastrado a Instituição do MEC para a filial ou nível de ensino

**Acesse: Módulo Gestão Fiscal | Cadastros | Globais | Filiais | Anexo | Dados Educacionais | Anexo | Instituição do MEC | Anexo | Curso do MEC**

**ou: Configurações | Níveis de ensino | Anexo | Instituição do MEC | Anexo | Curso do MEC**

Deve ser cadastrado os cursos do MEC para a instituição.

**Acesse: Currículo e Oferta | Matrizes curriculares | Anexo | Matriz Aplicada**

O curso do MEC deve ser associado à Matriz Aplicada

### **1.3 Cadastro da Situação de Matrícula**

**Acesse: Currículo e Oferta | Acadêmico | Situação de Matrícula [Guia: Status no Curso]**

A Situação de Matrícula do Aluno no curso/habilitação deverá conter o parâmetro ‘No curso’ habilitado.

### **1.4 Cadastro de Matriz Curricular**

**Acesse: Currículo e Oferta | Estrutura Curricular | Matrizes Curriculares**

Na matriz curricular dos alunos é importante conter as informações: Carga horária, Max de Crédito e Total de Créditos .

### **1.5 Cadastro de Campus/Polo**

**Acesse: Currículo e Oferta | Matrizes curriculares | Anexo | Matriz Aplicada**

****Acesse: Matrícula e Avaliação | Matrículas | Matrículas no curso****

O município do polo é obrigatório para cursos EaD. Para que essa informação seja enviada, o Campus/Polo deve ser cadastrado no anexo da matriz aplicada com registro de município.

Após realizarmos o cadastro do Campus/Polo o mesmo deve ser informado no Curso/Habilitação do aluno.

O sistema validará se o curso é presencial ou à distancia.

Curso à distancia: O mesmo deverá possuir um Campus/Polo informado no Curso/Habilitação do aluno. Caso não possua, o processo do ENADE não finalizará com sucesso.

Curso Presencial: Não possui necessidade de informar um Campus/Polo. O sistema encerrará o processo com sucesso mesmo que não possua Campus/Polo.

## 2. Geração do Arquivo

**Acesse: Atividades Acadêmicas | Assistentes | Geração de Arquivo ENADE**

### **2.1 Geração do Arquivo - Ingressantes**

Ingressantes

Estudantes Ingressantes são aqueles que tenham iniciado o respectivo curso no ano da edição do Enade, que estejam devidamente matriculados e que tenham de 0% (zero por cento) a 25% (vinte e cinco por cento) da carga horária mínima do currículo do curso integralizada até o último dia do período de retificação de inscrições.

#### **2.1.1 Parâmetros adicionais**

O indicador do Aluno é o tipo de arquivo que será gerado para o MEC, conforme a parametrização informada no passo anterior.

Fique atento para o cálculo de ano/semestre da formatura dos alunos baseado em:

Carga horária: O cálculo é feito baseado nas disciplinas já cumpridas do aluno(disciplinas obrigatórias, optativas, eletivas e componentes curriculares) e da carga horária da matriz curricular do aluno.

Períodos: Verifica o período em que o aluno está matriculado e quantos estão faltando realizar.

O Código do Projeto é formado pelos dois últimos dígitos do ano mais o número fixo "11101". Ex.: "1811101". 

Informar a faixa para cálculo correta e clicar no botão Avançar.

#### **2.1.2 Seleção de alunos**

Selecione os alunos que farão a prova do Enade, através de filtros para os cursos que foram selecionados no ano.

Após selecionar os alunos, clicar no botão avançar.

Clique em Executar.

Após finalizado o processo, um arquivo será gerado e o nome do arquivo sairá da seguinte forma:

ENADE[CO\_PROJETO]\_ N92\_BR\_[DATA\_GERAÇÃO]\_[CO\_CURSO]\_[ORIGEM][SEQ\_GERAL].TXT,

onde:

* [CO\_PROJETO] será o código do projeto que é enviado no arquivo. Esse código aparece na tela de geração do arquivo.
* [DATA\_GERAÇÃO] será a data atual da geração do arquivo no formato "AAAAMMDD";
* [CO\_CURSO] será o código do primeiro curso da lista de alunos selecionada para a geração do arquivo;
* [ORIGEM] será o tipo da origem que é enviado no arquivo;
* [SEQ\_GERAL] será o número sequencial escolhido na rotina de geração do arquivo.

Exemplo:

**=>** ENADE1811101\_N92\_BR\_20180717\_1\_E1.txt

O usuário tem a opção de Salvar o arquivo ou apenas Visualizá-lo.

 Para Salvar, o usuário irá clicar no botão Salvar Arquivo.

De acordo com o layout solicitado pelo MEC os dados do arquivo serão gerados separados em ponto e vírgula.

O arquivo será enviado para o MEC que irá se encarregar de inscrever os alunos para a prova.

No cadastro da Matrícula do Período Letivo dos alunos gerados será atualizado a opção I*ngressante.*

### **2.2 Geração do Arquivo - Concluinte**

Concluinte

Estudantes Concluintes dos Cursos de Bacharelado: aqueles que tenham expectativa de conclusão de curso até julho de 2019 ou que tenham cumprido 80% (oitenta por cento) ou mais da carga horária mínima do currículo do curso da IES e não tenham colado grau até o último dia do período de retificação de inscrições do Enade 2018.

Estudantes Concluintes dos Cursos Superiores de Tecnologia: aqueles que tenham expectativa de conclusão de curso até dezembro de 2018 ou que tenham integralizado 75% (setenta e cinco por cento) ou mais da carga horária mínima do currículo do curso definido pela IES e não tenham colado grau até o último dia do período de retificação de inscrições do Enade 2018.

#### **2.2.1 Parâmetros adicionais**

O indicador do Aluno é o tipo de arquivo que será gerado para o MEC, conforme a parametrização informada no passo anterior.

Fique atento para o cálculo de ano/semestre da formatura dos alunos baseado em:

Carga horária: O cálculo é feito baseado nas disciplinas já cumpridas do aluno(disciplinas obrigatórias, optativas, eletivas e componentes curriculares) e da carga horária da matriz curricular do aluno.

Períodos: Verifica o período em que o aluno está matriculado e quantos estão faltando realizar.

O Código do Projeto é formado pelos dois últimos dígitos do ano mais o número fixo "11101". Ex.: "1811101". 

Informar o Código do Projeto, e clicar no botão Avançar.

#### **2.2.2 Seleção de alunos**

Selecione os alunos que farão a prova do Enade, através de filtros para os cursos que foram selecionados no ano.

Após selecionar os alunos, clicar no botão avançar.

Clique em Executar.

Após finalizado o processo, um arquivo será gerado e o nome do arquivo sairá da seguinte forma:

ENADE[CO\_PROJETO]\_ N99\_BR\_[DATA\_GERAÇÃO]\_[CO\_CURSO]\_[ORIGEM][SEQ\_GERAL].TXT,

onde:

* [CO\_PROJETO] será o código do projeto que é enviado no arquivo. Esse código aparece na tela de geração do arquivo.
* [DATA\_GERAÇÃO] será a data atual da geração do arquivo no formato "AAAAMMDD";
* [CO\_CURSO] será o código do primeiro curso da lista de alunos selecionada para a geração do arquivo;
* [ORIGEM] será o tipo da origem que é enviado no arquivo;
* [SEQ\_GERAL] será o número sequencial escolhido na rotina de geração do arquivo.

Exemplo:

**=>** ENADE1811101\_N99\_BR\_20180717\_1\_E1.txt

O usuário tem a opção de Salvar o arquivo ou apenas Visualizá-lo. 

 Para Salvar, o usuário irá clicar no botão Salvar Arquivo.

De acordo com o layout solicitado pelo MEC os dados do arquivo serão gerados separados em ponto e vírgula.

O arquivo será enviado para o MEC que irá se encarregar de inscrever os alunos para a prova.

No cadastro da Matrícula do Período Letivo dos alunos gerados será atualizado a opção *Concluinte*.

### **2.3 Geração do Arquivo - Irregulares**

Irregulares

É considerado como Aluno irregular aquele que deveria ter comparecido no ENADE e não compareceu em anos anteriores.

#### **2.3.1 Parâmetros adicionais**

O indicador do Aluno é o tipo de arquivo que será gerado para o MEC, conforme a parametrização informada no passo anterior.

Informar o Código do Projeto, e clicar no botão Avançar.

**2.3.2 Seleção de alunos de outros períodos letivos**

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

## 3. Atualização de campos do ENADE

**Acesse: Currículo e Oferta | Aluno | Anexo | Matrícula no Período Letivo | Processo | Atualização de campos ENADE**

Após a prova, a instituição recebe um retorno do MEC com os dados dos alunos que foram dispensados e selecionados. E ainda se eles compareceram ou não. Para isso existe um processo que permite que estes dados sejam atualizados.

A *Atualização de campos do ENADE*, presente no processo da matrícula no período letivo, permite ao usuário atualizar de forma rápida os seguintes campos: Situação para a prova do MEC, Data da Realização e Comparecimento do aluno.

Informar os dados para atualização, e clicar no botão Executar.

Dessa forma, o cadastro do Aluno no Período Letivo, as seguintes informações são atualizadas:

Informações Técnicas
