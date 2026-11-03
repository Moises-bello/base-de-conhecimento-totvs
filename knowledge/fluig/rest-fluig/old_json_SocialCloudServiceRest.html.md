---
content_hash: 6be1e70929d765ae1250f47d35ebfde889628ffc9ce5450f4933135a2e611fd5
fetched_at: '2026-11-03T14:34:38.485384+00:00'
page_id: json_SocialCloudServiceRest
product: fluig
source: rest-fluig
title: Fluig REST — SocialCloudServiceRest Data Type
type: documentation
url: https://api.fluig.com/old/json_SocialCloudServiceRest.html
version: 1
---

# SocialCloudServiceRest Data Type

Cloud

Properties

| name | data type | description |
| --- | --- | --- |
| defaultAccessControlGroup | string | Return the default group |
| defaultRelationshipCloud | [Response](https://api.fluig.com/old/json_Response.html) | Get the default relationship cloud of current talent |
| Properties inherited from [GenericBean](https://api.fluig.com/old/json_GenericBean.html) | | |
| errorHandler | [ErrorHandler](https://api.fluig.com/old/json_ErrorHandler.html) |  |

Example

```
{
  "defaultAccessControlGroup" : "...",
  "defaultRelationshipCloud" : {
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
      "family" : "SERVER_ERROR"
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
