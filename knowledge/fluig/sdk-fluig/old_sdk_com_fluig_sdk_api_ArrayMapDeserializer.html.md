---
content_hash: 40c45dc33236b5649d83a19edaabf52d85ad9ada35eccd8eb1fd22d5c9b10910
fetched_at: '2026-11-03T14:35:03.417027+00:00'
page_id: com/fluig/sdk/api/ArrayMapDeserializer
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.ArrayMapDeserializer (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/ArrayMapDeserializer.html
version: 1
---

Package [com.fluig.sdk.api](https://api.fluig.com/old/sdk/com/fluig/sdk/api/package-summary.html)

## Class ArrayMapDeserializer

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fasterxml.jackson.databind.JsonDeserializer<[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html?is-external=true "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang"),​[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html?is-external=true "class or interface in java.lang")>>
  + - com.fluig.sdk.api.ArrayMapDeserializer

* All Implemented Interfaces:
  :   `com.fasterxml.jackson.databind.deser.NullValueProvider`

  ---

  ```
  public class ArrayMapDeserializer
  extends com.fasterxml.jackson.databind.JsonDeserializer<Map<String,​String>>
  ```

  Deserializa mapa de array

  Version:
  :   1.00.000

  Author:
  :   vanei

* + ### Nested Class Summary

    - ### Nested classes/interfaces inherited from class com.fasterxml.jackson.databind.JsonDeserializer

      `com.fasterxml.jackson.databind.JsonDeserializer.None`

  + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `ArrayMapDeserializer()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `Map<String,​String>` | `deserialize​(com.fasterxml.jackson.core.JsonParser jp, com.fasterxml.jackson.databind.DeserializationContext context)` | Deserializa mapa de array |

    - ### Methods inherited from class com.fasterxml.jackson.databind.JsonDeserializer

      `deserialize, deserializeWithType, findBackReference, getDelegatee, getEmptyAccessPattern, getEmptyValue, getEmptyValue, getKnownPropertyNames, getNullAccessPattern, getNullValue, getNullValue, getObjectIdReader, handledType, isCachable, replaceDelegatee, supportsUpdate, unwrappingDeserializer`
    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### ArrayMapDeserializer

      ```
      public ArrayMapDeserializer()
      ```

  + ### Method Detail

    - #### deserialize

      ```
      public Map<String,​String> deserialize​(com.fasterxml.jackson.core.JsonParser jp,
                                                  com.fasterxml.jackson.databind.DeserializationContext context)
                                           throws IOException
      ```

      Deserializa mapa de array

      Specified by:
      :   `deserialize` in class `com.fasterxml.jackson.databind.JsonDeserializer<Map<String,​String>>`

      Throws:
      :   `IOException`
