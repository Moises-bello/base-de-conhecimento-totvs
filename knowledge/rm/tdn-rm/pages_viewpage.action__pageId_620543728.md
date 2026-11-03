---
content_hash: 04c781810033c9d1597e0ea6c26e8a4399470bfe6da7fcbf606b2761425cac67
fetched_at: '2026-06-29T00:11:03.269221+00:00'
page_id: '620543728'
product: rm
source: tdn-rm
title: Provedores de Segurança - até versão 12.1.29
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=620543728
version: 7
---

# Índice:

---

.\*ndice:

# Objetivo:

---

        Realizar a integração e configuração no TReports com o RAC ou FLUIG

# Configurando o Provedor de Segurança - RAC:

---

        As informações de configuração devem ser cadastradas previamente no RAC e então após isso informadas no TReports conforme abaixo.

Rac

**racsettings.Production.json**

"Security": [

{  
     "ApiName": "authorization\_api",  
     "AuthorityEndpoint": "<http://localhost/totvs.rac/>",  
     "AuthorizationEndpoint": "<http://localhost/totvs.rac/>",  
     "ClientId": "oidc",  
     "ClientSecret": "\*\*\*\*\*\*\*\*",  
     "RequireHttpsMetadata": false,  
     "Scope": "authorization\_api"

}

]

**ApiName**: Identificador da API.  
**AuthorityEndpoint**: Url com o ambiente do RAC.  
**AuthorizationEndpoint**: Url com o ambiente do RAC.  
**ClientId**: Identificador do client OIDC.  
**ClientSecret**: Chave do client.  
**RequireHttpsMetadata**: Informações de metadados. Padrão false.  
**Scope**: Identificação do escopo.

Mais informações sobre o RAC

<https://tdn.totvs.com.br/pages/viewpage.action?pageId=538503350>

# Configurando o Provedor de Segurança - FLUIG:

---

        As informações de configuração devem ser cadastradas previamente no FLUIG e então após isso informadas no TReports conforme abaixo.

Rac

**racsettings.Production.json**

"Security": [

{

     "ApiName": "FluigIdentity",  
     "AuthorityEndpoint": "<https://localhost/totvs.fluig>",  
     "TokenEndpoint": "<https://localhost/token>",  
     "JwksEndpoint": "<https://localhost/jwks>",  
     "ClientId": "oidc",  
     "ClientSecret": "\*\*\*\*\*\*",  
     "RequireHttpsMetadata": false,  
     "Scope": "authorization\_api"  
}

]

**ApiName**: Identificador do Provedor de Segurança.  
**AuthorityEndpoint**: Url com o ambiente do FLUIG.  
**TokenEndpoint**: Url com Informações do token.  
**JwksEndpoint**: Url de chaves de verificação.  
**ClientId**: Identificador do client OIDC.  
**ClientSecret**: Chave do client.  
**RequireHttpsMetadata**: Informações de metadados. Padrão false.  
**Scope**: Identificação do escopo.

Mais informações sobre o FLUIG
