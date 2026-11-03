---
content_hash: 55ecdb508f0a252c6f2c2fe4865a89766e7d5b96b5c77d58292ad06c9e994751
fetched_at: '2026-11-03T14:34:38.092468+00:00'
page_id: json_ProcessStateDto
product: fluig
source: rest-fluig
title: Fluig REST — ProcessStateDto Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessStateDto.html
version: 1
---

# ProcessStateDto Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| stateDescription | string |  |  |
| sequence | number | required |  |
| companyId | number | required |  |
| stateName | string |  |  |
| counterSign | boolean |  |  |

Example

```
{
  "stateDescription" : "...",
  "sequence" : 12345,
  "companyId" : 12345,
  "stateName" : "...",
  "counterSign" : true
}
```
