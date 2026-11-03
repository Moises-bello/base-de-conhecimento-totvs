---
content_hash: 0dfc4c518faad8dfd7120e5a73f4f64c7b623b4590f82f0250879f72be396ef7
fetched_at: '2026-06-28T21:35:25.903268+00:00'
page_id: '321293932'
product: fluig
source: tdn-fluig
title: Identity | Existe um exemplo de JSON do método "Create Company User"?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=321293932
version: 6
---

---

Segue um exemplo do JSON, com o mínimo necessário, para ser incluído no *body* do método "Create Company User".

"password":"Senha@123",
"role":"USER", 
"companyId":"qycshwjp78ow7fun1495133511988"
} ]]>

Caso o usuário deva acessar sem e-mail, acrescentar o campo *login* em vez de *emailAddress*. Apenas um desses campos pode ser preenchido *(login* ou *emailAddress).*

Esse JSON pertence ao REST POST - /rest/v2/companies/{companyId}/users.
