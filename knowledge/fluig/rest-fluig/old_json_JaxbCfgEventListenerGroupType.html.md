---
content_hash: 55c69047b1ff68f070df15b653b709692b54218061033b22cafd61f7b492a049
fetched_at: '2026-11-03T14:34:37.226476+00:00'
page_id: json_JaxbCfgEventListenerGroupType
product: fluig
source: rest-fluig
title: Fluig REST — JaxbCfgEventListenerGroupType Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbCfgEventListenerGroupType.html
version: 1
---

# JaxbCfgEventListenerGroupType Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| type | [JaxbCfgEventTypeEnum](https://api.fluig.com/old/json_JaxbCfgEventTypeEnum.html) |  |
| listener | array of [JaxbCfgEventListenerType](https://api.fluig.com/old/json_JaxbCfgEventListenerType.html) |  |

Example

```
{
  "type" : "LOAD",
  "listener" : [ {
    "type" : "FLUSH",
    "clazz" : "..."
  }, {
    "type" : "AUTO_FLUSH",
    "clazz" : "..."
  } ]
}
```
