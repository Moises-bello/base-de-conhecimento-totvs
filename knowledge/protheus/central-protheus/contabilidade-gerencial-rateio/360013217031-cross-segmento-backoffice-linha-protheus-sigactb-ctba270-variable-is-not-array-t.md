---
article_id: 360013217031
category: Contabilidade Gerencial - Rateio
content_hash: 77acf8892a8e170719f5835c7a882a58cca791bd7f6d85dfb518b4a9b54f3339
fetched_at: '2026-06-28T22:40:35.577777+00:00'
product: protheus
section_id: 1500001548962
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA270 - VARIABLE IS
  NOT ARRAY - TYPE [C] ON CTB270CAD(CTBA270.PRW) '
type: support-article
updated_at: '2021-11-17T18:47:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013217031-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA270-VARIABLE-IS-NOT-ARRAY-TYPE-C-ON-CTB270CAD-CTBA270-PRW
---

**Ocorrência**

No módulo ***Contabilidade Gerencial***, rotina Cadastro de rateio off line (***CTBA270***), em Ações relacionadas, ao importar cadastro em  planilha ***CSV***, apresenta ***error log***:

*variable is not array - Type [C] on CTB270CAD(CTBA270.PRW) 20/09/2017 20:24:01 line : 733*

**Ambiente**Exemplo:  
Microsiga Protheus  – Contabilidade Gerencial – A partir da versão 11.80  
  
**Causa**Ocorrência apresentada devido a erro de configurações no array do cabeçalho.

**Solução**

Segue abaixo, modelo (exemplo) de ***user function***:

#Include 'Protheus.ch'  
#Include 'TBICONN.ch'  
  
User Function IncluiCTQ()  
Local nOpcA   
  
Local \_lOk := .T.   
Local aAutoItens := {}   
Local xCab := {}  
  
PRIVATE lMsErroAuto := .F.   
  
PREPARE ENVIRONMENT EMPRESA '99' FILIAL '01'  
  
cCtq\_Rateio := CriaVar("CTQ\_RATEIO")   
cCtq\_Desc := CriaVar("CTQ\_DESC")   
cCtq\_Tipo := CriaVar("CTQ\_TIPO")   
cCtq\_CtPar := CriaVar("CTQ\_CTPAR")   
cCtq\_CCPar := CriaVar("CTQ\_CCPAR")   
cCtq\_ItPar := CriaVar("CTQ\_ITPAR")   
cCtq\_ClPar := CriaVar("CTQ\_CLPAR")   
cCtq\_CtOri := CriaVar("CTQ\_CTORI")   
cCtq\_CCOri := CriaVar("CTQ\_CCORI")   
cCtq\_ItOri := CriaVar("CTQ\_ITORI")   
cCtq\_ClOri := CriaVar("CTQ\_CLORI")   
nCtq\_PerBas := CriaVar("CTQ\_PERBAS")   
cCtq\_MSBLQL := '0'   
  
aAdd(xCab,{{cCtq\_Rateio ,'000002' ,NIL},;   
      {cCtq\_Desc ,'EXECAUTO            ' ,NIL},;   
      {cCtq\_Tipo ,'1' ,NIL},;   
      {cCtq\_CtPar ,'000002              ' ,NIL},;   
      {cCtq\_CcPar ,'CC02    ' ,NIL},;   
      {cCtq\_ItPar ,'        ' ,NIL},;   
      {cCtq\_ClPar ,'        ' ,NIL},;   
      {cCtq\_CtOri ,'000001              ' ,NIL},;   
      {cCtq\_CCOri ,'CC01    ' ,NIL},;   
      {cCtq\_ItOri ,'        ' ,NIL},;   
      {cCtq\_ClOri ,'        ' ,NIL},;   
      {nCtq\_PerBas ,100 ,NIL},;   
      {cCtq\_MSBLQL ,'2' ,NIL} })   
  
aAdd(aAutoItens,{    {'CTQ\_FILIAL' ,'01' , NIL},;   
        {'CTQ\_CTORI' ,'000001              ' , NIL},;   
        {'CTQ\_CCORI' , 'CC01    ' , NIL},;   
        {'CTQ\_ITORI' ,'        ', NIL},;   
        {'CTQ\_CLORI' ,'        ' , NIL},;   
        {'CTQ\_CTPAR' ,'000002              ' , NIL},;   
        {'CTQ\_CCPAR' ,'CC01    ' , NIL},;   
        {'CTQ\_ITPAR' ,'        ' , NIL},;   
        {'CTQ\_CLPAR' ,'        ' , NIL},;   
        {'CTQ\_SEQUEN' ,'001' , NIL},;   
        {'CTQ\_CTCPAR' ,'000001              ' , NIL},;   
        {'CTQ\_CCCPAR' ,'        ' , NIL},;   
        {'CTQ\_ITCPAR' ,'        ' , NIL},;   
        {'CTQ\_CLCPAR' ,'        ' , NIL},;   
        {'CTQ\_UM' ,'UM' , NIL},;   
        {'CTQ\_VALOR' ,0 , NIL},;   
        {'CTQ\_PERCEN' ,100 , NIL},;   
        {'CTQ\_FORMUL' ,'1' , NIL},;   
        {'CTQ\_INTERC' ,'1', NIL} } )   
  
MSExecAuto( {|X,Y,Z| CTBA270(X,Y,Z)} ,xCab ,aAutoItens, 3)   
  
If lMsErroAuto <> Nil   
 If !lMsErroAuto   
  \_lOk := .T.   
  If !IsBlind()   
      MsgInfo('Inclusão com sucesso!')   
  EndIf   
 Else   
  \_lOk := .F.   
  If !IsBlind()   
      MostraErro()   
      MsgAlert('Erro na inclusao!')   
  Endif   
 EndIf   
EndIf
