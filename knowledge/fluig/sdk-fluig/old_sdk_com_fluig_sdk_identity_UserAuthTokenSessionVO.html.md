---
content_hash: c843f04e3d276d678c2a57d2a228d2f63be9f35d9a6600d24b74f38a42e497d1
fetched_at: '2026-11-03T14:35:06.312038+00:00'
page_id: com/fluig/sdk/identity/UserAuthTokenSessionVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.identity.UserAuthTokenSessionVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/identity/UserAuthTokenSessionVO.html
version: 1
---

Package [com.fluig.sdk.identity](https://api.fluig.com/old/sdk/com/fluig/sdk/identity/package-summary.html)

## Class UserAuthTokenSessionVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.identity.UserAuthTokenSessionVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class UserAuthTokenSessionVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.identity.UserAuthTokenSessionVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `UserAuthTokenSessionVO()` |  |
    | `UserAuthTokenSessionVO​(com.totvs.technology.foundation.security.entity.FDNUserMobileToken userMobileToken)` |  |

  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getAccessToken()` |  |
    | `String` | `getCompanyId()` |  |
    | `String` | `getDomain()` |  |
    | `Long` | `getExpiresIn()` |  |
    | `Long` | `getIssuedTime()` |  |
    | `String` | `getRefreshToken()` |  |
    | `static long` | `getSerialversionuid()` |  |
    | `HashMap<String,​String>` | `getSession()` |  |
    | `String` | `getUserIdIdp()` |  |
    | `void` | `setAccessToken​(String accessToken)` |  |
    | `void` | `setCompanyId​(String companyId)` |  |
    | `void` | `setDomain​(String domain)` |  |
    | `void` | `setExpiresIn​(Long expiresIn)` |  |
    | `void` | `setIssuedTime​(Long issuedTime)` |  |
    | `void` | `setRefreshToken​(String refreshToken)` |  |
    | `void` | `setSession​(HashMap<String,​String> session)` |  |
    | `void` | `setUserIdIdp​(String userIdIdp)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### UserAuthTokenSessionVO

      ```
      public UserAuthTokenSessionVO()
      ```
    - #### UserAuthTokenSessionVO

      ```
      public UserAuthTokenSessionVO​(com.totvs.technology.foundation.security.entity.FDNUserMobileToken userMobileToken)
      ```

  + ### Method Detail

    - #### getUserIdIdp

      ```
      public String getUserIdIdp()
      ```
    - #### setUserIdIdp

      ```
      public void setUserIdIdp​(String userIdIdp)
      ```
    - #### getCompanyId

      ```
      public String getCompanyId()
      ```
    - #### setCompanyId

      ```
      public void setCompanyId​(String companyId)
      ```
    - #### getAccessToken

      ```
      public String getAccessToken()
      ```
    - #### setAccessToken

      ```
      public void setAccessToken​(String accessToken)
      ```
    - #### getRefreshToken

      ```
      public String getRefreshToken()
      ```
    - #### setRefreshToken

      ```
      public void setRefreshToken​(String refreshToken)
      ```
    - #### getIssuedTime

      ```
      public Long getIssuedTime()
      ```
    - #### setIssuedTime

      ```
      public void setIssuedTime​(Long issuedTime)
      ```
    - #### getExpiresIn

      ```
      public Long getExpiresIn()
      ```
    - #### setExpiresIn

      ```
      public void setExpiresIn​(Long expiresIn)
      ```
    - #### getSerialversionuid

      ```
      public static long getSerialversionuid()
      ```
    - #### getSession

      ```
      public HashMap<String,​String> getSession()
      ```
    - #### setSession

      ```
      public void setSession​(HashMap<String,​String> session)
      ```
    - #### getDomain

      ```
      public String getDomain()
      ```
    - #### setDomain

      ```
      public void setDomain​(String domain)
      ```
