---
content_hash: 0a6c8d0c2d77f7ac63a2c13fc98fded8101f66a8d2c9cee34212d8fb42c6bd1b
fetched_at: '2026-11-03T14:35:03.882453+00:00'
page_id: com/fluig/sdk/api/customappkey/KeyVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.customappkey.KeyVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/customappkey/KeyVO.html
version: 1
---

Package [com.fluig.sdk.api.customappkey](https://api.fluig.com/old/sdk/com/fluig/sdk/api/customappkey/package-summary.html)

## Class KeyVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.customappkey.KeyVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class KeyVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.customappkey.KeyVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `KeyVO​(String user, Long tenantId, String consumerKey, String consumerSecret, String token, String tokenSecret, String domainUrl)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getConsumerKey()` |  |
    | `String` | `getConsumerSecret()` |  |
    | `String` | `getDomainUrl()` |  |
    | `Long` | `getTenantId()` |  |
    | `String` | `getToken()` |  |
    | `String` | `getTokenSecret()` |  |
    | `String` | `getUser()` |  |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### KeyVO

      ```
      public KeyVO​(String user,
                   Long tenantId,
                   String consumerKey,
                   String consumerSecret,
                   String token,
                   String tokenSecret,
                   String domainUrl)
      ```

  + ### Method Detail

    - #### getUser

      ```
      public String getUser()
      ```
    - #### getTenantId

      ```
      public Long getTenantId()
      ```
    - #### getConsumerKey

      ```
      public String getConsumerKey()
      ```
    - #### getConsumerSecret

      ```
      public String getConsumerSecret()
      ```
    - #### getToken

      ```
      public String getToken()
      ```
    - #### getTokenSecret

      ```
      public String getTokenSecret()
      ```
    - #### getDomainUrl

      ```
      public String getDomainUrl()
      ```
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
