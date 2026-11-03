---
content_hash: cd3d5223e248500e9980c7ea138bf4a084392441f11dcff82adce082fc6c90d1
fetched_at: '2026-11-03T14:34:36.371893+00:00'
page_id: json_CardIndexRest
product: fluig
source: rest-fluig
title: Fluig REST — CardIndexRest Data Type
type: documentation
url: https://api.fluig.com/old/json_CardIndexRest.html
version: 1
---

# CardIndexRest Data Type

Card Index

Available Since
:   1.5

Properties

| name | data type | description |
| --- | --- | --- |
| defaultFormFolderId | [Response](https://api.fluig.com/old/json_Response.html) | Retrieve Default form folder id |

Example

```
{
  "defaultFormFolderId" : {
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
      "family" : "REDIRECTION"
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
