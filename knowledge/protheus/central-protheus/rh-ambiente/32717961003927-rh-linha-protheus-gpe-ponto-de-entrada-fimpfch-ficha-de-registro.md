---
article_id: 32717961003927
category: RH - Ambiente
content_hash: 7668ed1e67b019e38e23f1cd0a21ba0c03ac74d32f7d80fa257f96ecbac43fa6
fetched_at: '2026-06-28T22:43:09.523997+00:00'
product: protheus
section_id: 20669342808471
source: central-protheus
title: RH - Linha Protheus - GPE - Ponto de Entrada FIMPFCH - Ficha de Registro
type: support-article
updated_at: '2026-06-25T10:53:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32717961003927-RH-Linha-Protheus-GPE-Ponto-de-Entrada-FIMPFCH-Ficha-de-Registro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32717980407703) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como utilizar o Ponto de Entrada FIMPFCH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O Ponto de Entrada é executado na **montagem do MenuDef** da rotina **GPEA260,** e pode ser utilizado para alterar o programa da **Ficha de Registro**, ou seja, quando o *rdmake* **GPER460** é customizado.  
Por padrão, a rotina executa a função GPER460, mas isso pode ser modificado alterando o conteúdo da variável **cImpFch** conforme exemplo abaixo:

**1) Chamada de uma User Function GPER460U**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | `#INCLUDE "PROTHEUS.CH"`    `User Function``FIMPFCH``()`    `If ExistBlock(``"gper460U"``)`  `cImpFch :=``'EXECBLOCK("gper460U",.F.,.F.)'`  `Endif`    `Return` |

**2) Chamada de uma Function GPER460F**

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | `#INCLUDE "PROTHEUS.CH"`    `User Function``FIMPFCH``()`    `If FindFunction(``"GPER460F"``)`  `cImpFch :=``"GPER460F(.F.)"`  `EndIf`    `Return` |

**Saiba Mais:**[DT - FIMPFCH](https://tdn.totvs.com/pages/releaseview.action?pageId=852901276)  
[RH - Linha Protheus - GPE - Fonte GPER460 (Ficha de Registro) para customização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007802222-RH-Linha-Protheus-GPE-Fonte-GPER460-Ficha-de-Registro-para-customiza%C3%A7%C3%A3o)
