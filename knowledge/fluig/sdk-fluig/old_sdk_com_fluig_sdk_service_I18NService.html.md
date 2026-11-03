---
content_hash: 569ef64a9babbcae252829a2c7f18c24ee2c09a78a5a7b1c14e336c66f8262df
fetched_at: '2026-11-03T14:35:06.760921+00:00'
page_id: com/fluig/sdk/service/I18NService
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.service.I18NService (Interface)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/service/I18NService.html
version: 1
---

Package [com.fluig.sdk.service](https://api.fluig.com/old/sdk/com/fluig/sdk/service/package-summary.html)

## Interface I18NService

* All Superinterfaces:
  :   `BaseAPIService`

  ---

  ```
  public interface I18NService
  extends BaseAPIService
  ```

  Fornece acesso aos serviços de internacioinalização.

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
    | `void` | `addResourceBundle​(Locale locale, String code, Properties props)` | Registra um ResourceBundle para um determinado componente. |
    | `String` | `transalateString​(String message, Object[] params)` | Retorna a tradução de uma String padrão do Fluig. |
    | `String` | `transalateString​(String code, String message, Object[] params)` | Retorna a tradução de uma String associada a um Bundle específico. |
    | `String[]` | `translateException​(Throwable ex)` | Retorna a tradução de uma exception. |

    - ### Methods inherited from interface com.fluig.sdk.service.[BaseAPIService](https://api.fluig.com/old/sdk/com/fluig/sdk/service/BaseAPIService.html "interface in com.fluig.sdk.service")

      `expand, generateOrderParam`

* + ### Field Detail

    - #### JNDI\_NAME

      ```
      static final String JNDI_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.I18NService.JNDI_NAME)
    - #### JNDI\_REMOTE\_NAME

      ```
      static final String JNDI_REMOTE_NAME
      ```

      See Also:
      :   [Constant Field Values](https://api.fluig.com/old/sdk/constant-values.html#com.fluig.sdk.service.I18NService.JNDI_REMOTE_NAME)

  + ### Method Detail

    - #### transalateString

      ```
      String transalateString​(String message,
                              Object[] params)
                       throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna a tradução de uma String padrão do Fluig.

      Parameters:
      :   `message` - String a ser traduzida.
      :   `params` - Valores a serem substituídos na String. **null** se não
          houver parâmetros.

      Returns:
      :   String traduzida ou a própria string original, se não encontrar a
          tradução.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### transalateString

      ```
      String transalateString​(String code,
                              String message,
                              Object[] params)
                       throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna a tradução de uma String associada a um Bundle específico.

      Parameters:
      :   `code` - Código do resource bundle onde procurar a tradução.
      :   `message` - String a ser traduzida.
      :   `params` - Valores a serem substituídos na String. **null** se não
          houver parâmetros.

      Returns:
      :   String traduzida ou a própria string original, se não encontrar a
          tradução.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### translateException

      ```
      String[] translateException​(Throwable ex)
                           throws com.fluig.sdk.api.common.SDKException
      ```

      Retorna a tradução de uma exception.

      Parameters:
      :   `ex` - Exception a ser traduzida.
      :   `params` - Valores a serem substituídos na String. **null** se não
          houver parâmetros.

      Returns:
      :   Array de duas dimensões, onde no índice **0** está a tradução
          da exception e no índice **1** está uma descrição mais
          detalhada da mensagem.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
    - #### addResourceBundle

      ```
      void addResourceBundle​(Locale locale,
                             String code,
                             Properties props)
                      throws com.fluig.sdk.api.common.SDKException
      ```

      Registra um ResourceBundle para um determinado componente.

      Parameters:
      :   `locale` - Idioma.
      :   `code` - Código do componente ao qual o ResourceBundle pertence.
      :   `props` - Conjunto de strings internacionalizadas.

      Throws:
      :   `com.fluig.sdk.api.common.SDKException`
