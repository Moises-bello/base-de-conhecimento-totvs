---
content_hash: 87cadce8be8ec6dfb011fb82f1a915a7d4c4d31586ff435b708e40d3a1d1f99f
fetched_at: '2026-11-03T14:34:38.034727+00:00'
page_id: json_ProcessDefinitionVersionAlertVO_vo
product: fluig
source: rest-fluig
title: Fluig REST — ProcessDefinitionVersionAlertVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessDefinitionVersionAlertVO_vo.html
version: 1
---

# ProcessDefinitionVersionAlertVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| local | number | required |  |
| id | number | required |  |
| type | number | required |  |
| description | string |  |  |
| details | map of object |  |  |

Example

```
{
  "local" : 12345,
  "id" : 12345,
  "type" : 12345,
  "description" : "...",
  "details" : {
    "property1" : { },
    "property2" : { }
  }
}
```
