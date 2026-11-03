---
content_hash: fc484b823f976c8a7d2eb97a4c225c90d248a5e10edce374ae2076585c5eda7b
fetched_at: '2026-06-28T21:35:22.857923+00:00'
page_id: '240309191'
product: fluig
source: tdn-fluig
title: Identity | Exceções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240309191
version: 27
---

# Índice

trueÍndicenone

# HTTP Status

---

Referência: <https://httpstatuses.com/>

## Códigos de Sucesso

| Código | Descrição | Resultado | Quando ocorre |
| --- | --- | --- | --- |
| 200 | OK | Operação executada com sucesso. | Quando a operação foi realizada com sucesso, e há um retorno no corpo da resposta. |
| 201 | CREATED | Operação de criação de recursos realizada com sucesso. | Utilizado para indicar que uma criação de recursos foi feita com sucesso.  Em seu retorno, deve incluir os dados que foram criados, bem como um *link* de acesso ao recurso recém criado. |
| 202 | ACCEPTED | Utilizado para indicar que uma requisição foi aceita pelo servidor e será processada eventualmente. | Em operações em lote, ou operações cujo processamento será feito de forma assíncrona.  Essa resposta deve conter em seu retorno um *link* para que seja possível consultar o andamento/resultado da execução. |
| 204 | NO CONTENT | Operação executada com sucesso. | Quando a operação foi realizada com sucesso, mas não existem dados de retorno. |

## Códigos de Erros do Cliente

| Código | Descrição | Resultado | Quando ocorre |
| --- | --- | --- | --- |
| 400 | BAD REQUEST | Indica um erro de sintaxe na requisição. | Quando a requisição não foi montada corretamente.  Pode ocorrer devido à parâmetros informados incorretamente. |
| 401 | UNAUTHORIZED | A requisição não foi executada por falta de autorização. | Pode ser causada por :   * Falta de credenciais de autenticação * Credenciais inválidas * Credenciais válidas, porém sem acesso ao recurso solicitado |

## Códigos de Erros do Servidor

| Código | Descrição | Resultado | Quando ocorre |
| --- | --- | --- | --- |
| 500 | INTERNAL SERVER ERROR | Erro interno do servidor. | Algum componente do sistema está falhando, favor verificar os logs da aplicação. |

# OAuth2Exception

---

# SecurityException

---

# Company Exceptions

---

# Desktop SSO Exceptions

---

# Role Exceptions

---

# User Account Exceptions

---

# User Company Account Exceptions

---
