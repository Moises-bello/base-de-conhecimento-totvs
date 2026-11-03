---
content_hash: 1a70af1b9637015d74ab8bcaef76b37191dfb15eb3fcbaadd63bfe9de76f64be
fetched_at: '2026-11-03T14:34:38.031504+00:00'
page_id: json_ProcessDefinitionVersionAlertVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessDefinitionVersionAlertVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessDefinitionVersionAlertVO.html
version: 1
---

# ProcessDefinitionVersionAlertVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| processVersion | number | required |  |
| id | number |  |  |
| alertType | number | required |  |
| details | string |  |  |
| scriptVersion | number | required |  |
| alertLocal | number | required |  |
| processId | string |  |  |

Example

```
{
  "processVersion" : 12345,
  "id" : 12345,
  "alertType" : 12345,
  "details" : "...",
  "scriptVersion" : 12345,
  "alertLocal" : 12345,
  "processId" : "..."
}
```
