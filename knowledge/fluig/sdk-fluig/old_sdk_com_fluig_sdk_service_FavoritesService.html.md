---
content_hash: c7edb8c8dc6d277822caf1314ccf2f5d8ee1c8fb437fbfa18c922ad784f853b3
fetched_at: '2026-11-03T14:35:06.650943+00:00'
page_id: com/fluig/sdk/service/FavoritesService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.FavoritesService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/FavoritesService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface FavoritesService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface FavoritesService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de favoritos.

  Since:
  :   1.5.2

  Author:
  :   marcelo.pereira

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `List<DocumentVO>` | `findFavoritesDocuments​(String colleagueId)` | Busca os documentos favoritos |
    | `List<ProcessDefinitionVersionVO>` | `findFavoritesProcess​(String colleagueId)` | Busca os processos favoritos |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.FavoritesService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.FavoritesService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### findFavoritesDocuments

      ```
      List<DocumentVO> findFavoritesDocuments​(String colleagueId)
                                       throws com.fluig.sdk.api.common.SDKException
      ```

      Busca os documentos favoritos

      Parameters:
      :   `colleagueId` -

      Returns:
      :   Documentos favoritos

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possivel encontrar os documentos favoritos
    - #### findFavoritesProcess

      ```
      List<ProcessDefinitionVersionVO> findFavoritesProcess​(String colleagueId)
                                                     throws com.fluig.sdk.api.common.SDKException
      ```

      Busca os processos favoritos

      Parameters:
      :   `colleagueId` -

      Returns:
      :   Processos favoritos

      Throws:
      :   `com.fluig.sdk.api.common.SDKException` - Não foi possivel encontrar os processos favoritos
