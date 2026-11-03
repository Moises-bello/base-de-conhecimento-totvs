---
content_hash: b9d4eb7505bd0f9002ae341acbaf089d5bf272c49c4c2cae220a2819a622640b
fetched_at: '2026-11-03T14:35:03.671062+00:00'
page_id: com/fluig/sdk/api/alert/AlertUserVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.alert.AlertUserVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/alert/AlertUserVO.html
version: 1
---

Package [com.fluig.sdk.api.alert](https://api.fluig.com/old/sdk/com/fluig/sdk/api/alert/package-summary.html)

## Class AlertUserVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.alert.AlertUserVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class AlertUserVO
  extends Object
  implements Serializable
  ```

  Author:
  :   luis.junior

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.alert.AlertUserVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `AlertUserVO()` |  |
    | `AlertUserVO​(com.totvs.technology.foundation.security.entity.FDNUserTenant user)` |  |
    | `AlertUserVO​(com.totvs.technology.foundation.security.vo.FDNUserVO userVO)` |  |
    | `AlertUserVO​(Long id, String login, String fullName, Long tenantId)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getFisrtName()` |  |
    | `String` | `getFullName()` |  |
    | `Long` | `getId()` |  |
    | `String` | `getLastName()` |  |
    | `Date` | `getLastUpdateDate()` |  |
    | `String` | `getLogin()` |  |
    | `Long` | `getTenantId()` |  |
    | `void` | `setFullName​(String fullName)` |  |
    | `void` | `setId​(Long id)` |  |
    | `void` | `setLastUpdateDate​(Date lastUpdateDate)` |  |
    | `void` | `setLogin​(String login)` |  |
    | `void` | `setTenantId​(Long tenantId)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### AlertUserVO

      ```
      public AlertUserVO()
      ```
    - #### AlertUserVO

      ```
      public AlertUserVO​(Long id,
                         String login,
                         String fullName,
                         Long tenantId)
      ```
    - #### AlertUserVO

      ```
      public AlertUserVO​(com.totvs.technology.foundation.security.vo.FDNUserVO userVO)
      ```
    - #### AlertUserVO

      ```
      public AlertUserVO​(com.totvs.technology.foundation.security.entity.FDNUserTenant user)
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
    - #### getLogin

      ```
      public String getLogin()
      ```
    - #### setLogin

      ```
      public void setLogin​(String login)
      ```
    - #### getFullName

      ```
      public String getFullName()
      ```
    - #### setFullName

      ```
      public void setFullName​(String fullName)
      ```
    - #### getFisrtName

      ```
      public String getFisrtName()
      ```
    - #### getLastName

      ```
      public String getLastName()
      ```
    - #### getLastUpdateDate

      ```
      public Date getLastUpdateDate()
      ```
    - #### setLastUpdateDate

      ```
      public void setLastUpdateDate​(Date lastUpdateDate)
      ```
    - #### getTenantId

      ```
      public Long getTenantId()
      ```
    - #### setTenantId

      ```
      public void setTenantId​(Long tenantId)
      ```
