---
content_hash: 44c577e0bd98e1dfb7bf447d16cf1471e212bc7420867e4d2f09a17881ac59af
fetched_at: '2026-06-29T00:08:53.363603+00:00'
page_id: '344471829'
product: rm
source: tdn-rm
title: Habilitação(Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344471829
version: 6
---

### Visão geral

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de **Curso\Habilitação (EduHabilitacaoData)** para a realização de requisições de consulta, inclusão, alteração ou exclusão de dados.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT, POST e DELETE e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### Consulta

Para a realização de uma consulta, é necessária a utilização do método ***GET.***

Através desse método, é possível realizar a consulta de apenas uma Habilitação ou de uma lista de Curso\Habilitação.

Para a requisição de informações de um Curso\Habilitação será necessário passar os valores da chave primária do Curso\Habilitação: **CODCOLIGADA,****CODCURSO e CODHABILITACAO.**

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL**, **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto.

#### Retornando uma lista e Curso\Habilitação:

Para a consulta de uma lista de Curso\Habilitação, é necessário a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rmsrestdataserver/rest/EduHabilitacaoData***

É possível, nessa consulta, utilizar filtros para a limitação da quantidade de informações retornadas e também para restringir o resultado.

Através do link [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll) é possível obter mais informações de como utilizar os filtros disponíveis.

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/EduHabilitacaoData?start=3&limit=2](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData?start=3&limit=2)

xmlMensagem de respostatrue

#### Retornando apenas uma Curso\Habilitação:

Para realizar a consulta de um Curso\Habilitação, será necessário a utilização dos valores de chave primária do Curso\Habilitação

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/E](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000108)duHabilitacaoData/7$\_$1$\_$1

O valor informado no final da URL "***7$\_$1\_$1***" se refere aos valores da coligada e do Código do Curso e o código da Habilitação.

Esse valores são separados pelos caracteres "$" e "\_".

Para a realização dessa requisição, deverá ser utilizado o método: **GET**.

### CADASTRO

#### Cadastrando um Curso/Habilitação:

Para realizar o cadastro de um Curso/Habilitação é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão inseridos e no cabeçalho da mensagem deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,****CODTIPOCURSO** e **CODSISTEMA**para criação do contexto em que o Curso\Habilitação será incluso.

URL que será utilizada para cadastro do curso\Habilitação: [http://localhost:8051/rmsrestdataserver/rest/EduHabilitacaoData](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData)

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Segue o exemplo de um conjunto mínimo de informações necessárias para cadastro de um Curso\Habilitação:

xmlCorpo da mensagemtrueImportante

A obrigatoriedade dos campos pode variar de acordo com a parametrização realizada no sistema.

Caso esteja utilizando a aplicação SoapUI, as informações do cabeçalho podem ser informadas conforme abaixo:

xmlMensagem de respostatrue

Alterações

#### Atualizando informações do Curso\Habilitação:

Para realizar a atualização de cadastro de um Curso\Habilitação é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados, assim como, a tag ID que informará qual Curso\Habilitação será alterado.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**e **CODSISTEMA** para criação do contexto em que o Curso\Habilitação será incluso.

URL que será utilizada para cadastro do Curso\Habilitação: [http://localhost:8051/rmsrestdataserver/rest/EduHabilitacaoData/1$\_$3-19](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000000226)

Para a realização dessa requisição, deverá ser utilizado o método: **PUT**.

Segue o exemplo de um conjunto de informações de um Curso\Habilitação que serão alterados:

xmlCorpo da mensagemtrueImportante

No corpo da mensagem é de suma importância informar os campos **CODCOLIGADA,** **CODCURSO e CODHABILITACAO.**

Exemplo da resposta:

xmlMensagem de respostatrue

### Exclusões

#### Excluindo um Curso\Habilitação:

A exclusão de um Curso\Habilitação seguirá a mesma ideia da alteração, onde precisaremos passar as chaves do Curso\Habilitação a ser excluído, assim como o corpo da mensagem com suas informações.

 No cabeçalho da mensagem, também deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**e **CODSISTEMA** para criação do contexto.

URL que será utilizada para cadastro do Curso\Habilitação: [http://localhost:8051/rmsrestdataserver/rest/EduHabilitacaoData/1$\_$3-19](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$ES-00230)

Para a realização dessa requisição, deverá ser utilizado o método: **DELETE**.

Segue o exemplo de um conjunto de informações de um Curso\Habilitação que serão alterados:

xmlCorpo da mensagemtrue

Resposta da mensagem:

xmlMensagem de respostatrue
