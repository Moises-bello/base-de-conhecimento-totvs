---
content_hash: 3da9709c89076dcfe5a5c90e5798c16587e4f3cf438f65bb163e5a42bdedf3a2
fetched_at: '2026-11-03T14:34:38.264713+00:00'
page_id: json_Response
product: fluig
source: rest-fluig
title: Fluig REST — Response Data Type
type: documentation
url: https://api.fluig.com/old/json_Response.html
version: 1
---

# Response Data Type

Properties

| name | data type | constraints | description |
| --- | --- | --- | --- |
| mediaType | [MediaType](https://api.fluig.com/old/json_MediaType_core.html) |  |  |
| status | number | required |  |
| metadata | map of array of object |  |  |
| lastModified | number |  |  |
| links | array of [Link](https://api.fluig.com/old/json_Link.html) |  |  |
| date | number |  |  |
| statusInfo | [StatusType](https://api.fluig.com/old/json_StatusType.html) |  |  |
| entityTag | [EntityTag](https://api.fluig.com/old/json_EntityTag.html) |  |  |
| entity | object |  |  |
| stringHeaders | map of array of string |  |  |
| headers | map of array of object |  |  |
| cookies | map of [NewCookie](https://api.fluig.com/old/json_NewCookie.html) |  |  |
| location | string |  |  |
| allowedMethods | array of string |  |  |
| length | number | required |  |
| language | string |  |  |

Example

```
{
  "mediaType" : {
    "subtype" : "...",
    "type" : "...",
    "parameters" : {
      "property1" : "...",
      "property2" : "..."
    },
    "wildcardType" : true,
    "wildcardSubtype" : true
  },
  "status" : 12345,
  "metadata" : {
    "property1" : [ { }, { } ],
    "property2" : [ { }, { } ]
  },
  "lastModified" : 12345,
  "links" : [ {
    "uri" : "...",
    "uriBuilder" : { },
    "rels" : [ "...", "..." ],
    "type" : "...",
    "rel" : "...",
    "title" : "...",
    "params" : {
      "property1" : "...",
      "property2" : "..."
    }
  }, {
    "uri" : "...",
    "uriBuilder" : { },
    "rels" : [ "...", "..." ],
    "type" : "...",
    "rel" : "...",
    "title" : "...",
    "params" : {
      "property1" : "...",
      "property2" : "..."
    }
  } ],
  "date" : 12345,
  "statusInfo" : {
    "reasonPhrase" : "...",
    "statusCode" : 12345,
    "family" : "CLIENT_ERROR"
  },
  "entityTag" : {
    "weak" : true,
    "value" : "..."
  },
  "entity" : { },
  "stringHeaders" : {
    "property1" : [ "...", "..." ],
    "property2" : [ "...", "..." ]
  },
  "headers" : {
    "property1" : [ { }, { } ],
    "property2" : [ { }, { } ]
  },
  "cookies" : {
    "property1" : {
      "secure" : true,
      "comment" : "...",
      "maxAge" : 12345,
      "httpOnly" : true,
      "expiry" : 12345,
      "name" : "...",
      "domain" : "...",
      "version" : 12345,
      "path" : "...",
      "value" : "..."
    },
    "property2" : {
      "secure" : true,
      "comment" : "...",
      "maxAge" : 12345,
      "httpOnly" : true,
      "expiry" : 12345,
      "name" : "...",
      "domain" : "...",
      "version" : 12345,
      "path" : "...",
      "value" : "..."
    }
  },
  "location" : "...",
  "allowedMethods" : [ "...", "..." ],
  "length" : 12345,
  "language" : "..."
}
```
