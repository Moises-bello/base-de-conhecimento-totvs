---
content_hash: dda3c97484b3471cff482442e762d454ef7fc07252a3a3da8b901d874bb4db4b
fetched_at: '2026-11-03T14:34:38.606438+00:00'
page_id: json_StatusType
product: fluig
source: rest-fluig
title: Fluig REST — StatusType Data Type
type: documentation
url: https://api.fluig.com/old/json_StatusType.html
version: 1
---

# StatusType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| reasonPhrase | string |  |  |
| statusCode | number | required |  |
| family | [Family](https://api.fluig.com/old/json_Family.html) |  |  |

Example

```
{
  "reasonPhrase" : "...",
  "statusCode" : 12345,
  "family" : "SUCCESSFUL"
}
```
