---
content_hash: d2ae3f82d2257806d0c644d4d0aba803a66d702ae8588817f05eb05c0243e3c2
fetched_at: '2026-11-03T14:34:38.095983+00:00'
page_id: json_ProcessStateVO
product: fluig
source: rest-fluig
title: Fluig REST — ProcessStateVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ProcessStateVO.html
version: 1
---

# ProcessStateVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| tenantId | number | required |  |
| sequence | number | required |  |
| stateName | string |  |  |
| stateDescription | string |  |  |

Example

```
{
  "tenantId" : 12345,
  "sequence" : 12345,
  "stateName" : "...",
  "stateDescription" : "..."
}
```
