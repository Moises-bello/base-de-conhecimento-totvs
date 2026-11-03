---
content_hash: 91c9b8b31c208d87d1447b3b21c133f5dabe6334fb51386f33433d90bab6cb91
fetched_at: '2026-11-03T14:35:06.770987+00:00'
page_id: com/fluig/sdk/service/IdentityService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.IdentityService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/IdentityService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface IdentityService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface IdentityService
  extends BaseAPIService
  ```

  Grant access to global parameter services

  Since:
  :   1.5.3

  Author:
  :   vinicius.michelutti

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `UserAuthTokenSessionVO` | `createSession()` | Retorna o uma nova sessão do identity |
    | `void` | `updateSession()` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.IdentityService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.IdentityService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### createSession

      ```
      UserAuthTokenSessionVO createSession()
                                    throws Exception
      ```

      Retorna o uma nova sessão do identity

      Returns:
      :   As informações da nova sessão, juntamente com a informaçõo do usuário referente a tal sessão

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
      :   `Exception`
    - #### updateSession

      ```
      void updateSession()
                  throws Exception
      ```

      Throws:
      :   `Exception`
