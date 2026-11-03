---
content_hash: b609cb8e1c8f935b618126c304487bc0e6c78e2e79eb1588882ee9bb9b00dae3
fetched_at: '2026-06-29T00:10:56.082320+00:00'
page_id: '590621544'
product: rm
source: tdn-rm
title: Nota/Falta de Etapa do Aluno (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=590621544
version: 6
---

## **01. VISÃO GERAL**

Através do serviço **RMSRestDataServer**, via ***RESTful***, o usuário poderá acessar o dataserver de Nota/Falta de Etapa **(EduAlunoEtapaData)** para a realização de requisições de consulta, inclusão, alteração ou exclusão de dados.  

Essas requisições são disponibilizadas através dos métodos: GET, PUT, POST e DELETE e são, sempre, utilizados os valores das chaves primárias como índice para que elas sejam realizadas.

No link [Serviços RESTful no RM](http://tdn.totvs.com/pages/viewpage.action?pageId=190515801) é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **Framework**, os serviços via ***RESTfull*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](http://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

## **02. CONSULTA**

Para a realização de uma consulta, é necessária a utilização do verbo ***GET.***

Através desse verbo, é possível realizar a consulta de apenas uma Nota/Falta de Etapa. É obrigatório informar os valores chaves na requisição: ***CODCOLIGADA , CODETAPA, TIPOETAPA, IDTURMADISC e RA.***

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL**, **CODTIPOCURSO** e **CODSISTEMA** para criação do contexto da aplicação.

Exemplo:

[http://localhost:8051/rmsrestdataserver/rest/](http://localhost:8051/rmsrestdataserver/rest/Eduprovasdata/1$_$4385$_$1$_$N$_$1)[EduAlunoEtapaData/1$\_$1$\_$F$\_$1114$\_$EB-00246](http://localhost:8051/rmsrestdataserver/rest/EduAlunoEtapaData/1$_$1$_$F$_$1114$_$EB-00246)

## **03. CADASTRO**

#### Cadastrando uma Nota/Falta de etapa:

Para realizar o cadastro de uma Nota/Falta é necessário que sejam passados os dados do contexto CODCOLIGADA, CODFILIAL, CODTIPOCURSO e CODSISTEMA como valores no Header da requisição. Além disso, deve ser informado todos os valores do registro a ser incluído, conforme padrão abaixo.

URL que será utilizada para cadastro da Etapa da turma Disciplina: [http://localhost:8051/rmsrestdataserver/rest/](http://localhost:8051/rmsrestdataserver/rest/Eduprovasdata/1$_$4385$_$1$_$N$_$1)[EduAlunoEtapaData](http://localhost:8051/rmsrestdataserver/rest/EduAlunoEtapaData/1$_$1$_$F$_$1114$_$EB-00246)

Para a realização dessa requisição, deverá ser utilizado o verbo ***POST***.

Segue o exemplo de um conjunto mínimo de dados necessários para cadastro de uma Nota/Falta de uma etapa.

jsCorpo da mensagemtrueImportante

A obrigatoriedade dos campos pode variar de acordo com a parametrização realizada no sistema.

## **04. ATUALIZANDO INFORMAÇÕES DE UMA NOTA/FALTA DE ETAPA**

Para realizar a atualização de registro é necessário que sejam passados, entre um conjunto de chaves, todos os campos que serão alterados, assim como, a chave do registro a ser alterado.

No cabeçalho da mensagem, também, deverão ser incluídos os campos **CODCOLIGADA**, **CODFILIAL,** **CODTIPOCURSO**e **CODSISTEMA** para criação do contexto em que a Avaliação será incluso.

URL que será utilizada para cadastro da Avaliação: [http://localhost:8051/rmsrestdataserver/rest/](http://localhost:8051/rmsrestdataserver/rest/Eduprovasdata/1$_$4385$_$1$_$N$_$1)[EduAlunoEtapaData/1$\_$1$\_$F$\_$1114$\_$EB-00246](http://localhost:8051/rmsrestdataserver/rest/EduAlunoEtapaData/1$_$1$_$F$_$1114$_$EB-00246)

Para a realização dessa requisição, deverá ser utilizado o método: ***PUT***.

Segue o exemplo de um conjunto de informações de uma Atividade que serão alterados:

xmlCorpo da mensagemtrue

Não encontra-se disponível as opções de listagem de vários registros e a opção de exclusão.
