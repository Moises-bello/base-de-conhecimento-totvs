---
content_hash: 4afcc2e457aeeee2d71359eb1b3924706a2bd3bb9b4fedeee4d42ec83e695dfd
fetched_at: '2026-11-03T14:35:06.932459+00:00'
page_id: com/fluig/sdk/service/SearchService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.SearchService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/SearchService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface SearchService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface SearchService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de busca

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |
    | `static int` | `MAX_INFLUENCERS_RESULT` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `DefaultSearchResponse` | `findInfluencers​(DefaultSearchRequest search)` | Retorna lista de influenciadores para um assunto(#tag) |
    | `DefaultSearchResponse` | `findInfluencers​(String search)` |  |
    | `List<Map<String,​Object>>` | `groupedSearch​(DefaultSearchRequest request)` | Retorna uma lista de resultados agrupadas |
    | `List<Map<String,​Object>>` | `groupedSearchByType​(DefaultSearchRequest request)` | Retorna uma lista de resultados agrupadas por tipo |
    | `DefaultSearchResponse` | `search​(DefaultSearchRequest request)` | Retorna a pesquisa padrão, com os tipos de documentos encontrados em forma de lista |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.SearchService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.SearchService.JNDI_REMOTE_NAME)
    - #### MAX\_INFLUENCERS\_RESULT

      ```
      static final int MAX_INFLUENCERS_RESULT
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.SearchService.MAX_INFLUENCERS_RESULT)

  + ### Method Detail

    - #### search

      ```
      DefaultSearchResponse search​(DefaultSearchRequest request)
                            throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna a pesquisa padrão, com os tipos de documentos encontrados em forma de lista

      Parameters:
      :   `request` -

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### findInfluencers

      ```
      DefaultSearchResponse findInfluencers​(DefaultSearchRequest search)
                                     throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna lista de influenciadores para um assunto(#tag)

      Parameters:
      :   `String` - search

      Returns:
      :   `InfluencersSearch`

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### findInfluencers

      ```
      DefaultSearchResponse findInfluencers​(String search)
                                     throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### groupedSearch

      ```
      List<Map<String,​Object>> groupedSearch​(DefaultSearchRequest request)
                                            throws com.fluig.sdk.api.common.SDKException,
                                                   NamingException
      ```

      Retorna uma lista de resultados agrupadas

      Parameters:
      :   `request` -

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
      :   `NamingException`
    - #### groupedSearchByType

      ```
      List<Map<String,​Object>> groupedSearchByType​(DefaultSearchRequest request)
                                                  throws com.fluig.sdk.api.common.SDKException,
                                                         NamingException
      ```

      Retorna uma lista de resultados agrupadas por tipo

      Parameters:
      :   `request` -

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
      :   `NamingException`
