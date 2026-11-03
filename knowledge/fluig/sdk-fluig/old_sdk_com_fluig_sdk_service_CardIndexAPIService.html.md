---
content_hash: ae371de31b9b496929c2e4dff5aeed575805bf209f4cfd4e9feff48c382ada31
fetched_at: '2026-11-03T14:35:06.511414+00:00'
page_id: com/fluig/sdk/service/CardIndexAPIService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.CardIndexAPIService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/CardIndexAPIService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface CardIndexAPIService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface CardIndexAPIService
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
    | `CardIndexAPIVO` | `createCardIndex​(File filecontent, String formName, Integer parentIdValue)` |  |
    | `CardIndexAPIVO` | `createCardIndex​(File filecontent, String mainFile, String formName, String descriptorField, String datasetName, Integer parentIdValue)` |  |
    | `boolean` | `deleteCardIndex​(Integer documentId)` |  |
    | `com.totvs.technology.foundation.sdk.service.vo.common.ResponseEnvelopeVO<CardIndexFindAPIVO>` | `findCardIndex​(Integer documentId, Integer version)` |  |
    | `com.totvs.technology.foundation.sdk.service.vo.common.ResponseEnvelopeVO<CardIndexFindAPIVO>` | `findCardIndex​(Integer documentId, Integer version, List order, Integer page, Integer pageSize)` |  |
    | `CardIndexAPIVO` | `patchCardIndex​(File filecontent, Integer documentIdValue, String updateMode, String mainFile, String formName, String descriptorField, String datasetName)` |  |
    | `CardIndexAPIVO` | `putCardIndex​(File filecontent, Integer documentIdValue, String updateMode, String mainFile, String formName, String descriptorField, String datasetName)` |  |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CardIndexAPIService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CardIndexAPIService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### findCardIndex

      ```
      com.totvs.technology.foundation.sdk.service.vo.common.ResponseEnvelopeVO<CardIndexFindAPIVO> findCardIndex​(Integer documentId,
                                                                                                                 Integer version,
                                                                                                                 List order,
                                                                                                                 Integer page,
                                                                                                                 Integer pageSize)
                                                                                                          throws Exception
      ```

      Parameters:
      :   `documentId` - numero do fomulário
      :   `version` - versão do formulário
      :   `order` - lista de ordenação (java.util.ArrayList)
      :   `page` - numero da pagina
      :   `pageSize` - numero de registros por pagina

      Returns:
      :   ResponseEnvelopeVO objeto com os dados do formulário

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
          Busca formulários
    - #### findCardIndex

      ```
      com.totvs.technology.foundation.sdk.service.vo.common.ResponseEnvelopeVO<CardIndexFindAPIVO> findCardIndex​(Integer documentId,
                                                                                                                 Integer version)
                                                                                                          throws Exception
      ```

      Parameters:
      :   `documentId` - numero do fomulário
      :   `version` - versão do formulário

      Returns:
      :   ResponseEnvelopeVO objeto com os dados do formulário

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
          Busca formulários
    - #### createCardIndex

      ```
      CardIndexAPIVO createCardIndex​(File filecontent,
                                     String mainFile,
                                     String formName,
                                     String descriptorField,
                                     String datasetName,
                                     Integer parentIdValue)
                              throws Exception
      ```

      Parameters:
      :   `filecontent` - Arquivo de conteúdo do formulário
      :   `mainFile` - Nome do arquivo principal
      :   `formName` - Descrição do Documento
      :   `descriptorField` - Descrição do Formulário
      :   `datasetName` - Nome do Dataset
      :   `parentIdValue` - Número do documento pai

      Returns:
      :   CardIndexAPIVO objeto com dados do formulário

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
          Cria formuários com base em arquivos html ou zip
    - #### createCardIndex

      ```
      CardIndexAPIVO createCardIndex​(File filecontent,
                                     String formName,
                                     Integer parentIdValue)
                              throws Exception
      ```

      Parameters:
      :   `filecontent` - Arquivo de conteúdo do formulário
      :   `formName` - Descrição do Documento
      :   `parentIdValue` - Número do documento pai

      Returns:
      :   CardIndexAPIVO objeto com dados do formulário

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
          Cria formuários com base em arquivos html ou zip
    - #### patchCardIndex

      ```
      CardIndexAPIVO patchCardIndex​(File filecontent,
                                    Integer documentIdValue,
                                    String updateMode,
                                    String mainFile,
                                    String formName,
                                    String descriptorField,
                                    String datasetName)
                             throws Exception
      ```

      Parameters:
      :   `filecontent` - Arquivo de conteúdo do formulário
      :   `documentIdValue` - Id do documento
      :   `updateMode` - Tipo de atualização 0 = Manter a versão atual e 2 = Nova versão
      :   `mainFile` - Nome do arquivo principal
      :   `formName` - Descrição do Documento
      :   `descriptorField` - Descrição do Formulário
      :   `datasetName` - Nome do Dataset

      Returns:
      :   CardIndexAPIVO objeto com dados do formulário

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
          Atualização parcial dos arquivos do formulário
    - #### putCardIndex

      ```
      CardIndexAPIVO putCardIndex​(File filecontent,
                                  Integer documentIdValue,
                                  String updateMode,
                                  String mainFile,
                                  String formName,
                                  String descriptorField,
                                  String datasetName)
                           throws Exception
      ```

      Parameters:
      :   `filecontent` - Arquivo de conteúdo do formulário
      :   `documentIdValue` - Id do documento
      :   `updateMode` - Tipo de atualização 0 = Manter a versão atual e 2 = Nova versão
      :   `mainFile` - Nome do arquivo principal
      :   `formName` - Descrição do Documento
      :   `descriptorField` - Descrição do Formulário
      :   `datasetName` - Nome do Dataset

      Returns:
      :   CardIndexAPIVO objeto com dados do formulário

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
          Atualiza completa dos arquivos do formulário
    - #### deleteCardIndex

      ```
      boolean deleteCardIndex​(Integer documentId)
                       throws Exception
      ```

      Parameters:
      :   `documentId` -

      Returns:
      :   Boolean true se a rotina executar com sucesso

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
          Manda um formulário para lixeira
