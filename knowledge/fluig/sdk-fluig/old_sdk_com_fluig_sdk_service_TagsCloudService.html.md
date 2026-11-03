---
content_hash: 45230e8d1139d578f0f69ada47ad2092a64efb77ee00e30d7497ccf532347b33
fetched_at: '2026-11-03T14:35:06.986161+00:00'
page_id: com/fluig/sdk/service/TagsCloudService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.TagsCloudService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/TagsCloudService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface TagsCloudService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface TagsCloudService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de tagscloud.

  Since:
  :   1.5

  Author:
  :   ricardo.andre

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `Map<String,​Long>` | `getTags​(String query, String filterQuery, List<String> communitiesAlias, Integer limit, String login)` | Pesquisa por TAGS mais populares baseado em um conjunto de parâmetros. |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.TagsCloudService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.TagsCloudService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### getTags

      ```
      Map<String,​Long> getTags​(String query,
                                     String filterQuery,
                                     List<String> communitiesAlias,
                                     Integer limit,
                                     String login)
                              throws com.fluig.sdk.api.common.SDKException
      ```

      Pesquisa por TAGS mais populares baseado em um conjunto de parâmetros.

      Parameters:
      :   `query` - Query do Solr com a busca de tags.
      :   `filterQuery` - Filtro do Solr com a busca de tags.
      :   `communitiesAlias` - Lista das comunidades.
      :   `limit` - Quantidade de registos.
      :   `login` - login do usuario logado

      Returns:
      :   Lista com as TAGS mais populares e o número de ocorrências por palavra.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5
