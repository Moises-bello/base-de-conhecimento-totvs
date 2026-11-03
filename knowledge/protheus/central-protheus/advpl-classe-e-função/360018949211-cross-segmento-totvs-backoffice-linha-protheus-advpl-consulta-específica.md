---
article_id: 360018949211
category: ADVPL - Classe e Função
content_hash: 50a31e8d90659cdad8bc749ef25670cf384164d90df0c627b60378e3e0656a7f
fetched_at: '2026-06-28T22:40:15.651947+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Consulta específica
type: support-article
updated_at: '2025-06-19T15:46:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018949211-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Consulta-espec%C3%ADfica
---

**Dúvida**Criar consulta específica  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - A partir da versão 11.80

**Solução**A seguir um exemplo de consulta específica para ser utilizado na rotina de Roteiro de Operações, acionada no F3 do campo C2\_ROTEIRO, irá apresentar uma listagem dos registros contendo os campos G2\_CODIGO, G2\_PRODUTO e G2\_DESCRI, após selecionar o registro irá retornar G2\_CODIGO ao campo C2\_ROTEIRO;

```
#Include 'Protheus.ch'  
  
User Function ConEspOp()  
   Local oDlg, oLbx  
   Local aCpos  := {}  
   Local aRet   := {}  
   Local cQuery := ""  
   Local cAlias := GetNextAlias()  
   Local lRet   := .F.  
  
   cQuery := " SELECT DISTINCT SG2.G2_CODIGO, SG2.G2_PRODUTO, SG2.G2_DESCRI "  
   cQuery +=   " FROM " + RetSqlName("SG2") + " SG2 "  
   cQuery +=  " WHERE SG2.D_E_L_E_T_ = ' ' "  
   cQuery +=    " AND SG2.G2_FILIAL  = '" + xFilial("SG2") + "' "  
   If !Empty(M->C2_PRODUTO)  
      cQuery += " AND SG2.G2_PRODUTO = '" + M->C2_PRODUTO + "' "  
   EndIf  
   cQuery += " ORDER BY 2,1 "  
  
   cQuery := ChangeQuery(cQuery)  
  
   dbUseArea(.T.,"TOPCONN",TcGenQry(,,cQuery),cAlias,.T.,.T.)  
  
   While (cAlias)->(!Eof())  
      aAdd(aCpos,{(cAlias)->(G2_CODIGO), (cAlias)->(G2_PRODUTO), (cAlias)->(G2_DESCRI)})  
      (cAlias)->(dbSkip())  
   End  
   (cAlias)->(dbCloseArea())  
  
   If Len(aCpos) < 1  
      aAdd(aCpos,{" "," "," "})  
   EndIf  
  
   DEFINE MSDIALOG oDlg TITLE /*STR0083*/ "Roteiro de operações" FROM 0,0 TO 240,500 PIXEL  
  
     @ 10,10 LISTBOX oLbx FIELDS HEADER 'Roteiro' /*"Roteiro"*/, 'Produto' /*"Produto"*/, 'Descricao' SIZE 230,95 OF oDlg PIXEL  
  
     oLbx:SetArray( aCpos )  
     oLbx:bLine     := {|| {aCpos[oLbx:nAt,1], aCpos[oLbx:nAt,2], aCpos[oLbx:nAt,3]}}  
     oLbx:bLDblClick := {|| {oDlg:End(), lRet:=.T., aRet := {oLbx:aArray[oLbx:nAt,1],oLbx:aArray[oLbx:nAt,2], oLbx:aArray[oLbx:nAt,3]}}}  
  
  DEFINE SBUTTON FROM 107,213 TYPE 1 ACTION (oDlg:End(), lRet:=.T., aRet := {oLbx:aArray[oLbx:nAt,1],oLbx:aArray[oLbx:nAt,2], oLbx:aArray[oLbx:nAt,3]})  ENABLE OF oDlg  
  ACTIVATE MSDIALOG oDlg CENTER  
  
  If Len(aRet) > 0 .And. lRet  
     If Empty(aRet[1])  
        lRet := .F.  
     Else  
        SG2->(dbSetOrder(1))  
        SG2->(dbSeek(xFilial("SG2")+aRet[2]+aRet[1]))  
     EndIf  
  EndIf  
Return lRet
```

Configure a consulta atrelando a função de usuário conforme prints a seguir;  
![](https://totvssuporte.zendesk.com/attachments/token/xBH87ZqlLNwnO2FfGoRERqIU1/?name=inline1457343769.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/NmjEOIuzx1EZnhNCKTizi4ubh/?name=inline-478627228.png)​  
Em seguida atribua a consulta SG2003 ao campo C2\_ROTEIRO

**Obs. O exemplo passado serve como uma referência, a regra da consulta específica é de responsabilidade do desenvolvedor/cliente, o suporte da TOTVS não se responsabiliza por eventuais erros e não prestará suporte ao desenvolvimento de regras específicas.**
