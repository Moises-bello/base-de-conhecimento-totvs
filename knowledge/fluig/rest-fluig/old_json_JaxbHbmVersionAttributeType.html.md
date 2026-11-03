---
content_hash: c0ca397ca4c731ec1449571dbeb0d141f7bf41ff60991ec2338f38848f3c5640
fetched_at: '2026-11-03T14:34:37.721932+00:00'
page_id: json_JaxbHbmVersionAttributeType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmVersionAttributeType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmVersionAttributeType.html
version: 1
---

# JaxbHbmVersionAttributeType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| insert | boolean |  |
| unsavedValue | [JaxbHbmUnsavedValueVersionEnum](https://api.fluig.com/old/json_JaxbHbmUnsavedValueVersionEnum.html) |  |
| column | array of [JaxbHbmColumnType](https://api.fluig.com/old/json_JaxbHbmColumnType.html) |  |
| type | string |  |
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
  "insert" : true,
  "unsavedValue" : "UNDEFINED",
  "column" : [ {
    "length" : 12345,
    "unique" : true,
    "scale" : 12345,
    "comment" : "...",
    "precision" : 12345,
    "sqlType" : "...",
    "read" : "...",
    "write" : "...",
    "index" : "...",
    "name" : "...",
    "notNull" : true,
    "check" : "...",
    "uniqueKey" : "...",
    "default" : "..."
  }, {
    "length" : 12345,
    "unique" : true,
    "scale" : 12345,
    "comment" : "...",
    "precision" : 12345,
    "sqlType" : "...",
    "read" : "...",
    "write" : "...",
    "index" : "...",
    "name" : "...",
    "notNull" : true,
    "check" : "...",
    "uniqueKey" : "...",
    "default" : "..."
  } ],
  "type" : "...",
  "columnAttribute" : "...",
  "name" : "...",
  "generated" : "NEVER",
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
