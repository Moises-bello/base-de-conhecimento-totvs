---
content_hash: d72a13be3df95150bc47ad6081f52725f804da8f2377d66781f8054ac6a57a81
fetched_at: '2026-11-03T14:34:39.004245+00:00'
page_id: json_WidgetPartDefaultPropertyVO
product: fluig
source: rest-fluig
title: Fluig REST — WidgetPartDefaultPropertyVO Data Type
type: documentation
url: https://api.fluig.com/old/json_WidgetPartDefaultPropertyVO.html
version: 1
---

# WidgetPartDefaultPropertyVO Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| pdfrenderengine | string |  |  |
| updateISOProperties | boolean | required |  |
| versionOption | number | required |  |
| mapNrDocument | map of object |  |  |
| customFields | boolean | required |  |
| listCustomFieldsVO | array of [WidgetPartDefaultPropertyCustomFieldsVO](https://api.fluig.com/old/json_WidgetPartDefaultPropertyCustomFieldsVO.html) |  |  |
| imutable | boolean | required |  |
| notifyUser | boolean | required |  |
| type | string |  |  |
| listPublisherTopicVO | array of [WidgetPartDefaultPropertyTopicVO](https://api.fluig.com/old/json_WidgetPartDefaultPropertyTopicVO.html) |  |  |
| listInheritCustomFieldsVO | array of [WidgetPartDefaultPropertyCustomFieldsVO](https://api.fluig.com/old/json_WidgetPartDefaultPropertyCustomFieldsVO.html) |  |  |
| internalVisualizer | boolean | required |  |
| downloadble | boolean | required |  |
| subject | number | required |  |
| listPublisherDocumentTypeVO | array of [WidgetPartDefaultPropertyDocumentTypeVO](https://api.fluig.com/old/json_WidgetPartDefaultPropertyDocumentTypeVO.html) |  |  |

Example

```
{
  "pdfrenderengine" : "...",
  "updateISOProperties" : true,
  "versionOption" : 12345,
  "mapNrDocument" : {
    "property1" : { },
    "property2" : { }
  },
  "customFields" : true,
  "listCustomFieldsVO" : [ {
    "customFieldDescription" : "...",
    "alwaysShow" : true,
    "valueId" : "...",
    "customFieldId" : "..."
  }, {
    "customFieldDescription" : "...",
    "alwaysShow" : true,
    "valueId" : "...",
    "customFieldId" : "..."
  } ],
  "imutable" : true,
  "notifyUser" : true,
  "type" : "...",
  "listPublisherTopicVO" : [ {
    "topicId" : 12345,
    "mandatory" : true,
    "description" : "..."
  }, {
    "topicId" : 12345,
    "mandatory" : true,
    "description" : "..."
  } ],
  "listInheritCustomFieldsVO" : [ {
    "customFieldDescription" : "...",
    "alwaysShow" : true,
    "valueId" : "...",
    "customFieldId" : "..."
  }, {
    "customFieldDescription" : "...",
    "alwaysShow" : true,
    "valueId" : "...",
    "customFieldId" : "..."
  } ],
  "internalVisualizer" : true,
  "downloadble" : true,
  "subject" : 12345,
  "listPublisherDocumentTypeVO" : [ {
    "description" : "...",
    "companyId" : 12345,
    "typeId" : "..."
  }, {
    "description" : "...",
    "companyId" : 12345,
    "typeId" : "..."
  } ]
}
```
