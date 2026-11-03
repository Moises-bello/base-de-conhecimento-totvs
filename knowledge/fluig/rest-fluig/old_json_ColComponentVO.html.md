---
content_hash: 0e93e410ad86cef6cae71b44a70787b64767f3d7e17f47404005d3123f6b9f15
fetched_at: '2026-11-03T14:34:36.429511+00:00'
page_id: json_ColComponentVO
product: fluig
source: rest-fluig
title: Fluig REST — ColComponentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ColComponentVO.html
version: 1
---

# ColComponentVO Data Type

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
  "fieldType" : "COL",
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
