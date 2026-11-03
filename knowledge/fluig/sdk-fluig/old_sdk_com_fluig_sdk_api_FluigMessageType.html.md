---
content_hash: a5cfc9b564fc6774a4ee495589b98d14570872979d96a9c1232d758808ce486d
fetched_at: '2026-11-03T14:35:03.498464+00:00'
page_id: com/fluig/sdk/api/FluigMessageType
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.FluigMessageType (Enum)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/FluigMessageType.html
version: 1
---

Package [com.fluig.sdk.api](https://api.fluig.com/old/sdk/com/fluig/sdk/api/package-summary.html)

## Enum FluigMessageType

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + [java.lang.Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")<[FluigMessageType](https://api.fluig.com/old/sdk/com/fluig/sdk/api/FluigMessageType.html "enum in com.fluig.sdk.api")>
  + - com.fluig.sdk.api.FluigMessageType

* All Implemented Interfaces:
  :   `Serializable`, `Comparable<FluigMessageType>`

  ---

  ```
  public enum FluigMessageType
  extends Enum<FluigMessageType>
  ```

  Define os tipos de mensagens suportadas pelo sistema para comunicação com o cliente.

  Version:
  :   1.00.000

  Author:
  :   vanei

* + ### Enum Constant Summary

    Enum Constants

    | Enum Constant | Description |
    | `ERROR` | Erro. |
    | `INFO` | Informações gerais. |
    | `QUESTION` | Pergunta. |
    | `WARNING` | Aviso importante. |

  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `static FluigMessageType` | `valueOf​(String name)` | Returns the enum constant of this type with the specified name. |
    | `static FluigMessageType[]` | `values()` | Returns an array containing the constants of this enum type, in the order they are declared. |

    - ### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Enum.html?is-external=true "class or interface in java.lang")

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `getClass, notify, notifyAll, wait, wait, wait`

* + ### Enum Constant Detail

    - #### INFO

      ```
      public static final FluigMessageType INFO
      ```

      Informações gerais.
    - #### WARNING

      ```
      public static final FluigMessageType WARNING
      ```

      Aviso importante.
    - #### ERROR

      ```
      public static final FluigMessageType ERROR
      ```

      Erro.
    - #### QUESTION

      ```
      public static final FluigMessageType QUESTION
      ```

      Pergunta.

  + ### Method Detail

    - #### values

      ```
      public static FluigMessageType[] values()
      ```

      Returns an array containing the constants of this enum type, in
      the order they are declared. This method may be used to iterate
      over the constants as follows:

      ```
      for (FluigMessageType c : FluigMessageType.values())
          System.out.println(c);
      ```

      Returns:
      :   an array containing the constants of this enum type, in the order they are declared
    - #### valueOf

      ```
      public static FluigMessageType valueOf​(String name)
      ```

      Returns the enum constant of this type with the specified name.
      The string must match *exactly* an identifier used to declare an
      enum constant in this type. (Extraneous whitespace characters are
      not permitted.)

      Parameters:
      :   `name` - the name of the enum constant to be returned.

      Returns:
      :   the enum constant with the specified name

      Throws:
      :   `IllegalArgumentException` - if this enum type has no constant with the specified name
      :   `NullPointerException` - if the argument is null
