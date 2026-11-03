---
content_hash: 4757bfa94ce5f86e2a89861f2c27bfe0d48bbbb92417b57d576f06c9070f1383
fetched_at: '2026-11-03T14:34:36.090930+00:00'
page_id: json_AlertEventVO
product: fluig
source: rest-fluig
title: Fluig REST — AlertEventVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AlertEventVO.html
version: 1
---

# AlertEventVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| groupDescription | string |  |
| active | boolean |  |
| descriptionKey | string |  |
| id | number |  |
| singleDescriptionKey | string |  |
| description | string |  |
| required | boolean |  |
| grouped | boolean |  |
| groupDescriptionKey | string |  |
| canRemove | boolean |  |
| singleDescription | string |  |
| icon | string |  |
| module | [AlertModuleVO](https://api.fluig.com/old/json_AlertModuleVO.html) |  |
| onlyAdmin | boolean |  |
| eventKey | string |  |

Example

```
{
  "groupDescription" : "...",
  "active" : true,
  "descriptionKey" : "...",
  "id" : 12345,
  "singleDescriptionKey" : "...",
  "description" : "...",
  "required" : true,
  "grouped" : true,
  "groupDescriptionKey" : "...",
  "canRemove" : true,
  "singleDescription" : "...",
  "icon" : "...",
  "module" : {
    "id" : 12345,
    "moduleKey" : "...",
    "tenantId" : 12345,
    "description" : "..."
  },
  "onlyAdmin" : true,
  "eventKey" : "..."
}
```
