---
content_hash: 76626acffc670eb07bfa2cce9938be10f90429b7722696217be4f6a24793edc6
fetched_at: '2026-06-29T00:09:04.184455+00:00'
page_id: '382557048'
product: rm
source: tdn-rm
title: Contrato (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382557048
version: 8
---

### Visão geral

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de **Contrato (EduContratoData)** para a realização de requisições de consulta, inclusão, alteração ou exclusão de dados.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT, POST e DELETE e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### Consulta

Para a realização de uma consulta, é necessária a utilização do método ***GET.***

Através desse método, é possível realizar a consulta de apenas um contrato ou de uma lista de contratos.

Para a requisição de informações de um contrato será necessário passar os valores da chave primária do contrato: **CODCOLIGADA, RA, IDPERLET** e **CODCONTRATO**.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL**, **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto.

#### Retornando uma lista de contratos:

Para a consulta de uma lista de contratos, é necessário a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rmsrestdataserver/rest/EduContratoData***

É possível, nessa consulta, utilizar filtros para a limitação da quantidade de informações retornadas e, também, para restringir o resultado.

Através do link [Serviço GetAll](http://tdn.totvs.com/display/LRM/GetAll) é possível obter mais informações de como utilizar os filtros disponíveis.

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/EduContratoData?start=3&limit=2](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData?start=3&limit=2)

xmlMensagem de respostatrue

#### Retornando apenas um contrato:

Para realizar a consulta de um contrato, será necessário a utilização dos valores de chave primária do contrato:

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/EduContratoData/1$\_$LFS-0007$\_$55$\_$1523](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000108)

O valor informado no final da URL "***1$\_$LFS-0007$\_$55$\_$1523***" ("**CODCOLIGADA$\_$RA$\_$IDPERLET$\_$CODCONTRATO**") se refere aos valores da coligada, do registro acadêmico, do período letivo e do código do contrato.

Esse valores são separados pelos caracteres "$" e "\_".

Para a realização dessa requisição, deverá ser utilizado o método: **GET**.

xmlMensagem de respostatrue

### CADASTRO

#### Cadastrando um contrato:

Para realizar o cadastro de um contrato é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão inseridos e no cabeçalho da mensagem deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**e **CODSISTEMA** para criação do contexto em que o contrato será incluído.

URL que será utilizada para cadastro do contrato: [http://localhost:8051/rmsrestdataserver/rest/EduContratoData](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData)

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Segue o exemplo de um conjunto mínimo de informações necessárias para cadastro de um contrato:

xmlCorpo da mensagemtrueImportante

A obrigatoriedade dos campos pode variar de acordo com a parametrização realizada no sistema.

Caso esteja utilizando a aplicação SoapUI, as informações do cabeçalho podem ser informadas conforme abaixo:

xmlMensagem de respostatrue

### Alterações

#### Atualizando informações do contrato:

Para realizar a atualização de cadastro de um contrato é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados, assim como, a tag ID que informará qual contrato será alterado.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**e **CODSISTEMA** para criação do contexto em que o contrato será incluso.

URL que será utilizada para cadastro do aluno: [http://localhost:8051/rmsrestdataserver/rest/EduContratoData/1$\_$LFS-0007$\_$55$\_$1522](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000000226)

Para a realização dessa requisição, poderá ser utilizado o método **PUT** ou **PATCH:**

Segue o exemplo de um conjunto de informações de um contrato que será alterado via método **PUT**:

xmlCorpo da mensagemtrue

Exemplo da resposta:

xmlMensagem de respostatrue

Segue o exemplo de um conjunto de informações de um contrato que será alterado via método **PATCH**:

xmlCorpo da mensagemtrue

Exemplo da resposta:

xmlMensagem de respostatrueImportante

Algumas validações são feitas na edição do contrato como:

* **Validação de alteração no período de competência contábil do contrato**: Quando o sistema está parametrizado para utilizar contabilização por competência e a data a ser utilizada é a data contábil do contrato, o sistema não permitirá a alteração se os campos de data inicial ou data final de competência forem alterados e existir alguma contabilização por competência realizada para o contrato.
* **Validação de data de competência do movimento**: Quando o sistema está parametrizado para gerar movimento por competência e a data a ser utilizada é a data de competência do contrato e plano de pagamento, o sistema não permitirá a alteração se os campos de data inicial ou data final de competência para emissão de NFS-e forem alterados e existir movimento por competência gerado para o contrato.

### Exclusões

#### Excluindo o contrato:

A exclusão de um contrato seguirá a mesma ideia da alteração, onde precisaremos passar as chaves do contrato a ser excluído, assim como o corpo da mensagem com suas informações.

 No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**e **CODSISTEMA** para criação do contexto.

URL que será utilizada para cadastro do contrato: [http://localhost:8051/rmsrestdataserver/rest/EduContratoData/1$\_$LFS-0007$\_$55$\_$1523](http://localhost:8051/rmsrestdataserver/rest/EduAlunoData/1$_$0000000226)

Para a realização dessa requisição, deverá ser utilizado o método: **DELETE**.

Segue o exemplo de um conjunto de informações de um contrato que serão removidos:

xmlCorpo da mensagemtrue

Resposta da mensagem:

xmlMensagem de respostatrue
