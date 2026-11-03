---
content_hash: e3c2aadfaec92243cfa337b794658e20800881614454922bfb06a9f623683a89
fetched_at: '2026-06-29T00:08:47.083057+00:00'
page_id: '318605570'
product: rm
source: tdn-rm
title: Alunos (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=318605570
version: 20
---

### Visão geral

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de **Aluno (EduAlunoData)** para a realização de requisições de consulta, inclusão, alteração ou exclusão de dados.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT, POST e DELETE e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### Consulta

Para a realização de uma consulta, é necessária a utilização do método ***GET.***

Através desse método, é possível realizar a consulta de apenas um aluno ou de uma lista de alunos.

Para a requisição de informações de um aluno será necessário passar os valores da chave primária do aluno: **CODCOLIGADA** e **RA**.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL**, **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto.

#### Retornando uma lista e alunos:

Para a consulta de uma lista de alunos, é necessário a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rmsrestdataserver/rest/EduAlunoData***

É possível, nessa consulta, utilizar filtros para a limitação da quantidade de informações retornadas e, também, para restringir o resultado.

Através do link [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll) é possível obter mais informações de como utilizar os filtros disponíveis.

Exemplo:

<http://localhost:8051/rmsrestdataserver/rest/EduAlunoData?start=3&limit=2>

xmlMensagem de respostatrue

#### Retornando apenas uma aluno:

Para realizar a consulta de um aluno, será necessário a utilização dos valores de chave primária do aluno:

Exemplo:

<http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000108>

O valor informado no final da URL "***1$\_$0000108***" se refere aos valores da coligada e do RA do aluno.

Esse valores são separados pelos caracteres "$" e "\_".

Para a realização dessa requisição, deverá ser utilizado o método: **GET**.

xmlMensagem de respostatrue

### CADASTRO

#### Cadastrando um aluno:

Para realizar o cadastro de um aluno é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão inseridos e no cabeçalho da mensagem deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto em que o aluno será incluso.

URL que será utilizada para cadastro do aluno: <http://localhost:8051/rmsrestdataserver/rest/EduAlunoData>

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Segue o exemplo de um conjunto mínimo de informações necessárias para cadastro de um aluno:

xmlCorpo da mensagemtrueImportante

A obrigatoriedade dos campos pode variar de acordo com a parametrização realizada no sistema.

Caso esteja utilizando a aplicação SoapUI, as informações do cabeçalho podem ser informadas conforme abaixo:

xmlMensagem de respostatrue

### Alterações

#### Atualizando informações do aluno:

Para realizar a atualização de cadastro de um aluno é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados, assim como, a tag ID que informará qual aluno será alterado.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto em que o aluno será incluso.

URL que será utilizada para cadastro do aluno: <http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000000226>

Para a realização dessa requisição, deverá ser utilizado o método: **PUT**.

Segue o exemplo de um conjunto de informações de um aluno que serão alterados:

xmlCorpo da mensagemtrueImportante

No corpo da mensagem é de suma importância informar os campos **CODPESSOA** e **CODIGO** com o mesmo valor.

Exemplo da resposta:

xmlMensagem de respostatrue

### Exclusões

#### Excluindo o aluno:

A exclusão de um aluno seguirá a mesma ideia da alteração, onde precisaremos passar as chaves do aluno a ser excluído, assim como o corpo da mensagem com suas informações.

 No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL**, **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto.

URL que será utilizada para cadastro do aluno: <http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$ES-00230>

Para a realização dessa requisição, deverá ser utilizado o método: **DELETE**.

Segue o exemplo de um conjunto de informações de um aluno que serão alterados:

xmlCorpo da mensagemtrue

Resposta da mensagem:

xmlMensagem de respostatrue
