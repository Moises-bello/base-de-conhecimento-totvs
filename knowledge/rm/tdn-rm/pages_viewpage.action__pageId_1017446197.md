---
content_hash: 3e02152c5da2e9baebf0897b6d16a88eb467de2289fe77a0d32be523bf82e3a2
fetched_at: '2026-06-29T00:05:47.785625+00:00'
page_id: '1017446197'
product: rm
source: tdn-rm
title: URIs legíveis - Endpoints
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1017446197
version: 2
---

## **Padrão de nomenclatura**

**http://{{host}}/api/{{agrupador}}/{{versão}}/{{resource}}**

* Dê preferência para o plural ao disponibilizar o **resource**. Utilize `/users`ao invés de `/user;`
* Dê preferência para URL's em minúsculo, evite `GET /Users`, use `GET /users;`
* Na API, utilizamos [semantic versioning](https://semver.org/), um padrão que é dividido em *major*, *minor* e *patch*. Somente a *Major Version* é utilizada na URL. Por exemplo: V1 ou V2;
* Deve ser orientada a recursos representados por substantivos no plural. **Não se deve orientar a verbos Get, Put, Post e Delete.**

A raiz do resource deve retornar uma coleção. Por exemplo `/users` deve retornar um lista de usuários.  
Se desejar obter um **resource** especifico utilize o nível seguinte especificando seu identificador único. GET `/users/2`. Não precisa ser o id do banco, poderia ser outro campo, desde que seja identificador único. Um usuário poderia ser o username.

* **`GET /users`** -> Retorna uma lista de usuários
* **`GET /users/bruno`** -> Retorna o usuário com username bruno
* **`POST /users`**-> Cria um usuário
* **`PUT /users/bruno`** -> Atualiza o usuário bruno
* **`PATCH /users/bruno`** -> Atualiza parcialmente o usuário bruno
* **`DELETE /users/bruno`**-> Remove o usuário bruno

**Relacionamento filho** - Se existir alguma tabela filho do **resource**, eles devem estar mapeados para o mesmo endpoint. Exemplo

* **`GET /users/bruno/claims`** -> Retorna uma lista de claims do usuário bruno
* **`GET /users/bruno/claims/6`** -> Retorna o claims com Id 6
* **`POST /users/bruno/claims`** -> Cria uma claim para usuário bruno
* **`PUT /users/bruno/claims/6`** -> Atualiza a claim 6 do usuário bruno
* **`PATCH /users/bruno/claims/6`**-> Atualiza parcialmente a claim 6 do usuário bruno
* **`DELETE /users/bruno/claims/6`** -> Remove a claim 6 do usuário bruno

**Chave composta**

* **`GET /sales/20_1020/rules`** -> Retorna uma lista de regras da coligada 20 e venda 1020
* **`GET /sales/20_1020/rules/6`** -> Retorna uma a regra 6 da coligada 20 e venda 1020
* **`POST /sales/20_1020/rules`** -> Cria a regra 6  da coligada 20 e venda 1020
* **`PUT /sales/20_1020/rules/6`** -> Atualiza a regra 6  da coligada 20 e venda 1020
* **`PATCH /sales/20_1020/rules/6`**-> Atualiza parcialmente a regra 6  da coligada 20 e venda 1020
* **`DELETE /sales/20_1020/rules/6`** -> Remove a regra 6  da coligada 20 e venda 1020

#### Exemplo

[RoutePrefix("imb/v1/modalities")]

[Route("{modalityId}/enterprises/{companyId}\_{enterpriseId}")]  
[HttpGet]  
public List<ImbVendaModalidadeRegraEntity> GetTabelaPrecoModalidade(int modalityId, int companyId, int enterpriseId)

#### As propriedades devem ser sempre em minúsculo

[JsonProperty("codcoligada")]

#### Evite adicionar na URI a operação a ser realizada no recurso

Os recursos que uma aplicação gerencia podem ser manipulados de diversas maneiras, sendo para isso disponibilizada algumas operações para manipula-los, tais como: criar, listar, excluir, atualizar, etc.

A manipulação dos recursos deve ser feita utilizando-se os métodos do protocolo HTTP, que inclusive é um dos princípios do REST que será discutido mais adiante.

Portanto, evite definir URIs que contenham a operação a ser realizada em um recurso, tais como:

* **`GET/PUT/DELETE/PATCH /users/Cadastrar`**;
* **`GET/PUT/DELETE/PATCH /users/bruno/Excluir`**;
* **`GET/PUT/DELETE/PATCH /users/bruno/Atualizar`**.

Logo ações se fazem necessários no dia-a-dia. E é importante reforçar que **não fere os padrões REST**.

* `POST /candidatos/{id}/candidatar -- Grava a aplicação de um candidato a uma vaga`
* `POST /candidatos/{id}/aprovar -- Aprova um candidato`
* `DELETE /candidatos/{id}/aprovar -- Cancela a aprovação`
* `POST /candidatos/{id}/reprovar -- Reprova o candidato`
* `DELETE /candidatos/{id}/reprovar -- Cancela a reprovação`
* `POST /candidatos/{id}/transferir -- Transfere o candidato para outra vaga`
* `DELETE /candidatos/{id}/transferir -- Cancela a transferência`

Nesse formato a comunicação é clara. No backend o desenvolvedor não vai precisar criar if's ou switchs e traduzir a intenção do método "CRUD". O próprio endpoint comunica sua intenção.
