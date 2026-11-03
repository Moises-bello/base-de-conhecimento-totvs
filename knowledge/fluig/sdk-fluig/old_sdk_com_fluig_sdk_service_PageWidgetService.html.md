---
content_hash: f72fbf3bd6ebea58b002b0f70654532ce9d47326ad6c14dc85e9c1d787bacb2e
fetched_at: '2026-11-03T14:35:06.906259+00:00'
page_id: com/fluig/sdk/service/PageWidgetService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.PageWidgetService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/PageWidgetService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface PageWidgetService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface PageWidgetService
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
    | `void` | `disableForMobileApp​(long instanceId)` |  |
    | `void` | `enableForMobileApp​(long instanceId)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.PageWidgetService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.PageWidgetService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### enableForMobileApp

      ```
      void enableForMobileApp​(long instanceId)
                       throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### disableForMobileApp

      ```
      void disableForMobileApp​(long instanceId)
                        throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
