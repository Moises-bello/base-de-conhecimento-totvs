---
content_hash: f3783253c0f2af9b5acdf4b6b6359c3b35339c102aff832e403ddaf52d7afc94
fetched_at: '2026-11-03T14:35:06.967092+00:00'
page_id: com/fluig/sdk/service/SocialBreadcrumbService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.SocialBreadcrumbService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/SocialBreadcrumbService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface SocialBreadcrumbService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface SocialBreadcrumbService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de breadcrumb.

  Since:
  :   1.5.4

  Author:
  :   marcus.carvalho

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `SocialBreadcrumbVO` | `get​(String alias, Long documentId, String folderType)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.SocialBreadcrumbService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.SocialBreadcrumbService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### get

      ```
      SocialBreadcrumbVO get​(String alias,
                             Long documentId,
                             String folderType)
                      throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
