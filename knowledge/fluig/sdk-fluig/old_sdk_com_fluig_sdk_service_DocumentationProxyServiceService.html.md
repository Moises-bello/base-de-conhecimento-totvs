---
content_hash: 4d41de81536fcb37b11bc5ed31fbbdc8f8704fe4d94f8b6d2752a6045db97406
fetched_at: '2026-11-03T14:35:06.640497+00:00'
page_id: com/fluig/sdk/service/DocumentationProxyServiceService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.DocumentationProxyServiceService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/DocumentationProxyServiceService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface DocumentationProxyServiceService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface DocumentationProxyServiceService
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
    | `String` | `getUrlResult​(String expression)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.DocumentationProxyServiceService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.DocumentationProxyServiceService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### getUrlResult

      ```
      String getUrlResult​(String expression)
                   throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
