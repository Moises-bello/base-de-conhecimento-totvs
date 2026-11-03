---
content_hash: e26bf92cf831a3ca6acc6a44d339d4f6943a602146f5ce8937ad03e91f0625fe
fetched_at: '2026-11-03T14:34:36.096421+00:00'
page_id: json_AlertEventVO_alert
product: fluig
source: rest-fluig
title: Fluig REST — AlertEventVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AlertEventVO_alert.html
version: 1
---

# AlertEventVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| canRemove | boolean |  |
| groupDescription | string |  |
| eventKey | string |  |
| icon | string |  |
| groupDescriptionKey | string |  |
| id | number |  |
| onlyAdmin | boolean |  |
| description | string |  |
| descriptionKey | string |  |
| singleDescriptionKey | string |  |
| active | boolean |  |
| grouped | boolean |  |
| module | [AlertModuleVO](https://api.fluig.com/old/json_AlertModuleVO_alert.html) |  |
| singleDescription | string |  |
| required | boolean |  |

Example

```
{
  "canRemove" : true,
  "groupDescription" : "...",
  "eventKey" : "...",
  "icon" : "...",
  "groupDescriptionKey" : "...",
  "id" : 12345,
  "onlyAdmin" : true,
  "description" : "...",
  "descriptionKey" : "...",
  "singleDescriptionKey" : "...",
  "active" : true,
  "grouped" : true,
  "module" : {
    "description" : "...",
    "id" : 12345,
    "moduleKey" : "...",
    "tenantId" : 12345
  },
  "singleDescription" : "...",
  "required" : true
}
```
