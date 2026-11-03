---
content_hash: 73894137538ab2db224176384c46b6ac9fc3a1aa79519defc23ea044814c9375
fetched_at: '2026-11-03T14:35:06.289722+00:00'
page_id: com/fluig/sdk/filter/FilterVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.filter.FilterVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/filter/FilterVO.html
version: 1
---

Package [com.fluig.sdk.filter](https://api.fluig.com/old/sdk/com/fluig/sdk/filter/package-summary.html)

## Class FilterVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.filter.FilterVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class FilterVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.filter.FilterVO)

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `String` | `processId` |  |

  + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `FilterVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `List<FilterFieldVO>` | `getFields()` |  |
    | `FilterOrderVO` | `getFilterOrder()` |  |
    | `Long` | `getId()` |  |
    | `boolean` | `getIsPublic()` |  |
    | `String` | `getName()` |  |
    | `String` | `getProcessId()` |  |
    | `String` | `getType()` |  |
    | `void` | `setFields​(List<FilterFieldVO> fields)` |  |
    | `void` | `setFilterOrder​(FilterOrderVO filterOrder)` |  |
    | `void` | `setId​(Long id)` |  |
    | `void` | `setIsPublic​(boolean isPublic)` |  |
    | `void` | `setName​(String name)` |  |
    | `void` | `setProcessId​(String processId)` |  |
    | `void` | `setType​(String type)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### processId

      ```
      public String processId
      ```

  + ### Constructor Detail

    - #### FilterVO

      ```
      public FilterVO()
      ```

  + ### Method Detail

    - #### getId

      ```
      public Long getId()
      ```
    - #### setId

      ```
      public void setId​(Long id)
      ```
    - #### getName

      ```
      public String getName()
      ```
    - #### setName

      ```
      public void setName​(String name)
      ```
    - #### getType

      ```
      public String getType()
      ```
    - #### setType

      ```
      public void setType​(String type)
      ```
    - #### getProcessId

      ```
      public String getProcessId()
      ```
    - #### setProcessId

      ```
      public void setProcessId​(String processId)
      ```
    - #### getIsPublic

      ```
      public boolean getIsPublic()
      ```
    - #### setIsPublic

      ```
      public void setIsPublic​(boolean isPublic)
      ```
    - #### getFields

      ```
      public List<FilterFieldVO> getFields()
      ```
    - #### setFields

      ```
      public void setFields​(List<FilterFieldVO> fields)
      ```
    - #### getFilterOrder

      ```
      public FilterOrderVO getFilterOrder()
      ```
    - #### setFilterOrder

      ```
      public void setFilterOrder​(FilterOrderVO filterOrder)
      ```
