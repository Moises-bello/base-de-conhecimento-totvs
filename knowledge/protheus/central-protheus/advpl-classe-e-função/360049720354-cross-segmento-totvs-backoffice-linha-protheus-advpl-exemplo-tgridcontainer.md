---
article_id: 360049720354
category: ADVPL - Classe e Função
content_hash: bf8180ff20a6797261ba365fb6c94b07df34e8c12aaf0cb39a692b297f29f242
fetched_at: '2026-06-28T22:40:14.158406+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Exemplo TGridContainer
type: support-article
updated_at: '2021-05-06T19:27:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049720354-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Exemplo-TGridContainer
---

**Dúvida**Exemplo utilizando usar o componente **TGridContainer**.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.25  
  
**Solução**A classe **TGridContainer**cria um objeto do tipo grade, que permite a inserção de outros objetos visuais em suas células.

Para ter controle sobre as cores de uma célula segue exemplo abaixo

```
#Include 'Protheus.ch'  
  
USER FUNCTION TContainer()  
  
DEFINE DIALOG oDlg TITLE "Exemplo TGridContainer" FROM 180,180 TO 550,700 PIXEL  
  
nLines := 10  
  
nCols :=5  
  
oBrowse:=TGridContainer():New( 01,01,260,156, nLines, nCols,oDLG,.T.,.T., {|o,nKey| conout(o, nKey)} )  
  
@ 029, 021 MSPANEL frameNew SIZE 143, 040 OF oDlg COLOR CLR_YELLOW,CLR_HRED  
  
@ 005, 004 SAY oSay PROMPT "APERTE" SIZE 063, 007 OF frameNew COLORS 8421376, 16777215 PIXEL  
  
frameNew:blClicked := {|| msgAlert("Posiciona na primeira celula"),oBrowse:SetCurrentCell(1,1) }  
  
oBrowse:setCellWidget(2,2, frameNew)  
  
ACTIVATE DIALOG oDlg CENTERED  
  
RETURN
```

**![tgridcontainer.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360076232313/tgridcontainer.gif)**

**Saiba Mais**

[**TGridContainer**](https://tdn.totvs.com/display/tec/TGridContainer)
