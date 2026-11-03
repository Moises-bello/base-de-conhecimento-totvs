---
content_hash: f3a3918b398a13c845d480be8e469ffca4978923a89cbc651bc75a1f7216900d
fetched_at: '2026-11-03T14:35:04.530126+00:00'
page_id: com/fluig/sdk/api/log/ScriptingLog
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.log.ScriptingLog (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/log/ScriptingLog.html
version: 1
---

Package [com.fluig.sdk.api.log](https://api.fluig.com/old/sdk/com/fluig/sdk/api/log/package-summary.html)

## Class ScriptingLog

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.log.ScriptingLog

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class ScriptingLog
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.log.ScriptingLog)

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `protected static org.slf4j.Logger` | `log` |  |
    | `static int` | `truncateLength` |  |

  + ### Method Summary

    All Methods [Static Methods](javascript:show(1);) [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `void` | `debug​(Object... messages)` |  |
    | `void` | `dir​(Object... objs)` |  |
    | `void` | `error​(Object... messages)` |  |
    | `void` | `fatal​(Object... messages)` |  |
    | `static ScriptingLog` | `getInstance()` |  |
    | `void` | `info​(Object... messages)` |  |
    | `boolean` | `isDebugEnabled()` |  |
    | `boolean` | `isErrorEnabled()` |  |
    | `boolean` | `isFatalEnabled()` |  |
    | `boolean` | `isInfoEnabled()` |  |
    | `boolean` | `isTraceEnabled()` |  |
    | `boolean` | `isWarnEnabled()` |  |
    | `void` | `log​(Object... messages)` |  |
    | `void` | `trace​(Object... messages)` |  |
    | `void` | `warn​(Object... messages)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### log

      ```
      protected static org.slf4j.Logger log
      ```
    - #### truncateLength

      ```
      public static final int truncateLength
      ```

  + ### Method Detail

    - #### getInstance

      ```
      public static ScriptingLog getInstance()
      ```
    - #### isTraceEnabled

      ```
      public boolean isTraceEnabled()
      ```
    - #### trace

      ```
      public void trace​(Object... messages)
      ```
    - #### isDebugEnabled

      ```
      public boolean isDebugEnabled()
      ```
    - #### debug

      ```
      public void debug​(Object... messages)
      ```
    - #### isInfoEnabled

      ```
      public boolean isInfoEnabled()
      ```
    - #### info

      ```
      public void info​(Object... messages)
      ```
    - #### log

      ```
      public void log​(Object... messages)
      ```
    - #### isWarnEnabled

      ```
      public boolean isWarnEnabled()
      ```
    - #### warn

      ```
      public void warn​(Object... messages)
      ```
    - #### isErrorEnabled

      ```
      public boolean isErrorEnabled()
      ```
    - #### error

      ```
      public void error​(Object... messages)
      ```
    - #### isFatalEnabled

      ```
      public boolean isFatalEnabled()
      ```
    - #### fatal

      ```
      public void fatal​(Object... messages)
      ```
    - #### dir

      ```
      public void dir​(Object... objs)
      ```
