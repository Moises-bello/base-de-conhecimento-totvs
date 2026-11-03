---
content_hash: 97cbc59915e34c7d2f91e8bcd728813f8c82e8ec1e7c4ecf041521fb0c6cf12f
fetched_at: '2026-11-03T14:34:36.456851+00:00'
page_id: json_ComboComponentVO
product: fluig
source: rest-fluig
title: Fluig REST — ComboComponentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_ComboComponentVO.html
version: 1
---

# ComboComponentVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| datasetkey | string |  |
| datasetorder | string |  |
| datasetid | string |  |
| datasetvalue | string |  |
| options | array of [OptionValueVO](https://api.fluig.com/old/json_OptionValueVO.html) |  |
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
  "datasetkey" : "...",
  "datasetorder" : "...",
  "datasetid" : "...",
  "datasetvalue" : "...",
  "options" : [ {
    "value" : "...",
    "label" : "..."
  }, {
    "value" : "...",
    "label" : "..."
  } ],
  "fieldType" : "COMBO",
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
