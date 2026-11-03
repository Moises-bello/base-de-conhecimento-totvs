---
content_hash: 7217c97a7836b9cdd008444ea0eb89c7811caf5f6fc9e2f8c4d6d89feeb4d0a5
fetched_at: '2026-11-03T14:34:37.249821+00:00'
page_id: json_JaxbCfgSessionFactory
product: fluig
source: rest-fluig
title: Fluig REST — JaxbCfgSessionFactory Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbCfgSessionFactory.html
version: 1
---

# JaxbCfgSessionFactory Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| listener | array of [JaxbCfgEventListenerType](https://api.fluig.com/old/json_JaxbCfgEventListenerType.html) |  |
| mapping | array of [JaxbCfgMappingReferenceType](https://api.fluig.com/old/json_JaxbCfgMappingReferenceType.html) |  |
| classCacheOrCollectionCache | array of object |  |
| event | array of [JaxbCfgEventListenerGroupType](https://api.fluig.com/old/json_JaxbCfgEventListenerGroupType.html) |  |
| property | array of [JaxbCfgConfigPropertyType](https://api.fluig.com/old/json_JaxbCfgConfigPropertyType.html) |  |
| name | string |  |

Example

```
{
  "listener" : [ {
    "type" : "CREATE",
    "clazz" : "..."
  }, {
    "type" : "DIRTY_CHECK",
    "clazz" : "..."
  } ],
  "mapping" : [ {
    "jar" : "...",
    "package" : "...",
    "file" : "...",
    "resource" : "...",
    "clazz" : "..."
  }, {
    "jar" : "...",
    "package" : "...",
    "file" : "...",
    "resource" : "...",
    "clazz" : "..."
  } ],
  "classCacheOrCollectionCache" : [ { }, { } ],
  "event" : [ {
    "type" : "POST_DELETE",
    "listener" : [ {
      "type" : "PRE_COLLECTION_RECREATE",
      "clazz" : "..."
    }, {
      "type" : "POST_COLLECTION_REMOVE",
      "clazz" : "..."
    } ]
  }, {
    "type" : "LOCK",
    "listener" : [ {
      "type" : "POST_COLLECTION_UPDATE",
      "clazz" : "..."
    }, {
      "type" : "SAVE_UPDATE",
      "clazz" : "..."
    } ]
  } ],
  "property" : [ {
    "value" : "...",
    "name" : "..."
  }, {
    "value" : "...",
    "name" : "..."
  } ],
  "name" : "..."
}
```
