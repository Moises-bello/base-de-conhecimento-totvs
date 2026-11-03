---
article_id: 360000321567
category: ADVPL - Classe e Função
content_hash: 617c850d7c9bf79c53596a3ae32157b62ed218ce70cdc08f8974cba9d3acbc14
fetched_at: '2026-06-28T22:40:14.213339+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - TCheckBox como
  validar se o mesmo foi marcado ou não
type: support-article
updated_at: '2024-06-26T20:43:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000321567-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TCheckBox-como-validar-se-o-mesmo-foi-marcado-ou-n%C3%A3o
---

**Dúvida**TCheckBox como validar se o mesmo foi marcado ou não?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**A propriedade **LMODIFIED** traz a informação se foi modificado.

Exemplo:

```
#include "TOTVS.CH"  
User Function Box()  
  
  Local oDlg, oPanel,oCheck1,oCheck2, oCheck3  
  
  lCHECK_1 := .F.  
  cCHECK_1 := "Check numero 1"  
  
  lCHECK_2 := .F.  
  cCHECK_2 := "Check numero 2"  
  
  lCHECK_3 := .F.  
  cCHECK_3 := "Check numero 3"  
  
  DEFINE MSDIALOG oDlg TITLE "Teste check" FROM 200,1 TO 620,600 PIXEL //Montagem da tela  
  oPanel:= TPanel():New(0, 0, "", oDlg,, .F., .F.,,, 0, 0) //Criação do painel   
  
  oCheck1:= TCheckBox():New(10,10,cCHECK_1,bSETGET(lCHECK_1),oPanel,215,10,,,,,,,,.T.)  
  
  //Bloco de código que será executado quando clicar, com o botão esquerdo do mouse, sobre o objeto.  
  oCheck1:bLClicked := {|| u_tstChk(oCheck1,lCHECK_1)}  
  
  oCheck2:=TCheckBox():New(19,10,cCHECK_2,bSETGET(lCHECK_2),oPanel,215,10,,,,,,,,.T.)  
  oCheck2:bLClicked := {||u_tstChk(oCheck2, lCHECK_2)}  
  
  oCheck3:=TCheckBox():New(28,10,cCHECK_3,bSETGET(lCHECK_3),oPanel,215,10,,,,,,,,.T.)  
  oCheck3:bLClicked := {|| u_tstChk(oCheck3,lCHECK_3)}  
  
  oPanel:Align:= CONTROL_ALIGN_ALLCLIENT  
  
  ACTIVATE DIALOG oDlg CENTERED  
Return  
  
//Função que irá verificar se houve modificação o clique do check   
User Function tstChk(oCheck, lCHECK)  
  
  If valType(oCheck) <> "U"  
    If oCheck:lModified //Verifica se foi alterado  
      msgInfo("Ação de check no: " + oCheck:cTitle + " Estado: "+cValToChar(lCHECK))  
    EndIf  
  Endif  
  
Return .T.
```

**Saiba mais**  
[ADV0070 Tcheckbox](http://tdn.totvs.com/display/PROT/ADV0070_TCHECKBOX)
