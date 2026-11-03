---
content_hash: 714f9cad1c5003c71afc24625b164a26a675b6fff0d4da0a05da9a6f81c6988b
fetched_at: '2026-06-28T21:35:26.165566+00:00'
page_id: '346490172'
product: fluig
source: tdn-fluig
title: Identity | Existem APIs para consultar o CN dos usuários importados do Active
  Directory?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=346490172
version: 7
---

---

Existem duas APIs disponíveis para consulta de CN dos usuários aceitos: uma individual e outra para todos os usuários aceitos.

**Obter usuário AD pelo e-mail**

|  |  |
| --- | --- |
| Serviço | Companies |
| Descrição | Get an AD user by email |
| Operação | **GET** |
| Endpoint | [/rest/v2/companies/{companyId}/active-directories/{adId}/users/email/{email}](https://app.fluigidentity.com/rest/swagger-ui/index.html#!/companies/getADUserByEmail_get_62) |
| Parâmetros | companyId  adId  email |

**companyId:** o ID da Empresa está disponível na aba  do menu de Configuração do Identity.

**adId:** token de configuração do Active Directory gerado pelo Identity. Disponível na página .

**email:** endereço de e-mail do usuário aceito.

**Obter todos os usuários AD aceitos**

|  |  |
| --- | --- |
| Serviço | Companies |
| Descrição | Get all accepted AD Users |
| Operação | **GET** |
| Endpoint | [/rest/v2/companies/{companyId}/active-directories/{adId}/accepted-users](https://app.fluigidentity.com/rest/swagger-ui/index.html#!/companies/getAcceptedUsers_get_69) |
| Parâmetros | companyId  adId |
