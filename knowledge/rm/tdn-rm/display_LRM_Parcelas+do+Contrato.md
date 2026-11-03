---
content_hash: f7c2713ef34fc6ce14ef1a7daed1a4a04901d382835a66cbd46fe5fc85be4924
fetched_at: '2026-06-29T00:08:48.566136+00:00'
page_id: '325855056'
product: rm
source: tdn-rm
title: Parcelas do Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Parcelas+do+Contrato
version: 12
---

### Visão geral

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de **Parcela (EduParcelaData)** para a realização de requisições de consulta, inclusão, alteração ou exclusão de dados.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT, POST e DELETE e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### Consulta

Para a realização de uma consulta, é necessária a utilização do método ***GET.***

Através desse método, é possível realizar a consulta de apenas uma parcela ou de uma lista de parcelas.

Para a requisição de informações de uma parcela será necessário passar os valores da chave primária da parcela: **CODCOLIGADA** e **IDPARCELA**.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL**, **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto.

#### Retornando uma lista de parcelas:

Para a consulta de uma lista de parcelas, é necessário a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rmsrestdataserver/rest/EduParcelaData***

É possível, nessa consulta, utilizar filtros para a limitação da quantidade de informações retornadas e, também, para restringir o resultado.

Através do link [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll) é possível obter mais informações de como utilizar os filtros disponíveis.

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/EduParcelaData?start=3&limit=2](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData?start=3&limit=2)

xmlMensagem de respostatrue

#### Retornando apenas uma parcela:

Para realizar a consulta de uma parcela, será necessário a utilização dos valores de chave primária da parcela:

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/EduParcelaData/1$\_$17816](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000108)

O valor informado no final da URL "***1$\_$17816***" ("***CODCOLIGADA$\_$IDPARCELA***") se refere aos valores da coligada e do id da parcela.

Esse valores são separados pelos caracteres "$" e "\_".

Para a realização dessa requisição, deverá ser utilizado o método: **GET**.

xmlMensagem de respostatrue

### CADASTRO

#### Cadastrando uma parcela:

Para realizar o cadastro de uma parcela é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão inseridos e no cabeçalho da mensagem deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto em que a parcela será incluída.

URL que será utilizada para cadastro da parcela: [http://localhost:8051/rmsrestdataserver/rest/EduParcelaData](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData)

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Segue o exemplo de um conjunto mínimo de informações necessárias para cadastro de uma parcela:

xmlCorpo da mensagemtrueImportante

A obrigatoriedade dos campos pode variar de acordo com a parametrização realizada no sistema.

Caso esteja utilizando a aplicação SoapUI, as informações do cabeçalho podem ser informadas conforme abaixo:

xmlMensagem de respostatrue

### Alterações

#### Atualizando informações da parcela:

Para realizar a atualização de cadastro de uma parcela é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados, assim como, a tag ID que informará qual parcela será alterada.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** **e****CODSISTEMA**para criação do contexto em que a parcela será inclusa.

URL que será utilizada para cadastro do aluno: [http://localhost:8051/rmsrestdataserver/rest/EduParcelaData/1$\_$18133](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000000226)

Para a realização dessa requisição, deverá ser utilizado o método: **PUT**.

Segue o exemplo de um conjunto de informações de uma parcela que será alterada:

xmlCorpo da mensagemtrue

Exemplo da resposta:

xmlMensagem de respostatrue

### Exclusões

#### Excluindo a parcela:

A exclusão de uma parcela seguirá a mesma ideia da alteração, onde precisaremos passar as chaves da parcela a ser excluída, assim como o corpo da mensagem com suas informações.

 No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** e **CODSISTEMA**para criação do contexto.

URL que será utilizada para cadastro da parcela: [http://localhost:8051/rmsrestdataserver/rest/EduParcelaData/1$\_$18133](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000000226)

Para a realização dessa requisição, deverá ser utilizado o método: **DELETE**.

Segue o exemplo de um conjunto de informações de uma parcela que serão removidas:

xmlCorpo da mensagemtrue

Resposta da mensagem:

xmlMensagem de respostatrue
