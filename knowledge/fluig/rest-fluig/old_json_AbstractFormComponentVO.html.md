---
content_hash: 51107cdac2efd7f37f0a40496200699ef9dfafd50bebd7c64e5500a2cd9024cc
fetched_at: '2026-11-03T14:34:36.035188+00:00'
page_id: json_AbstractFormComponentVO
product: fluig
source: rest-fluig
title: Fluig REST — AbstractFormComponentVO Data Type
type: documentation
url: https://api.fluig.com/old/json_AbstractFormComponentVO.html
version: 1
---

# AbstractFormComponentVO Data Type

Properties

| name | data type | description |
| --- | --- | --- |
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
  "fieldType" : "AbstractFormComponentVO",
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
