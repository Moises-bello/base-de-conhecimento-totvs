---
content_hash: 0f94e5a45d0ece9c5df2abfc90d6dc46ec3ea98e56f1dfda5ea9a7513196d51e
fetched_at: '2026-06-28T21:35:27.460239+00:00'
page_id: '550330927'
product: fluig
source: tdn-fluig
title: Identity | Operações RAC pendentes de um usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550330927
version: 4
---

# Índice

true.\*ndicenone

# Operações RAC pendentes de um usuário

A API que mostra as operações RAC pendentes de um usuário (**/pending-user-operations**) retornava as informações necessárias para que a aplicação externa conclua a operação, mas não incluía o autor da operação no Identity, e nem a data.

Essas informações foram acrescentadas no retorno dessa API na forma do campo “***author***” e “***date***”.

Exemplo do que era retornado antes para uma operação de adicionar usuário a um papel (*role*):

jsRetorno anterior

Exemplo do que é retornado atualmente para a operação de adicionar um usuário a um papel (*role*). Note o campo novo “***author***”:

jsRetorno atual

API em questão:

* Endpoint: <https://app.fluigidentity.com/rest/v2/companies/>**{COMPANY\_ID}**/users/**{USER\_ID}**/applications/**{APPLICATION\_ID}**/pending-user-operations
* Método HTTP: **GET**

Descrição no [Swagger](https://app.fluigidentity.com/rest/swagger-ui/index.html#!/companies): *“get pending user operations for an application”*
