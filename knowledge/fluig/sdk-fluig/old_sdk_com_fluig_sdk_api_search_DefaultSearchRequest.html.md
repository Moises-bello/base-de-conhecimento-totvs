---
content_hash: 040e37e980e1c94cb4066e621107f3d0bd52e3a09a129827d85834e981b2c89f
fetched_at: '2026-11-03T14:35:04.653193+00:00'
page_id: com/fluig/sdk/api/search/DefaultSearchRequest
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.search.DefaultSearchRequest (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/search/DefaultSearchRequest.html
version: 1
---

Package [com.fluig.sdk.api.search](https://api.fluig.com/old/sdk/com/fluig/sdk/api/search/package-summary.html)

## Class DefaultSearchRequest

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.search.DefaultSearchRequest

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class DefaultSearchRequest
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.search.DefaultSearchRequest)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `DefaultSearchRequest()` |  |
    | `DefaultSearchRequest​(String pattern)` |  |
    | `DefaultSearchRequest​(String pattern, String ordering, int limit, int offset)` |  |
    | `DefaultSearchRequest​(String pattern, String searchType, String ordering, int limit, int offset)` |  |
    | `DefaultSearchRequest​(String searchType, String pattern, Date startPeriod, Date endPeriod, com.totvs.technology.foundation.indexer.common.DateGap period, String ordering, int limit, int offset)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `Date` | `getEndPeriod()` |  |
    | `int` | `getLimit()` |  |
    | `int` | `getOffset()` |  |
    | `String` | `getOrdering()` |  |
    | `String` | `getPattern()` |  |
    | `com.totvs.technology.foundation.indexer.common.DateGap` | `getPeriod()` |  |
    | `String` | `getSearchType()` |  |
    | `Date` | `getStartPeriod()` |  |
    | `void` | `setEndPeriod​(Date endPeriod)` |  |
    | `void` | `setLimit​(int limit)` |  |
    | `void` | `setOffset​(int offset)` |  |
    | `void` | `setOrdering​(String ordering)` |  |
    | `void` | `setPattern​(String pattern)` |  |
    | `void` | `setPeriod​(com.totvs.technology.foundation.indexer.common.DateGap period)` |  |
    | `void` | `setSearchType​(String searchType)` |  |
    | `void` | `setStartPeriod​(Date startPeriod)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### DefaultSearchRequest

      ```
      public DefaultSearchRequest()
      ```
    - #### DefaultSearchRequest

      ```
      public DefaultSearchRequest​(String pattern,
                                  String ordering,
                                  int limit,
                                  int offset)
      ```
    - #### DefaultSearchRequest

      ```
      public DefaultSearchRequest​(String pattern,
                                  String searchType,
                                  String ordering,
                                  int limit,
                                  int offset)
      ```
    - #### DefaultSearchRequest

      ```
      public DefaultSearchRequest​(String searchType,
                                  String pattern,
                                  Date startPeriod,
                                  Date endPeriod,
                                  com.totvs.technology.foundation.indexer.common.DateGap period,
                                  String ordering,
                                  int limit,
                                  int offset)
      ```
    - #### DefaultSearchRequest

      ```
      public DefaultSearchRequest​(String pattern)
      ```

  + ### Method Detail

    - #### getSearchType

      ```
      public String getSearchType()
      ```
    - #### setSearchType

      ```
      public void setSearchType​(String searchType)
      ```
    - #### getPattern

      ```
      public String getPattern()
      ```
    - #### setPattern

      ```
      public void setPattern​(String pattern)
      ```
    - #### getStartPeriod

      ```
      public Date getStartPeriod()
      ```
    - #### setStartPeriod

      ```
      public void setStartPeriod​(Date startPeriod)
      ```
    - #### getEndPeriod

      ```
      public Date getEndPeriod()
      ```
    - #### setEndPeriod

      ```
      public void setEndPeriod​(Date endPeriod)
      ```
    - #### getPeriod

      ```
      public com.totvs.technology.foundation.indexer.common.DateGap getPeriod()
      ```
    - #### setPeriod

      ```
      public void setPeriod​(com.totvs.technology.foundation.indexer.common.DateGap period)
      ```
    - #### getOrdering

      ```
      public String getOrdering()
      ```
    - #### setOrdering

      ```
      public void setOrdering​(String ordering)
      ```
    - #### getLimit

      ```
      public int getLimit()
      ```
    - #### setLimit

      ```
      public void setLimit​(int limit)
      ```
    - #### getOffset

      ```
      public int getOffset()
      ```
    - #### setOffset

      ```
      public void setOffset​(int offset)
      ```
