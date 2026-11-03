---
content_hash: ee869fd662d40640b2c168d9e58746ce9538b8eb41acac5519a3edd4fb3e73d8
fetched_at: '2026-11-03T14:34:39.762508+00:00'
page_id: resource_DocumentationProxyRest
product: fluig
source: rest-fluig
title: Fluig REST — DocumentationProxyRest Resource
type: documentation
url: https://api.fluig.com/old/resource_DocumentationProxyRest.html
version: 1
---

*Paths relativos à base da API pública do Fluig (normalmente `https://[servidor]/api/public`). Autenticação OAuth — ver TDN "Fluig API".*

# DocumentationProxyRest Resource

DocumentationProxyRest

Available Since
:   1.6

### GET /2.0/documentationproxy/search

Executa uma operação 'get' em um serviço externo com a intenção de evitar erros de cross-domain.
Funciona apenas para o domínio tdn.totvs.com.

Request Parameters

| name | type | description |
| --- | --- | --- |
| url | query | utilize enconding ao passar a string para o serviço (Exemplo em javascript: encodeURIComponent(url)) |

Response Body

| media type | data type | description |
| --- | --- | --- |
| application/json | object (JSON) | json com o resultado do serviço |
