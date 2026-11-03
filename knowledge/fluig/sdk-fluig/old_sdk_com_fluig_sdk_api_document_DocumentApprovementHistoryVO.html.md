---
content_hash: eaa885ea2dadb6f857e96af7d9dd8515df9ff1176bb9aa63ce7ce03195e46afd
fetched_at: '2026-11-03T14:35:03.925529+00:00'
page_id: com/fluig/sdk/api/document/DocumentApprovementHistoryVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.document.DocumentApprovementHistoryVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/document/DocumentApprovementHistoryVO.html
version: 1
---

Package [com.fluig.sdk.api.document](https://api.fluig.com/old/sdk/com/fluig/sdk/api/document/package-summary.html)

## Class DocumentApprovementHistoryVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.document.DocumentApprovementHistoryVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class DocumentApprovementHistoryVO
  extends Object
  implements Serializable
  ```

  VO Utilizado pelo ws para mostrar o historico de aprovacoes do documento

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.document.DocumentApprovementHistoryVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `DocumentApprovementHistoryVO()` |  |
    | `DocumentApprovementHistoryVO​(int documentVersion, int iterationSequence, int levelId, int movementSequence, String colleagueId, Date approvementDate, int status, String observation, boolean signed, String colleagueName)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `Date` | `getApprovementDate()` |  |
    | `String` | `getColleagueId()` |  |
    | `String` | `getColleagueName()` |  |
    | `int` | `getDocumentVersion()` |  |
    | `int` | `getIterationSequence()` |  |
    | `int` | `getLevelId()` |  |
    | `int` | `getMovementSequence()` |  |
    | `String` | `getObservation()` |  |
    | `int` | `getStatus()` |  |
    | `boolean` | `isSigned()` |  |
    | `void` | `setApprovementDate​(Date approvementDate)` |  |
    | `void` | `setColleagueId​(String colleagueId)` |  |
    | `void` | `setColleagueName​(String colleagueName)` |  |
    | `void` | `setDocumentVersion​(int documentVersion)` |  |
    | `void` | `setIterationSequence​(int iterationSequence)` |  |
    | `void` | `setLevelId​(int levelId)` |  |
    | `void` | `setMovementSequence​(int movementSequence)` |  |
    | `void` | `setObservation​(String observation)` |  |
    | `void` | `setSigned​(boolean signed)` |  |
    | `void` | `setStatus​(int status)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### DocumentApprovementHistoryVO

      ```
      public DocumentApprovementHistoryVO()
      ```
    - #### DocumentApprovementHistoryVO

      ```
      public DocumentApprovementHistoryVO​(int documentVersion,
                                          int iterationSequence,
                                          int levelId,
                                          int movementSequence,
                                          String colleagueId,
                                          Date approvementDate,
                                          int status,
                                          String observation,
                                          boolean signed,
                                          String colleagueName)
      ```

  + ### Method Detail

    - #### getDocumentVersion

      ```
      public int getDocumentVersion()
      ```
    - #### setDocumentVersion

      ```
      public void setDocumentVersion​(int documentVersion)
      ```
    - #### getIterationSequence

      ```
      public int getIterationSequence()
      ```
    - #### setIterationSequence

      ```
      public void setIterationSequence​(int iterationSequence)
      ```
    - #### getLevelId

      ```
      public int getLevelId()
      ```
    - #### setLevelId

      ```
      public void setLevelId​(int levelId)
      ```
    - #### getMovementSequence

      ```
      public int getMovementSequence()
      ```
    - #### setMovementSequence

      ```
      public void setMovementSequence​(int movementSequence)
      ```
    - #### getColleagueId

      ```
      public String getColleagueId()
      ```
    - #### setColleagueId

      ```
      public void setColleagueId​(String colleagueId)
      ```
    - #### getApprovementDate

      ```
      public Date getApprovementDate()
      ```
    - #### setApprovementDate

      ```
      public void setApprovementDate​(Date approvementDate)
      ```
    - #### getStatus

      ```
      public int getStatus()
      ```
    - #### setStatus

      ```
      public void setStatus​(int status)
      ```
    - #### getObservation

      ```
      public String getObservation()
      ```
    - #### setObservation

      ```
      public void setObservation​(String observation)
      ```
    - #### isSigned

      ```
      public boolean isSigned()
      ```
    - #### setSigned

      ```
      public void setSigned​(boolean signed)
      ```
    - #### getColleagueName

      ```
      public String getColleagueName()
      ```
    - #### setColleagueName

      ```
      public void setColleagueName​(String colleagueName)
      ```
