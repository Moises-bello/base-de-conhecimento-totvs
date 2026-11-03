---
content_hash: 9480fb2ab0a4bd0b73a3f73ae78a6401a5ba85ff430643725702d214ffc3d5ca
fetched_at: '2026-11-03T14:34:37.676334+00:00'
page_id: json_JaxbHbmTimestampAttributeType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmTimestampAttributeType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmTimestampAttributeType.html
version: 1
---

# JaxbHbmTimestampAttributeType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| source | [JaxbHbmTimestampSourceEnum](https://api.fluig.com/old/json_JaxbHbmTimestampSourceEnum.html) |  |
| unsavedValue | [JaxbHbmUnsavedValueTimestampEnum](https://api.fluig.com/old/json_JaxbHbmUnsavedValueTimestampEnum.html) |  |
| Properties inherited from [JaxbHbmBaseVersionAttributeType](https://api.fluig.com/old/json_JaxbHbmBaseVersionAttributeType.html) | | |
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
  "source" : "DB",
  "unsavedValue" : "UNDEFINED",
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
