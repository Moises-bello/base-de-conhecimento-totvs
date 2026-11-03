---
content_hash: a0bb563048daf267e34ba843ac35ba9eba1a49b4168ea373d1e791d74abb06ad
fetched_at: '2026-06-29T00:09:04.001980+00:00'
page_id: '382541855'
product: rm
source: tdn-rm
title: Avaliação da Etapa da Turma Disciplina(Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382541855
version: 5
---

### Visão geral

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de Avaliação **(EduprovasData)** para a realização de requisições de consulta, inclusão, alteração ou exclusão de dados.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT, POST e DELETE e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### Consulta

Para a realização de uma consulta, é necessária a utilização do método ***GET.***

Através desse método, é possível realizar a consulta de apenas uma Avaliação ou de uma lista de Avaliações de uma Etapa da Turma Disciplina.

Para a requisição de informações de uma Avaliação será necessário passar os valores da chave primária: ***CODCOLIGADA , IDTURMADISC, CODETAPA, TIPOETAPA e CODPROVA.***

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL**, **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto.

#### Retornando uma lista e uma Avaliação:

Para a consulta de uma lista de Avaliações, é necessário a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rmsrestdataserver/rest/EduProvasData***

É possível, nessa consulta, utilizar filtros para a limitação da quantidade de informações retornadas e também para restringir o resultado.

Através do link [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll) é possível obter mais informações de como utilizar os filtros disponíveis.

Exemplo:

<http://localhost:8051/rmsrestdataserver/rest/EduprovasData?start=3&limit=2>

xmlMensagem de respostatrue

#### Retornando apenas uma Avaliação:

Para realizar a consulta de um Avaliação, será necessário a utilização dos valores de chave primária de Avaliações (Sprovas)

Exemplo:

<http://localhost:8051/rmsrestdataserver/rest/Eduprovasdata/1$_$4385$_$1$_$N$_$1>

O valor informado no final da URL "[1$\_$4385$\_$1$\_$N$\_$1](http://localhost:8051/rmsrestdataserver/rest/Eduprovasdata/1$_$4385$_$1$_$N$_$1)" se refere aos valores da coligada,  o código da coligada, o código da Turma Disciplina, o código da Etapa, tipo da Etapa e o código da Prova da Avaliação

Esse valores são separados pelos caracteres "$" e "\_".

Para a realização dessa requisição, deverá ser utilizado o método: **GET**.

### CADASTRO

#### Cadastrando uma Avaliação na Etapa de uma Turma Disciplina:

Para realizar o cadastro de uma Avaliação é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão inseridos e no cabeçalho da mensagem deverão ser incluídos os campos ***CODCOLIGADA , IDTURMADISC, CODETAPA, TIPOETAPA e CODPROVA*** para criação do contexto em que a Avaliação será inclusa.

URL que será utilizada para cadastro da Etapa da turma Disciplina: [http://localhost:8051/rmsrestdataserver/rest/EduprovasData](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData)

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Segue o exemplo de um conjunto mínimo de informações necessárias para cadastro de uma Avaliação.

xmlCorpo da mensagemtrueImportante

A obrigatoriedade dos campos pode variar de acordo com a parametrização realizada no sistema.

Caso esteja utilizando a aplicação SoapUI, as informações do cabeçalho podem ser informadas conforme abaixo:

Preenchendo o Cabeçalho para o Post

Informe os campos do contexto: CODCOLIGADA, CODFILIAL, CODTIPOCURSO e CODSISTEMA

xmlMensagem de respostatrue

Alterações

#### Atualizando informações a Avaliação de uma Etapa da turma

Para realizar a atualização de cadastro de uma Avaliação é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados, assim como, a tag ID que informará qual Avaliação que será alterada.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**e **CODSISTEMA** para criação do contexto em que a Avaliação será incluso.

URL que será utilizada para cadastro da Avaliação: [http://localhost:8051/rmsrestdataserver/rest/EduprovasData/1$\_$4388$\_$1$\_$N$\_$3](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000000226)

Para a realização dessa requisição, deverá ser utilizado o método: **PUT**.

Segue o exemplo de um conjunto de informações de uma Atividade que serão alterados:

xmlCorpo da mensagemtrueImportante

No corpo da mensagem é de suma importância informar os campos **CODCOLIGADA, CODFILIAL,****CODTIPOCURSO**e  **CODSISTEMA.**

Exemplo da resposta:

xmlMensagem de respostatrue

### Exclusões

#### Excluindo uma Atividades de uma Etapa.

A exclusão de uma Atividade seguirá a mesma ideia da alteração, onde precisaremos passar as chaves da Atividade a ser excluído, assim como o corpo da mensagem com suas informações.

 No cabeçalho da mensagem, também deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**e **CODSISTEMA** para criação do contexto.

URL que será utilizada para cadastro da Atividade de uma Etapa: [http://localhost:8051/rmsrestdataserver/rest/EduHabilitacaoData/1$\_$4388$\_$1$\_$N$\_$3](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$ES-00230)

Para a realização dessa requisição, deverá ser utilizado o método: **DELETE**.

Segue o exemplo de um conjunto de informações de uma Avaliação que será deletado.

xmlCorpo da mensagemtrue

Resposta da mensagem:

xmlMensagem de respostatrue
