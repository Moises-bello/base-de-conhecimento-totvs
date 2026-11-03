---
content_hash: 3c8de28e7815547ffb5aea8d47ce56f9b5d59204993c971827b1d851b1eef86d
fetched_at: '2026-11-03T14:34:37.306721+00:00'
page_id: json_JaxbHbmBasicCollectionElementType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbHbmBasicCollectionElementType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbHbmBasicCollectionElementType.html
version: 1
---

# JaxbHbmBasicCollectionElementType Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| columnAttribute | string |  |  |
| notNull | boolean | required |  |
| typeAttribute | string |  |  |
| length | number |  |  |
| node | string |  |  |
| formulaAttribute | string |  |  |
| scale | number |  |  |
| columnOrFormula | array of [Serializable](https://api.fluig.com/old/json_Serializable.html) |  |  |
| precision | number |  |  |
| unique | boolean | required |  |
| type | [JaxbHbmTypeSpecificationType](https://api.fluig.com/old/json_JaxbHbmTypeSpecificationType.html) |  |  |

Example

```
{
  "columnAttribute" : "...",
  "notNull" : true,
  "typeAttribute" : "...",
  "length" : 12345,
  "node" : "...",
  "formulaAttribute" : "...",
  "scale" : 12345,
  "columnOrFormula" : [ { }, { } ],
  "precision" : 12345,
  "unique" : true,
  "type" : {
    "name" : "...",
    "configParameters" : [ {
      "value" : "...",
      "name" : "..."
    }, {
      "value" : "...",
      "name" : "..."
    } ]
  }
}
```
