---
content_hash: 32b37307eac3a346eb943b2c6e8b9a9c85af99e990dfe1d52f4d0045e42170f1
fetched_at: '2026-11-03T14:35:06.530636+00:00'
page_id: com/fluig/sdk/service/CardService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.CardService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/CardService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface CardService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface CardService
  extends BaseAPIService
  ```

  Fornece operações para gerenciamento de Card's

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
    | `CardItemVO` | `createItem​(CardItemVO vo)` | Criação de um novo card |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CardService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CardService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### createItem

      ```
      CardItemVO createItem​(CardItemVO vo)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Criação de um novo card

      Parameters:
      :   `vo` -

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
