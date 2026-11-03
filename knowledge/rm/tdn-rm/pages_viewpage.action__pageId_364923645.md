---
content_hash: 1cbfdf57a5c95484bb2358d2fabc6b82cc5ec4a8f6113a319d5a80105cfc2296
fetched_at: '2026-06-29T00:09:00.186531+00:00'
page_id: '364923645'
product: rm
source: tdn-rm
title: Processo Seletivo Terceirizado (REST)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364923645
version: 4
---

### Visão geral

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de **Candidatos do Processo Seletivo Terceirizado (EduCandidatoProcSelData)** para a realização de requisições de consulta, inclusão ou alteração de dados.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT e POST e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### Consulta

Para a realização de uma consulta, é necessária a utilização do método ***GET.***

Através desse método, é possível realizar a consulta de apenas um candidato ou de uma lista de candidatos.

Para a requisição de informações de um candidato será necessário passar os valores da chave primária do candidato: **CODCOLIGADA, IDPROCSEL** e **NUMEROINSCPROCSEL**.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL**, **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto.

#### Retornando uma lista de candidatos:

Para a consulta de uma lista de candidatos, é necessário a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rmsrestdataserver/rest/EduCandidatoProcSelData***

É possível, nessa consulta, utilizar filtros para a limitação da quantidade de informações retornadas e, também, para restringir o resultado.

Através do link [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll) é possível obter mais informações de como utilizar os filtros disponíveis.

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/EduCandidatoProcSelData?start=3&limit=2](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData?start=3&limit=2)

xmlMensagem de respostatrue

#### Retornando apenas um candidato:

Para realizar a consulta de um candidato, será necessário a utilização dos valores de chave primária do candidato:

Exemplo:

<http://localhost:8051/rmsrestdataserver/rest/EduCandidatoProcSelData/1$_$8$_$1>

O valor informado no final da URL "***1$\_$8$\_$1***" se refere aos valores da coligada, código do processo seletivo e do número de inscrição do candidato.

Esse valores são separados pelos caracteres "$" e "\_".

Para a realização dessa requisição, deverá ser utilizado o método: **GET**.

xmlMensagem de respostatrue

### CADASTRO

#### Cadastrando um candidato:

Para realizar o cadastro de um candidato é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão inseridos e no cabeçalho da mensagem deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**e **CODSISTEMA** para criação do contexto em que o candidato será incluso.

URL que será utilizada para cadastro do candidato: <http://localhost:8051/rmsrestdataserver/rest/EduCandidatoProcSelData>

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Segue o exemplo de um conjunto mínimo de informações necessárias para cadastro de um candidato:

xmlCorpo da mensagemtrueImportante

A obrigatoriedade dos campos pode variar de acordo com a parametrização realizada no sistema.

Caso esteja utilizando a aplicação SoapUI, as informações do cabeçalho podem ser informadas conforme abaixo:

xmlMensagem de respostatrue

### Alterações

#### Atualizando informações do candidato:

Para realizar a atualização de cadastro de um candidato é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados, assim como, a tag ID que informará qual candidato será alterado.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL**, **CODTIPOCURSO**e **CODSISTEMA** para criação do contexto em que o candidato será incluso.

URL que será utilizada para cadastro do candidato: <http://localhost:8051/rmsrestdataserver/rest/EduCandidatoProcSelData/1$_$8$_$4>

Para a realização dessa requisição, deverá ser utilizado o método: **PUT**.

Segue o exemplo de um conjunto de informações de um candidato que serão alterados:

xmlCorpo da mensagemtrue

Exemplo da resposta:

xmlMensagem de respostatrue
