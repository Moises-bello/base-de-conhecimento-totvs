---
content_hash: effc41dad8b0981b1d9cf980079791a5100f20b8785bd12bbe683cfa482000fc
fetched_at: '2026-06-29T00:10:16.570731+00:00'
page_id: '471949494'
product: rm
source: tdn-rm
title: Frequência Diária / Justificativa de Falta (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=471949494
version: 11
---

### Visão geral

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de **Frequência diária / Justificativa de falta (EduFrequenciaDiariaWSData)** para a realização de requisições de consultas de frequências e inclusões de justificativas de faltas.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT, POST e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### Consulta

Para a realização de uma consulta, é necessária a utilização do método ***GET.***

Através desse método, é possível realizar a consulta de apenas uma frequência diária ou de uma lista de frequências.

Para a requisição de informações de uma frequência diária será necessário passar os valores da chave primária da frequência diária: **CODCOLIGADA**, **IDTURMADISC**, **IDHORARIOTURMA**, **RA** e **DATA**

Atenção ao Formato da Data

É essencial informar a data com o formato utilizado no banco, pois o mesmo será validado na chave primaria.

false

Para todas as operações é necessário que sejam passadas as informações do contexto no cabeçalho da mensagem: **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**e **CODSISTEMA**.

Retornando uma lista de frequência diária:

Para a consulta de uma lista de frequência diárias, é necessário a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rmsrestdataserver/rest/EduFrequenciaDiariaWSData***

É possível, nessa consulta, utilizar filtros para a limitação da quantidade de informações retornadas e, também, para restringir o resultado.

Através do link [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll) é possível obter mais informações de como utilizar o serviço.

Para a utilização do **GetAll** na frequência diária, é necessário que um filtro seja informado, porém, apesar de termos uma flexibilidade nesse serviço, ele dataserver permite a utilização de apenas um filtro.

Para isso, é necessário que seja informado um parâmetro "**filter**" para a inclusão do filtro:

Filtro para pesquisa de período de frequências da etapa de uma turma/disciplina em um determinado período:

sql

Filtro para pesquisa de período de frequências da etapa de uma subturma de uma turma/disciplina em um determinado período:

sqlxmlMensagem de respostatrue

#### Retornando apenas a frequência diária de um aluno:

Para realizar a consulta da frequência diária de um aluno, será necessária a utilização dos valores de chave primária da frequência diária.

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/EduFrequenciaDiariaWSData/1$\_$295$\_$1055$\_$0000112$\_$2018-10-22T00:00:00](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000108)

O valor informado no final da URL **"1$\_$295$\_$1055$\_$0000112$\_$2018-10-22T00:00:00"** se referem aos valores da coligada, id. do horário da turma, id. da turma/disciplina, do RA do aluno e a data da frequência.

Esse valores são separados pelos caracteres "$" e "\_".

Para a realização dessa requisição, deverá ser utilizado o método: **GET**.

xmlMensagem de respostatrue

### CADASTRO

#### Inclusão de uma falta na frequência diária:

Para realizar a inclusão de uma falta na frequência é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão inseridos e no cabeçalho da mensagem deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** e **CODSISTEMA**para criação do contexto em que a frequência diária será incluso.

URL que será utilizada para cadastro da frequência: [http://localhost:8051/rmsrestdataserver/rest/EduFrequenciaDiariaWSData](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData)

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Segue o exemplo de um conjunto mínimo de informações necessárias para o lançamento de uma frequência de um aluno:

É necessário que sejam informadas as tabelas **"AlunosFreq"** e **"PARAMS"** na inclusão de frequências.

xmlCorpo da mensagemtrue

Exemplo da resposta:

xmlMensagem de respostatrueImportante

O campo **Presenca** espera dois valores. (P ou A)

P: Presença

A: Ausência.

O campo **Justificada** espera dois valores. (1 ou 0)

1: Falta abonada

0: Falta não abonada.

Para a inclusão de uma justificativa, será necessário informar o código da mesma, cadastrada anteriormente, através do menu de cadastros auxiliares.

***Educacional | Currículo e Oferta | Auxiliares | Justificativas de falta***

Exemplo:

2 - Visita ao médico

*"**JUSTIFICADA**": 1*

*"**IDJUSTIFICATIVAFALTA**": 2*

### Alterações

#### Atualizando a frequência diária de um aluno:

Para realizar a atualização de uma frequência é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados.

false

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**e **CODSISTEMA** para criação do contexto.

URL que será utilizada para a atualização da frequência: [http://localhost:8051/rmsrestdataserver/rest/EduFrequenciaDiariaWSData/1$\_$295$\_$1055$\_$0000112$\_$2018-10-15T00:00:00](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000000226)

Esse código **"1$\_$295$\_$1055$\_$0000112$\_$2018-10-15T00:00:00"** é soma dos valores que compõem a chave da frequência diária: **CODCOLIGADA**, **IDHORARIOTURMA**, **IDTURMADISC**, **RA** e **DATA**

Para a realização dessa requisição, deverá ser utilizado o método: **PUT**.

Segue o exemplo de um conjunto de informações que serão alteradas:

xmlCorpo da mensagemtrueImportante

No corpo da mensagem é de suma importância informar os campos **CODCOLIGADA, IDTURMADISC, IDHORARIOTURMA, RA, DATA** e as tabelas **AlunosFreq** e **PARAMS** com os mesmos valores.

Exemplo da resposta:

xmlMensagem de respostatruefalse

### Exclusões

Não é possível utilizar o **DeleteRecord** do dataserver **EduFrequenciaDiariaWSData**.

Se for remover frequência do(s) aluno(s) utilize o **SaveRecord**, via SOAP, ou a operação de **PUT** informando na tag **"PRESENCA"** igual o valor **"P"**.
