---
content_hash: 70a0355749263fd74870fea04e81f80e6c0f5f7c3b5256fdecd2e85394a38ba4
fetched_at: '2026-11-03T14:35:04.669039+00:00'
page_id: com/fluig/sdk/api/search/DefaultSearchResponse
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.search.DefaultSearchResponse (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/search/DefaultSearchResponse.html
version: 1
---

Package [com.fluig.sdk.api.search](https://api.fluig.com/old/sdk/com/fluig/sdk/api/search/package-summary.html)

## Class DefaultSearchResponse

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.search.DefaultSearchResponse

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class DefaultSearchResponse
  extends Object
  implements Serializable
  ```

  Value Object for Influencers

  Version:
  :   1.00.000

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.search.DefaultSearchResponse)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `DefaultSearchResponse()` |  |
    | `DefaultSearchResponse​(ArrayList<Map<String,​Object>> items)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `List<Map<String,​Object>>` | `getItems()` |  |
    | `int` | `getOffset()` |  |
    | `Long` | `getTimeElapsed()` |  |
    | `Long` | `getTotalHits()` |  |
    | `boolean` | `isSolrAvailable()` |  |
    | `void` | `setItems​(List<Map<String,​Object>> items)` |  |
    | `void` | `setOffset​(int offset)` |  |
    | `void` | `setSolrAvailable​(boolean solrAvailable)` |  |
    | `void` | `setTimeElapsed​(Long timeElapsed)` |  |
    | `void` | `setTotalHits​(Long totalHits)` |  |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### DefaultSearchResponse

      ```
      public DefaultSearchResponse()
      ```
    - #### DefaultSearchResponse

      ```
      public DefaultSearchResponse​(ArrayList<Map<String,​Object>> items)
      ```

  + ### Method Detail

    - #### getTimeElapsed

      ```
      public Long getTimeElapsed()
      ```
    - #### setTimeElapsed

      ```
      public void setTimeElapsed​(Long timeElapsed)
      ```
    - #### getTotalHits

      ```
      public Long getTotalHits()
      ```
    - #### setTotalHits

      ```
      public void setTotalHits​(Long totalHits)
      ```
    - #### getOffset

      ```
      public int getOffset()
      ```
    - #### setOffset

      ```
      public void setOffset​(int offset)
      ```
    - #### isSolrAvailable

      ```
      public boolean isSolrAvailable()
      ```
    - #### setSolrAvailable

      ```
      public void setSolrAvailable​(boolean solrAvailable)
      ```
    - #### getItems

      ```
      public List<Map<String,​Object>> getItems()
      ```
    - #### setItems

      ```
      public void setItems​(List<Map<String,​Object>> items)
      ```
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
