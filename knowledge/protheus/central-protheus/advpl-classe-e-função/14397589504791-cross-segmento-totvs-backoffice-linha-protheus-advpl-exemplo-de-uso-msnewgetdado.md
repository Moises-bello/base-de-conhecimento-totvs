---
article_id: 14397589504791
category: ADVPL - Classe e Função
content_hash: 7d69734b8d19a1601a020e96b7579449f4921337beb03fe0982a59bfd79f6516
fetched_at: '2026-06-28T22:40:16.700001+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Exemplo de uso MsNewGetDados
  com dicionário em banco
type: support-article
updated_at: '2023-10-11T13:21:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14397589504791-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Exemplo-de-uso-MsNewGetDados-com-dicion%C3%A1rio-em-banco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Na documentação da *msnewgetdados* possui exemplo apenas para ambientes que não estão com o dicionário em banco.  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 12.1.33  
  
**Causa**Por conta da migração do dicionário para o banco de dados não se pode mais realizar o acesso direto as SXs, assim o exemplo documentado na função não pode ser utilizado neste cenário.

**Solução**Foi criado o exemplo abaixo montando o *aHeader* e o *aCols*, ele não realiza acesso direto as SXs e sim as funções auxiliares de dicionário, assim é valido para ambientes com dicionário em banco.

```
#include "totvs.ch"  
  
User Function MrbwGtCl()  
  
Private cCadastro := "Exemplo MsNewGetDados"  
Private aRotina := {{"Pesquisar" , "axPesqui" , 0, 1},;  
{"Incluir" , "U_ModGtd" , 0, 3}}  
  
DbSelectArea("SC5")  
DbSetOrder(1)  
MBrowse(6,1,22,75,"SC5")  
  
Return  
  
User Function ModGtd(cAlias,nReg,nOpc)  
Local nX := 0  
Local nG := 0  
Local nUsado := 0  
Local aButtons := {}  
Local cAliasGD := "SC6"  
Local cIniCpos := "C6_ITEM"  
Local nSuperior := 30  
Local nEsquerda := 000  
Local nInferior := 250  
Local nDireita := 400  
Local cLinOk := "AllwaysTrue"  
Local cTudoOk := "AllwaysTrue"  
Local nFreeze := 000  
Local nMax := 999  
Local cFieldOk := "AllwaysTrue"  
Local cSuperDel := ""  
Local cDelOk := "AllwaysFalse"  
Local aAlterGDa := {}  
Local aCamposUsados:= {}  
Local aCampos:= {}  
Local cSX3Cache  
  
Private aHeader := {}  
Private aCols := {}  
Private oDlg  
Private oGetD  
Private oEnch  
Private aTELA[0][0]  
Private aGETS[0]  
Private N :=0  
  
// Define a tabela a ser utilizada  
cAliasGD := "SC6"  
  
// Obtêm as informações dos campos da tabela SC6  
aCampos := FWSX3Util():GetAllFields(cAliasGD)  
aCamposUsados := {}  
For nG:=1 to len(aCampos)  
// Obtêm as informações dos campos usados no dicionário SX3  
cSX3Cache := getsx3cache(aCampos[nG],"X3_USADO")  
If X3USO(cSX3Cache)  
AADD(aCamposUsados, aCampos[nG])  
aStruct:=FWSX3Util():GetFieldStruct(aCampos[nG])  
Aadd(aHeader,{AllTrim(X3Titulo(aCampos[nG])),aCampos[nG],X3Picture(aCampos[nG]),aStruct[3],aStruct[4], "", "", aStruct[2], "", ""})  
EndIf  
next  
  
nUsado:=Len(aCamposUsados)  
  
If nOpc==3 // Caso seja inclusão  
aCols:={Array(nUsado+1)}  
aCols[1,nUsado]:=.F.  
  
For nX:=1 to nUsado  
aCols[1,nX]:=CriaVar(aHeader[nX,2])  
Next  
Else  
  
aCols:={}  
  
dbSelectArea("SC6")  
dbSetOrder(1)  
dbSeek(xFilial())  
  
While !eof().and.C6_NUM==M->C5_NUM  
AADD(aCols,Array(nUsado+1))  
For nX:=1 to nUsado  
aCols[Len(aCols),nX]:=FieldGet(FieldPos(aHeader[nX,2]))  
Next  
aCols[Len(aCols),nUsado+1]:=.F.  
dbSkip()  
End  
Endif  
  
aAlterGDa:=aClone(aCamposUsados)  
  
oDlg := MSDIALOG():New(000,000,600,800, cCadastro,,,,,,,,,.T.)  
oGetD:= MsNewGetDados():New(nSuperior,nEsquerda,nInferior,nDireita, nOpc,cLinOk,cTudoOk,cIniCpos,aAlterGDa,nFreeze,nMax,cFieldOk, cSuperDel,cDelOk, oDLG, aHeader, aCols)  
oGetD:oBrowse:bRClicked := { || Alert("clique direita")}  
oGetD:oBrowse:brabsClicked := { || Alert("clique esquerda")}  
oDlg:bInit := {|| EnchoiceBar(oDlg, {||oDlg:End()}, {||oDlg:End()},,aButtons)}  
oDlg:lCentered := .T.  
oDlg:Activate()  
Return
```

**Saiba Mais**

[MsNewGetDados](https://tdn.totvs.com/display/public/framework/MsNewGetDados)

[Funções Auxiliares de Dicionário](https://tdn.totvs.com.br/pages/releaseview.action?pageId=353290193)
