---
content_hash: b5110f6a165a08b39319b728c03601be2534439099151418372bcf30073206cf
fetched_at: '2026-11-03T14:35:06.583568+00:00'
page_id: com/fluig/sdk/service/ContentFilesService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.ContentFilesService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/ContentFilesService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface ContentFilesService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface ContentFilesService
  extends BaseAPIService
  ```

  Disponibiliza operação para upload de arquivo

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
    | `String` | `getDeployableArtifactsDirectory()` | Recupera diretório do artefato a ser implantado |
    | `void` | `upload​(String fileName, byte[] fileContent)` | Executa o upload de um arquivo |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.ContentFilesService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.ContentFilesService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### upload

      ```
      void upload​(String fileName,
                  byte[] fileContent)
           throws com.fluig.sdk.api.common.SDKException
      ```

      Executa o upload de um arquivo

      Parameters:
      :   `fileName` -
      :   `fileContent` -

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### getDeployableArtifactsDirectory

      ```
      String getDeployableArtifactsDirectory()
                                      throws com.fluig.sdk.api.common.SDKException
      ```

      Recupera diretório do artefato a ser implantado

      Returns:
      :   String diretorio

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
