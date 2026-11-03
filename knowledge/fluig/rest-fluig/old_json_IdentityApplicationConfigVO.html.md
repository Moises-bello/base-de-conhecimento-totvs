---
content_hash: c412daab5aa27a3244b92e5d2a2f0d1ec9fd0f2631b2ccf8ccad91f72f46436f
fetched_at: '2026-11-03T14:34:37.139550+00:00'
page_id: json_IdentityApplicationConfigVO
product: fluig
source: rest-fluig
title: Fluig REST — IdentityApplicationConfigVO Data Type
type: documentation
url: https://api.fluig.com/old/json_IdentityApplicationConfigVO.html
version: 1
---

# IdentityApplicationConfigVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| application | [ApplicationDTO](https://api.fluig.com/old/json_ApplicationDTO.html) |  |
| SAMLCertificate | [Certificate](https://api.fluig.com/old/json_Certificate.html) |  |
| v2PrivateKey | [PrivateKey](https://api.fluig.com/old/json_PrivateKey.html) |  |
| applicationMetadata | string |  |
| company | [CompanyDTO](https://api.fluig.com/old/json_CompanyDTO.html) |  |
| Properties inherited from [VO](https://api.fluig.com/old/json_VO.html) | | |
| displayName | string |  |
| success | boolean |  |
| externalId | string |  |
| id | string |  |
| selected | boolean |  |
| customfilter | string |  |

Example

```
{
  "application" : { },
  "SAMLCertificate" : {
    "encoded" : "...",
    "publicKey" : { },
    "type" : "..."
  },
  "v2PrivateKey" : { },
  "applicationMetadata" : "...",
  "company" : { },
  "displayName" : "...",
  "success" : true,
  "externalId" : "...",
  "id" : "...",
  "selected" : true,
  "customfilter" : "..."
}
```
