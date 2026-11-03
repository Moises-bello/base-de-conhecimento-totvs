---
content_hash: 204744885a4fec29765032bca505f27e2e9aea7b4c9598920832fac4b868abff
fetched_at: '2026-11-03T14:35:06.521649+00:00'
page_id: com/fluig/sdk/service/CardIndexService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.CardIndexService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/CardIndexService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface CardIndexService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface CardIndexService
  extends BaseAPIService
  ```

  Fornece operações para gerenciamento card index

  Since:
  :   1.5

  Author:
  :   vanei.heidemann

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `CardIndexVO` | `create​(CardIndexVO vo)` | Criação de um novo card index |
    | `void` | `delete​(Integer documentId)` | Exclusão de um card index |
    | `Integer` | `getDefaultFormFolderId()` | Retorna a pasta padrão de formulário |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CardIndexService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CardIndexService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### create

      ```
      CardIndexVO create​(CardIndexVO vo)
                  throws com.fluig.sdk.api.common.SDKException
      ```

      Criação de um novo card index

      Parameters:
      :   `vo` - - object to persist

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### delete

      ```
      void delete​(Integer documentId)
      ```

      Exclusão de um card index

      Parameters:
      :   `Integer` - documentId
    - #### getDefaultFormFolderId

      ```
      Integer getDefaultFormFolderId()
                              throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna a pasta padrão de formulário

      Parameters:
      :   `Integer` - documentId

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
