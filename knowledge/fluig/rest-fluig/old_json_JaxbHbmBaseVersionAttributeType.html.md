---
content_hash: 4e5f91e18a817acdc6ec3c7f8175b7edcf0e2c23b1dcb2b474b8fedda2928550
fetched_at: '2026-11-03T14:34:37.295260+00:00'
page_id: json_JaxbHbmBaseVersionAttributeType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmBaseVersionAttributeType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmBaseVersionAttributeType.html
version: 1
---

# JaxbHbmBaseVersionAttributeType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| columnAttribute | string |  |
| name | string |  |
| generated | [GenerationTiming](https://api.fluig.com/old/json_GenerationTiming.html) |  |
| access | string |  |
| node | string |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |

Example

```
{
  "columnAttribute" : "...",
  "name" : "...",
  "generated" : "ALWAYS",
  "access" : "...",
  "node" : "...",
  "toolingHints" : [ {
    "name" : "...",
    "inheritable" : true,
    "value" : "..."
  }, {
    "name" : "...",
    "inheritable" : true,
    "value" : "..."
  } ]
}
```
