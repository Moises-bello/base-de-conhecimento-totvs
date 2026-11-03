---
content_hash: 6d5cad6dd2f02ebc67d9b1c52e93648383cb9bd9f9f6f35d288f364e2acc17df
fetched_at: '2026-07-02T19:24:21.385474+00:00'
page_id: '267780196'
product: protheus
source: tdn-tec
title: '#ifndef'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267780196
version: 2
---

INLINE

Compile a section of code if an identifier is undefined.

## Syntax

[#else]
#endif]]>

## Arguments

| Name | Description |
| --- | --- |
| <identifier> | <identifier> is the name of a definition whose existence is being verified. |

## Description

#ifndef...#endif lets you perform conditional compilation by identifying a section of source code to compile if the specified <identifier> is undefined.

The #else directive specifies the code to compile if <identifier> is defined. The #endif terminates the conditional compilation block.
