---
content_hash: 804b2dc51b6a131cf983fcb0899a9b237732c32f2e0954ac94a13fa81b807e82
fetched_at: '2026-11-03T14:34:38.746573+00:00'
page_id: json_UserRest
product: fluig
source: rest-fluig
title: Fluig REST — UserRest Data Type
type: documentation
url: https://api.fluig.com/old/json_UserRest.html
version: 1
---

# UserRest Data Type

User - V2

Available Since
:   1.5

Properties

| name | data type | description |
| --- | --- | --- |
| current | [Response](https://api.fluig.com/old/json_Response.html) | Get current user |

Example

```
{
  "current" : {
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
}
```
