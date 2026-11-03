---
content_hash: 824447ef5d5fafdccf28a3e016cebf31e3b36ae377ee2718587c7ebddbcb37d2
fetched_at: '2026-11-03T14:35:06.669060+00:00'
page_id: com/fluig/sdk/service/FilterAPIService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.FilterAPIService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/FilterAPIService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface FilterAPIService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface FilterAPIService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de filtros.

  Since:
  :   1.6.0

  Author:
  :   leandro.carlos

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `FilterResultVO` | `createFilter​(FilterVO filterVO)` |  |
    | `FilterResultVO` | `findById​(Long filterId)` |  |
    | `List<FilterGroupResultVO>` | `findFiltersGroupByFilterId​(Long filterId, String pattern, int limit, int offset, String orderBy)` |  |
    | `List<FilterResultVO>` | `getProcessFilters​(boolean onlyMyFilters, boolean findPublicFilters, String pattern, int limit, int offset, String orderBy)` |  |
    | `void` | `removeFilters​(List<Long> filtersId)` |  |
    | `List<FilterGroupResultVO>` | `saveFiltersGroup​(FilterGroupVO filterGroupVO)` |  |
    | `FilterResultVO` | `updateFilter​(FilterVO filterVO)` |  |
    | `FilterResultVO` | `updateFilterName​(long filterId, FilterUpdateNameVO filterUpdateNameVO)` |  |
    | `void` | `updateFilterSequence​(Long applicationInstanceId, Map<String,​String> filtersSequence)` |  |
    | `FilterResultVO` | `updatePublicProcessFilter​(long filterId, boolean isPublic)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.FilterAPIService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.FilterAPIService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### getProcessFilters

      ```
      List<FilterResultVO> getProcessFilters​(boolean onlyMyFilters,
                                             boolean findPublicFilters,
                                             String pattern,
                                             int limit,
                                             int offset,
                                             String orderBy)
                                      throws Exception
      ```

      Throws:
      :   `Exception`
    - #### findById

      ```
      FilterResultVO findById​(Long filterId)
                       throws Exception
      ```

      Throws:
      :   `Exception`
    - #### updatePublicProcessFilter

      ```
      FilterResultVO updatePublicProcessFilter​(long filterId,
                                               boolean isPublic)
                                        throws Exception
      ```

      Throws:
      :   `Exception`
    - #### removeFilters

      ```
      void removeFilters​(List<Long> filtersId)
                  throws Exception
      ```

      Throws:
      :   `Exception`
    - #### createFilter

      ```
      FilterResultVO createFilter​(FilterVO filterVO)
                           throws Exception
      ```

      Throws:
      :   `Exception`
    - #### updateFilter

      ```
      FilterResultVO updateFilter​(FilterVO filterVO)
                           throws Exception
      ```

      Throws:
      :   `Exception`
    - #### findFiltersGroupByFilterId

      ```
      List<FilterGroupResultVO> findFiltersGroupByFilterId​(Long filterId,
                                                           String pattern,
                                                           int limit,
                                                           int offset,
                                                           String orderBy)
                                                    throws Exception
      ```

      Throws:
      :   `Exception`
    - #### saveFiltersGroup

      ```
      List<FilterGroupResultVO> saveFiltersGroup​(FilterGroupVO filterGroupVO)
                                          throws Exception
      ```

      Throws:
      :   `Exception`
    - #### updateFilterSequence

      ```
      void updateFilterSequence​(Long applicationInstanceId,
                                Map<String,​String> filtersSequence)
                         throws Exception
      ```

      Throws:
      :   `Exception`
    - #### updateFilterName

      ```
      FilterResultVO updateFilterName​(long filterId,
                                      FilterUpdateNameVO filterUpdateNameVO)
                               throws Exception
      ```

      Throws:
      :   `Exception`
