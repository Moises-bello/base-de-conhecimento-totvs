---
content_hash: 896c5507aa501b22c8bd67701fb340a6a2cc8b622ee90dacc2ff62252520db01
fetched_at: '2026-11-03T14:35:06.452172+00:00'
page_id: com/fluig/sdk/service/AuthorizeClientSdkService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.AuthorizeClientSdkService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/AuthorizeClientSdkService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface AuthorizeClientSdkService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface AuthorizeClientSdkService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços externos com autenticação oauth.

  Since:
  :   1.5.10

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `OAuthSdkVO` | `create​(OAuthSdkVO vo)` |  |
    | `AuthorizeClientSdkServiceVO` | `invoke​(AuthorizeClientSdkServiceVO vo)` |  |
    | `AuthorizeClientSdkServiceVO` | `invoke​(String data)` |  |
    | `AuthorizeClientSdkServiceVO` | `invokeService​(String data)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.AuthorizeClientSdkService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.AuthorizeClientSdkService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### invoke

      ```
      AuthorizeClientSdkServiceVO invoke​(AuthorizeClientSdkServiceVO vo)
                                  throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### invoke

      ```
      AuthorizeClientSdkServiceVO invoke​(String data)
                                  throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### invokeService

      ```
      AuthorizeClientSdkServiceVO invokeService​(String data)
                                         throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### create

      ```
      OAuthSdkVO create​(OAuthSdkVO vo)
                 throws com.totvs.technology.foundation.common.exception.FDNException
      ```

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException`
