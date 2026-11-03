---
content_hash: 7e52662e27ad554596d5f114bd33ed03243042df82862c6a14c4c7dbdda062ec
fetched_at: '2026-11-03T14:35:03.653472+00:00'
page_id: com/fluig/sdk/api/alert/AlertSenderVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.alert.AlertSenderVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/alert/AlertSenderVO.html
version: 1
---

Package [com.fluig.sdk.api.alert](https://api.fluig.com/old/sdk/com/fluig/sdk/api/alert/package-summary.html)

## Class AlertSenderVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.alert.AlertSenderVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class AlertSenderVO
  extends Object
  implements Serializable
  ```

  Author:
  :   luis.junior

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.alert.AlertSenderVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `AlertSenderVO()` |  |
    | `AlertSenderVO​(Long id, AlertUserVO user, Date creationDate, String via)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `Date` | `getCreationDate()` |  |
    | `Long` | `getId()` |  |
    | `AlertUserVO` | `getUser()` |  |
    | `String` | `getVia()` |  |
    | `void` | `setCreationDate​(Date creationDate)` |  |
    | `void` | `setId​(Long id)` |  |
    | `void` | `setUser​(AlertUserVO user)` |  |
    | `void` | `setVia​(String via)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### AlertSenderVO

      ```
      public AlertSenderVO()
      ```
    - #### AlertSenderVO

      ```
      public AlertSenderVO​(Long id,
                           AlertUserVO user,
                           Date creationDate,
                           String via)
      ```

  + ### Method Detail

    - #### getId

      ```
      public Long getId()
      ```
    - #### setId

      ```
      public void setId​(Long id)
      ```
    - #### getUser

      ```
      public AlertUserVO getUser()
      ```
    - #### setUser

      ```
      public void setUser​(AlertUserVO user)
      ```
    - #### getCreationDate

      ```
      public Date getCreationDate()
      ```
    - #### setCreationDate

      ```
      public void setCreationDate​(Date creationDate)
      ```
    - #### getVia

      ```
      public String getVia()
      ```
    - #### setVia

      ```
      public void setVia​(String via)
      ```
