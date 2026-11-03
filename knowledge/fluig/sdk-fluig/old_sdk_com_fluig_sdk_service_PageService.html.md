---
content_hash: 499351c5bc75c851f4a59145d559106d4de2675fd3657d607584b3d80e1b5f8d
fetched_at: '2026-11-03T14:35:06.897150+00:00'
page_id: com/fluig/sdk/service/PageService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.PageService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/PageService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface PageService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface PageService
  extends BaseAPIService
  ```

  Fornece acesso a serviços de segurança.

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
    | `void` | `createPageDraftFromVersion​(String pageCode, Number pageVersion)` |  |
    | `void` | `disable​(String pageCode)` |  |
    | `void` | `enable​(String pageCode)` |  |
    | `List<PublicApiPageVO>` | `findMenuFromPage​(String pageCode)` | Retorna itens de menu da página |
    | `List<PublicApiPageVO>` | `findPages​(String parentPageCode, Boolean isMobile, String filter, int start, int size, int searchLevel, Boolean internalPages)` | Consulta páginas do fluig |
    | `List<PublicApiPageVO>` | `findPages​(String parentPageCode, Boolean isMobile, String filter, int start, int size, int searchLevel, Boolean internalPages, String codePage)` | Consulta páginas do fluig |
    | `String` | `getServerURL()` | Retorna o endereco emque o servidor foi instalado |
    | `Map<String,​String>` | `getWidgetPreferences​(Long instanceId)` | Recupera os valores de preferências para uma instância de uma widget. |
    | `void` | `hide​(String pageCode)` |  |
    | `PageMobileApiVO` | `mobileMapping​(String pageCode)` |  |
    | `List<String>` | `pageHistory​(String pageCode)` |  |
    | `void` | `publishPageDraft​(String pageCode, String publicationDescription)` |  |
    | `void` | `reloadPageLayout​(String pageCode)` | Recarrega o layout de uma página. |
    | `void` | `setWidgetPreference​(Long instanceId, String key, String value)` | Seta o valor de uma preferência para uma instância de uma widget. |
    | `void` | `show​(String pageCode)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.PageService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.PageService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### setWidgetPreference

      ```
      void setWidgetPreference​(Long instanceId,
                               String key,
                               String value)
                        throws com.fluig.sdk.api.common.SDKException
      ```

      Seta o valor de uma preferência para uma instância de uma widget.

      Parameters:
      :   `instanceId` - ID da instância.
      :   `key` - Chave da preferência.
      :   `value` - Valor da preferência.

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException` - Não foi possível incluir/alterar a preferência.
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5
    - #### getWidgetPreferences

      ```
      Map<String,​String> getWidgetPreferences​(Long instanceId)
                                             throws com.fluig.sdk.api.common.SDKException
      ```

      Recupera os valores de preferências para uma instância de uma widget.

      Parameters:
      :   `instanceId` - ID da instância da widget.

      Returns:
      :   Mapa com os valores de preferências para uma instância de uma widget.

      Throws:
      :   `com.totvs.technology.foundation.common.exception.FDNException` - Não foi possível recuperar as preferências.
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5.8
    - #### findPages

      ```
      List<PublicApiPageVO> findPages​(String parentPageCode,
                                      Boolean isMobile,
                                      String filter,
                                      int start,
                                      int size,
                                      int searchLevel,
                                      Boolean internalPages)
                               throws com.fluig.sdk.api.common.SDKException
      ```

      Consulta páginas do fluig

      Parameters:
      :   `parentPageCode` -
      :   `isMobile` -
      :   `filter` -
      :   `start` -
      :   `size` -
      :   `searchLevel` -
      :   `internalPages` -

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### findPages

      ```
      List<PublicApiPageVO> findPages​(String parentPageCode,
                                      Boolean isMobile,
                                      String filter,
                                      int start,
                                      int size,
                                      int searchLevel,
                                      Boolean internalPages,
                                      String codePage)
                               throws com.fluig.sdk.api.common.SDKException
      ```

      Consulta páginas do fluig

      Parameters:
      :   `parentPageCode` -
      :   `isMobile` -
      :   `filter` -
      :   `start` -
      :   `size` -
      :   `searchLevel` -
      :   `internalPages` -
      :   `codePage` -

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### findMenuFromPage

      ```
      List<PublicApiPageVO> findMenuFromPage​(String pageCode)
                                      throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna itens de menu da página

      Parameters:
      :   `pageCode` -

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getServerURL

      ```
      String getServerURL()
                   throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna o endereco emque o servidor foi instalado

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### reloadPageLayout

      ```
      void reloadPageLayout​(String pageCode)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Recarrega o layout de uma página.

      Parameters:
      :   `pageCode` -

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### publishPageDraft

      ```
      void publishPageDraft​(String pageCode,
                            String publicationDescription)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### createPageDraftFromVersion

      ```
      void createPageDraftFromVersion​(String pageCode,
                                      Number pageVersion)
                               throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### pageHistory

      ```
      List<String> pageHistory​(String pageCode)
                        throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### mobileMapping

      ```
      PageMobileApiVO mobileMapping​(String pageCode)
                             throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### hide

      ```
      void hide​(String pageCode)
         throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### show

      ```
      void show​(String pageCode)
         throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### enable

      ```
      void enable​(String pageCode)
           throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### disable

      ```
      void disable​(String pageCode)
            throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
