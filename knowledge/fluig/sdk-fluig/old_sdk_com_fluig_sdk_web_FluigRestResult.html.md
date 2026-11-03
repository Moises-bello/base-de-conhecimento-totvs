---
content_hash: 4553bd838cb69e200b284cdb07e4fad75b280546d24c0a043118bfe19d1b8b5e
fetched_at: '2026-11-03T14:35:07.492609+00:00'
page_id: com/fluig/sdk/web/FluigRestResult
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.web.FluigRestResult (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/web/FluigRestResult.html
version: 1
---

Package [com.fluig.sdk.web](https://api.fluig.com/old/sdk/com/fluig/sdk/web/package-summary.html)

## Class FluigRestResult

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.web.FluigRestResult

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class FluigRestResult
  extends Object
  implements Serializable
  ```

  Classe para ser usada como padrão para o retorno dos REST.

  Version:
  :   1.00.000

  Author:
  :   vanei

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.web.FluigRestResult)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `FluigRestResult()` |  |
    | `FluigRestResult​(FluigMessage message)` | Nova instancia do FluigRestResult de acordo com o message |
    | `FluigRestResult​(Object content)` | Nova instancia do FluigRestResult de acordo com o content |
    | `FluigRestResult​(Object content, FluigMessage message)` | Nova instancia do FluigRestResult de acordo com o content e message |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `Object` | `getContent()` | Recupera valor do content |
    | `FluigMessage` | `getMessage()` | Recupera valor do message |
    | `void` | `setContent​(Object content)` | Atribui valor para content |
    | `void` | `setMessage​(FluigMessage message)` | Atribui valor para message |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### FluigRestResult

      ```
      public FluigRestResult()
      ```
    - #### FluigRestResult

      ```
      public FluigRestResult​(Object content)
      ```

      Nova instancia do FluigRestResult de acordo com o content

      Parameters:
      :   `content` -
    - #### FluigRestResult

      ```
      public FluigRestResult​(Object content,
                             FluigMessage message)
      ```

      Nova instancia do FluigRestResult de acordo com o content e message

      Parameters:
      :   `content` -
      :   `message` -
    - #### FluigRestResult

      ```
      public FluigRestResult​(FluigMessage message)
      ```

      Nova instancia do FluigRestResult de acordo com o message

      Parameters:
      :   `message` -

  + ### Method Detail

    - #### getContent

      ```
      public Object getContent()
      ```

      Recupera valor do content

      Returns:
      :   the content
    - #### setContent

      ```
      public void setContent​(Object content)
      ```

      Atribui valor para content

      Parameters:
      :   `content` - the content to set
    - #### getMessage

      ```
      public FluigMessage getMessage()
      ```

      Recupera valor do message

      Returns:
      :   the message
    - #### setMessage

      ```
      public void setMessage​(FluigMessage message)
      ```

      Atribui valor para message

      Parameters:
      :   `message` - the message to set
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
