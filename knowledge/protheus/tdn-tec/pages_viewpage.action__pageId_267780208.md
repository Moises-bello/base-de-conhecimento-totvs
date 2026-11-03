---
content_hash: ba8bb07adab44fb52e2171488db8f4331c3dcefd3af90850c7d2c52a7302855f
fetched_at: '2026-07-02T19:24:21.388872+00:00'
page_id: '267780208'
product: protheus
source: tdn-tec
title: '#include'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267780208
version: 2
---

INLINE

Include a file into the current source file.

## Syntax

]]>

## Arguments

| Name | Description |
| --- | --- |
| <headerFileSpec> | <headerFileSpec> specifies the name of another source file to include in the current source file.  The preprocessor searches the following places: \* Source file directory \* Directories specified in the INCLUDE variable (project) |

## Description

#include inserts the contents of the specified file in place of the #include directive in the source file. By convention, the file inserted is referred to as a header file. Header files should contain only preprocessor directives and external declarations. By convention header files have a ".ch" extension.

When deciding where to locate your header files, you have two basic choices. You can place them in the source file directory where they are local to the current system; or, you can make them globally available by placing them in the directory specified in the INCLUDE variable. A list of one or more directories can be specified.

Header files overcome the one major drawback of defining constants or inline functions --the #define directive only affects the file in which it is contained. This means that every program which needs access to these statements must have a list of directives at the top. The solution to this problem is to place #define statements in a separate file and use the #include directive to tell the preprocessor to include that file before compiling.

For example, suppose the file "inKey.ch" contains a list of #define directives assigning key values to constants. Instead of including these directives at the top of each program file (.prw) requiring access to them, you can simply place the following line at the top of each program file:

This causes the preprocessor to look for inKey.ch and place all the directives contained within it at the top of this program.

Another advantage of using the #include directive is that all the #define statements are contained in one file. If any modifications to these statements are necessary, only the #include file need be altered, the program itself remains untouched.
