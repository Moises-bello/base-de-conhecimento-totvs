---
article_id: 360022454272
category: ADVPL - Classe e Função
content_hash: f5c270d6ccfe4635532d0990d9cd9782e8e56f7a807cf599189929b8e15f75bb
fetched_at: '2026-06-28T22:40:18.062126+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Tabela de cores MSDIALOG
type: support-article
updated_at: '2021-11-16T20:26:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022454272-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Tabela-de-cores-MSDIALOG
---

**Dúvida**Gostaria da tabela de cores da classe MSDIALOG.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - AdvPL - Todas as versões  
  
**Solução**

**Tabela de cores**CLR\_BLACK         // RGB( 0, 0, 0 )  
CLR\_BLUE           // RGB( 0, 0, 128 )  
CLR\_GREEN        // RGB( 0, 128, 0 )  
CLR\_CYAN          // RGB( 0, 128, 128 )  
CLR\_RED            // RGB( 128, 0, 0 )  
CLR\_MAGENTA    // RGB( 128, 0, 128 )  
CLR\_BROWN       // RGB( 128, 128, 0 )  
CLR\_HGRAY        // RGB( 192, 192, 192 )  
CLR\_LIGHTGRAY // RGB( 192, 192, 192 )  
CLR\_GRAY          // RGB( 128, 128, 128 )  
CLR\_HBLUE        // RGB( 0, 0, 255 )  
CLR\_HGREEN      // RGB( 0, 255, 0 )  
CLR\_HCYAN        // RGB( 0, 255, 255 )  
CLR\_HRED          // RGB( 255, 0, 0 )  
CLR\_HMAGENTA  // RGB( 255, 0, 255 )  
CLR\_YELLOW      // RGB( 255, 255, 0 )  
CLR\_WHITE        // RGB( 255, 255, 255 )

**Segue ilustração para apoio**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019704271/mceclip0.png)

**PoC:**

```
#Include 'Protheus.ch'  
  
#include "TOTVS.CH"  
  
User Function cores()  
  
//Tabela de cores dialog  
  
    Local oDlg  
  
    local nX  
  
    local acor:= {CLR_BLACK,CLR_BLUE,CLR_GREEN,CLR_CYAN,CLR_RED,CLR_MAGENTA,CLR_BROWN,CLR_HGRAY,CLR_LIGHTGRAY,CLR_GRAY,CLR_HBLUE,CLR_HGREEN,CLR_HCYAN,CLR_HRED,CLR_HMAGENTA,CLR_YELLOW,CLR_WHITE}  
  
    local acorT:= {"CLR_BLACK","CLR_BLUE","CLR_GREEN","CLR_CYAN","CLR_RED","CLR_MAGENTA","CLR_BROWN","CLR_HGRAY","CLR_LIGHTGRAY","CLR_GRAY","CLR_HBLUE","CLR_HGREEN","CLR_HCYAN","CLR_HRED","CLR_HMAGENTA","CLR_YELLOW","CLR_WHITE"}  
  
// Cria diálogo    
  
    For nX := 1 To Len(acor)  
  
        oDlg := MSDialog():New(180,180,550,700,'Exemplo MSDialog',,,,,acor[nX],acor[nX],,,.T.)  
  
        oDlg:Activate(,,,.T.,{||msgstop('Posição: '+ cvaltochar(nX)),.T.},,{||msgstop('Cor: '+ cvaltochar(acorT[nX]))} )  
  
    Next  
  
Return
```
