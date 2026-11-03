---
content_hash: 3d6e401c12a12b9e2816a8db80b7b21b7498fd6f79688a4a63aea755a152ca28
fetched_at: '2026-11-03T14:35:03.480119+00:00'
page_id: com/fluig/sdk/api/FluigMessage
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.FluigMessage (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/FluigMessage.html
version: 1
---

Package [com.fluig.sdk.api](https://api.fluig.com/old/sdk/com/fluig/sdk/api/package-summary.html)

## Class FluigMessage

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.FluigMessage

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class FluigMessage
  extends Object
  implements Serializable
  ```

  Mensagens a serem enviadas ao lado cliente.

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.FluigMessage)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `FluigMessage()` | Construtor default. |
    | `FluigMessage​(FluigMessageType type, String message)` | Construtor com o tipo e a mensagem. |
    | `FluigMessage​(FluigMessageType type, String message, String detail)` | Construtor com o tipo, a mensagem e uma descrição detalhada. |
    | `FluigMessage​(FluigMessageType type, String message, String detail, String errorCode)` | Construtor com o tipo, a mensagem e uma descrição detalhada. |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getDetail()` | Retorna a descrição detalhada da mensagem. |
    | `String` | `getErrorCode()` |  |
    | `String` | `getMessage()` | Retorna a mensagem. |
    | `FluigMessageType` | `getType()` | Retorna o tipo da mensagem. |
    | `void` | `setDetail​(String detail)` | Informa uma descrição detalhada para a mensagem. |
    | `void` | `setErrorCode​(String errorCode)` |  |
    | `void` | `setMessage​(String message)` | Altera a mensagem. |
    | `void` | `setType​(FluigMessageType type)` |  |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### FluigMessage

      ```
      public FluigMessage()
      ```

      Construtor default.
    - #### FluigMessage

      ```
      public FluigMessage​(FluigMessageType type,
                          String message)
      ```

      Construtor com o tipo e a mensagem. O detalhe será igual a mensagem.

      Parameters:
      :   `type` - Tipo.
      :   `message` - Mensagem.
    - #### FluigMessage

      ```
      public FluigMessage​(FluigMessageType type,
                          String message,
                          String detail)
      ```

      Construtor com o tipo, a mensagem e uma descrição detalhada.

      Parameters:
      :   `type` - Tipo da menagem.
      :   `message` - Mensagem.
      :   `detail` - Descrição detalhada da mensagem.
    - #### FluigMessage

      ```
      public FluigMessage​(FluigMessageType type,
                          String message,
                          String detail,
                          String errorCode)
      ```

      Construtor com o tipo, a mensagem e uma descrição detalhada.

      Parameters:
      :   `type` - Tipo da menagem.
      :   `message` - Mensagem.
      :   `detail` - Descrição detalhada da mensagem.
      :   `errorCode` - Nome da classe de exceção.

  + ### Method Detail

    - #### getMessage

      ```
      public String getMessage()
      ```

      Retorna a mensagem.

      Returns:
      :   Mensagem.
    - #### setMessage

      ```
      public void setMessage​(String message)
      ```

      Altera a mensagem.

      Parameters:
      :   `message` - Mensagem.
    - #### getType

      ```
      public FluigMessageType getType()
      ```

      Retorna o tipo da mensagem.

      Returns:
      :   Tipo da mensagem.
    - #### setType

      ```
      public void setType​(FluigMessageType type)
      ```
    - #### getErrorCode

      ```
      public String getErrorCode()
      ```
    - #### setErrorCode

      ```
      public void setErrorCode​(String errorCode)
      ```
    - #### getDetail

      ```
      public String getDetail()
      ```

      Retorna a descrição detalhada da mensagem.

      Returns:
      :   Descrição detalhada da mensagem.
    - #### setDetail

      ```
      public void setDetail​(String detail)
      ```

      Informa uma descrição detalhada para a mensagem.

      Parameters:
      :   `detail` - Detalhes da mensagem.
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
