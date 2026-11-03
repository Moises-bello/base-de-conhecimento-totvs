---
content_hash: c6cf49ffee0046427a2e2a16da036013efe6ceab7b3472e8c1a522a93d2c62a2
fetched_at: '2026-11-03T14:35:03.905819+00:00'
page_id: com/fluig/sdk/api/document/AllocatedDocumentVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.document.AllocatedDocumentVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/document/AllocatedDocumentVO.html
version: 1
---

Package [com.fluig.sdk.api.document](https://api.fluig.com/old/sdk/com/fluig/sdk/api/document/package-summary.html)

## Class AllocatedDocumentVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.document.AllocatedDocumentVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class AllocatedDocumentVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.document.AllocatedDocumentVO)

* + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `AllocatedDocumentVO​(long companyId, int sourceDocument, int sourceVersion, int destinationDocument)` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `Boolean` | `getActive()` |  |
    | `Date` | `getCheckinDate()` |  |
    | `String` | `getCheckinTime()` |  |
    | `Boolean` | `getCheckoutAllowed()` |  |
    | `Date` | `getCheckoutDate()` |  |
    | `String` | `getCheckoutTime()` |  |
    | `String` | `getColleagueId()` |  |
    | `String` | `getColleagueName()` |  |
    | `String` | `getComment()` |  |
    | `long` | `getCompanyId()` |  |
    | `int` | `getDestinationDocument()` |  |
    | `int` | `getSourceDocument()` |  |
    | `int` | `getSourceVersion()` |  |
    | `void` | `setActive​(Boolean active)` |  |
    | `void` | `setCheckinDate​(Date checkinDate)` |  |
    | `void` | `setCheckinTime​(String checkinTime)` |  |
    | `void` | `setCheckoutAllowed​(Boolean checkoutAllowed)` |  |
    | `void` | `setCheckoutDate​(Date checkoutDate)` |  |
    | `void` | `setCheckoutTime​(String checkoutTime)` |  |
    | `void` | `setColleagueId​(String colleagueId)` |  |
    | `void` | `setColleagueName​(String colleagueName)` |  |
    | `void` | `setComment​(String comment)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Constructor Detail

    - #### AllocatedDocumentVO

      ```
      public AllocatedDocumentVO​(long companyId,
                                 int sourceDocument,
                                 int sourceVersion,
                                 int destinationDocument)
      ```

  + ### Method Detail

    - #### getCompanyId

      ```
      public long getCompanyId()
      ```
    - #### getSourceDocument

      ```
      public int getSourceDocument()
      ```
    - #### getSourceVersion

      ```
      public int getSourceVersion()
      ```
    - #### getDestinationDocument

      ```
      public int getDestinationDocument()
      ```
    - #### getColleagueId

      ```
      public String getColleagueId()
      ```
    - #### setColleagueId

      ```
      public void setColleagueId​(String colleagueId)
      ```
    - #### getCheckoutDate

      ```
      public Date getCheckoutDate()
      ```
    - #### setCheckoutDate

      ```
      public void setCheckoutDate​(Date checkoutDate)
      ```
    - #### getCheckoutTime

      ```
      public String getCheckoutTime()
      ```
    - #### setCheckoutTime

      ```
      public void setCheckoutTime​(String checkoutTime)
      ```
    - #### getCheckinDate

      ```
      public Date getCheckinDate()
      ```
    - #### setCheckinDate

      ```
      public void setCheckinDate​(Date checkinDate)
      ```
    - #### getCheckinTime

      ```
      public String getCheckinTime()
      ```
    - #### setCheckinTime

      ```
      public void setCheckinTime​(String checkinTime)
      ```
    - #### getComment

      ```
      public String getComment()
      ```
    - #### setComment

      ```
      public void setComment​(String comment)
      ```
    - #### getActive

      ```
      public Boolean getActive()
      ```
    - #### setActive

      ```
      public void setActive​(Boolean active)
      ```
    - #### getCheckoutAllowed

      ```
      public Boolean getCheckoutAllowed()
      ```
    - #### setCheckoutAllowed

      ```
      public void setCheckoutAllowed​(Boolean checkoutAllowed)
      ```
    - #### getColleagueName

      ```
      public String getColleagueName()
      ```
    - #### setColleagueName

      ```
      public void setColleagueName​(String colleagueName)
      ```
