---
content_hash: c39c66228c610031dea0166cee961b309bdad60c417b9d27b15842b9c97545ca
fetched_at: '2026-11-03T14:34:37.906121+00:00'
page_id: json_OAuthVO
product: fluig
source: rest-fluig
title: Fluig REST — OAuthVO Data Type
type: documentation
url: https://api.fluig.com/old/json_OAuthVO.html
version: 1
---

# OAuthVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| token | string |  |  |
| params | map of object |  |  |
| refreshTokenURL | string |  |  |
| useSSL | boolean | required |  |
| consumerSecret | string |  |  |
| mediaType | string |  |  |
| grantType | string |  |  |
| authenticationType | string |  |  |
| providerName | string |  |  |
| password | string |  |  |
| serviceTestUrl | string |  |  |
| consumerKey | string |  |  |
| passwordConfirmation | string |  |  |
| expirationDate | number |  |  |
| requestTokenURL | string |  |  |
| clientId | string |  |  |
| strParams | string |  |  |
| requestMethod | string |  |  |
| tenantId | number |  |  |
| description | string |  |  |
| method | string |  |  |
| clientData | string |  |  |
| userAuthorizationURL | string |  |  |
| clientSecret | string |  |  |
| code | string |  |  |
| accessTokenURL | string |  |  |
| redirectUri | string |  |  |
| creationDate | number |  |  |
| custom | string |  |  |
| tokenAccess | string |  |  |
| authorizationURL | string |  |  |
| headers | map of string |  |  |
| tokenSecret | string |  |  |
| scope | string |  |  |
| callbackUrl | string |  |  |
| id | number |  |  |
| serviceUrl | string |  |  |
| logMessages | boolean | required |  |
| domain | string |  |  |
| signatureMethod | string |  |  |
| username | string |  |  |
| timeoutService | number |  |  |
| encoding | string |  |  |
| refreshToken | string |  |  |

Example

```
{
  "token" : "...",
  "params" : {
    "property1" : { },
    "property2" : { }
  },
  "refreshTokenURL" : "...",
  "useSSL" : true,
  "consumerSecret" : "...",
  "mediaType" : "...",
  "grantType" : "...",
  "authenticationType" : "...",
  "providerName" : "...",
  "password" : "...",
  "serviceTestUrl" : "...",
  "consumerKey" : "...",
  "passwordConfirmation" : "...",
  "expirationDate" : 12345,
  "requestTokenURL" : "...",
  "clientId" : "...",
  "strParams" : "...",
  "requestMethod" : "...",
  "tenantId" : 12345,
  "description" : "...",
  "method" : "...",
  "clientData" : "...",
  "userAuthorizationURL" : "...",
  "clientSecret" : "...",
  "code" : "...",
  "accessTokenURL" : "...",
  "redirectUri" : "...",
  "creationDate" : 12345,
  "custom" : "...",
  "tokenAccess" : "...",
  "authorizationURL" : "...",
  "headers" : {
    "property1" : "...",
    "property2" : "..."
  },
  "tokenSecret" : "...",
  "scope" : "...",
  "callbackUrl" : "...",
  "id" : 12345,
  "serviceUrl" : "...",
  "logMessages" : true,
  "domain" : "...",
  "signatureMethod" : "...",
  "username" : "...",
  "timeoutService" : 12345,
  "encoding" : "...",
  "refreshToken" : "..."
}
```
