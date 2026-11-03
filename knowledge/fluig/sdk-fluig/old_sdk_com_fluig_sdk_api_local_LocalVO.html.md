---
content_hash: 1965ad3a946bba8cb75f64c9e6460f999c79321ad64bf63451b9bd056d0b21b2
fetched_at: '2026-11-03T14:35:04.510531+00:00'
page_id: com/fluig/sdk/api/local/LocalVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.local.LocalVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/local/LocalVO.html
version: 1
---

Package [com.fluig.sdk.api.local](https://api.fluig.com/old/sdk/com/fluig/sdk/api/local/package-summary.html)

## Class LocalVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.local.LocalVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class LocalVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.local.LocalVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `LocalVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `boolean` | `equals​(Object o)` |  |
    | `List<String>` | `getExpandables()` |  |
    | `List<HolidayVO>` | `getHolidays()` |  |
    | `Long` | `getId()` |  |
    | `double` | `getLatitude()` |  |
    | `List<LocalUserVO>` | `getLocalUsers()` |  |
    | `double` | `getLongitude()` |  |
    | `String` | `getName()` |  |
    | `double` | `getRadius()` |  |
    | `String` | `getTimezone()` |  |
    | `int` | `hashCode()` |  |
    | `boolean` | `isDefaultLocale()` |  |
    | `void` | `setDefaultLocale​(boolean defaultLocale)` |  |
    | `void` | `setExpandables​(List<String> expandables)` |  |
    | `void` | `setHolidays​(List<HolidayVO> holidays)` |  |
    | `void` | `setId​(Long id)` |  |
    | `void` | `setLatitude​(double latitude)` |  |
    | `void` | `setLocalUsers​(List<LocalUserVO> localUsers)` |  |
    | `void` | `setLongitude​(double longitude)` |  |
    | `void` | `setName​(String name)` |  |
    | `void` | `setRadius​(double radius)` |  |
    | `void` | `setTimezone​(String timezone)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### LocalVO

      ```
      public LocalVO()
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
    - #### getTimezone

      ```
      public String getTimezone()
      ```
    - #### setTimezone

      ```
      public void setTimezone​(String timezone)
      ```
    - #### getLatitude

      ```
      public double getLatitude()
      ```
    - #### setLatitude

      ```
      public void setLatitude​(double latitude)
      ```
    - #### getLongitude

      ```
      public double getLongitude()
      ```
    - #### setLongitude

      ```
      public void setLongitude​(double longitude)
      ```
    - #### getRadius

      ```
      public double getRadius()
      ```
    - #### setRadius

      ```
      public void setRadius​(double radius)
      ```
    - #### isDefaultLocale

      ```
      public boolean isDefaultLocale()
      ```
    - #### setDefaultLocale

      ```
      public void setDefaultLocale​(boolean defaultLocale)
      ```
    - #### getLocalUsers

      ```
      public List<LocalUserVO> getLocalUsers()
      ```
    - #### setLocalUsers

      ```
      public void setLocalUsers​(List<LocalUserVO> localUsers)
      ```
    - #### equals

      ```
      public boolean equals​(Object o)
      ```

      Overrides:
      :   `equals` in class `Object`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Overrides:
      :   `hashCode` in class `Object`
    - #### getExpandables

      ```
      public List<String> getExpandables()
      ```
    - #### setExpandables

      ```
      public void setExpandables​(List<String> expandables)
      ```
    - #### getHolidays

      ```
      public List<HolidayVO> getHolidays()
      ```
    - #### setHolidays

      ```
      public void setHolidays​(List<HolidayVO> holidays)
      ```
