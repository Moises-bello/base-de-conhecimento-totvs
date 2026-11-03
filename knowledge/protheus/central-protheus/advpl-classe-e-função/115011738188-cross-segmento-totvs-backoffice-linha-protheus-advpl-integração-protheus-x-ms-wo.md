---
article_id: 115011738188
category: ADVPL - Classe e Função
content_hash: ea9bb85bd1bc9587072cd4c5c121181944117258b8ae0f5d6168763f9f8f4852
fetched_at: '2026-06-28T22:40:20.613880+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Integração Protheus
  x MS Word
type: support-article
updated_at: '2021-09-01T18:36:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011738188-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Integra%C3%A7%C3%A3o-Protheus-x-MS-Word
---

**Dúvida**Como efetuar a integração Protheus x MS Word?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**Para efetuar a integração entre um documento MS Word e o Protheus devemos criar um modelo (.dot) no formato desejado e incluir as devidas variáveis.

Antes, porém será útil configurarmos o Word de forma a visualizarmos as variáveis incluídas.

```
Modelo de rotina (.PRW)  
  
#include "rwmake.ch"           
  
User Function intword()  
@ 96,012 TO 250,400 DIALOG oDlg TITLE OemToAnsi("Integracao com MS-Word")  
@ 08,005 TO 048,190  
@ 18,010 SAY OemToAnsi("Impressao de orcamentos")  
  
@ 56,130 BMPBUTTON TYPE 1 ACTION WordImp()  
@ 56,160 BMPBUTTON TYPE 2 ACTION Close(oDlg)  
  
ACTIVATE DIALOG oDlg CENTERED  
Return()  
  
Static Function WordImp()  
Local wcOrcam, wcData, wcCliente, wcNroLinha  
Local waCod         := {}  
Local waDescr := {}  
Local waVTot := {}  
Local nAuxTot := 0  
Local nK  
Local cPathDot             := "C:\PROTHEUS\AP_PDV\DOT\INTWORD.DOT"  
Private      hWord  
  
Close(oDlg)  
wcNumero     := "121212"  
wcData       := AllTrim(Str(Day(dDataBase),2))+;  
' de '+AllTrim(MesExtenso(dDataBase))+' de '+;  
AllTrim(Str(Year(dDataBase),4))  
wcCliente    := "CLIENTE TESTE INTEGRACAO WORD"  
  
for nK := 1 to 10  
       aAdd(waCod,"PR"+strZero(nK,3))  
       aAdd(waDescr,"PRODUTO NRO "+strZero(nK,3))  
       aAdd(waVTot,Transform(nK*100,"@E 999,999,999.99"))  
       nAuxTot += nK*100  
next  
  
//Conecta ao word  
hWord  := OLE_CreateLink()  
OLE_NewFile(hWord, cPathDot )  
  
//Montagem das variaveis do cabecalho           
OLE_SetDocumentVar(hWord, 'Prt_numero', wcNumero)  
OLE_SetDocumentVar(hWord, 'Prt_Data', wcData)  
OLE_SetDocumentVar(hWord, 'Prt_Cliente', wcCliente)  
OLE_SetDocumentVar(hWord, 'Prt_nroitens',str(Len(waCod)))   //variavel para identificar o numero total de linhas na parte variavel  
  
//Sera utilizado na macro do documento para execucao do for next  
//Montagem das variaveis dos itens. No documento word estas variaveis serao criadas //dinamicamente da seguinte forma:  
//prt_cod1, prt_cod2 ... prt_cod10  
  
for nK := 1 to Len(waCod)  
OLE_SetDocumentVar(hWord,"Prt_Cod"+AllTrim(Str(nK)),waCod[nK])  
       OLE_SetDocumentVar(hWord,"Prt_Descr"+AllTrim(Str(nK)),waDescr[nK])  
       OLE_SetDocumentVar(hWord,"Prt_VTot"+AllTrim(Str(nK)),waVTot[nK])  
next  
  
OLE_ExecuteMacro(hWord,"tabitens")  
OLE_SetDocumentVar(hWord, 'prt_totorc', Transform(nAuxTot,"@E 999,999,999.99"))  
OLE_UpdateFields(hWord)    // Atualizando as variaveis do documento do Word  
  
If MsgYesNo("Imprime o Documento ?")  
       Ole_PrintFile(hWord,"ALL",,,1)  
EndIf  
   
If MsgYesNo("Fecha o Word e Corta o Link ?")  
       OLE_CloseFile( hWord )  
       OLE_CloseLink( hWord )  
Endif   
Return()  
  
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  
Modelo de macro (.BAS)  
Sub tabitens()  
' Item Macro  
' Macro recorded 31/03/2005 by Adalberto  
'  
Dim nItens As Integer  
Dim Campo  As String  
  
Selection.GoTo What:=wdGoToBookmark, Name:="tabitens"  
Selection.Find.ClearFormatting  
With Selection.Find  
    .Text = ""  
    .Replacement.Text = ""  
    .Forward = True  
    .Wrap = wdFindContinue  
    .Format = False  
    .MatchCase = False  
    .MatchWholeWord = False  
    .MatchWildcards = False  
    .MatchSoundsLike = False  
    .MatchAllWordForms = False  
End With  
  
nItens = Val(ActiveDocument.Variables.ITEM("prt_nroitens").Value)  
For K = 1 To nItens  
    ' Insere uma nova linha na tabela  
    Selection.MoveRight Unit:=wdCell  
    ' Insere o campo Codigo do Produto  
    Campo = "DOCVARIABLE prt_cod" & Trim(Str(K))  
    Selection.Fields.Add Range:=Selection.Range, Type:=wdFieldEmpty, Text:=Campo, PreserveFormatting:=True  
    ' Insere o campo Descricao do Produto  
    Selection.MoveRight  
    Campo = "DOCVARIABLE prt_descr" & Trim(Str(K))  
    Selection.Fields.Add Range:=Selection.Range, Type:=wdFieldEmpty, Text:=Campo, PreserveFormatting:=True  
  
    ' Insere o campo Total  
    Selection.MoveRight  
    Campo = "DOCVARIABLE prt_vtot" & Trim(Str(K))  
    Selection.Fields.Add Range:=Selection.Range, Type:=wdFieldEmpty, Text:=Campo, PreserveFormatting:=True  
Next  
  
End Sub
```

**Saiba mais**  
[Integração Protheus x MS Word](http://tdn.totvs.com/pages/viewpage.action?pageId=272155768)
