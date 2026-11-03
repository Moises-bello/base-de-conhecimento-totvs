---
content_hash: d152efacee2c100fcaa2a6599e932658a427016d6a349439184f74a4e8249b43
fetched_at: '2026-11-03T14:35:03.865450+00:00'
page_id: com/fluig/sdk/api/cardindex/CardIndexFindAPIVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.cardindex.CardIndexFindAPIVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/cardindex/CardIndexFindAPIVO.html
version: 1
---

Package [com.fluig.sdk.api.cardindex](https://api.fluig.com/old/sdk/com/fluig/sdk/api/cardindex/package-summary.html)

## Class CardIndexFindAPIVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.cardindex.CardIndexFindAPIVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class CardIndexFindAPIVO
  extends Object
  implements Serializable
  ```

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.cardindex.CardIndexFindAPIVO)

* + ### Field Summary

    Fields

    | Modifier and Type | Field | Description |
    | `protected String` | `additionalComments` |  |
    | `protected List<AttachmentVO>` | `attachments` |  |
    | `protected String` | `cardDescription` |  |
    | `protected String` | `colleagueId` |  |
    | `protected Date` | `createDate` |  |
    | `protected long` | `createDateInMilliseconds` |  |
    | `protected String` | `documentDescription` |  |
    | `protected Integer` | `documentPropertyNumber` |  |
    | `protected Integer` | `documentPropertyVersion` |  |
    | `protected String` | `documentTypeId` |  |
    | `protected Date` | `lastModifiedDate` |  |
    | `protected Integer` | `parentDocumentId` |  |
    | `protected String` | `phisicalFile` |  |
    | `protected String` | `publisherId` |  |
    | `protected String` | `publisherName` |  |

  + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `CardIndexFindAPIVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `String` | `getAdditionalComments()` |  |
    | `List<AttachmentVO>` | `getAttachments()` |  |
    | `String` | `getCardDescription()` |  |
    | `String` | `getColleagueId()` |  |
    | `long` | `getCompanyId()` |  |
    | `Date` | `getCreateDate()` |  |
    | `long` | `getCreateDateInMilliseconds()` |  |
    | `String` | `getDatasetName()` |  |
    | `String` | `getDocumentDescription()` |  |
    | `Integer` | `getDocumentId()` |  |
    | `Integer` | `getDocumentPropertyNumber()` |  |
    | `Integer` | `getDocumentPropertyVersion()` |  |
    | `String` | `getDocumentTypeId()` |  |
    | `Date` | `getLastModifiedDate()` |  |
    | `Integer` | `getParentDocumentId()` |  |
    | `String` | `getPhisicalFile()` |  |
    | `Float` | `getPhisicalFileSize()` |  |
    | `String` | `getPublisherId()` |  |
    | `String` | `getPublisherName()` |  |
    | `int` | `getVersion()` |  |
    | `void` | `setAdditionalComments​(String additionalComments)` |  |
    | `void` | `setAttachments​(List<AttachmentVO> attachments)` |  |
    | `void` | `setCardDescription​(String cardDescription)` |  |
    | `void` | `setColleagueId​(String colleagueId)` |  |
    | `void` | `setCompanyId​(long companyId)` |  |
    | `void` | `setCreateDate​(Date createDate)` |  |
    | `void` | `setCreateDateInMilliseconds​(long createDateInMilliseconds)` |  |
    | `void` | `setDatasetName​(String datasetName)` |  |
    | `void` | `setDocumentDescription​(String documentDescription)` |  |
    | `void` | `setDocumentId​(Integer documentId)` |  |
    | `void` | `setDocumentPropertyNumber​(Integer documentPropertyNumber)` |  |
    | `void` | `setDocumentPropertyVersion​(Integer documentPropertyVersion)` |  |
    | `void` | `setDocumentTypeId​(String documentTypeId)` |  |
    | `void` | `setLastModifiedDate​(Date lastModifiedDate)` |  |
    | `void` | `setParentDocumentId​(Integer parentDocumentId)` |  |
    | `void` | `setPhisicalFile​(String phisicalFile)` |  |
    | `void` | `setPhisicalFileSize​(Float phisicalFileSize)` |  |
    | `void` | `setPublisherId​(String publisherId)` |  |
    | `void` | `setPublisherName​(String publisherName)` |  |
    | `void` | `setVersion​(int version)` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

* + ### Field Detail

    - #### documentTypeId

      ```
      protected String documentTypeId
      ```
    - #### colleagueId

      ```
      protected String colleagueId
      ```
    - #### documentDescription

      ```
      protected String documentDescription
      ```
    - #### additionalComments

      ```
      protected String additionalComments
      ```
    - #### phisicalFile

      ```
      protected String phisicalFile
      ```
    - #### createDate

      ```
      protected Date createDate
      ```
    - #### createDateInMilliseconds

      ```
      protected long createDateInMilliseconds
      ```
    - #### lastModifiedDate

      ```
      protected Date lastModifiedDate
      ```
    - #### parentDocumentId

      ```
      protected Integer parentDocumentId
      ```
    - #### publisherId

      ```
      protected String publisherId
      ```
    - #### publisherName

      ```
      protected String publisherName
      ```
    - #### cardDescription

      ```
      protected String cardDescription
      ```
    - #### documentPropertyNumber

      ```
      protected Integer documentPropertyNumber
      ```
    - #### documentPropertyVersion

      ```
      protected Integer documentPropertyVersion
      ```
    - #### attachments

      ```
      protected List<AttachmentVO> attachments
      ```

  + ### Constructor Detail

    - #### CardIndexFindAPIVO

      ```
      public CardIndexFindAPIVO()
      ```

  + ### Method Detail

    - #### getDocumentId

      ```
      public Integer getDocumentId()
      ```
    - #### setDocumentId

      ```
      public void setDocumentId​(Integer documentId)
      ```
    - #### getVersion

      ```
      public int getVersion()
      ```
    - #### setVersion

      ```
      public void setVersion​(int version)
      ```
    - #### getCompanyId

      ```
      public long getCompanyId()
      ```
    - #### setCompanyId

      ```
      public void setCompanyId​(long companyId)
      ```
    - #### getDocumentTypeId

      ```
      public String getDocumentTypeId()
      ```
    - #### setDocumentTypeId

      ```
      public void setDocumentTypeId​(String documentTypeId)
      ```
    - #### getColleagueId

      ```
      public String getColleagueId()
      ```
    - #### setColleagueId

      ```
      public void setColleagueId​(String colleagueId)
      ```
    - #### getDocumentDescription

      ```
      public String getDocumentDescription()
      ```
    - #### setDocumentDescription

      ```
      public void setDocumentDescription​(String documentDescription)
      ```
    - #### getAdditionalComments

      ```
      public String getAdditionalComments()
      ```
    - #### setAdditionalComments

      ```
      public void setAdditionalComments​(String additionalComments)
      ```
    - #### getPhisicalFile

      ```
      public String getPhisicalFile()
      ```
    - #### setPhisicalFile

      ```
      public void setPhisicalFile​(String phisicalFile)
      ```
    - #### getCreateDate

      ```
      public Date getCreateDate()
      ```
    - #### setCreateDate

      ```
      public void setCreateDate​(Date createDate)
      ```
    - #### getCreateDateInMilliseconds

      ```
      public long getCreateDateInMilliseconds()
      ```
    - #### setCreateDateInMilliseconds

      ```
      public void setCreateDateInMilliseconds​(long createDateInMilliseconds)
      ```
    - #### getLastModifiedDate

      ```
      public Date getLastModifiedDate()
      ```
    - #### setLastModifiedDate

      ```
      public void setLastModifiedDate​(Date lastModifiedDate)
      ```
    - #### getParentDocumentId

      ```
      public Integer getParentDocumentId()
      ```
    - #### setParentDocumentId

      ```
      public void setParentDocumentId​(Integer parentDocumentId)
      ```
    - #### getPublisherId

      ```
      public String getPublisherId()
      ```
    - #### setPublisherId

      ```
      public void setPublisherId​(String publisherId)
      ```
    - #### getPublisherName

      ```
      public String getPublisherName()
      ```
    - #### setPublisherName

      ```
      public void setPublisherName​(String publisherName)
      ```
    - #### getCardDescription

      ```
      public String getCardDescription()
      ```
    - #### setCardDescription

      ```
      public void setCardDescription​(String cardDescription)
      ```
    - #### getDocumentPropertyNumber

      ```
      public Integer getDocumentPropertyNumber()
      ```
    - #### setDocumentPropertyNumber

      ```
      public void setDocumentPropertyNumber​(Integer documentPropertyNumber)
      ```
    - #### getDocumentPropertyVersion

      ```
      public Integer getDocumentPropertyVersion()
      ```
    - #### setDocumentPropertyVersion

      ```
      public void setDocumentPropertyVersion​(Integer documentPropertyVersion)
      ```
    - #### getDatasetName

      ```
      public String getDatasetName()
      ```
    - #### setDatasetName

      ```
      public void setDatasetName​(String datasetName)
      ```
    - #### getPhisicalFileSize

      ```
      public Float getPhisicalFileSize()
      ```
    - #### setPhisicalFileSize

      ```
      public void setPhisicalFileSize​(Float phisicalFileSize)
      ```
    - #### getAttachments

      ```
      public List<AttachmentVO> getAttachments()
      ```
    - #### setAttachments

      ```
      public void setAttachments​(List<AttachmentVO> attachments)
      ```
