---
content_hash: e4b446df08401ac460202a0ddf7d8728ac0247bf77404cc2150b4198ea3ed58f
fetched_at: '2026-06-29T00:08:53.341467+00:00'
page_id: '344469811'
product: rm
source: tdn-rm
title: Curso (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344469811
version: 12
---

### Visão geral

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de **Curso (EduCursoData)** para a realização de requisições de consulta, inclusão, alteração ou exclusão de dados.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT, POST e DELETE e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### Consulta

Para a realização de uma consulta, é necessária a utilização do método ***GET.***

Através desse método, é possível realizar a consulta de apenas um Curso ou de uma lista de Cursos.

Para a requisição de informações de um Curso será necessário passar os valores da chave primária do Curso: **CODCOLIGADA** e **CODCURSO.**

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL**, **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto.

#### Retornando uma lista e Cursos:

Para a consulta de uma lista de Cursos, é necessário a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rmsrestdataserver/rest/EduCursoData***

É possível, nessa consulta, utilizar filtros para a limitação da quantidade de informações retornadas e também para restringir o resultado.

Através do link [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll) é possível obter mais informações de como utilizar os filtros disponíveis.

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/EduCursoData?start=3&limit=2](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData?start=3&limit=2)

xmlMensagem de respostatrue

#### Retornando apenas um Curso:

Para realizar a consulta de um Curso, será necessário a utilização dos valores de chave primária do Curso:

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/E](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000108)duCursoData/1$\_$3-1

O valor informado no final da URL "***1$\_$3-1***" se refere aos valores da coligada e do Código do Curso.

Esse valores são separados pelos caracteres "$" e "\_".

Para a realização dessa requisição, deverá ser utilizado o método: **GET**.

### CADASTRO

#### Cadastrando um Curso:

Para realizar o cadastro de um curso é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão inseridos e no cabeçalho da mensagem deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto em que o Curso será incluso.

URL que será utilizada para cadastro do curso: [http://localhost:8051/rmsrestdataserver/rest/EduCursoData](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData)

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Segue o exemplo de um conjunto mínimo de informações necessárias para cadastro de um Curso:

xmlCorpo da mensagemtrueImportante

A obrigatoriedade dos campos pode variar de acordo com a parametrização realizada no sistema.

Caso esteja utilizando a aplicação SoapUI, as informações do cabeçalho podem ser informadas conforme abaixo:

xmlMensagem de respostatrue

Alterações

#### Atualizando informações do Curso:

Para realizar a atualização de cadastro de um Curso é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados, assim como, a tag ID que informará qual Curso será alterado.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**e **CODSISTEMA** para criação do contexto em que o Curso será incluso.

URL que será utilizada para cadastro do curso: [http://localhost:8051/rmsrestdataserver/rest/EduCursoData/1$\_$3-19](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000000226)

Para a realização dessa requisição, deverá ser utilizado o método: **PUT**.

Segue o exemplo de um conjunto de informações de um Curso que serão alterados:

xmlCorpo da mensagemtrueImportante

No corpo da mensagem é de suma importância informar os campos **CODCOLIGADA** e **CODCURSO**.

Exemplo da resposta:

xmlMensagem de respostatrue

### Exclusões

#### Excluindo um Curso:

A exclusão de um Curso seguirá a mesma ideia da alteração, onde precisaremos passar as chaves do Curso a ser excluído, assim como o corpo da mensagem com suas informações.

 No cabeçalho da mensagem, também deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** e **CODSISTEMA**para criação do contexto.

URL que será utilizada para cadastro do Curso: [http://localhost:8051/rmsrestdataserver/rest/EduCursoData/1$\_$3-19](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$ES-00230)

Para a realização dessa requisição, deverá ser utilizado o método: **DELETE**.

Segue o exemplo de um conjunto de informações de um Curso que serão alterados:

xmlCorpo da mensagemtrue

Resposta da mensagem:

xmlMensagem de respostatrue
