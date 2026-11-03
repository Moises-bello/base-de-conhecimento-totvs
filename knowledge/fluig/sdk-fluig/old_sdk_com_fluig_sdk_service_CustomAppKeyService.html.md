---
content_hash: f4d2bb4727274fd878e2ac45eefd0ac699cc3a78c57ff30c83a25339575b885c
fetched_at: '2026-11-03T14:35:06.593414+00:00'
page_id: com/fluig/sdk/service/CustomAppKeyService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.CustomAppKeyService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/CustomAppKeyService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface CustomAppKeyService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface CustomAppKeyService
  extends BaseAPIService
  ```

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `KeyVO` | `getKey​(Long tenantId, String key)` |  |
    | `KeyVO` | `provisionKey​(Long tenantId, String key)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CustomAppKeyService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CustomAppKeyService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### provisionKey

      ```
      KeyVO provisionKey​(Long tenantId,
                         String key)
                  throws ApplicationKeyCreationException
      ```

      Throws:
      :   `ApplicationKeyCreationException`
    - #### getKey

      ```
      KeyVO getKey​(Long tenantId,
                   String key)
            throws ApplicationKeyNotFoundException
      ```

      Throws:
      :   `ApplicationKeyNotFoundException`
