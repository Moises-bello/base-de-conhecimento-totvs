---
content_hash: 1fb91862dade8837c6f4b58e45c818899c0c692c63b8f1e37278b0629307edd3
fetched_at: '2026-11-03T14:34:37.302079+00:00'
page_id: json_JaxbHbmBasicAttributeType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmBasicAttributeType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmBasicAttributeType.html
version: 1
---

# JaxbHbmBasicAttributeType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| lazy | boolean | required |  |
| unique | boolean | required |  |
| precision | string |  |  |
| update | boolean |  |  |
| columnOrFormula | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |  |
| typeAttribute | string |  |  |
| formulaAttribute | string |  |  |
| generated | [GenerationTiming](https://api.fluig.com/old/json_GenerationTiming.html) |  |  |
| scale | string |  |  |
| type | [JaxbHbmTypeSpecificationType](https://api.fluig.com/old/json_JaxbHbmTypeSpecificationType.html) |  |  |
| notNull | boolean |  |  |
| length | number |  |  |
| name | string |  |  |
| node | string |  |  |
| index | string |  |  |
| columnAttribute | string |  |  |
| insert | boolean |  |  |
| uniqueKey | string |  |  |
| access | string |  |  |
| optimisticLock | boolean | required |  |
| Properties inherited from [JaxbHbmToolingHintContainer](https://api.fluig.com/old/json_JaxbHbmToolingHintContainer.html) | | | |
| toolingHints | array of [JaxbHbmToolingHintType](https://api.fluig.com/old/json_JaxbHbmToolingHintType.html) |  |  |

Example

```
{
  "lazy" : true,
  "unique" : true,
  "precision" : "...",
  "update" : true,
  "columnOrFormula" : [ { }, { } ],
  "typeAttribute" : "...",
  "formulaAttribute" : "...",
  "generated" : "INSERT",
  "scale" : "...",
  "type" : {
    "name" : "...",
    "configParameters" : [ {
      "value" : "...",
      "name" : "..."
    }, {
      "value" : "...",
      "name" : "..."
    } ]
  },
  "notNull" : true,
  "length" : 12345,
  "name" : "...",
  "node" : "...",
  "index" : "...",
  "columnAttribute" : "...",
  "insert" : true,
  "uniqueKey" : "...",
  "access" : "...",
  "optimisticLock" : true,
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
