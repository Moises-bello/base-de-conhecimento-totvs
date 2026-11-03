---
content_hash: 66449f3bb7f3834b5b73acc67c9f6ffcacf7664e5a3e9e0225800ae8d378e660
fetched_at: '2026-06-29T00:08:53.397754+00:00'
page_id: '344473439'
product: rm
source: tdn-rm
title: Turma/Disciplina (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344473439
version: 4
---

### Visão geral

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de **Turma/Disciplina (EduTurmaDiscData)** para a realização de requisições de consulta, inclusão, alteração ou exclusão de dados.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT, POST e DELETE e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### Consulta

Para a realização de uma consulta, é necessária a utilização do método ***GET.***

Através desse método, é possível realizar a consulta de apenas uma Turma/Disc ou de uma lista de Turma/Disciplinas.

Para a requisição de informações de uma Turma/Disciplina será necessário passar os valores da chave primária da Turma/Disciplina: **CODCOLIGADA e IDTURMADISC****.**

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL**, **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto.

#### Retornando uma lista e Turma/Disciplina:

Para a consulta de uma lista de Turmas/Disciplinas, é necessário a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rmsrestdataserver/rest/EduTurmaDiscData***

É possível, nessa consulta, utilizar filtros para a limitação da quantidade de informações retornadas e também para restringir o resultado.

Através do link [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll) é possível obter mais informações de como utilizar os filtros disponíveis.

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/EduTurmaDiscData?start=3&limit=2](http://localhost:8051/rmsrestdataserver/rest/EduTurmaData?start=3&limit=2)

xmlMensagem de respostatrue

#### Retornando apenas uma Turma/Disciplina:

Para realizar a consulta de uma Turma/Disciplina, será necessário a utilização dos valores de chave primária da Turma/Disciplina:

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/EduTurmaDiscData/1$\_$2944](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000108)

O valor informado no final da URL "**1$\_$2944**" se refere aos valores da Coligada e Id da Turma/Disciplina.

Esse valores são separados pelos caracteres "$" e "\_".

Para a realização dessa requisição, deverá ser utilizado o método: **GET**.

### CADASTRO

#### Cadastrando uma Turma/Disciplina:

Para realizar o cadastro de uma turma/Disciplina é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão inseridos e no cabeçalho da mensagem deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**  e **CODSISTEMA**para criação do contexto em que o Turma/Disciplina será inclusa.

URL que será utilizada para cadastro da turma/Disciplina: [http://localhost:8051/rmsrestdataserver/rest/EduTurmaDiscData](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData)

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Segue o exemplo de um conjunto mínimo de informações necessárias para cadastro de uma Turma/Disciplina:

xmlCorpo da mensagemtrue

No momento de informar o IDTURMADISC deve-se informar o digito 0 "Zero". Desta forma o sistema gerará o código.

Importante

A obrigatoriedade dos campos pode variar de acordo com a parametrização realizada no sistema.

Caso esteja utilizando a aplicação SoapUI, as informações do cabeçalho podem ser informadas conforme abaixo:

xmlMensagem de respostatrue

Alterações

#### Atualizando informações da Turma/Disciplina:

Para realizar a atualização de cadastro de uma Turma/Disciplina é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** e **CODSISTEMA**para criação do contexto em que a Turma/Disciplina será inclusa.

URL que será utilizada para cadastro da turma/disciplina: [http://localhost:8051/rmsrestdataserver/rest/EduTurmaDiscData/1$\_$2945](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000000226)

Para a realização dessa requisição, deverá ser utilizado o método: **PUT**.

Segue o exemplo de um conjunto de informações de uma Turma/Disciplina que serão alteradas:

xmlCorpo da mensagemtrueImportante

No corpo da mensagem é de suma importância informar os campos **CODCOLIGADA e ID****TURMADISC.**

Exemplo da resposta:

xmlMensagem de respostatrue

### Exclusões

#### Excluindo uma Turma/Disciplina:

A exclusão de uma Turma/Disciplina seguirá a mesma ideia da alteração, onde precisaremos passar as chaves da Turma/Disciplina a ser excluída, assim como o corpo da mensagem com suas informações.

 No cabeçalho da mensagem, também deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO** e **CODSISTEMA**para criação do contexto.

URL que será utilizada para cadastro do Curso: [http://localhost:8051/rmsrestdataserver/rest/EduTurmaDiscData/1$\_$2945](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$ES-00230)

Para a realização dessa requisição, deverá ser utilizado o método: **DELETE**.

Segue o exemplo de um conjunto de informações de uma Turma/Disciplina que serão alteradas:

xmlCorpo da mensagemtrue

Resposta da mensagem:

xmlMensagem de respostatrue
