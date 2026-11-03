---
content_hash: 9f4045733e51cae31c1cdaad6492a4d60b476685d2d949273cca7380911cabfc
fetched_at: '2026-06-28T21:35:19.408886+00:00'
page_id: '203766752'
product: fluig
source: tdn-fluig
title: Identity | Modelos REST do Identity
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Modelos+REST+do+Identity
version: 14
---

# Índice

4true.\*ndicenone

# Visão Geral

---

A documentação a seguir fornece uma introdução as APIs REST V2 do Identity. As [APIs REST V2](https://app.fluigidentity.com/rest/doc/#/) seguem o padrão de autenticação servidor a servidor OAuth2.0 utilizando JWT.

# Models

---

Esta página contém uma lista de todos os *Models* utilizados pelas APIs REST Identity. Os valores mostrados para cada campo são valores padrões.

### UserAccountDTO

Informações pessoais de um usuário, independente da natureza multicontexto da conta.

xml

### UserCompanyAccountDTO

Informações de um usuário dentro do contexto da empresa.

### GroupDTO

Entidade que une usuários e aplicativos dentro de uma empresa.

### CompanyDTO

Informações sobre a empresa.

### CustomFieldDTO

Campos customizados de uma empresa.

### JwtClaimDTO

JWT Claim, necessário para OAuth 2.0.

### RefreshToken

Token retornado como resposta para OAuth.

### AccessToken

Token utilizado para chamadas REST.

### Application

Informação sobre um determinado aplicativo.

### UserApplicationLoginDTO

Detalhes de um usuário para um determinado aplicativo dentro de uma empresa.

### UserLiteDTO

Versão simplificada de UserCompanyAccountDTO para casos em que é necessário uma resposta em grandes quantidades, por exemplo, todos usuários de uma empresa.

### SearchResults

Resposta para consultas que geram listas como “GET em todos usuários de uma empresa”

]]>
