---
content_hash: 684f99d765d7264cf6d0c53d8571dedd8aae9d57904151a96fcab63640fd087f
fetched_at: '2026-11-03T14:35:06.746229+00:00'
page_id: com/fluig/sdk/service/HolidayAPIService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.HolidayAPIService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/HolidayAPIService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface HolidayAPIService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface HolidayAPIService
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
    | `HolidayVO` | `create​(HolidayVO holidayVO)` | Cria feriado. |
    | `void` | `delete​(Long id)` | Deleta feriado. |
    | `HolidayVO` | `find​(Long id, String expand)` | Busca feriado. |
    | `com.totvs.technology.foundation.sdk.service.vo.common.ResponseEnvelopeVO<HolidayVO>` | `find​(String description, Long localId, List<com.totvs.technology.foundation.sdk.service.vo.common.OrderParam> orderParams, int page, int pageSize, int offset, int limit, boolean populateLocals, boolean populateUsers, boolean exclusive)` | Busca feriado. |
    | `com.totvs.technology.foundation.sdk.service.vo.common.ResponseEnvelopeVO<HolidayVO>` | `find​(String description, String localId, String order, String page, String pageSize, String offset, String limit, String expand, String exclusive)` | Busca feriado. |
    | `List<HolidayVO>` | `findAll()` | Busca todos os feriados da base a partir do código da empresa do usuário logado. |
    | `HolidayVO` | `patch​(Long id, HolidayVO holidayVO)` | Atualiza feriado. |
    | `HolidayVO` | `update​(Long id, HolidayVO holidayVO)` | Atualiza feriado. |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.HolidayAPIService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.HolidayAPIService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### create

      ```
      HolidayVO create​(HolidayVO holidayVO)
                throws Exception
      ```

      Cria feriado.

      Parameters:
      :   `holidayVO` - VO do feriado.

      Returns:
      :   VO do feriado criado.

      Throws:
      :   `Exception` - Qualquer exceção.
    - #### delete

      ```
      void delete​(Long id)
           throws Exception
      ```

      Deleta feriado.

      Parameters:
      :   `id` - Código do feriado.

      Throws:
      :   `Exception` - Qualquer exceção.
    - #### update

      ```
      HolidayVO update​(Long id,
                       HolidayVO holidayVO)
                throws Exception
      ```

      Atualiza feriado.

      Parameters:
      :   `id` - Código atual do feriado.
      :   `holidayVO` - VO do novo.

      Returns:
      :   VO do feriado atualizado.

      Throws:
      :   `Exception` - Qualquer exceção.
    - #### find

      ```
      HolidayVO find​(Long id,
                     String expand)
              throws Exception
      ```

      Busca feriado.

      Parameters:
      :   `id` - Código do feriado.
      :   `expand` - Campos de expansão, pode ser locals para buscar localizações relacionadas e locals.localUsers para ser os relacionamentos com usuários dos locais.

      Throws:
      :   `Exception` - Qualquer exceção.
    - #### findAll

      ```
      List<HolidayVO> findAll()
                       throws Exception
      ```

      Busca todos os feriados da base a partir do código da empresa do usuário logado.

      Throws:
      :   `Exception` - Qualquer exceção.
    - #### patch

      ```
      HolidayVO patch​(Long id,
                      HolidayVO holidayVO)
               throws Exception
      ```

      Atualiza feriado.

      Parameters:
      :   `id` - Código atual do feriado.
      :   `holidayVO` - VO do novo.

      Returns:
      :   VO do feriado atualizado.

      Throws:
      :   `Exception` - Qualquer exceção.
    - #### find

      ```
      com.totvs.technology.foundation.sdk.service.vo.common.ResponseEnvelopeVO<HolidayVO> find​(String description,
                                                                                               String localId,
                                                                                               String order,
                                                                                               String page,
                                                                                               String pageSize,
                                                                                               String offset,
                                                                                               String limit,
                                                                                               String expand,
                                                                                               String exclusive)
                                                                                        throws Exception
      ```

      Busca feriado.

      Parameters:
      :   `description` - Descrição do feriado.
      :   `localId` - Id do local para parâmetro da pesquisa.
      :   `order` - Ordenação da busca, pode ser apenas por id (descrição do feriado).
      :   `page` - Página da busca.
      :   `pageSize` - Quantidade de itens por página.
      :   `expand` - Campos de expansão, pode ser locals para buscar localizações relacionadas e locals.localUsers para ser os relacionamentos com usuários dos locais.
      :   `exclusive` - Se os feriados devem ser exclusivos daquele local.

      Throws:
      :   `Exception` - Qualquer exceção.
    - #### find

      ```
      com.totvs.technology.foundation.sdk.service.vo.common.ResponseEnvelopeVO<HolidayVO> find​(String description,
                                                                                               Long localId,
                                                                                               List<com.totvs.technology.foundation.sdk.service.vo.common.OrderParam> orderParams,
                                                                                               int page,
                                                                                               int pageSize,
                                                                                               int offset,
                                                                                               int limit,
                                                                                               boolean populateLocals,
                                                                                               boolean populateUsers,
                                                                                               boolean exclusive)
                                                                                        throws Exception
      ```

      Busca feriado.

      Parameters:
      :   `description` - Descrição do feriado.
      :   `localId` - Id do local para parâmetro da pesquisa.
      :   `orderParams` - Ordenação da busca, pode ser apenas por id (descrição do feriado).
      :   `page` - Página da busca.
      :   `pageSize` - Quantidade de itens por página.
      :   `populateLocals` - Se popula locais na lista do VO.
      :   `populateUsers` - Se popula usuários na lista do VO de local.
      :   `exclusive` - Se os feriados devem ser exclusivos daquele local.

      Throws:
      :   `Exception` - Qualquer exceção.
