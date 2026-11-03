---
content_hash: 161c5bb16035fde68ab83e353cb3e2c86f586645ffab22d7863ac570a9c75325
fetched_at: '2026-06-29T00:08:58.676279+00:00'
page_id: '360454215'
product: rm
source: tdn-rm
title: Tipo de Referência (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=360454215
version: 5
---

### Visão geral

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de **Tipo de Referência****(BibTipoRefData)** para a realização de requisições de consulta, inclusão, alteração ou exclusão de dados.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT, POST e DELETE e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### Consulta

Para a realização de uma consulta, é necessária a utilização do método ***GET.***

Através desse método, é possível realizar a consulta de apenas um tipo de referência ou de uma lista de tipos de referência.

Para a requisição de informações de um tipo de referência será necessário passar os valores da chave primária do tipo de referência: **CODCOLIGADA** e **CODIGO**.

#### Retornando uma lista e tipos de referência:

Para a consulta de uma lista de tipos de referência, é necessário a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rmsrestdataserver/rest/BibTipoRefData***

É possível, nessa consulta, utilizar filtros para a limitação da quantidade de informações retornadas e, também, para restringir o resultado.

Através do link [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll) é possível obter mais informações de como utilizar os filtros disponíveis.

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/BibTipoRefData?start=3&limit=2](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData?start=3&limit=2)

xmlMensagem de respostatrue

#### Retornando apenas um tipo de referência:

Para realizar a consulta de um tipo de referência, será necessário a utilização dos valores de chave primária do tipo de referência:

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/BibTipoRefData/1$\_$](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000108)5

O valor informado no final da URL "***1$\_$0000108***" se refere aos valores da coligada e do codigo do tipo de Referência.

Esse valores são separados pelos caracteres "$" e "\_".

Para a realização dessa requisição, deverá ser utilizado o método: **GET**.

xmlMensagem de respostatrue

### CADASTRO

#### Cadastrando um tipo de referência:

Para realizar o cadastro de um tipo de referência é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão inseridos e no cabeçalho da mensagem deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL** e **CODUNIDADE** para criação do contexto em que o tipo de referência será incluso.

URL que será utilizada para cadastro do tipo de referência: [http://localhost:8051/rmsrestdataserver/rest/BibTipoRefData](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData)

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Segue o exemplo de um conjunto mínimo de informações necessárias para cadastro de um tipo de referência:

xmlCorpo da mensagemtrueImportante

A obrigatoriedade dos campos pode variar de acordo com a parametrização realizada no sistema.

Caso esteja utilizando a aplicação SoapUI, as informações do cabeçalho podem ser informadas conforme abaixo:

xmlMensagem de respostatrue

### Alterações

#### Atualizando informações do tipo de referência:

Para realizar a atualização de cadastro de um tipo de referência é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados, assim como, a tag ID que informará qual tipo de referência será alterado.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL** e **CODUNIDADE** para criação do contexto em que o tipo de referencia será incluso.

URL que será utilizada para cadastro do tipo de referência: [http://localhost:8051/rmsrestdataserver/rest/BibTipoRefData/1$\_$12](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000000226)

Para a realização dessa requisição, deverá ser utilizado o método: **PUT**.

Segue o exemplo de um conjunto de informações de um tipo de referência que serão alterados:

xmlCorpo da mensagemtrue

Exemplo da resposta:

xmlMensagem de respostatrue

### Exclusões

#### Excluindo o tipo de referência:

A exclusão de um tipo de referência seguirá a mesma ideia da alteração, onde precisaremos passar as chaves do tipo de referência a ser excluído, assim como o corpo da mensagem com suas informações.

 No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL** e **CODUNIDADE** para criação do contexto.

URL que será utilizada para cadastro do tipo de referência: [http://localhost:8051/rmsrestdataserver/rest/BibTipoRefData/1$\_$12](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$ES-00230)

Para a realização dessa requisição, deverá ser utilizado o método: **DELETE**.

Segue o exemplo de um conjunto de informações de um tipo de referência que serão alterados:

xmlCorpo da mensagemtrue

Resposta da mensagem:

xmlMensagem de respostatrue
