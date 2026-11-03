---
content_hash: df49d6f669182043f746621530b6cbbf19219babbf391020c827943f13102338
fetched_at: '2026-11-03T14:35:06.975948+00:00'
page_id: com/fluig/sdk/service/SocialSDKService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.SocialSDKService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/SocialSDKService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface SocialSDKService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface SocialSDKService
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
    | `SocialVO` | `findSocialUser​(Long userId)` | Find social user by id |
    | `SocialVO` | `findSocialVOByAlias​(String alias)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.SocialSDKService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.SocialSDKService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### findSocialUser

      ```
      SocialVO findSocialUser​(Long userId)
                       throws com.fluig.sdk.api.common.SDKException
      ```

      Find social user by id

      Parameters:
      :   `userId` -

      Returns:
      :   SocialVO

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### findSocialVOByAlias

      ```
      SocialVO findSocialVOByAlias​(String alias)
                            throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
