---
content_hash: 1c8940bad880ef9b55bb870c50a5da41c0b524ad8676ca44478716e7ac1504c0
fetched_at: '2026-06-29T00:12:15.272277+00:00'
page_id: '975767973'
product: rm
source: tdn-rm
title: Grupo W03 – Total da NF-e - IBS / CBS / IS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=975767973
version: 12
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Grupo W03 – Total da NF-e - IBS / CBS / IS** | | | | |
| **Campo** | **Ele** | **Pai** | **Ocorrência** | **Campo de Origem** |
| **ISTot** | **G** | **W01** | **0-1** |  |
| vIS | E | W31 | 1-1 |  |
| **IBSCBSTot** | **G** | **W01** | **0-1** |  |
| vBCIBSCBS | E | W34 | 1-1 | Valor total da BC do IBS e da CBS |
| **gIBS** | **G** | **W34** | **0-1** |  |
| **gIBSUF** | **G** | **W36** | **1-1** |  |
| vDif | E | W37 | 1-1 |  |
| vDevTrib | E | W37 | 1-1 |  |
| vIBSUF | E | W37 | 1-1 | Totalizador dos valores TTRBITMMOV.VALOR para tributação IBSUF |
| **gIBSMun** | **G** | **W36** | **1-1** |  |
| vDif | E | W42 | 1-1 |  |
| vDevTrib | E | W42 | 1-1 |  |
| vIBSMun | E | W42 | 1-1 | Totalizador dos valores TTRBITMMOV.VALOR para tributação IBSMun |
| **-x-** |  |  |  |  |
| vIBS | E | W36 | 1-1 | Soma dos valores das tags vIBSMun e vIBSUF |
| vCredPres | E | W36 | 1-1 |  |
| vCredPresCondSus | E | W36 | 1-1 |  |
| **gCBS** | **G** | **W34** | **0-1** |  |
| vDif | E | W50 | 1-1 |  |
| vDevTrib | E | W50 | 1-1 |  |
| vCBS | E | W50 | 1-1 | Totalizador dos valores TTRBITMMOV.VALOR para tributação CBS |
| vCredPres | E | W50 | 1-1 |  |
| vCredPresCondSus | E | W50 | 1-1 |  |
| **gMono** | **G** | **W34** | **0-1** |  |
| vIBSMono | E | W57 | 1-1 |  |
| vCBSMono | E | W57 | 1-1 |  |
| vIBSMonoReten | E | W57 | 1-1 |  |
| vCBSMonoReten | E | W57 | 1-1 |  |
| vIBSMonoRet | E | W57 | 1-1 |  |
| vCBSMonoRet | E | W57 | 1-1 |  |
| **-x-** |  |  |  |  |
| vNFTot | E | W01 | 0-1 | Soma dos valores das tags vItem |
