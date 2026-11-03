---
content_hash: 2f9ba4214afc9bd7861b6da85c66d44e4d1c1b5708563925e980e4ca3ae41751
fetched_at: '2026-11-03T14:35:06.561593+00:00'
page_id: com/fluig/sdk/service/CommentService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.CommentService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/CommentService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface CommentService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface CommentService
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
    | `void` | `editComment​(Long commentId, String text)` | Edit a single comment |
    | `CommentVO` | `findComment​(Long sociableId)` | Find a single comment |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CommentService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CommentService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### editComment

      ```
      void editComment​(Long commentId,
                       String text)
                throws com.fluig.sdk.api.common.SDKException,
                       com.totvs.technology.foundation.common.exception.FDNException,
                       NamingException
      ```

      Edit a single comment

      Parameters:
      :   `commentId` -
      :   `text` -

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
      :   `NamingException`
      :   `com.totvs.technology.foundation.common.exception.FDNException`
    - #### findComment

      ```
      CommentVO findComment​(Long sociableId)
                     throws NamingException
      ```

      Find a single comment

      Parameters:
      :   `sociableId` -

      Returns:

      Throws:
      :   `NamingException`
