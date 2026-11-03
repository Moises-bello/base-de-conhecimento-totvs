---
content_hash: 3a8957d8aa85544951b13a434ce9894eff1bc16e205966343b2f3a4c86bb8824
fetched_at: '2026-11-03T14:35:06.870871+00:00'
page_id: com/fluig/sdk/service/OAuthUserService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.OAuthUserService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/OAuthUserService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface OAuthUserService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface OAuthUserService
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
    | `OAuthSdkVO` | `generateUserOAuthKeys​(String appKey, String login)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.OAuthUserService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.OAuthUserService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### generateUserOAuthKeys

      ```
      OAuthSdkVO generateUserOAuthKeys​(String appKey,
                                       String login)
                                throws Exception
      ```

      Throws:
      :   `Exception`
