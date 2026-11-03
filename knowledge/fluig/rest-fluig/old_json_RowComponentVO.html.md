---
content_hash: 43f5a264bdb4c4d5065874944b81603674331d72d4b4ddeb06e8c8c999ebc4a0
fetched_at: '2026-11-03T14:34:38.295509+00:00'
page_id: json_RowComponentVO
product: fluig
source: rest-fluig
title: Fluig REST — RowComponentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_RowComponentVO.html
version: 1
---

# RowComponentVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| Properties inherited from [AbstractFormComponentVO](https://api.fluig.com/old/json_AbstractFormComponentVO.html) | | |
| minsize | string |  |
| configurations | [ConfigurationVO](https://api.fluig.com/old/json_ConfigurationVO.html) |  |
| type | string |  |
| helpmessage | string |  |
| fieldid | string |  |
| label | string |  |
| configuratorId | string |  |
| size | string |  |
| children | array of [AbstractFormComponentVO](https://api.fluig.com/old/json_AbstractFormComponentVO.html) |  |
| sensitivedata | [SensitiveDataVO](https://api.fluig.com/old/json_SensitiveDataVO.html) |  |
| fieldType | string |  |
| placeholder | string |  |
| value | object |  |

Example

```
{
  "fieldType" : "ROW",
  "minsize" : "...",
  "configurations" : {
    "analyticsText" : [ {
      "index" : 12345,
      "fieldId" : "..."
    }, {
      "index" : 12345,
      "fieldId" : "..."
    } ],
    "analyticsNumber" : [ {
      "index" : 12345,
      "fieldId" : "..."
    }, {
      "index" : 12345,
      "fieldId" : "..."
    } ],
    "fieldDescription" : "...",
    "datasetName" : "..."
  },
  "type" : "...",
  "helpmessage" : "...",
  "fieldid" : "...",
  "label" : "...",
  "configuratorId" : "...",
  "size" : "...",
  "children" : [ {
    "fieldType" : "AbstractFormComponentVO",
    "minsize" : "...",
    "configurations" : {
      "analyticsText" : [ { }, { } ],
      "analyticsNumber" : [ { }, { } ],
      "fieldDescription" : "...",
      "datasetName" : "..."
    },
    "type" : "...",
    "helpmessage" : "...",
    "fieldid" : "...",
    "label" : "...",
    "configuratorId" : "...",
    "size" : "...",
    "children" : [ { }, { } ],
    "sensitivedata" : {
      "canAnonymizeData" : true,
      "sensitiveDataType" : "...",
      "sensitiveData" : true,
      "reasons" : [ { }, { } ]
    },
    "placeholder" : "...",
    "value" : { },
    "extension1" : "...",
    "extension2" : "..."
  }, {
    "fieldType" : "AbstractFormComponentVO",
    "minsize" : "...",
    "configurations" : {
      "analyticsText" : [ { }, { } ],
      "analyticsNumber" : [ { }, { } ],
      "fieldDescription" : "...",
      "datasetName" : "..."
    },
    "type" : "...",
    "helpmessage" : "...",
    "fieldid" : "...",
    "label" : "...",
    "configuratorId" : "...",
    "size" : "...",
    "children" : [ { }, { } ],
    "sensitivedata" : {
      "canAnonymizeData" : true,
      "sensitiveDataType" : "...",
      "sensitiveData" : true,
      "reasons" : [ { }, { } ]
    },
    "placeholder" : "...",
    "value" : { },
    "extension1" : "...",
    "extension2" : "..."
  } ],
  "sensitivedata" : {
    "canAnonymizeData" : true,
    "sensitiveDataType" : "...",
    "sensitiveData" : true,
    "reasons" : [ {
      "sensitiveDataClassification" : "...",
      "sensitiveDataClassificationJustify" : "..."
    }, {
      "sensitiveDataClassification" : "...",
      "sensitiveDataClassificationJustify" : "..."
    } ]
  },
  "placeholder" : "...",
  "value" : { },
  "extension1" : "...",
  "extension2" : "..."
}
```
