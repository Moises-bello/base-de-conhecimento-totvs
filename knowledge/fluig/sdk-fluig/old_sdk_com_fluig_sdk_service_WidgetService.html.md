---
content_hash: 6b13d840dae535ace0415214b4e2233b3995324b6259390deb47c839a6cd31a9
fetched_at: '2026-11-03T14:35:07.082528+00:00'
page_id: com/fluig/sdk/service/WidgetService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.WidgetService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/WidgetService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface WidgetService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface WidgetService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de permissão.

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `Map<String,​Properties>` | `findWidgetPermissionList​(String widgetCode)` | Busca pelas permissões em banco de uma determinada widget |
    | `void` | `grantWidgetDefaultPermission​(String widgetCode)` | Adiciona as permissões padrão de um widget |
    | `List<Properties>` | `listAllWidgetsPermission()` | Lista as permissões de todas as widgets |
    | `void` | `revokeWidgetPermission​(String widgetCode)` | Remove as permissões gerais de uma widget |
    | `List<String>` | `searchForbiddenResourceCodes()` | Busca códigos de recursos que não devem ser listados |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.WidgetService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.WidgetService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### revokeWidgetPermission

      ```
      void revokeWidgetPermission​(String widgetCode)
                           throws com.fluig.sdk.api.common.SDKException
      ```

      Remove as permissões gerais de uma widget

      Parameters:
      :   `widgetCode` -

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5.13
    - #### grantWidgetDefaultPermission

      ```
      void grantWidgetDefaultPermission​(String widgetCode)
                                 throws com.fluig.sdk.api.common.SDKException
      ```

      Adiciona as permissões padrão de um widget

      Parameters:
      :   `widgetCode` -

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### findWidgetPermissionList

      ```
      Map<String,​Properties> findWidgetPermissionList​(String widgetCode)
                                                     throws com.fluig.sdk.api.common.SDKException
      ```

      Busca pelas permissões em banco de uma determinada widget

      Parameters:
      :   `widgetCode` -

      Returns:
      :   Mapa de permissões

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`

      Since:
      :   1.5.13
    - #### listAllWidgetsPermission

      ```
      List<Properties> listAllWidgetsPermission()
                                         throws com.fluig.sdk.api.common.SDKException
      ```

      Lista as permissões de todas as widgets

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### searchForbiddenResourceCodes

      ```
      List<String> searchForbiddenResourceCodes()
                                         throws com.fluig.sdk.api.common.SDKException
      ```

      Busca códigos de recursos que não devem ser listados

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
