---
content_hash: eea099632dccb08a1378111e566cd303834bbe3829d3e4b9e3c6ec75958731b9
fetched_at: '2026-06-29T00:08:53.385914+00:00'
page_id: '344472914'
product: rm
source: tdn-rm
title: Turma (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344472914
version: 7
---

### Visão geral

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de **Turma (EduTurmaData)** para a realização de requisições de consulta, inclusão, alteração ou exclusão de dados.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT, POST e DELETE e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### Consulta

Para a realização de uma consulta, é necessária a utilização do método ***GET.***

Através desse método, é possível realizar a consulta de apenas uma Turma ou de uma lista de Turmas.

Para a requisição de informações de uma Turma será necessário passar os valores da chave primária da Turma: **CODCOLIGADA, CODFILIAL, IDPERLET** e **CODTURMA.**

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL**, **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto.

#### Retornando uma lista e Turmas:

Para a consulta de uma lista de Turmas, é necessário a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rmsrestdataserver/rest/EduTurmaData***

É possível, nessa consulta, utilizar filtros para a limitação da quantidade de informações retornadas e também para restringir o resultado.

Através do link [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll) é possível obter mais informações de como utilizar os filtros disponíveis.

Exemplo:

<http://localhost:8051/rmsrestdataserver/rest/EduTurmaData?start=3&limit=2>

xmlMensagem de respostatrue

#### Retornando apenas uma Turma:

Para realizar a consulta de uma Turma, será necessário a utilização dos valores de chave primária da Turma:

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/E](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000108)duTurmaData/1$\_$2$\_$18$\_$EF4C

O valor informado no final da URL "**1$\_$2$\_$18$\_$EF4C**" se refere aos valores da Coligada, Filial, Id do Periodo Letivo e Código da Turma.

Esse valores são separados pelos caracteres "$" e "\_".

Para a realização dessa requisição, deverá ser utilizado o método: **GET**.

### CADASTRO

#### Cadastrando uma Turma:

Para realizar o cadastro de uma turma é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão inseridos e no cabeçalho da mensagem deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** e **CODSISTEMA**para criação do contexto em que o Turma será incluso.

URL que será utilizada para cadastro do turma: [http://localhost:8051/rmsrestdataserver/rest/EduTurmaData](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData)

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Segue o exemplo de um conjunto mínimo de informações necessárias para cadastro de uma Turma:

xmlCorpo da mensagemtrueImportante

A obrigatoriedade dos campos pode variar de acordo com a parametrização realizada no sistema.

Caso esteja utilizando a aplicação SoapUI, as informações do cabeçalho podem ser informadas conforme abaixo:

xmlMensagem de respostatrue

Alterações

#### Atualizando informações da Turma:

Para realizar a atualização de cadastro de uma Turma é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** e **CODSISTEMA**para criação do contexto em que a Turma será inclusa.

URL que será utilizada para cadastro da turma: [http://localhost:8051/rmsrestdataserver/rest/EduTurmaData//1$\_$2$\_$18$\_$EF12C](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000000226)

Para a realização dessa requisição, deverá ser utilizado o método: **PUT**.

Segue o exemplo de um conjunto de informações de uma Turma que serão alteradas:

xmlCorpo da mensagemtrueImportante

No corpo da mensagem é de suma importância informar os campos **CODCOLIGADA, CODFILIAL, IDPERLET** e **CODTURMA.**

Exemplo da resposta:

xmlMensagem de respostatrue

### Exclusões

#### Excluindo uma Turma:

A exclusão de uma Turma seguirá a mesma ideia da alteração, onde precisaremos passar as chaves da Turma a ser excluída, assim como o corpo da mensagem com suas informações.

 No cabeçalho da mensagem, também deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** e **CODSISTEMA**para criação do contexto.

URL que será utilizada para cadastro do Curso: [http://localhost:8051/rmsrestdataserver/rest/EduTurmaData/1$\_$2$\_$18$\_$EF12C](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$ES-00230)

Para a realização dessa requisição, deverá ser utilizado o método: **DELETE**.

Segue o exemplo de um conjunto de informações de uma Turma que serão alteradas:

xmlCorpo da mensagemtrue

Resposta da mensagem:

xmlMensagem de respostatrue
