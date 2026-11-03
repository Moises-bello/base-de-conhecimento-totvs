---
content_hash: 3927e5bb95953b899fbf82e1690f0b149d669348faebcf1329d92f9e36ebc389
fetched_at: '2026-11-03T14:35:06.701242+00:00'
page_id: com/fluig/sdk/service/GlobalParameterService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.GlobalParameterService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/GlobalParameterService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface GlobalParameterService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface GlobalParameterService
  extends BaseAPIService
  ```

  Grant access to global parameter services

  Since:
  :   1.5.3

  Author:
  :   vinicius.michelutti

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `static String` | `JNDI_NAME` |  |
    | `static String` | `JNDI_REMOTE_NAME` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Abstract Methods](javascript:show(4);)

    | Modifier and Type | Method | Description |
    | `Long` | `getMaxUploadSize()` |  |
    | `Long` | `getMaxUploadSizeForConnect()` | Retorna o tamanho configurado, do máximo de upload pelo fluig Connect |
    | `Boolean` | `getViewJustProcessWithApproval()` | retorna se a empresa irá mostrar somente as tarefas configuradas para o app approval nos dispositivos mobile |
    | `void` | `setMaxUploadsizeForConnect​(Integer size)` | Seta o tamanho máximo de upload via fluig Connect |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.GlobalParameterService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.GlobalParameterService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### getMaxUploadSizeForConnect

      ```
      Long getMaxUploadSizeForConnect()
                               throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna o tamanho configurado, do máximo de upload pelo fluig Connect

      Returns:
      :   O tamanho em bytes

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### setMaxUploadsizeForConnect

      ```
      void setMaxUploadsizeForConnect​(Integer size)
                               throws com.fluig.sdk.api.common.SDKException
      ```

      Seta o tamanho máximo de upload via fluig Connect

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getViewJustProcessWithApproval

      ```
      Boolean getViewJustProcessWithApproval()
                                      throws com.fluig.sdk.api.common.SDKException
      ```

      retorna se a empresa irá mostrar somente as tarefas configuradas para o app approval nos dispositivos mobile

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getMaxUploadSize

      ```
      Long getMaxUploadSize()
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
