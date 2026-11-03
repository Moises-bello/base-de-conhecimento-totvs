---
content_hash: 7f05053e02cf1680b432ad610af14de388ccea162d9395ba821df1dccfde2e3f
fetched_at: '2026-11-03T14:35:06.489375+00:00'
page_id: com/fluig/sdk/service/CardAPIService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.CardAPIService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/CardAPIService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface CardAPIService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface CardAPIService
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
    | `CardFindFieldVO` | `create​(Integer documentId, List<CardFieldVO> cardFieldVOs)` | Cria um registro de Formulário |
    | `CardChildrenVO` | `createChild​(Integer cardId, List<CardFieldVO> cardFieldVos)` | Cria um registro no formulário filho |
    | `CardFindFieldVO` | `edit​(Integer cardId, List<CardFieldVO> cardFieldVOs)` | altera um registro de Formulário |
    | `CardChildrenVO` | `editChild​(Integer cardId, Integer row, List<CardFieldVO> cardFieldVOS)` | Cria um registro no formulário filho |
    | `com.totvs.technology.foundation.sdk.service.vo.common.ResponseEnvelopeVO<CardFindFieldVO>` | `find​(Integer documentId, Integer page, Integer pageSize, List order, List<String> fields, List<CardFieldFilterVO> cardFieldFilterVOS, Boolean listInactiveRecords)` | Lista os registros do formulário |
    | `CardFindFieldVO` | `findById​(Integer documentId, Integer cardId, List<String> fields, List<String> expandedFields)` | Lista os registros do formulário pelo numero do formulário e numero da ficha |
    | `CardChildrenVO` | `findChildByCardIdAndRow​(Integer cardId, Integer row, List<String> fields)` | Lista os registros do formulário filho pelo numero do registro e linha |
    | `com.totvs.technology.foundation.sdk.service.vo.common.ResponseEnvelopeVO<CardChildrenVO>` | `findChildrenByCardId​(Integer cardId, Integer page, Integer pageSize, List<String> fields)` | Lista os registros do formulário filho |
    | `Boolean` | `remove​(Integer cardId)` | Remove um registro de formulário |
    | `CardChildrenVO` | `removeChild​(Integer cardId, Integer row)` | Remove os registros do formulário filho |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CardAPIService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.CardAPIService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### find

      ```
      com.totvs.technology.foundation.sdk.service.vo.common.ResponseEnvelopeVO<CardFindFieldVO> find​(Integer documentId,
                                                                                                     Integer page,
                                                                                                     Integer pageSize,
                                                                                                     List order,
                                                                                                     List<String> fields,
                                                                                                     List<CardFieldFilterVO> cardFieldFilterVOS,
                                                                                                     Boolean listInactiveRecords)
                                                                                              throws Exception
      ```

      Lista os registros do formulário

      Parameters:
      :   `documentId` - numero do formulário (\* Obrigatório)
      :   `page` - numero da pagina
      :   `pageSize` - numero de registros por pagina
      :   `order` - lista de ordenação (java.util.ArrayList)
      :   `fields` - Campos dinâmicos
      :   `cardFieldFilterVOS` - filtro de campos de formulário
          Filtra por ODATA, consultas implementadas eq ne e or, use [] para identificar campos de formulário, exemplos:
          Para o campo igual ao valor: $filter=field eq ‘value’
          Para o campo que não é igual ao valor: $filter=field ne ‘value’
          Para dois filtros: $filter=field1 eq ‘value1’ and field2 eq ‘value2’
          Para ou operador: $filter=field1 eq ‘value1’ or field1 eq ‘value2’
          Entre o operador: $filter=field1 ge ‘value1’ and field1 le ‘value2’
          Para campos de opção: $filter=field[optionField] eq ‘value’
          Para pesquisas semelhantes: $filter=field eq ‘%value%’
          Regras para esta versão beta:
          Você não pode pesquisar apenas com o operador ge or le , DEVE ser usado between
          Você não pode pesquisar usando ne nas operações
          Você não pode usar nenhuma operação, apenas um operador referenciando o campo
      :   `listInactiveRecords` - Lista registros inativos

      Returns:
      :   ResponseEnvelopeVO objeto com os registros do fomulário

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
    - #### findById

      ```
      CardFindFieldVO findById​(Integer documentId,
                               Integer cardId,
                               List<String> fields,
                               List<String> expandedFields)
                        throws Exception
      ```

      Lista os registros do formulário pelo numero do formulário e numero da ficha

      Parameters:
      :   `documentId` - numero do formulário (\* Obrigatório)
      :   `cardId` - numero do registro do formulário (\* Obrigatório)
      :   `fields` - Campos dinâmicos
      :   `expandedFields` - Campos expansíveis (java.util.ArrayList) opção = children

      Returns:
      :   CardFindFieldVO objeto com os registros do fomulário

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
    - #### create

      ```
      CardFindFieldVO create​(Integer documentId,
                             List<CardFieldVO> cardFieldVOs)
                      throws Exception
      ```

      Cria um registro de Formulário

      Parameters:
      :   `documentId` - numero do formulário (\* Obrigatório)
      :   `cardFieldVOs` - (java.util.ArrayList) de objeto CardFieldVO que possui os campos :
          fieldId : String
          value : String

      Returns:
      :   CardFindFieldVO objeto com os registros do fomulário criado

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
    - #### edit

      ```
      CardFindFieldVO edit​(Integer cardId,
                           List<CardFieldVO> cardFieldVOs)
                    throws Exception
      ```

      altera um registro de Formulário

      Parameters:
      :   `cardId` - numero do registro do formulário (\* Obrigatório)
      :   `cardFieldVOs` - (java.util.ArrayList) de objeto CardFieldVO que possui os campos :
          fieldId : String
          value : String

      Returns:
      :   CardFindFieldVO objeto com o registros do fomulário editado

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
    - #### remove

      ```
      Boolean remove​(Integer cardId)
              throws Exception
      ```

      Remove um registro de formulário

      Parameters:
      :   `cardId` - numero do registro do formulário (\* Obrigatório)

      Returns:
      :   Boolean true se a rotina executar com sucesso

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
    - #### findChildrenByCardId

      ```
      com.totvs.technology.foundation.sdk.service.vo.common.ResponseEnvelopeVO<CardChildrenVO> findChildrenByCardId​(Integer cardId,
                                                                                                                    Integer page,
                                                                                                                    Integer pageSize,
                                                                                                                    List<String> fields)
                                                                                                             throws Exception
      ```

      Lista os registros do formulário filho

      Parameters:
      :   `cardId` - numero do registro do formulário (\* Obrigatório)
      :   `page` - numero da pagina
      :   `pageSize` - numero de registros por pagina
      :   `fields` - Campos dinâmicos

      Returns:

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
    - #### findChildByCardIdAndRow

      ```
      CardChildrenVO findChildByCardIdAndRow​(Integer cardId,
                                             Integer row,
                                             List<String> fields)
                                      throws Exception
      ```

      Lista os registros do formulário filho pelo numero do registro e linha

      Parameters:
      :   `cardId` - numero do registro do formulário (\* Obrigatório)
      :   `fields` - Campos dinâmicos
      :   `row` - linha do registro (\* Obrigatório)

      Returns:
      :   ResponseEnvelopeVO com os registros do fomulário

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
    - #### createChild

      ```
      CardChildrenVO createChild​(Integer cardId,
                                 List<CardFieldVO> cardFieldVos)
                          throws Exception
      ```

      Cria um registro no formulário filho

      Parameters:
      :   `cardId` - numero do registro do formulário (\* Obrigatório)
      :   `cardFieldVos` - (java.util.ArrayList) de objeto CardFieldVO que possui os campos :
          fieldId : String
          value : String

      Returns:
      :   CardChildrenVO com os registros do formulário

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
    - #### editChild

      ```
      CardChildrenVO editChild​(Integer cardId,
                               Integer row,
                               List<CardFieldVO> cardFieldVOS)
                        throws Exception
      ```

      Cria um registro no formulário filho

      Parameters:
      :   `cardId` - numero do registro do formulário (\* Obrigatório)
      :   `row` - linha do registro (\* Obrigatório)
      :   `cardFieldVOS` - (java.util.ArrayList) de objeto CardFieldVO que possui os campos :
          fieldId : String
          value : String

      Returns:
      :   CardChildrenVO com os registros do formulário

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
    - #### removeChild

      ```
      CardChildrenVO removeChild​(Integer cardId,
                                 Integer row)
                          throws Exception
      ```

      Remove os registros do formulário filho

      Parameters:
      :   `cardId` - numero do registro do formulário (\* Obrigatório)
      :   `row` - linha do registro (\* Obrigatório)

      Returns:
      :   CardChildrenVO com os registros do formulário

      Throws:
      :   `Exception`

      Since:
      :   1.6.5
