---
content_hash: 852b79fa304c002adfcb6f7db5276e7d4694486ea985ad5111fd600c0c2a7f43
fetched_at: '2026-11-03T14:35:07.466660+00:00'
page_id: com/fluig/sdk/web/FluigRest
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.web.FluigRest (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/web/FluigRest.html
version: 1
---

Package [com.fluig.sdk.web](https://api.fluig.com/old/sdk/com/fluig/sdk/web/package-summary.html)

## Class FluigRest

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.web.FluigRest

* ---

  ```
  public abstract class FluigRest
  extends Object
  ```

  Super classe para suporte aos serviços rest

  Version:
  :   1.00.000

  Author:
  :   vanei

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `FluigRest()` | Nova instância para FluigRest.java |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `protected javax.ws.rs.core.Response` | `buildErrorResponse​(Throwable throwable)` | Tratamento e criaçao de mensagem de erro para ao lado cliente |
    | `protected javax.ws.rs.core.Response` | `buildErrorResponse​(Throwable throwable, Object[] params)` | Tratamento e criaçao de mensagem de erro com parâmetros de retorno do serviço para ao lado cliente |
    | `javax.ws.rs.core.Response` | `buildErrorResponseTranslated​(String translatedMessage)` | Build an error response with an already translated message |
    | `protected javax.ws.rs.core.Response` | `buildSuccessMessageResponse​(String code, String messageKey, Object[] params)` | Tratamento e criaçao de mensagem de sucesso com código e lista de parâmetros para ao lado cliente |
    | `protected javax.ws.rs.core.Response` | `buildSuccessResponse()` | Tratamento e criaçao de mensagem de sucesso para ao lado cliente |
    | `protected javax.ws.rs.core.Response` | `buildSuccessResponse​(FluigRestResult result)` | Tratamento e criaçao de mensagem de sucesso com retorno do serviço para ao lado cliente |
    | `protected javax.ws.rs.core.Response` | `buildSuccessResponse​(Object result)` | Tratamento e criaçao de mensagem de sucesso com retorno do serviço para ao lado cliente |
    | `javax.ws.rs.core.Response` | `buildSuccessResponseTranslated​(String translatedMessage)` |  |
    | `protected void` | `copyValues​(Object from, Object to)` | Cópia de atributos da camada de serviços rest para objetos internos do componente SDK |
    | `protected boolean` | `hasMobileAnnotation​(Object content)` | Verifica se tem a anotação de Mobile. |
    | `protected boolean` | `isMobileRequest()` | Verifica se é uma requisição mobile |
    | `protected Map<String,​Object>` | `jsonToMap​(String json)` | Converão de objeto json para Mapa |
    | `protected <T> T` | `jsonToObject​(String json, Class<T> clazz)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### FluigRest

      ```
      public FluigRest()
      ```

      Nova instância para FluigRest.java

  + ### Method Detail

    - #### buildSuccessResponse

      ```
      protected javax.ws.rs.core.Response buildSuccessResponse()
      ```

      Tratamento e criaçao de mensagem de sucesso para ao lado cliente

      Returns:
      :   Json response
    - #### buildSuccessResponse

      ```
      protected javax.ws.rs.core.Response buildSuccessResponse​(Object result)
      ```

      Tratamento e criaçao de mensagem de sucesso com retorno do serviço para ao lado cliente

      Parameters:
      :   `result` -

      Returns:
      :   Json Response
    - #### buildSuccessMessageResponse

      ```
      protected javax.ws.rs.core.Response buildSuccessMessageResponse​(String code,
                                                                      String messageKey,
                                                                      Object[] params)
      ```

      Tratamento e criaçao de mensagem de sucesso com código e lista de parâmetros para ao lado cliente

      Parameters:
      :   `code` -
      :   `messageKey` -
      :   `params` -

      Returns:
      :   Json Response
    - #### buildSuccessResponse

      ```
      protected javax.ws.rs.core.Response buildSuccessResponse​(FluigRestResult result)
      ```

      Tratamento e criaçao de mensagem de sucesso com retorno do serviço para ao lado cliente

      Parameters:
      :   `result` -

      Returns:
      :   Json Response
    - #### buildErrorResponse

      ```
      protected javax.ws.rs.core.Response buildErrorResponse​(Throwable throwable)
      ```

      Tratamento e criaçao de mensagem de erro para ao lado cliente

      Parameters:
      :   `throwable` -

      Returns:
      :   JsonResponse
    - #### buildErrorResponse

      ```
      protected javax.ws.rs.core.Response buildErrorResponse​(Throwable throwable,
                                                             Object[] params)
      ```

      Tratamento e criaçao de mensagem de erro com parâmetros de retorno do serviço para ao lado cliente

      Parameters:
      :   `throwable` -
      :   `params` -

      Returns:
      :   Json Response
    - #### buildErrorResponseTranslated

      ```
      public javax.ws.rs.core.Response buildErrorResponseTranslated​(String translatedMessage)
      ```

      Build an error response with an already translated message

      Parameters:
      :   `translatedMessage` -

      Returns:
      :   Response
    - #### jsonToObject

      ```
      protected <T> T jsonToObject​(String json,
                                   Class<T> clazz)
      ```

      Parameters:
      :   `json` - - Objeto no formato json String
      :   `clazz` - - classe que será convertida

      Returns:
      :   T - Objeto de acordo com a classe passada ou null, caso haja
          falha na conversão
    - #### jsonToMap

      ```
      protected Map<String,​Object> jsonToMap​(String json)
      ```

      Converão de objeto json para Mapa

      Parameters:
      :   `json` -

      Returns:
      :   Map
    - #### copyValues

      ```
      protected void copyValues​(Object from,
                                Object to)
      ```

      Cópia de atributos da camada de serviços rest para objetos internos
      do componente SDK

      Parameters:
      :   `from` -
      :   `to` -
    - #### isMobileRequest

      ```
      protected boolean isMobileRequest()
      ```

      Verifica se é uma requisição mobile

      Returns:
    - #### hasMobileAnnotation

      ```
      protected boolean hasMobileAnnotation​(Object content)
      ```

      Verifica se tem a anotação de Mobile.

      Parameters:
      :   `content` -

      Returns:
    - #### buildSuccessResponseTranslated

      ```
      public javax.ws.rs.core.Response buildSuccessResponseTranslated​(String translatedMessage)
      ```
