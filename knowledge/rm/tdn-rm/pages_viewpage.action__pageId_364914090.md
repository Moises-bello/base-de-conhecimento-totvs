---
content_hash: 7c1d429cc45bb6b8a013015f8714cf1b6de42cc3a35ed264d2e415935282201c
fetched_at: '2026-06-29T00:08:59.782784+00:00'
page_id: '364914090'
product: rm
source: tdn-rm
title: Inscrição de candidatos (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364914090
version: 13
---

### Visão geral

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de **Inscrições (EduPsInscricaoAreaOfertadaData)** para a realização de requisições de consulta, inclusão ou alteração de dados, para cancelar ou excluir uma inscrição é necessário utilizar os processos disponibilizados na visão de inscrições.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT e POST e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### Consulta

Para a realização de uma consulta, é necessária a utilização do método ***GET.***

Através desse método, é possível realizar a consulta de apenas um inscrito ou de uma lista de inscristos.

Para a requisição de informações de um inscrito será necessário passar os valores da chave primária do aluno: **CODCOLIGADA** , **IDPS** ,****NUMEROINSCRICAO****.

#### Retornando uma lista e inscrições:

Para a consulta de uma lista de inscrições, é necessário a utilização da URL abaixo utilizando filtros, conforme descrito logo abaixo através do [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll):

***HTTP://<SERVIDOR>:<HTTPORT>/rmsrestdataserver/rest/EduPSInscricaoAreaOfertadaData***

É possível, nessa consulta, utilizar filtros para a limitação da quantidade de informações retornadas e, também, para restringir o resultado.

Através do link [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll) é possível obter mais informações de como utilizar os filtros disponíveis.

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/EduPSInscricaoAreaOfertadaData?start=0&limit=](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData?start=3&limit=2)3

xmlMensagem de respostatrue

#### Retornando apenas uma inscrição:

Para realizar a consulta de uma inscrição, será necessário a utilização dos valores de chave primária da inscrição (CODCOLIGADA, IDPS e NUMEROINSCRICAO).

Exemplo:

<http://localhost:8051/rmsrestdataserver/rest/EduPSInscricaoAreaOfertadaData/1$_$26$_$1>

O valor informado no final da URL "***1$\_$26$\_$1***" se refere aos valores da coligada, do código do processo seletivo e do número de inscrição do candidato.

Esse valores são separados pelos caracteres "$" e "\_".

Para a realização dessa requisição

xmlMensagem de respostatrue

### CADASTRO

#### Cadastrando uma inscrição:

Para realizar o cadastro de uma inscrição é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão inseridos e no cabeçalho da mensagem deverão ser incluídos os campos **CODCOLIGADA e** **CODFILIAL** para criação do contexto em que a inscrição será inclusa.

URL que será utilizada para cadastro da inscrição: [http://localhost:8051/rmsrestdataserver/rest/EduPSInscricaoAreaOfertadaData](http://localhost:8051/rmsrestdataserver/rest/EduPSInscricaoAreaOfertadaDataEduAlunoData)

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Segue o exemplo de um conjunto mínimo de informações necessárias para cadastro de uma inscrição:

xmlCorpo da mensagemtrueImportante

A obrigatoriedade dos campos pode variar de acordo com a parametrização realizada no sistema.

### Alterações

#### Atualizando informações da inscrição:

Para realizar a atualização de uma inscrição o é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados, assim como, a tag ID que informará qual inscrição será alterada.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**e **CODFILIAL**para criação do contexto em que a inscrição será alterada.

URL que será utilizada para cadastro do aluno: <http://localhost:8051//RMSRestDataServer/Rest/EduPSInscricaoAreaOfertadaData/1$_$26$_$1>

Para a realização dessa requisição, deverá ser utilizado o método: **PUT**.

Segue o exemplo de um conjunto de informações de uma inscrição que serão alteradas:

xmlCorpo da mensagemtrue

Exemplo da resposta:

xmlMensagem de respostatrue

### Alterações (patch)

#### Atualizando informações da inscrição:

Para realizar a atualização de uma inscrição o é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**e **CODFILIAL**para criação do contexto em que a inscrição será alterada.

URL que será utilizada para cadastro do aluno: <http://localhost:8051//RMSRestDataServer/Rest/EduPSInscricaoAreaOfertadaData/1$_$26$_$1>

Para a realização dessa requisição, deverá ser utilizado o método: **Patch**.

jsRequisição de exemplotrueObservação 

Nesse caso atualizamos especificamente o campo Status (Caso a intenção for atualizar outro campo seja de outro objeto ou não, basta seguir o modelo acima).

Outra possível abordagem utilizando o método patch é  passar o objeto completo (como no put) e alterar apenas os campos desejados.

Exemplo da resposta:

jsExemplo da resposta true
