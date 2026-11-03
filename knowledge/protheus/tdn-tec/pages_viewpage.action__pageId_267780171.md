---
content_hash: c45f1907d6c43486282e5bbab1b0d53ffd9373d66d8ab3e60506de9161907800
fetched_at: '2026-07-02T19:24:21.382568+00:00'
page_id: '267780171'
product: protheus
source: tdn-tec
title: '#ifdef'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267780171
version: 2
---

INLINE

Compile a section of code if an identifier is defined.

## Syntax

[#else]
#endif]]>

## Arguments

| Name | Description |
| --- | --- |
| <identifier> | <identifier> is the name of a definition whose existence is being verified. |

## Description

#ifdef...#endif lets you perform a conditional compilation. It does this by identifying a section of source code to be compiled if the specified <identifier> is defined.

The #else directive specifies the code to compile if <identifier> is undefined. The #endif terminates the conditional compilation block.
