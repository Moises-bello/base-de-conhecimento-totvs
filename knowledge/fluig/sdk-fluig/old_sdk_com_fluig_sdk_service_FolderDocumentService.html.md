---
content_hash: e23025c25ce7a427a05ac58ebfcf0cb84c3f3ec389c4ef313be1d1ae12e7fe8a
fetched_at: '2026-11-03T14:35:06.688398+00:00'
page_id: com/fluig/sdk/service/FolderDocumentService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.FolderDocumentService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/FolderDocumentService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface FolderDocumentService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface FolderDocumentService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de pastas (GED).

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
    | `FolderVO` | `create​(FolderVO vo)` | Criação de uma nova pasta |
    | `DocumentVO` | `get​(int documentId)` | Recupera um documento através do id |
    | `List<DocumentVO>` | `list​(int folderId)` | Recupera lista de documentos através do id da pasta |
    | `List<DocumentVO>` | `list​(int folderId, int permission)` | Recupera lista de documentos através do id da pasta |
    | `List<DocumentVO>` | `listDocumentsByFolder​(FolderVO folderVO, int limit, int offset)` | Retorna os documentos de uma pasta |
    | `DocumentVO` | `updateDocumentDescription​(long companyId, int documentId, String description)` | Atualiza documento ou pasta |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.FolderDocumentService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.FolderDocumentService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### get

      ```
      DocumentVO get​(int documentId)
              throws com.fluig.sdk.api.common.SDKException
      ```

      Recupera um documento através do id

      Parameters:
      :   `documentId` -

      Returns:
      :   DocumentVO

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### create

      ```
      FolderVO create​(FolderVO vo)
               throws com.fluig.sdk.api.common.SDKException
      ```

      Criação de uma nova pasta

      Parameters:
      :   `vo` -

      Returns:
      :   FolderVO

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### list

      ```
      List<DocumentVO> list​(int folderId)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Recupera lista de documentos através do id da pasta

      Parameters:
      :   `folderId` -

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### updateDocumentDescription

      ```
      DocumentVO updateDocumentDescription​(long companyId,
                                           int documentId,
                                           String description)
                                    throws com.fluig.sdk.api.common.SDKException
      ```

      Atualiza documento ou pasta

      Parameters:
      :   `companyId` -
      :   `documentId` -
      :   `description` -

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### list

      ```
      List<DocumentVO> list​(int folderId,
                            int permission)
                     throws com.fluig.sdk.api.common.SDKException
      ```

      Recupera lista de documentos através do id da pasta

      Parameters:
      :   `folderId` -
      :   `permission` -

      Returns:

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### listDocumentsByFolder

      ```
      List<DocumentVO> listDocumentsByFolder​(FolderVO folderVO,
                                             int limit,
                                             int offset)
                                      throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna os documentos de uma pasta

      Parameters:
      :   `FolderVO` -
      :   `limit` -
      :   `offset` -

      Returns:
      :   List

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
