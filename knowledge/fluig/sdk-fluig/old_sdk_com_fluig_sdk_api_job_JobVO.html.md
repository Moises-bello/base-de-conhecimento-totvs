---
content_hash: 67fdbae9c40330c4f4eb74bfd8cb0f36351d3d1057fa6e88e223076196e13664
fetched_at: '2026-11-03T14:35:04.442783+00:00'
page_id: com/fluig/sdk/api/job/JobVO
product: fluig
source: sdk-fluig
title: Fluig SDK — com.fluig.sdk.api.job.JobVO (Class)
type: documentation
url: https://api.fluig.com/old/sdk/com/fluig/sdk/api/job/JobVO.html
version: 1
---

Package [com.fluig.sdk.api.job](https://api.fluig.com/old/sdk/com/fluig/sdk/api/job/package-summary.html)

## Class JobVO

* [java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")
* + com.fluig.sdk.api.job.JobVO

* All Implemented Interfaces:
  :   `Serializable`

  ---

  ```
  public class JobVO
  extends Object
  implements Serializable
  ```

  VO com informações utilizadas para criar Jobs

  Author:
  :   marcus.carvalho

  See Also:
  :   [Serialized Form](https://api.fluig.com/old/sdk/serialized-form.html#com.fluig.sdk.api.job.JobVO)

* + ### Nested Class Summary

    Nested Classes

    | Modifier and Type | Class | Description |
    | `static class` | `JobVO.IntervalType` |  |

  + ### Constructor Summary

    Constructors

    | Constructor | Description |
    | `JobVO()` |  |

  + ### Method Summary

    All Methods [Instance Methods](javascript:show(2);) [Concrete Methods](javascript:show(8);)

    | Modifier and Type | Method | Description |
    | `boolean` | `equals​(Object obj)` |  |
    | `long` | `getCompanyId()` |  |
    | `Map<String,​String>` | `getData()` |  |
    | `String` | `getDescription()` |  |
    | `int` | `getExecutionHour()` |  |
    | `int` | `getExecutionMinute()` |  |
    | `int` | `getInterval()` |  |
    | `String` | `getIntervalDescriptions()` |  |
    | `JobVO.IntervalType` | `getIntervalType()` |  |
    | `String` | `getJobId()` |  |
    | `int` | `getJobType()` |  |
    | `Date` | `getLastExecution()` |  |
    | `Date` | `getNextExecution()` |  |
    | `int` | `getOrdinalNumber()` |  |
    | `String` | `getRecurrenceExpression()` |  |
    | `long` | `getStartDateInMillis()` |  |
    | `Boolean` | `getStarted()` |  |
    | `int` | `getTarget()` |  |
    | `int` | `hashCode()` |  |
    | `void` | `setCompanyId​(long companyId)` |  |
    | `void` | `setData​(Map<String,​String> data)` |  |
    | `void` | `setDescription​(String description)` |  |
    | `void` | `setExecutionHour​(int executionHour)` |  |
    | `void` | `setExecutionMinute​(int executionMinute)` |  |
    | `void` | `setInterval​(int interval)` |  |
    | `void` | `setIntervalDescriptions​(String intervalDescriptions)` |  |
    | `void` | `setIntervalType​(JobVO.IntervalType intervalType)` |  |
    | `void` | `setJobId​(String jobId)` |  |
    | `void` | `setJobType​(int jobType)` |  |
    | `void` | `setLastExecution​(Date lastExecution)` |  |
    | `void` | `setNextExecution​(Date nextExecution)` |  |
    | `void` | `setOrdinalNumber​(int ordinalNumber)` |  |
    | `void` | `setRecurrenceExpression​(String recurrenceExpression)` |  |
    | `void` | `setStartDateInMillis​(long startDateInMillis)` |  |
    | `void` | `setStarted​(Boolean started)` |  |
    | `void` | `setTarget​(int target)` |  |
    | `String` | `toString()` |  |

    - ### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html?is-external=true "class or interface in java.lang")

      `clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

* + ### Constructor Detail

    - #### JobVO

      ```
      public JobVO()
      ```

  + ### Method Detail

    - #### getJobId

      ```
      public String getJobId()
      ```

      Returns:
      :   the jobId
    - #### setJobId

      ```
      public void setJobId​(String jobId)
      ```

      Parameters:
      :   `jobId` - the jobId to set
    - #### getCompanyId

      ```
      public long getCompanyId()
      ```

      Returns:
      :   the companyId
    - #### setCompanyId

      ```
      public void setCompanyId​(long companyId)
      ```

      Parameters:
      :   `companyId` - the companyId to set
    - #### getJobType

      ```
      public int getJobType()
      ```

      Returns:
      :   the jobType
    - #### setJobType

      ```
      public void setJobType​(int jobType)
      ```

      Parameters:
      :   `jobType` - the jobType to set
    - #### getDescription

      ```
      public String getDescription()
      ```

      Returns:
      :   the description
    - #### setDescription

      ```
      public void setDescription​(String description)
      ```

      Parameters:
      :   `description` - the description to set
    - #### getOrdinalNumber

      ```
      public int getOrdinalNumber()
      ```

      Returns:
      :   the ordinalNumber
    - #### setOrdinalNumber

      ```
      public void setOrdinalNumber​(int ordinalNumber)
      ```

      Parameters:
      :   `ordinalNumber` - the ordinalNumber to set
    - #### getExecutionHour

      ```
      public int getExecutionHour()
      ```

      Returns:
      :   the executionHour
    - #### getStartDateInMillis

      ```
      public long getStartDateInMillis()
      ```
    - #### setStartDateInMillis

      ```
      public void setStartDateInMillis​(long startDateInMillis)
      ```
    - #### setExecutionHour

      ```
      public void setExecutionHour​(int executionHour)
      ```

      Parameters:
      :   `executionHour` - the executionHour to set
    - #### getExecutionMinute

      ```
      public int getExecutionMinute()
      ```

      Returns:
      :   the executionMinute
    - #### setExecutionMinute

      ```
      public void setExecutionMinute​(int executionMinute)
      ```

      Parameters:
      :   `executionMinute` - the executionMinute to set
    - #### getData

      ```
      public Map<String,​String> getData()
      ```

      Returns:
      :   the data
    - #### setData

      ```
      public void setData​(Map<String,​String> data)
      ```

      Parameters:
      :   `data` - the data to set
    - #### getLastExecution

      ```
      public Date getLastExecution()
      ```

      Returns:
      :   the lastExecution
    - #### setLastExecution

      ```
      public void setLastExecution​(Date lastExecution)
      ```

      Parameters:
      :   `lastExecution` - the lastExecution to set
    - #### getNextExecution

      ```
      public Date getNextExecution()
      ```

      Returns:
      :   the nextExecution
    - #### setNextExecution

      ```
      public void setNextExecution​(Date nextExecution)
      ```

      Parameters:
      :   `nextExecution` - the nextExecution to set
    - #### getStarted

      ```
      public Boolean getStarted()
      ```

      Returns:
      :   the started
    - #### setStarted

      ```
      public void setStarted​(Boolean started)
      ```

      Parameters:
      :   `started` - the started to set
    - #### getRecurrenceExpression

      ```
      public String getRecurrenceExpression()
      ```

      Returns:
      :   the recurrenceExpression
    - #### setRecurrenceExpression

      ```
      public void setRecurrenceExpression​(String recurrenceExpression)
      ```

      Parameters:
      :   `recurrenceExpression` - the recurrenceExpression to set
    - #### getInterval

      ```
      public int getInterval()
      ```
    - #### setInterval

      ```
      public void setInterval​(int interval)
      ```
    - #### getTarget

      ```
      public int getTarget()
      ```
    - #### setTarget

      ```
      public void setTarget​(int target)
      ```
    - #### getIntervalType

      ```
      public JobVO.IntervalType getIntervalType()
      ```
    - #### setIntervalType

      ```
      public void setIntervalType​(JobVO.IntervalType intervalType)
      ```
    - #### toString

      ```
      public String toString()
      ```

      Overrides:
      :   `toString` in class `Object`
    - #### hashCode

      ```
      public int hashCode()
      ```

      Overrides:
      :   `hashCode` in class `Object`
    - #### equals

      ```
      public boolean equals​(Object obj)
      ```

      Overrides:
      :   `equals` in class `Object`
    - #### getIntervalDescriptions

      ```
      public String getIntervalDescriptions()
      ```
    - #### setIntervalDescriptions

      ```
      public void setIntervalDescriptions​(String intervalDescriptions)
      ```
