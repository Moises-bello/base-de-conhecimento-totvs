---
content_hash: bfe8fde14a2e686983e93492fb7be412d3a771d132bed9744cffb5e2b81591ee
fetched_at: '2026-11-03T14:34:37.513169+00:00'
page_id: json_JaxbHbmMapKeyBasicType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmMapKeyBasicType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmMapKeyBasicType.html
version: 1
---

# JaxbHbmMapKeyBasicType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| typeAttribute | string |  |
| node | string |  |
| columnOrFormula | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |
| type | [JaxbHbmTypeSpecificationType](https://api.fluig.com/old/json_JaxbHbmTypeSpecificationType.html) |  |
| columnAttribute | string |  |
| formulaAttribute | string |  |
| length | number |  |

Example

```
{
  "typeAttribute" : "...",
  "node" : "...",
  "columnOrFormula" : [ { }, { } ],
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
  "columnAttribute" : "...",
  "formulaAttribute" : "...",
  "length" : 12345
}
```
