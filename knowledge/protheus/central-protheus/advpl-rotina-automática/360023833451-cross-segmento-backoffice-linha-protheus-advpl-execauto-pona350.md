---
article_id: 360023833451
category: ADVPL - Rotina Automática
content_hash: 8c6f9c33b8ea9ff1c627aec715a44cf26bc88c443778ad5078b832f7b84ebc25
fetched_at: '2026-06-28T22:40:24.042178+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - EXECAUTO PONA350
type: support-article
updated_at: '2021-12-29T14:54:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023833451-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-EXECAUTO-PONA350
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Solicito exemplo da ExecAuto na rotina PONA350 - Pré Abono

**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**

Segue abaixo modelo para auxilio na customização da rotina PONA350

Exemplo de Inclusão

```
#Include 'Protheus.ch'  
#Include 'tbiconn.ch'  
  
//Rotina de teste da Rotina Automática do programa Pona350  
  
User Function My350I()  
Local aArea := {}  
Local aSRAArea := {}  
Local aSP6Area := {}  
Local aCabec := {}  
Local aItens := {}  
Local cFuncionario := ""  
   
Local dPerIni := Ctod('')  
Local dPerFim := Ctod('')  
  
Private lMsHelpAuto := .T. // se .t. direciona as mensagens de help para o arq. de log  
Private lMsErroAuto := .F. //necessário a criação, pois sera //atualizado quando houver   
 //alguma inconsistência nos parâmetros  
  
   
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Abertura do ambiente |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
PREPARE ENVIRONMENT EMPRESA '01' FILIAL "01" TABLES "SRA", "SP6", "RF0" MODULO "PON"  
  
aArea := (GetArea())  
aSRAArea := SRA->(GetArea())  
aSP6Area := SP6->(GetArea())  
  
  
//-- Obtem o Periodo de Apontamento em Aberto  
GetPonMesDat( @dPerIni , @dPerFim )  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Obtem 1 funcionario |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
dbSelectArea("SRA")  
SRA->(DBGOTOP())  
cFuncionario := SRA->RA_MAT  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Obtem 1 Motivo |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
dbSelectArea("SP6")  
SP6->(DBGOTOP())  
cMotivo := SP6->P6_CODIGO  
  
  
 //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
 //| Teste de Inclusao |  
 //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
 ConOut(Repl("-",80))  
 ConOut(PadC("Teste de Inclusão de Períodos de Pre-Abonos",80))  
 ConOut("Inicio: "+Time())  
   
 aCabec := {}  
 aItens := {}  
 aLinha := {}  
 aadd(aCabec,{"RF0_MAT" , cFuncionario ,})  
 aadd(aLinha,{"RF0_DTPREI" , dPerIni ,})  
 aadd(aLinha,{"RF0_HORINI" , 2.00 ,})  
 aadd(aLinha,{"RF0_DTPREF" , dPerFim ,})  
 aadd(aLinha,{"RF0_HORFIM" , 4.00 ,})  
 aadd(aLinha,{"RF0_CODABO" , cMotivo ,})  
 aadd(aLinha,{"RF0_HORTAB" , 'S' ,})  
 aadd(aItens, aLinha)   
   
 MSExecAuto({|x,y,z| PONA350(x,y,z)},aCabec,aItens,3)   
   
 If !lMsErroAuto  
 ConOut("Incluido com sucesso! "+cFuncionario)   
 Else  
 ConOut("Erro na inclusao!")  
 EndIf  
 ConOut("Fim : "+Time())  
  
RESET ENVIRONMENT  
  
Return(.T.)
```

**Exemplo de Alteração**

