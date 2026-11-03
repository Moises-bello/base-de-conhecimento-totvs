---
content_hash: 37a19d47228fb0d2e78a45073ffd679d49f8de4cd9091de42d36879c5ea44fff
fetched_at: '2026-11-03T14:34:37.240954+00:00'
page_id: json_JaxbCfgHibernateConfiguration
product: fluig
source: rest-fluig
title: Fluig REST — JaxbCfgHibernateConfiguration Data Type
type: documentation
url: https://api.fluig.com/old/json_JaxbCfgHibernateConfiguration.html
version: 1
---

# JaxbCfgHibernateConfiguration Data Type

Properties

| name | data type | description |
| --- | --- | --- |
| security | [JaxbCfgSecurity](https://api.fluig.com/old/json_JaxbCfgSecurity.html) |  |
| sessionFactory | [JaxbCfgSessionFactory](https://api.fluig.com/old/json_JaxbCfgSessionFactory.html) |  |

Example

```
{
  "security" : {
    "context" : "...",
    "grant" : [ {
      "entityName" : "...",
      "actions" : "...",
      "role" : "..."
    }, {
      "entityName" : "...",
      "actions" : "...",
      "role" : "..."
    } ]
  },
  "sessionFactory" : {
    "listener" : [ {
      "type" : "POST_DELETE",
      "clazz" : "..."
    }, {
      "type" : "POST_COLLECTION_REMOVE",
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
      "type" : "LOCK",
      "listener" : [ { }, { } ]
    }, {
      "type" : "LOAD_COLLECTION",
      "listener" : [ { }, { } ]
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
}
```
