---
content_hash: 3b91d833cc7a02ee6f1c290f316bc9d31687efd8f6c5eccc3e2faa863b3882ae
fetched_at: '2026-11-03T14:35:06.917312+00:00'
page_id: com/fluig/sdk/service/PostService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.PostService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/PostService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface PostService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface PostService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de post.

  Since:
  :   1.5

  Author:
  :   vanei

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `PostVO` | `create​(PostVO vo)` | Realiza um post em uma timeline, seja pessoal ou de alguma comunidade. |
    | `PostVO` | `createWithUpload​(PostVO vo)` | Realiza um post com anexo em uma timeline, seja pessoal ou de alguma comunidade. |
    | `void` | `editPost​(Long postId, String text)` | Edit a single post |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.PostService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.PostService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### create

      ```
      PostVO create​(PostVO vo)
             throws com.fluig.sdk.api.common.SDKException
      ```

      Realiza um post em uma timeline, seja pessoal ou de alguma comunidade.

      Parameters:
      :   `vo` - Dados do post.

      Returns:
      :   Dados do post criado.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possível efetuar o post.
    - #### createWithUpload

      ```
      PostVO createWithUpload​(PostVO vo)
                       throws com.fluig.sdk.api.common.SDKException
      ```

      Realiza um post com anexo em uma timeline, seja pessoal ou de alguma comunidade.

      Parameters:
      :   `vo` - Dados do post.

      Returns:
      :   Dados do post criado.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possível efetuar o post.
    - #### editPost

      ```
      void editPost​(Long postId,
                    String text)
             throws com.fluig.sdk.api.common.SDKException,
                    com.totvs.technology.foundation.common.exception.FDNException,
                    NamingException
      ```

      Edit a single post

      Parameters:
      :   `postId` -
      :   `text` -

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
      :   `NamingException`
      :   `com.totvs.technology.foundation.common.exception.FDNException`