```
#Include 'Protheus.ch'  
#Include 'tbiconn.ch'  
  
User Function My350A()  
Local aArea            :=    {}  
Local aSRAArea        :=    {}  
Local aSP6Area        :=    {}  
Local aCabec        :=  {}  
Local aItens        :=  {}  
Local cFuncionario     :=  ""  
                               
Local dPerIni        := Ctod('')  
Local dPerFim        := Ctod('')  
  
Private lMsHelpAuto := .T.     // se .t. direciona as mensagens de help para o arq. de log  
Private lMsErroAuto := .F.     //necessário a criação, pois sera //atualizado quando houver   
                            //alguma inconsistência nos parâmetros  
  
  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Abertura do ambiente                                         |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
PREPARE ENVIRONMENT EMPRESA '01' FILIAL "01" TABLES "SRA", "SP6", "RF0" MODULO "PON"   
  
aArea            :=    (GetArea())  
aSRAArea        :=    SRA->(GetArea())  
aSP6Area        :=    SP6->(GetArea())  
  
                                 
//-- Obtem o Periodo de Apontamento em Aberto  
GetPonMesDat( @dPerIni , @dPerFim )  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Obtem 1 funcionario                                             |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
dbSelectArea("SRA")  
SRA->(DBGOTOP())  
cFuncionario := SRA->RA_MAT  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Obtem 1 Motivo                                                 |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
dbSelectArea("SP6")  
SP6->(DBGOTOP())  
cMotivo     := SP6->P6_CODIGO  
  
  
       
  
    //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
    //| Teste de Alteracao                                           |  
    //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
    ConOut(Repl("-",80))   
    ConOut("Inicio: "+Time())  
    ConOut(PadC("Teste de Alteracao de Periodos de Pre-Abonos",80))  
      
    aCabec := {}   
    aItens := {}   
    aLinha := {}  
    aadd(aCabec,{"RF0_MAT"        , cFuncionario    ,})  
    aadd(aLinha,{"RF0_DTPREI"     , dPerIni        ,})  
    aadd(aLinha,{"RF0_HORINI"     , 9.00            ,})  
    aadd(aLinha,{"RF0_DTPREF"     , dPerFim        ,})  
    aadd(aLinha,{"RF0_HORFIM"     , 10.00            ,})  
    aadd(aLinha,{"RF0_CODABO"     , cMotivo        ,})  
    aadd(aLinha,{"RF0_HORTAB"     , 'S'            ,})  
    aadd(aItens, aLinha)  
      
    MSExecAuto({|x,y,z| PONA350(x,y,z)},aCabec,aItens,4)  
      
      
    If !lMsErroAuto  
        ConOut("Alterado com sucesso! "+cFuncionario)      
    Else  
        ConOut("Erro na Alteracao!")  
    EndIf  
    ConOut("Fim  : "+Time())  
      
  
  
RESET ENVIRONMENT  
  
Return(.T.)
```

**Exemplo de Exclusão**

```
#Include 'Protheus.ch'  
#Include 'tbiconn.ch'  
  
User Function My350E()  
Local aArea            :=    {}  
Local aSRAArea        :=    {}  
Local aSP6Area        :=    {}  
Local aCabec        :=  {}  
Local aItens        :=  {}  
Local cFuncionario     :=  ""  
                               
Local dPerIni        := Ctod('')  
Local dPerFim        := Ctod('')  
  
Private lMsHelpAuto := .T.     // se .t. direciona as mensagens de help para o arq. de log  
Private lMsErroAuto := .F.     //necessário a criação, pois sera //atualizado quando houver   
                            //alguma inconsistência nos parâmetros  
  
  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Abertura do ambiente                                         |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
PREPARE ENVIRONMENT EMPRESA '01' FILIAL "01" TABLES "SRA", "SP6", "RF0" MODULO "PON"   
  
aArea            :=    (GetArea())  
aSRAArea        :=    SRA->(GetArea())  
aSP6Area        :=    SP6->(GetArea())  
  
                                 
//-- Obtém o Período de Apontamento em Aberto  
GetPonMesDat( @dPerIni , @dPerFim )  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Obtem 1 funcionario                                             |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
dbSelectArea("SRA")  
SRA->(DBGOTOP())  
cFuncionario := SRA->RA_MAT  
  
//ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
//| Obtem 1 Motivo                                                 |  
//ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ  
dbSelectArea("SP6")  
SP6->(DBGOTOP())  
cMotivo     := SP6->P6_CODIGO  
  
    //ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿  
    //| Teste de Exclusão                                            |  
    //ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ   
    ConOut(Repl("-",80))   
    ConOut("Inicio: "+Time())  
    ConOut(PadC("Teste de Exclusão de Períodos de Pre-Abonos",80))  
      
    aCabec := {}  
    aItens := {}      
    aLinha := {}      
    aadd(aCabec,{"RF0_MAT"        , cFuncionario    ,})  
      
    aadd(aLinha,{"RF0_DTPREI"     , dPerIni        ,})  
    aadd(aLinha,{"RF0_HORINI"     , 0.00            ,})  
    aadd(aLinha,{"RF0_DTPREF"     , dPerFim        ,})  
    aadd(aLinha,{"RF0_HORFIM"     , 0.00            ,})  
    aadd(aLinha,{"RF0_CODABO"     , cMotivo        ,})  
    aadd(aLinha,{"RF0_HORTAB"     , 'S'            ,})  
    aadd(aItens, aLinha)  
      
    MSExecAuto({|x,y,z| PONA350(x,y,z)},aCabec,aItens,5)  
      
    If !lMsErroAuto  
        ConOut("Excluído com sucesso! "+cFuncionario)      
    Else  
        ConOut("Erro na Exclusão!")  
    EndIf  
    ConOut("Fim  : "+Time())  
  
RESET ENVIRONMENT  
  
Return(.T.) 
```
