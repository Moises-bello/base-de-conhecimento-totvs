---
article_id: 4409361581591
category: ADVPL - Classe e Função
content_hash: 3b22f7070da38e6fe86a1f5a791c87430394a2a584517fb6bdaea81ba11696d0
fetched_at: '2026-06-28T22:40:16.801159+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Função Modelo2
type: support-article
updated_at: '2023-08-10T16:52:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409361581591-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-Modelo2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16672465013399) Tempo aproximado para leitura: 00:01:00 min **Dúvida**Há algum exemplo referente a função Modelo2?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**A função Modelo2 exibe formulário para cadastro contendo: uma enchoice, uma getdados e uma área que pode ser utilizada para apresentar totalizadores ou outros dados mais relevantes.  
  
Exemplo

```
#include "protheus.ch"  
  
#INCLUDE "rwmake.ch"  
  
User Function Md2()  
  
    Local nOpcx:=3  
    Local nG := 0  
    Local nX := 0  
    Local nInd := 0  
    Local nUsado := 0  
    Local aCamposUsados:= {}  
    Local aCampos:= {}  
    Local cSX3Cache  
    Local cAliasGD := "ZA1"  
  
    Private aHeader := {}  
    Private aCols := {}  
  
//+-----------------------------------------------+  
//¦ Montando aHeader para a Getdados ¦  
//+-----------------------------------------------+  
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
  
//+-----------------------------------------------+  
//¦ Montando aCols para a GetDados ¦  
//+-----------------------------------------------+  
    If nOpcx==3 // Caso seja inclusão  
        aCols:={Array(nUsado+1)}  
        aCols[1,nUsado+1]:=.F.  
        For nX:=1 to nUsado  
            aCols[1,nX]:=CriaVar(aHeader[nX,2])  
        Next  
    Else  
        aCols:={}  
        dbSelectArea("ZA1")  
        dbSetOrder(1)  
        dbSeek(xFilial())  
        While !eof()  
            AADD(aCols,Array(nUsado+1))  
            For nX:=1 to nUsado  
                aCols[Len(aCols),nX]:=FieldGet(FieldPos(aHeader[nX,2]))  
            Next  
            aCols[Len(aCols),nUsado+1]:=.F.  
            dbSkip()  
        End  
    Endif  
//+----------------------------------------------+  
//¦ Variaveis do Cabecalho do Modelo 2 ¦  
//+----------------------------------------------+  
    cCliente:=Space(6)  
    cLoja :=Space(2)  
    dData :=Date()  
  
//+----------------------------------------------+  
//¦ Variaveis do Rodape do Modelo 2  
//+----------------------------------------------+  
    nLinGetD:=0  
//+----------------------------------------------+  
//¦ Titulo da Janela ¦  
//+----------------------------------------------+  
    cTitulo:="TESTE DE MODELO2"  
//+----------------------------------------------+  
//¦ Array com descricao dos campos do Cabecalho ¦  
//+----------------------------------------------+  
    aC:={}  
    #IFDEF WINDOWS  
        AADD(aC,{"cCliente" ,{15,10} ,"Cod. do Cliente","@!",'ExecBlock("MD2VLCLI",.F.,.F.)',"SA1",})  
        AADD(aC,{"cLoja" ,{15,200},"Loja","@!",,,})  
        AADD(aC,{"dData" ,{27,10} ,"Data de Emissao",,,,})  
    #ELSE  
        AADD(aC,{"cCliente" ,{6,5} ,"Cod. do Cliente","@!",'ExecBlock("MD2VLCLI",.F.,.F.)',"SA1",})  
        AADD(aC,{"cLoja" ,{6,40},"Loja","@!",,,})  
        AADD(aC,{"dData" ,{7,5} ,"Data de Emissao",,,,})  
    #ENDIF  
//+-------------------------------------------------+  
//¦ Array com descricao dos campos do Rodape ¦  
//+-------------------------------------------------+  
    aR:={}  
    #IFDEF WINDOWS  
        AADD(aR,{"nLinGetD" ,{120,10},"Linha na GetDados", "@E 999",,,.F.})  
    #ELSE  
        AADD(aR,{"nLinGetD" ,{19,05},"Linha na GetDados","@E 999",,,.F.})  
    #ENDIF  
  
//+------------------------------------------------+  
//¦ Array com coordenadas da GetDados no modelo2 ¦  
//+------------------------------------------------+  
    #IFDEF WINDOWS  
        aCGD:={44,5,118,315}  
    #ELSE  
        aCGD:={10,04,15,73}  
    #ENDIF  
  
//+----------------------------------------------+  
//¦ Validacoes na GetDados da Modelo 2 ¦  
//+----------------------------------------------+  
  
    cLinhaOk := "ExecBlock('Md2LinOk',.f.,.f.)"  
    cTudoOk := "ExecBlock('Md2TudOk',.f.,.f.)"  
  
//+----------------------------------------------+  
//¦ Chamada da Modelo2 ¦  
//+----------------------------------------------+  
  
// lRet = .t. se confirmou  
// lRet = .f. se cancelou  
    lRet:= Modelo2(cTitulo,aC,aR,aCGD,nOpcx,cLinhaOk,cTudoOk, , , ,999)  
    If lRet  
  
//Inclui os Registros na tabela SZF  
       For nInd := 1 to len( aCols )  
            If !(aCols[nInd][len(aHeader)+1]) //não foi deletado  
                RecLock("ZA1",.t.)  
                Replace ZA1->ZA1_FILIAL with xFilial('SZF') , ;  
                    ZA1->ZA1_MUSICA with aCols[nInd][aScan( aHeader, { |x| x[2]="ZA1_MUSICA" } )] , ;  
                    ZA1->ZA1_TITULO with aCols[nInd][aScan( aHeader, { |x| x[2]="ZA1_TITULO" } )] , ;//cCCustoMO , ;  
                    ZA1->ZA1_DATA with aCols[nInd][aScan( aHeader, { |x| x[2]="ZA1_DATA" } )] , ;  
                    ZA1->ZA1_GENERO with aCols[nInd][aScan( aHeader, { |x| x[2]="ZA1_GENERO" } )]  
                ZA1->(MsUnlock())  
            EndIf  
        Next  
    EndIf  
Return lRet  
User function Md2LinOk()  
//Msginfo("Validando a linha")  
Return .t.  
  
User function Md2TudOk()  
//Msginfo("Validando o Formulário")  
Return .t.  
  
User function Md2valid()  
//Msginfo("Validando")  
Return .t.  
  
User function MD2VLCLI()  
//Msginfo("Validando")  
Return .t.
```

**Saiba Mais****[Modelo2](http://tdn.totvs.com/pages/releaseview.action?pageId=6814982)**
